#!/bin/bash
NOTE_DIR="/home/amy/Documents/notes/"

menu() {
  find "${NOTE_DIR}" -maxdepth 4 -type f \( -iname "*.txt" -o -iname "*.md" \)
}

main() {
  choice=$(menu | wofi --show dmenu --prompt "Select Wallpaper:" -n)
  selected_wallpaper=$(echo "$choice" | sed 's/^img://')
  echo "$selected_wallpaper"
}
main
