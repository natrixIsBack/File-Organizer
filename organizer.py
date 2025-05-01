import os
import shutil

# Define folder categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"]
}

def organize_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("❌ Provided path is not a folder.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            found = False

            for folder, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"✅ Moved: {filename} → {folder}")
                    found = True
                    break

            if not found:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"📁 Moved: {filename} → Others")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path>")
    else:
        organize_folder(sys.argv[1])
