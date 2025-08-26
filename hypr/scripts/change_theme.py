from subprocess import run
import os


SCRIPT_DIR="/home/amy/.config/hypr/scripts/"
THEMES_DIR = "/home/amy/.config/Woke-Dot-Files/Themes/"
COLOURS_FILE = "/var/cache/theme/colours.css"
KITTY_COLOURS = "/home/amy/.config/Woke-Dot-Files/kitty/current-theme.conf"

def get_theme():
    WALLPAPER = run([SCRIPT_DIR+"wallpaper.sh"], capture_output=True, text=True).stdout.strip()
    if(len(WALLPAPER) > 0):
        THEME = WALLPAPER.split("/")
        THEME.pop(-1)
        THEME.pop(0)
        THEME = "/".join(THEME)
        print(THEME)
        return THEME
    return ""

def change_file(THEME: str, BASE_FILE_NAME: str):
    FILE_NAME: str = BASE_FILE_NAME.split("/")[-1]
    THEME_FILE: str = f"{"/"+THEME+"/"}{FILE_NAME}"
    if(os.path.exists(BASE_FILE_NAME) and os.path.exists(THEME_FILE)):
        os.system(f"cp {THEME_FILE} {BASE_FILE_NAME}")
    else:
        os.system(f"notify-send -t 1500 \" Failed to change {FILE_NAME} \"")

def main():
    THEME = get_theme()
    if(len(THEME) > 0):
        change_file(THEME, COLOURS_FILE)
        change_file(THEME, KITTY_COLOURS)
        os.system(f"notify-send -t 700 \" Changed theme to {THEME} \"")


if(__name__=="__main__"):
    main()
