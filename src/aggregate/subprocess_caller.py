import subprocess

if __name__ == "__main__":
  print("testing subprocess")
  subprocess.run(['start', '', r'C:/Users/andys/AppData/Roaming/Microsoft/Windows/Start Menu/Programs\Zoom\Zoom Workplace.lnk'], shell=True)

  process = subprocess.Popen(['grep', 'python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, shell=True)
  output, _ = process.communicate('python is awesome\nhello world')
  print(output)



