import os
import subprocess

RULES = "/home/amy/.config/hypr/rules/workspacerules.conf"
DOUBLE_RULES = " workspace = 1, monitor:DP-1\n workspace = 2, monitor:HDMI-A-1"

SINGLE_RULES = "workspace = 1, monitor:DP-1"


def get_command_output(cmd: str) -> str:
    return subprocess.check_output(cmd, shell=True, text=True)
   
def main():
    monitors = get_command_output("hyprctl monitors")
    wanted = []
    final = []
    for i in monitors.split("\n"):
        if("Monitor" in i):
            wanted.append(i)
    for i in wanted:
        final.append(i.split(" ")[1])

    with open(RULES, "w+") as f:
        if(len(final) > 1):
            f.write(DOUBLE_RULES)
        else:
            f.write(SINGLE_RULES)
    





if(__name__ == "__main__"):
    main()
