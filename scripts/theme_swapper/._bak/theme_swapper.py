import os
from subprocess import run
from shutil import rmtree
from time import sleep

config_dir = "/home/amy/.config/"
this_dir = "/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/"

def restart_themes():
    os.system("killall waybar ; waybar")
    os.system("killall hyprpaper")
    os.system("hyprctl reload")
    os.system("hyprpaper")


def backup_theme(theme: str):
    backup_location: str = f"{this_dir}.{theme}_bak/"
    if(os.path.exists(backup_location)):
        rmtree(backup_location)

    os.system(f"mkdir {this_dir}.{theme}_bak/ ; cp -rf {this_dir}{theme}/* {this_dir}.{theme}_bak/")
    # os.system(f"rm -r {theme}/.{theme}_bak/.{theme}_bak")

def backup_full_config():
    backup_location: str = f"{this_dir}.config_bak"
    if(os.path.exists(backup_location)):
        rmtree(backup_location)

    os.mkdir(backup_location)
    os.system(f"cp -rf {config_dir}* {backup_location}")

def overwrite_config(theme: str):
    for i in (os.listdir(config_dir)):
        for j in (os.listdir(f"{this_dir}{theme}")):
            if(i == j):
                to_link: str = f"{this_dir}{theme}/{j}"
                print(f"i: {i} \n j: {j}")
                rmtree(f"{config_dir}{i}")
                if(os.path.isdir(to_link)):
                    print(f"Copying {to_link}  to {config_dir+i}")
                    os.system(f"cp -rf {to_link} {config_dir+i}")
                else:
                    os.system(f"cp {to_link} {config_dir+i}")

def update_themes(theme: str):
    print(f"Updating: {theme}")
    backup_theme(theme)
    backup_full_config()
    overwrite_config(theme)
    restart_themes()



def main():
    theme = run(["/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/create_wofi.sh"], capture_output=True, text=True)
    theme:str = theme.stdout.strip()
    
    if(os.path.isdir(this_dir+theme)):
        update_themes(theme)
    else:
        print(f"{this_dir+theme} is not a valid theme directory")

    
if(__name__ == "__main__"):
    main()
