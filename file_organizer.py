import os
import shutil

# File categories and their extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Python": [".py"],
    "Archives": [".zip", ".rar", ".7z"]
}


def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    moved_files = 0

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        # Ignore folders
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()

        category = "Others"

        for folder_name, extensions in FILE_TYPES.items():
            if extension in extensions:
                category = folder_name
                break

        destination_folder = os.path.join(folder_path, category)

        # Create category folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)

        # Prevent overwriting existing files
        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            count = 1

            while os.path.exists(destination_path):
                new_filename = f"{name}_{count}{ext}"
                destination_path = os.path.join(
                    destination_folder,
                    new_filename
                )
                count += 1

        shutil.move(file_path, destination_path)

        print(f"✅ {filename} → {category}")
        moved_files += 1

    print(f"\n🎉 Organization complete! {moved_files} files moved.")


folder = input("Enter the folder path you want to organize: ").strip()

# Allows paths pasted with quotes
folder = folder.strip('"')

organize_files(folder)