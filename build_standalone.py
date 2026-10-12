import json

def build_standalone():
    print("Reading source files...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    with open('styles.css', 'r', encoding='utf-8') as f:
        css = f.read()
        
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        questions_json = f.read()
        
    with open('app.js', 'r', encoding='utf-8') as f:
        js = f.read()

    # Inline CSS
    style_tag = f"<style>\n{css}\n</style>"
    if '<link rel="stylesheet" href="styles.css">' in html:
        html = html.replace('<link rel="stylesheet" href="styles.css">', style_tag)
    else:
        # Fallback insertion in head
        html = html.replace('</head>', f'{style_tag}\n</head>')

    # Ensure JS supports embedded data
    embedded_data_script = f"<script>\nwindow.GES201_EMBEDDED_QUESTIONS = {questions_json};\n</script>"
    
    old_fetch_block = """      const response = await fetch('data/questions.json');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      state.allQuestions = await response.json();"""

    new_fetch_block = """      if (window.GES201_EMBEDDED_QUESTIONS && Array.isArray(window.GES201_EMBEDDED_QUESTIONS)) {
        state.allQuestions = window.GES201_EMBEDDED_QUESTIONS;
      } else {
        const response = await fetch('data/questions.json');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        state.allQuestions = await response.json();
      }"""

    if old_fetch_block in js:
        js = js.replace(old_fetch_block, new_fetch_block)

    # Inline JS
    full_script_block = f"{embedded_data_script}\n<script>\n{js}\n</script>"
    if '<script src="app.js"></script>' in html:
        html = html.replace('<script src="app.js"></script>', full_script_block)
    else:
        html = html.replace('</body>', f'{full_script_block}\n</body>')

    output_filename = "GES201_CBT_Master_Offline.html"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Standalone file created successfully: {output_filename} ({len(html)} bytes)")

if __name__ == '__main__':
    build_standalone()
