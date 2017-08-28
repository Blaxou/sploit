#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import cmd
import os
import socket
import subprocess

import gnureadline

import netifaces  # IMPORT
from spf import core, fmt, threadedCracker
from spf.fmt import print_error, print_info, print_status, print_success
from terminaltables import AsciiTable, DoubleTable, SingleTable  # IMPORT


def bye():
    print("\n")
    print_success("Successfully exited the programm")
    exit()


class sploit_shell(cmd.Cmd):

    ### Setting the shell up ###
    use_rawinput = True
    intro_table_data = [
        [fmt.red + "Codename" + fmt.blue, fmt.red + "SPloit Framework" + fmt.blue],
        [fmt.green + "Author" + fmt.blue, fmt.green + "Blaxou" + fmt.blue]
    ]
    intro_table = DoubleTable(intro_table_data)
    intro = '''

		███████╗██████╗ ██╗	  ██████╗ ██╗████████╗
		██╔════╝██╔══██╗██║	 ██╔═══██╗██║╚══██╔══╝
		███████╗██████╔╝██║	 ██║   ██║██║   ██║
		╚════██║██╔═══╝ ██║	 ██║   ██║██║   ██║
		███████║██║	 ███████╗╚██████╔╝██║   ██║
		╚══════╝╚═╝	 ╚══════╝ ╚═════╝ ╚═╝   ╚═╝

''' + fmt.blue + intro_table.table + fmt.clear + "\n\n\n"
    prompt = fmt.clear + 'Sploit > '
    clear = '\033[0m'
    bold = '\033[1m'
    ylw = '\033[93m'
    ruler = "-"
    doc_header = clear + ylw + bold + "[?] " + clear + "Enter one of these commands :\n" + clear + \
        ylw + bold + "[?] " + clear + \
        "Enter `help <command>` to get help for specific command" + fmt.ylw

    def default(self, line):
        print_info("'" + fmt.bold + line + fmt.clear +
                   "' isn't a valid command !")

    def emptyline(self):
        self.onecmd("?")
### Commands ###

    def do_use(self, arg):
        "Use a module"
        os.chdir("module")
        print(os.getcwd())
        # core.use(arg)

    def do_shell(self, arg):
        "Executes the command in the shell"
        try:
            shell = subprocess.run(
                arg.split(" "), stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
            print("[{}SHELL{}] : {}".format(fmt.ylw, fmt.clear, shell))
        except FileNotFoundError:
            print_error("'{}{}{}' isn't a shell command".format(
                fmt.bold, arg.split(' ')[0], fmt.clear))

    def do_show(self, arg):
        core.show(arg)

    def do_net(self, arg):
        "Get your ip adress"
        print('')
        table_datas = [[fmt.ylw + "Interface" +
                        fmt.blue, fmt.mag + "Ip Address" + fmt.blue]]

        interfaces = netifaces.interfaces()
        for i in interfaces:
            if i == 'lo':
                continue
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
            if iface != None:
                for j in iface:
                    if j['addr'][:3] == "127":
                        pass
                    else:
                        table_datas.append(
                            [fmt.ylw + i + fmt.blue, fmt.mag + j["addr"] + fmt.blue])
        table = DoubleTable(table_datas)
        print(fmt.blue + table.table)
        print('')

    def do_exit(self, arg):
        "Exits the programm (You can use CTRL + C too)"
        bye()

    def do_crack(self,arg):
        try :
            while 1 :
                print_info("Choose what to crack :")
                print(" 1 - Zip")
                i = input("# > ")
                if i == '1':
                    threadedCracker.main()
                    break
                os.system('clear')
        except KeyboardInterrupt :
            print("")
            print_error("Aborted command !")
            return


    def do_banner(self, arg):
        "Print the banner"
        print(self.banner)


if __name__ == '__main__':
    os.system("clear")
    try:
        sploit_shell().cmdloop()
    except KeyboardInterrupt:
        bye()
