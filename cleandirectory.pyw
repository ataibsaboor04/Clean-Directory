import os
import shutil
from pathlib import PurePath
from mymodules.notification import notify


class CleanDirectory:
    categories = {
        "Documents": [".pdf", ".txt", ".pptx", ".ppt", ".docx", ".doc", ".xlsx", ".xls", ".csv", ".pub"],
        "Audio": [".mp3", ".wav", ".wma", ".amr", ".ogg", ".m4a"],
        "Pictures": [".jpg", ".png", ".gif", ".jpeg"],
        "Videos": [".mp4", ".3gp", ".mkv", ".3gpp", ".avi", ".mov", ".flv", ".tar"],
        "Applications": [".exe"],
        "Compressed": [".zip", ".rar", ".7z"],
        "Web": [".html", ".css", ".js", ".xml"],
        "Python Files": [".py"]
    }

    def __init__(self, path):
        self.path = path
        self.files = os.listdir(self.path)

    def extensions(self):
        files_with_path = [self.path + file for file in self.files]
        pure_path = [PurePath(file_directory)
                     for file_directory in files_with_path]
        extensions = {file: file_path.suffix for file,
                      file_path in zip(self.files, pure_path)}
        return extensions

    def create_directory(self):
        extensions = self.extensions()
        for file, extension in extensions.items():
            for category in self.categories:
                if extension in self.categories[category] and category not in self.files:
                    os.makedirs(self.path + category)
                    self.files = os.listdir(self.path)

    def remove_empty_directories(self):
        for folder in os.listdir(self.path):
            folder_path = self.path + '/' + folder
            if os.path.isdir(folder_path) and len(os.listdir(folder_path)) == 0:
                os.rmdir(folder_path)

    def clean(self):
        self.remove_empty_directories()
        self.create_directory()
        extensions = self.extensions()
        for file, extension in extensions.items():
            for category in self.categories:
                if extension in self.categories[category]:
                    shutil.move(self.path + file, self.path +
                                f"{category}/" + file)


def main():
    path = 'C:/Users/HP 14 cm0009AU/Downloads/'
    for file in os.listdir(path):
        if (not os.path.isdir(path+file)) and ('.ini' not in file):
            notify("Downloads", "Cleaning Directory...")
            downloads = CleanDirectory(path)
            downloads.clean()
            notify("Dowloads", "\nDirectory has been cleaned.")
            return
    notify("Downloads", "Directory is already clean.")


if __name__ == '__main__':
    main()
