# Python File Organizer

A lightweight Python automation tool that organizes files into categorized directories based on their file extensions. The project is designed to simplify file management and demonstrate practical Python automation, file handling, and directory management.

# Overview

The **Python File Organizer** scans a user-selected directory, identifies files based on their extensions, creates appropriate category folders, and automatically moves the files into those folders.

It is useful for keeping directories such as Downloads, Desktop, or project folders clean and organized.

# Features

* Automatically organizes files by type
* Supports images, documents, videos, music, Python files, and archives
* Creates category folders automatically
* Handles duplicate filenames without overwriting existing files
* Supports unknown file types through an `Others` category
* Validates the provided folder path
* Provides clear terminal-based progress and completion messages
* Uses Python's built-in libraries with no external dependencies

# Supported File Categories

| Category  | File Types                                |
| --------- | ----------------------------------------- |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`  |
| Documents | `.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx` |
| Videos    | `.mp4`, `.mkv`, `.avi`, `.mov`            |
| Music     | `.mp3`, `.wav`, `.aac`                    |
| Python    | `.py`                                     |
| Archives  | `.zip`, `.rar`, `.7z`                     |
| Others    | Unsupported or unrecognized extensions    |

# Technologies Used

* **Python 3**
* `os` — directory and file operations
* `shutil` — moving files
* `pathlib` / file path handling concepts

# Project Structure

```text
Python-File-Organizer/
│
├── file_organizer.py
├── README.md
└── .gitignore
```

## How It Works

1. The user provides the path of the directory to organize.
2. The program scans the directory for files.
3. Each file's extension is identified.
4. The extension is matched with a predefined category.
5. The required category folder is created automatically.
6. The file is moved into the corresponding folder.
7. Duplicate filenames are renamed instead of being overwritten.
8. A completion summary is displayed.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Python-File-Organizer
```

No external Python packages are required.

## Usage

Run the program using:

```bash
python file_organizer.py
```

When prompted, enter the path of the directory you want to organize.

Example:

```text
Enter the folder path you want to organize:
C:\Users\YourName\Desktop\Test-Files
```

## Example

### Before Organization

```text
Test-Files/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── notes.txt
└── program.py
```

### After Organization

```text
Test-Files/
├── Images/
│   └── photo.jpg
├── Documents/
│   ├── resume.pdf
│   └── notes.txt
├── Music/
│   └── song.mp3
└── Python/
    └── program.py
```

## Error Handling

The application includes basic safeguards to:

* Detect invalid directory paths
* Skip existing directories
* Prevent accidental file overwrites
* Handle duplicate filenames by generating unique names

## Future Improvements

Potential enhancements include:

* Graphical User Interface (GUI).
* Drag-and-drop folder selection.
* Custom file categories.
* Detailed activity logs.
* Undo functionality.
* Recursive organization of files inside subdirectories.
* Configurable file-extension mappings.
* File organization statistics.

## Learning Outcomes

This project demonstrates practical understanding of:

* Python file handling
* Directory management
* Automation with Python
* Conditional logic
* Functions and loops
* Exception-safe file operations
* Working with file extensions
* Building reusable command-line utilities

# License

This project is open-source and available for educational and personal use.

# Author

**Mittapally Sai Vivek**

Computer Science & Engineering.

GitHub: [https://github.com/viveksai1700-del]

## Latest Update
Project documentation and repository structure updated.
