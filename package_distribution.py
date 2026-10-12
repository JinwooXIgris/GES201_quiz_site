import os
import shutil
import zipfile

def package():
    dist_dir = "web_distribution"
    os.makedirs(dist_dir, exist_ok=True)
    os.makedirs(os.path.join(dist_dir, "data"), exist_ok=True)

    # 1. Copy core web files
    files_to_copy = [
        ("index.html", os.path.join(dist_dir, "index.html")),
        ("styles.css", os.path.join(dist_dir, "styles.css")),
        ("app.js", os.path.join(dist_dir, "app.js")),
        ("GES201_CBT_Master_Offline.html", os.path.join(dist_dir, "GES201_CBT_Master_Offline.html")),
        (os.path.join("data", "questions.json"), os.path.join(dist_dir, "data", "questions.json")),
    ]

    for src, dst in files_to_copy:
        shutil.copy2(src, dst)
        print(f"Copied {src} -> {dst}")

    # 2. Also create an index.html inside web_distribution that is self-contained if deployed directly on static host
    # (Copy GES201_CBT_Master_Offline.html to web_distribution/standalone.html)
    shutil.copy2("GES201_CBT_Master_Offline.html", os.path.join(dist_dir, "standalone.html"))

    # 3. Create zip package
    zip_filename = "GES201_CBT_Web_Package.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(dist_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, dist_dir)
                zf.write(filepath, arcname)

    print(f"Created {zip_filename} ({os.path.getsize(zip_filename)} bytes)")

if __name__ == '__main__':
    package()
