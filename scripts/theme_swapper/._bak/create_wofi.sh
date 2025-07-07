#!/bin/bash

# Define the menu options
OPTIONS="Catppuccin\nNord"

# Show the menu and capture the user's selection
CHOICE=$(echo -e "$OPTIONS" | wofi -n --dmenu --prompt "Select a theme:")

if [ -n "$CHOICE" ]; then
  echo "$CHOICE"
fi
