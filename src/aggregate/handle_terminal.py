import shutil
import subprocess
import os
import re

import questionary
import ast
from icecream import ic
from file_handler import FileHandleComponent
# from src.config import program_path

"""
    TODO move this file to components
"""

program_path = [r"C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs", r"C:\Program Files (x86)", r"C:\Program Files"]

pc = r"E:\projects\2024\FormiBlocks\cache\program_cache.txt"

class FileSystem(FileHandleComponent):
    def __init__(self) -> None:
        self.program_dict = {}
        self.all_program_paths = program_path
        self.daily_cache()


        #regrez
        self.not_program = re.compile(pattern="uninstall")

    def daily_cache(self):
        import time

        if os.path.exists(pc):
            # Get the current time
            now = time.time()
            # Define the time threshold (24 hours ago)
            time_threshold = now - 24 * 60 * 60 # time last 24 hours ago

            last_mod = os.path.getmtime(pc) #last mod

            if last_mod > time_threshold:
                self.find_programs()
                self.cache_programs()
            else:
                self.load_program()

            ic(last_mod, time_threshold)
            return

        self.find_programs()
        self.cache_programs()

    def find_programs(self):
        """
        Recursively finds all .lnk shortcut files in the given directory.

        :param root_dir: The directory to start searching from
        :return: List of paths to .lnk files
        """

        for path in self.all_program_paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    #when shortcut or exe add to program_dict
                    if file.lower().endswith('.lnk') or file.lower().endswith('.url') or file.lower().endswith('.exe'):
                        self.program_dict[file.lower()] = os.path.join(root, file)

    def ask_user_search_key(self, shortcut_choice : list):
        choice = questionary.select(
            "Select an option:",
            choices=shortcut_choice
        ).ask()

        return self.program_dict[choice]

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

        if list_of_match:
            return self.ask_user_search_key(list_of_match)

        print("Found no matches")

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

"""
  steam://rungameid/{id of game}
  we could just find a way to regex and pin the id to the game then call steam://rungameid/id of game
    -> if game not in x then we can just return error call
"""

if __name__ == "__main__":
  fs = FileSystem()
  print(fs.get_programs())
  print(fs.search_key("unity"))
#   print(fs.search_key("zoom")) # returns C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs\Steam\Apex Legends.url

  """
    take format into into lower
    keep links until \
    call this every time we run and cache them into a txt file
    make regex command to call this -> subprocess,

    hey jarvis can you open x, must return lower then we regex file in program dir and call it through subprocess! -> whats how we will open the file of any program on computer
  """