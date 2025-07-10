import SetTheme
from os import system

def main():
    theme: str
    with open(SetTheme.CURRENT_DIR+"theme.txt", "r") as f:
        theme = f.read()
    if(len(theme) != 0):
        SetTheme.update_theme(theme)
    else:
        system(f"hyprctl notify 0 3000 \"rgb(ff1ea3)\" \"The current theme at {SetTheme.CURRENT_DIR}theme.txt is not set!\"")

if(__name__ == "__main__"):
    main()
