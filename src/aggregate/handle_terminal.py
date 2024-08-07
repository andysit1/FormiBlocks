import shutil
import subprocess
import os

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
  print("testing terminal commands / subprocess")
  desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
  print(desktop_path)
  executable_path = shutil.which("echo")
  print(executable_path)

  # Set the root directory to search from
  root_directory = "C:/"  # Change this to the directory you want to search
  game_dir = "C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam"
  program_dir = "C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"

  shortcuts = find_shortcuts(program_dir)

  # Print out the list of shortcuts
  print(f"Found {len(shortcuts)} shortcut files:")
  for shortcut in shortcuts:
      print(shortcut)


  """
    take format into into lower
    keep links until \
    call this every time we run and cache them into a txt file
    make regex command to call this -> subprocess,

    hey jarvis can you open x, must return lower then we regex file in program dir and call it through subprocess! -> whats how we will open the file of any program on computer
  """