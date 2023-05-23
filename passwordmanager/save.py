import json
import os
from encrypt import AES256

class Saver:
    def __init__(self, file):
        # Store the file name as an attribute
        self.file = file

    def save(self, data):
        # Open the file in write mode and dump the data as JSON
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def read(self):
        # Open the file in read mode and load the data as JSON
        with open(self.file, "r") as file:
            data = file.read()
            # Return an empty list if the file is empty
            if os.stat(self.file).st_size == 0:
                return []
            return json.loads(data)
        
        