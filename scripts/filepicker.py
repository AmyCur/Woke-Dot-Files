import os
import subprocess
import webbrowser
from sys import argv

def main():
    file_choice = subprocess.run(['/home/amy/Documents/scripts/filepicker.sh'], capture_output=True,  text=True)
    file_choice = file_choice.stdout.strip()

    print(file_choice)
    split_choice = file_choice.split(".")
    if(split_choice[1] == "ln"):
        with open(file_choice) as f:
            url = f.read().strip()
            print(f"Opening {url}")
            webbrowser.open(url)
    else:
        os.system(f"kitty nvim {file_choice}")

if(__name__ == "__main__"):
    main()
