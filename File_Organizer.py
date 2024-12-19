import os, shutil

directory = os.path.join(os.path.expanduser("~"), "Desktop")
extensions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".mp3": "Music",
    ".wav": "Music",
    ".aac": "Music",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".psd": "Photoshop",
    ".ai": "Illustrator"
}

def main():
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isfile(file_path):
            extension = os.path.splitext(file_name)[1].lower()

            if extension in extensions:
                folder_name = extensions[extension]

                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                destination_path = os.path.join(folder_path, file_name)
                shutil.move(file_path, destination_path)

                print(f"Moved {file_name} to {folder_name} folder.")
            else:
                print(f"Skipped {file_name}. Unknown file extension.")


if __name__ == '__main__':
    main()