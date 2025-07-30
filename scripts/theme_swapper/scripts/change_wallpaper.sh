#!/bin/sh

WALLPAPER_DIR="$HOME/Pictures/wallpapers" # Define wallpaper directory

# Find and list image files
images=$(find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0 | sort -z)

# Use dmenu to select a wallpaper
selected_image=$(echo -e "$images" | dmenu -i -p "Select Wallpaper:" -l 10)

# # Set the wallpaper
# if [ -n "$selected_image" ]; then
#   feh --bg-fill "$selected_image" # Or use xwallpaper, wal, etc.
# fi
