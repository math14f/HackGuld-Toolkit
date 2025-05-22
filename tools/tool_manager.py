# coding=utf-8
import os
from time import sleep

from core import HackingTool
from core import HackingToolsCollection


class UpdateTool(HackingTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update HackGuld-Toolkit", self.update_ht)
        ], installable=False, runnable=False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system("sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):  # ← Nu er den korrekt defineret i klassen
        print("Opdaterer HackGuld-Toolkit...\n")
        os.system("git pull origin main")
        print("Opdatering færdig!")



class UninstallTool(HackingTool):
    TITLE = "Uninstall HackGuld-Toolkit"
    DESCRIPTION = "Uninstall HackGuld-Toolkit"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable = False, runnable = False)

    def uninstall(self):
        print("HackGuld-Toolkit started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/HackGuld-Toolkit/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/HackGuld-Toolkit/;")
        print("\nHackingtoolkit Successfully Uninstalled..")
        print("Happy Hacking..!!")
        sleep(1)


class ToolManager(HackingToolsCollection):
    TITLE = "Update or Uninstall | HackGuld-Toolkit"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]
