import os

class FileReader:
    def __init__(self, filenames):
        self.filenames = filenames
    
    def read_files(self):
        file_data = []
        for file in self.filenames:
            if os.path.isfile(file):
                with open(file, "r") as f:
                    print(f"File {file} read.")
                    file_data.append(f.readlines())
            else:
                print(f"File {file} does not exist.")
        return file_data

