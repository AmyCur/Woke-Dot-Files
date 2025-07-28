from subprocess import run
import os

POSSIBLE_THEMES = ["Catppuccin", "Nord", "Undertale"]
CURRENT_DIR = "/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/scripts/"
THEMES_DIR = "/home/amy/Documents/Themes/"
COLOURS_FILE = "/var/cache/theme/colours.css" 
WALLPAPER1 = "/var/cache/theme/wallpaper1.jpg"
THEME=""

def select_theme():
    THEME = run([CURRENT_DIR+"CreateWofiSelector.sh"], capture_output=True, text=True).stdout.strip()
    print(f"Selected: {THEME}")
    if(len(THEME) != 0):
        with open(CURRENT_DIR+"theme.txt", "w") as f:
            f.write(THEME)
    return THEME

                # theme name, name of the file to be replaced, name of the file
def change_file(BASE_FILE_NAME: str,FILE_NAME: str):
    CURRENT_THEME_DIR = THEMES_DIR+THEME+"/"
    os.system(f"cp {CURRENT_THEME_DIR}{FILE_NAME} {BASE_FILE_NAME}")

def update_theme(theme:str):
    THEME=theme
    change_file(COLOURS_FILE, "colours.css")
    change_file(WALLPAPER1, "wallpaper1.jpg")
    os.system(f"swww img --transition-type wipe --transition-pos 0.854,0.977 --transition-step 90 --transition-fps 60 {WALLPAPER1}")
    os.system(f"notify-send -t 700 \" Changed theme to {THEME} \"")
    # os.system("killall hyprpaper; hyprpaper")

def main():
    # If the user didnt enter a value
    if(len(THEME) != 0):
        update_theme(THEME)

if(__name__ == "__main__"):
    THEME=select_theme()
    main()
