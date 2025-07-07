#!/bin/bash

SELECTED=$(find "$HOME/Documents/flatpak/" -maxdepth 1 -type f | wofi -n --dmenu --prompt "Search:")

if [ -n "$SELECTED" ]; then
  # echo "You picked: $SELECTED"
  # Do something with the file, e.g., open it
  echo "$SELECTED"
fi
