import os


def main():
    theme = run(["/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/create_wofi.sh"], capture_output=True, text=True)
    theme:str = theme.stdout.strip()
    
    if(os.path.isdir(this_dir+theme)):
        update_themes(theme)
    else:
        print(f"{this_dir+theme} is not a valid theme directory")

    
if(__name__ == "__main__"):
    main()

