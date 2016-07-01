# required modules
from sys import *
from urllib2 import *
from colorama import *
from json import *
import os

# List all entered mods
mods = []

# configuration file
config = load(open("config.json","r"))

# repository location for mods
repo = load(urlopen(config["repo"][raw_input("version: ")]))
print("\n")

# modpack file w/ user input
modpack = open(config["modpack-folder"] + raw_input("modpack name: ") + ".txt","w")
print("\n")

# tests to see if your editing a modpack
editing = True

# Mod found detection
found = False

while editing:
    # get user input for mod name
    mod = raw_input("mod name: ")
    # Search for mod
    if mod != "!!done".lower():
        for item in repo:
            if item["name"].lower() == mod.lower():
                # add mod to file
                found = True
                modpack.write(item["name"] + " - " + item["shorturl"] + "\n")
                mods.append(mod.lower())
                deps = ""
                for dep in item["dependencies"]:
                    if dep.lower() in mods:
                        deps += Fore.GREEN + dep + Fore.WHITE + ", "
                    else:
                        deps += Fore.RED + dep + Fore.WHITE + ", "
                print("Dependencies: " + deps + "\n")
        if found:
            # If mod found, print this and reset found value
            print(Fore.GREEN + "Mod added to modpack file" + Fore.WHITE + "\n")
            found = False
        else:
            # If mod not found, or error print this
            print(Fore.RED + "Mod Not Found" + Fore.WHITE + "\n")
    else:
        # Finish editing and close file
        editing = False
        modpack.close()
        print(Fore.GREEN + "Modpack Finished" + Fore.WHITE + "\n")
