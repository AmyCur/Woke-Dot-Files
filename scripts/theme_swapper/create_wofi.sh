#!/bin/bash

# Define the menu options
options="Catppuccin\nNord"

# Show the menu and capture the user's selection
echo $(echo -e "$options" | wofi -n --dmenu --prompt "Select a theme:")
