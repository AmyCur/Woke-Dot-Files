#!/bin/bash

DIR="${1:-$HOME}" # Use argument as directory, or default to $HOME

SELECTED=$(find "$HOME/Documents/notes" -maxdepth 1 -type f | wofi -n --dmenu --prompt "Pick a file:")

if [ -n "$SELECTED" ]; then
  # echo "You picked: $SELECTED"
  # Do something with the file, e.g., open it
  echo "$SELECTED"
fi
