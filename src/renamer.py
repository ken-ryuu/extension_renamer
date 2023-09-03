import os

class Renamer:
    def __init__(self, old_extension, new_extension):
        self.old_extension = old_extension
        self.new_extension = new_extension

    def rename_files(self, file_paths):
        renamed_files = []
        for file_path in file_paths:
            if file_path.endswith(self.old_extension):
                new_file_path = file_path.rsplit(self.old_extension, 1)[0] + self.new_extension
                try:
                    os.rename(file_path, new_file_path)
                    renamed_files.append(new_file_path)
                except Exception as e:
                    print(f"Error renaming {file_path}: {e}")
        return renamed_files