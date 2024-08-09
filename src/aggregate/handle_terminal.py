import shutil
import subprocess
import os
import re

import ast
from icecream import ic
program_path = "C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"
from file_handler import FileHandleComponent


pc = r"E:\projects\2024\FormiBlocks\cache\program_cache.txt"

class FileSystem(FileHandleComponent):
    def __init__(self) -> None:
        self.program_dict = {}
        self.find_programs()
        self.cache_programs()
        self.not_program = re.compile(pattern="uninstall")


    def find_programs(self):
        """
        Recursively finds all .lnk shortcut files in the given directory.

        :param root_dir: The directory to start searching from
        :return: List of paths to .lnk files
        """


        for root, dirs, files in os.walk(program_path):
            for file in files:
                if file.lower().endswith('.lnk'):
                    self.program_dict[file.lower()] = os.path.join(root, file)

                if file.lower().endswith('.url'):
                    self.program_dict[file.lower()] = os.path.join(root, file)

    def search_key(self, key : str):

        regex_cmd = re.compile(pattern="({})".format(key.lower()))
        list_of_match = []
        for key in self.program_dict.keys():
            found : list = regex_cmd.findall(key)

            if found and not self.not_program.findall(key):
              list_of_match.append(key)

            # in the event that we do have similar program names we should prob return the list and get the user to pick the correct program

        ic(list_of_match, len(list_of_match))

        if len(list_of_match) == 1:
            return self.program_dict[list_of_match[0]]

        if len(list_of_match) == 0:
            return None

        raise TypeError("need a more specific key word to find key")

    #on start up
    def cache_programs(self):
      #TODO/FEATURE: check if cache file has been updated within day if not then cache new programs

      #https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file
      with open(pc, 'w') as f:
        print(self.program_dict, file=f)

    def load_program(self):
      with open(pc, 'r') as f:
          info = f.read()
          return ast.literal_eval(info)

    def get_programs(self):
        return self.program_dict

def find_shortcuts(root_dir):
    """
    Recursively finds all .lnk shortcut files in the given directory.

    :param root_dir: The directory to start searching from
    :return: List of paths to .lnk files
    """
    shortcuts = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.lnk'):
                shortcuts.append(os.path.join(root, file))
            if file.lower().endswith('.url'):
                shortcuts.append(os.path.join(root, file))

    return shortcuts

"""
  steam://rungameid/{id of game}
  we could just find a way to regex and pin the id to the game then call steam://rungameid/id of game
    -> if game not in x then we can just return error call
"""

if __name__ == "__main__":
  fs = FileSystem()
  print(fs.search_key("apex")) # returns C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs\Steam\Apex Legends.url

  """
    take format into into lower
    keep links until \
    call this every time we run and cache them into a txt file
    make regex command to call this -> subprocess,

    hey jarvis can you open x, must return lower then we regex file in program dir and call it through subprocess! -> whats how we will open the file of any program on computer
  """