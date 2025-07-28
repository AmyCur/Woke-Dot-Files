#!/bin/bash

OPTIONS="Catppuccin\nNord\nUndertale\nVanisher"

CHOICE=$(echo -e "$OPTIONS" | wofi -n --dmenu --prompt "Select a theme:")

if [ -n "$CHOICE" ]; then
  echo "$CHOICE"
fi
