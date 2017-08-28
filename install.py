#!/usr/bin/env python3

import subprocess
from spf import fmt
import importlib
import os


def pp1(string, color):
    rows, cols = os.popen('stty size', 'r').read().split()
    hyphens = round((int(cols) - len(string)) / 2 - 6.25)
    print(hyphens * "-" + "[     " + color + string +
          fmt.clear + "     ]" + hyphens * "-")


def pp2(string, color):
    rows, cols = os.popen('stty size', 'r').read().split()
    hyphens = round((int(cols) - len(string)) / 2 - 6.25)
    print(hyphens * "=" + "[     " + color + string +
          fmt.clear + "     ]" + hyphens * "=")


def Main():

    if not os.geteuid() == 0:
        pp2("You need to run this script as root", fmt.red)
        exit()

    os.system("clear")

    i = checkAPT()
    if len(i) > 0:
        if installAPT(i):
            pp2("Success", fmt.green)
        else:
            pp2("SOMETHING WENT WRONG", fmt.red)
    else:
        pp2("Success", fmt.green)
    print("\n\n")

    i = checkMods()
    if len(i) > 0:
        if installMods(i):
            pp2("Success", fmt.green)
        else:
            pp2("SOMETHING WENT WRONG", fmt.red)
    else:
        pp2("Success", fmt.green)
    print("\n\n")

    pp2("                     ", fmt.clear)
    pp2("Installation Finished", fmt.green + fmt.bold)
    pp2("                     ", fmt.clear)


def checkAPT():

    packs = ["python3", "pip3"]

    pp1("Checking package depedencies", fmt.ylw)
    toInstall = []
    for pack in packs:
        print("[*] Checking for {}{}{}...".format(fmt.ylw, pack, fmt.clear), end="")
        i = subprocess.run(["hash", pack], stderr=subprocess.PIPE).returncode
        if i == 0:
            print("[{}OK{}]".format(fmt.green, fmt.clear))
        else:
            print("[{}NOT INSTALLED{}]".format(fmt.red, fmt.clear))
            toInstall.append(pack)
    return toInstall


def installAPT(modules):
    status = True
    pp1("Following packages will be installed", fmt.ylw)
    print("")
    for mod in modules:
        print(" - " + mod)
    print("")
    for mod in modules:
        print("[*] Installing {}{}{}...".format(fmt.ylw, mod, fmt.clear), end="")
        i = subprocess.run(["echo", "install", mod],
                           stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        if i == 0:
            print("[{}DONE{}]".format(fmt.green, fmt.clear))
        else:
            print("[{}ERROR{}]".format(fmt.red, fmt.clear))
            status = False
    return status


def checkMods():

    modules = ["terminaltables", "netifaces"]

    pp1("Checking modules depedencies", fmt.ylw)
    importedModules = []
    toInstall = []
    for mod in modules:
        print("[*] Checking for {}{}{}...".format(fmt.ylw, mod, fmt.clear), end="")
        try:
            importedModules.append(importlib.import_module(mod))
            print("[{}OK{}]".format(fmt.green, fmt.clear))
        except Exception as e:
            print("[{}NOT INSTALLED{}]".format(fmt.red, fmt.clear))
            toInstall.append(mod)
    return toInstall


def installMods(modules):
    status = True
    pp1("Following modules will be installed", fmt.ylw)
    print("")
    for mod in modules:
        print(" - " + mod)
    print("")
    for mod in modules:
        print("[*] Installing {}{}{}...".format(fmt.ylw, mod, fmt.clear), end="")
        i = subprocess.run(["pip3", "install", mod],
                           stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        if i == 0:
            print("[{}DONE{}]".format(fmt.green, fmt.clear))
        else:
            print("[{}ERROR{}]".format(fmt.red, fmt.clear))
            status = False
    print(status)
    return status


Main()
