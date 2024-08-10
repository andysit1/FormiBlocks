"""
  Import aggregate from other project
"""

import os
import glob

import unittest
from icecream import ic
import unittest
from unittest.mock import MagicMock
import os



"""
  File Standards - files names that are universal for this projects
    community -> this file will be cleared and emptied for any clips
    the-rest -> will be whenever we want to save specific videos for later comparison
                  -> needs a file system to handle the files
"""

#Note: will add try statements when I look at document to figure what exceptions it raises

class FileHandleComponent:
    def set_file_path(self, path):
        if self.path_exists(path):
            self.file_path = path

    def fix_str_path(self, file_path : str) -> str:
        return file_path.replace('\\', '/')

    def makedirs(self, file_path : str):
      print(file_path)

      os.makedirs(file_path, exist_ok=True)
      ic("Created dir located {}".format(file_path))

      #DOCS: TODO: figure a good way to fix this issue future bug fix
        # except OSE rror:
        # # Cannot rely on checking for EEXIST, since the operating system
        # # could give priority to other errors like EACCES or EROFS
        # if not exist_ok or not path.isdir(name):
        #     raise

    def path_exists(self, file_path : str):
        return os.path.exists(file_path)

    #my methods
    def remove_all_contents_output_frame(self, path: str):

        if os.path.exists(path):
            frames = glob.glob(self.input_video_path)

            for frame in frames:
                ic("Removed {}".format(frame))
                os.remove(frame)
        else:
            raise FileNotFoundError("Input file not found.")

    #AI genereated for the sake of just having them. Might remove in future if super redundant to reduce code amount
    def read_file(self, path: str) -> str:
        """Read the entire file content and return as a string."""
        with open(path, 'r') as file:
            return file.read()

    def write_file(self, path, content: str) -> None:
        """Write the provided content to the file."""
        with open(path, 'w') as file:
            file.write(str(content))

    def append_to_file(self, path, content: str) -> None:
        """Append the provided content to the file."""
        with open(path, 'a+') as file:
            file.write(content)

    def read_lines(self, path) -> list[str]:
        """Read the file and return a list of lines."""
        with open(path, 'r') as file:
            return file.readlines()

    def write_lines(self, path, lines: list) -> None:
        """Write a list of lines to the file."""
        with open(path, 'w') as file:
            file.writelines(str(line) + '\n' for line in lines)

    

    def file_exists(self, path) -> bool:
        """Check if the file exists."""
        return os.path.isfile(path)

    def delete_file(self, path) -> None:
        """Delete the file."""
        if self.file_exists(path):
            os.remove(path)




"""
    Test cases...
"""


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.file_handler = FileHandleComponent()
        self.test_file_path = 'test.txt'
        with open(self.test_file_path, 'w') as f:
            f.write('Sample content')

    def tearDown(self):
        import os
        os.remove(self.test_file_path)

    def test_read_file(self):
        content = self.file_handler.read_file(self.test_file_path)
        self.assertEqual(content, 'Sample content')

    def test_write_file(self):
        new_content = 'New content'
        self.file_handler.write_file(self.test_file_path, new_content)
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, new_content)

    def test_append_file(self):
        append_content = ' Appended content'
        self.file_handler.append_to_file(self.test_file_path, append_content)
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Sample content' + append_content)

    def test_file_exists(self):
        self.assertTrue(self.file_handler.file_exists(self.test_file_path))
        self.assertFalse(self.file_handler.file_exists('non_existent_file.txt'))



if __name__ == '__main__':
    unittest.main()
