import webbrowser
import argparse
import sys

NOTES_URL = "https://docs.google.com/document/d/1o8gHUvDhzXA-4LCzBjO7j8GF_kaJMGFDit22RfDiN9E/edit?usp=sharing";



def main():
    if(sys.argv[1] == "-l"):
        webbrowser.open(NOTES_URL, 0)
    
    elif(sys.argv[1] == "-m"):
        webbrowser.open(NOTES_URL, 1)
    print(sys.argv)



if(__name__ == "__main__"):
    main()
