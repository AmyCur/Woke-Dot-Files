#!/bin/bash

OPTIONS="Vesktop"

CHOICE=$(echo -e "$OPTIONS" | wofi -n --dmenu --prompt "Search")

if [ -n "$CHOICE" ]; then
  echo "$CHOICE"
fi
