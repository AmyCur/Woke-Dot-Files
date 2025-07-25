from subprocess import run
import os

SCRIPT_DIR: str = "/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/"

def get_theme():   
    THEME = run([SCRIPT_DIR+"CreateWofiSelector.sh"], capture_output=True, text=True).stdout.strip()
    print(f"Selected: {THEME}")
    if(len(THEME) != 0):
        with open(SCRIPT_DIR+"theme.txt", "w") as f:
            f.write(THEME)
    return THEME

THEME:str = get_theme()
THEME_DIR: str =  f"{SCRIPT_DIR}Themes/{THEME}/"

def update_wallpaper():
    WALLPAPER1: str = f"{THEME_DIR}wallpaper1.jpg"
    os.system(f"{SCRIPT_DIR}ChangeWallpaper.sh {WALLPAPER1}")

def main():
    update_wallpaper()

if(__name__=="__main__"):
    main()
