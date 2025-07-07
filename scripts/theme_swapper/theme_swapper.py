import os
from subprocess import run
from shutil import rmtree

def restart_themes():
    pass

def backup_theme(theme: str):
    backup_location: str = f"{theme}/{theme}.bak/"
    if(os.path.exists(backup_location)):
        rmtree(backup_location)

    os.system(f"mkdir {theme}/.{theme}_bak/ ; cp -rf {theme}/* {theme}/.{theme}_bak/")
    os.system(f"rm -r {theme}/.{theme}_bak/.{theme}_bak")

def update_themes(theme: str):
    print(f"Updating: {theme}")
    backup_theme(theme)


def main():
    theme = run(["/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/create_wofi.sh"], capture_output=True, text=True)
    theme:str = theme.stdout.strip()
    
    if(os.path.isdir(theme)):
        update_themes(theme)
    else:
        print(f"{theme} is not a valid theme directory")

    
if(__name__ == "__main__"):
    main()
