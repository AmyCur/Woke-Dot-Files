import os
import subprocess
import webbrowser
from sys import argv

def main():
    file_choice = subprocess.run(['/home/amy/Documents/scripts/flatpicker.sh'], capture_output=True,  text=True)
    file_choice = file_choice.stdout.strip()

    match file_choice:
        case "Vesktop":
            os.system("notify-send \"Opening Vesktop\" -t 800 -i ~/Pictures/icons/7a499c8bc6d5b013f80fb82d61bfcf5f.png -u low")
            os.system("flatpak run dev.vencord.Vesktop")

if(__name__ == "__main__"):
    main()

