# #!/bin/bash
# NOTE_DIR="/home/amy/Documents/notes/"
#
# menu() {
#   find "${NOTE_DIR}" -maxdepth 4 -type f \( -iname "*.txt" -o -iname "*.md" \)
# }
#
# main() {
#   choice=$(menu | wofi --show dmenu --prompt "Select Wallpaper:" -n)
#   selected_wallpaper=$(echo "$choice" | sed 's/^img://')
#   echo "$selected_wallpaper"
#   # swww img "$selected_wallpaper" --transition-type any --transition-fps 60 --transition-duration .5
#   # swaync-client --reload-css
#   # echo $selected_wallpaper
# }
# main

import os
from subprocess import run



NOTE_DIR="/home/amy/Documents/notes/"
SCRIPT_DIR="/home/amy/.config/hypr/scripts/waybar/"


def menu() -> int:
    return os.system(f"find \"{NOTE_DIR}\" -maxdepth 4 -type f \\( -iname \"*.txt\" -o -iname \"*.md\" \\)")


def main():
    NOTE = run([SCRIPT_DIR+"note_opener.sh"], capture_output=True, text=True).stdout.strip()



if(__name__=="__main__"):
    main()


