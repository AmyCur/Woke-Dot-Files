import os
from subprocess import run

def restart_themes():
    pass

def update_themes(theme: str):
    pass


def main():
    inp = run(["/home/amy/.config/Woke-Dot-Files/scripts/theme_swapper/create_wofi.sh"], capture_output=True, text=True)
    print("\n\n\n\n")
    print(inp)
    # choice = str(inp) 
    # if(os.path.isdir(choice)):
    #     update_themes(choice)
    # else:
    #     print(f"{choice} is not a valid theme directory")

    
if(__name__ == "__main__"):
    main()
