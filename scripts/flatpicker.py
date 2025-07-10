import os
import subprocess
import webbrowser
from sys import argv

def main():
    file_choice = subprocess.run(['/home/amy/Documents/scripts/flatpicker.sh'], capture_output=True,  text=True)
    file_choice = file_choice.stdout.strip()

    match file_choice:
        case "Vesktop":
            os.system("flatpak run dev.vencord.Vesktop")
            

if(__name__ == "__main__"):
    main()

