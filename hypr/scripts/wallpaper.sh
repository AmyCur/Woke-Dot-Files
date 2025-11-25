#!/bin/bash
WALLPAPER_DIR="/home/amy/.config/Woke-Dot-Files/Themes/"

menu() {
  find "${WALLPAPER_DIR}" -maxdepth 4 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" \) | awk '{print "img:"$0}'
}

main() {
  choice=$(menu | wofi -c ~/.config/wofi/wallpaper --show dmenu --prompt "Select Wallpaper:" -n)
  selected_wallpaper=$(echo "$choice" | sed 's/^img://')
  swww img "$selected_wallpaper" --transition-type any --transition-fps 60 --transition-duration .5
  swaync-client --reload-css
  echo $selected_wallpaper
}
main
