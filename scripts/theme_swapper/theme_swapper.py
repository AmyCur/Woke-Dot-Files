import os
from subprocess import run
from shutil import rmtree


config_dir = "/home/amy/.config/"

def restart_themes():
    pass

def backup_theme(theme: str):
    backup_location: str = f".{theme}_bak/"
    if(os.path.exists(backup_location)):
        rmtree(backup_location)

    os.system(f"mkdir .{theme}_bak/ ; cp -rf {theme}/* .{theme}_bak/")
    # os.system(f"rm -r {theme}/.{theme}_bak/.{theme}_bak")

def backup_full_config():
    backup_location: str = f"./.config_bak"
    if(os.path.exists(backup_location)):
        rmtree(backup_location)

    os.mkdir(backup_location)
    os.system(f"cp -rf {config_dir}* {backup_location}")

def overwrite_config(theme: str):
    for i in (os.listdir(config_dir)):
        for j in (os.listdir(f"{theme}")):
            if(i == j):
                print(f"i: {i} \n j: {j}")
                rmtree(i)
                if(os.isdir(j)):
                    os.system(f"ln -rs {j} {i}")
                else:
                    os.system(f"ln {j} {i}")

def update_themes(theme: str):
    print(f"Updating: {theme}")
    backup_theme(theme)
    backup_full_config()
    overwrite_config(theme)



def main():
    theme = run(["/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/create_wofi.sh"], capture_output=True, text=True)
    theme:str = theme.stdout.strip()
    
    if(os.path.isdir(theme)):
        update_themes(theme)
    else:
        print(f"{theme} is not a valid theme directory")

    
if(__name__ == "__main__"):
    main()
