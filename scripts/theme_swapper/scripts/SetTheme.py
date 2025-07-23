from subprocess import run
import os

POSSIBLE_THEMES = ["Catppuccin", "Nord", "Undertale"]
CURRENT_DIR = "/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/scripts/"
THEMES_DIR = "/home/amy/Documents/Themes/"
COLOURS_FILE = "/var/cache/theme/colours.css" 
WALLPAPER1 = "/var/cache/theme/wallpaper1.jpg"

def select_theme(DIR: str):
    THEME = run([DIR+"CreateWofiSelector.sh"], capture_output=True, text=True).stdout.strip()
    print(f"Selected: {THEME}")
    if(len(THEME) != 0):
        for i in POSSIBLE_THEMES:
            if(i == THEME):
                with open(DIR+"theme.txt", "w") as f:
                    f.write(THEME)
    return THEME

                # theme name, name of the file to be replaced, name of the file
def change_file(THEME: str, BASE_FILE_NAME: str,FILE_NAME: str):
    CURRENT_THEME_DIR = THEMES_DIR+THEME
    os.system(f"cp {CURRENT_THEME_DIR}/{FILE_NAME} {BASE_FILE_NAME}")

def update_theme(THEME: str):
    change_file(THEME, COLOURS_FILE, "colours.css")
    change_file(THEME, WALLPAPER1, "wallpaper1.jpg")
    os.system(f"notify-send -t 700 \" Changed theme to {THEME} \"")
    os.system("killall hyprpaper; hyprpaper")
    os.system("wal -c")

def main():
    theme = select_theme(CURRENT_DIR)

    # If the user didnt enter a value
    if(len(theme) != 0):
        update_theme(theme)

if(__name__ == "__main__"):
    main()
