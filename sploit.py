#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmd
import os
import socket
import subprocess


from spf.fmt import print_error, print_info, print_status, print_success
#import gnureadline

try :
	from spf import core, fmt

	import netifaces  # IMPORT
	from terminaltables import AsciiTable, DoubleTable, SingleTable  # IMPORT
except ImportError:
	print_error('Be sure to run the install.py script first !')
	exit()

def bye():
	print("\n")
	print_success("Successfully exited the programm")
	exit()


class sploit_shell(cmd.Cmd):

	### Setting the shell up ###
	use_rawinput = True
	intro_table_data = [
		[fmt.green + "Codename" + fmt.blue, fmt.red+fmt.bold+"SPloit Framework"+fmt.clear+fmt.blue],
		[fmt.green + "Author" + fmt.blue, fmt.red+fmt.bold+"Blaxou"+fmt.clear+fmt.blue]
	]
	intro_table = DoubleTable(intro_table_data)
	intro = fmt.green+'''

		███████╗██████╗ ██╗	  ██████╗ ██╗████████╗
		██╔════╝██╔══██╗██║	 ██╔═══██╗██║╚══██╔══╝
		███████╗██████╔╝██║	 ██║   ██║██║   ██║
		╚════██║██╔═══╝ ██║	 ██║   ██║██║   ██║
		███████║██║	 ███████╗╚██████╔╝██║   ██║
		╚══════╝╚═╝	 ╚══════╝ ╚═════╝ ╚═╝   ╚═╝

'''+fmt.blue+intro_table.table+fmt.clear+"\n\n\n"
	prompt = '{}{}Sploit {}>{} '.format(fmt.clear,fmt.bold,fmt.red,fmt.clear)
	clear = '\033[0m'
	bold = '\033[1m'
	ylw = '\033[93m'
	ruler = ""
	doc_header = clear + ylw + bold + "[?] " + clear + "Enter one of these commands :\n" + clear + \
		ylw + bold + "[?] " + clear + \
		"Enter `help <command>` to get help for specific command" + fmt.ylw + '\n'

	def default(self, line):
		print_error("'{}{}{}' isn't a valid command !".format(fmt.bold,line,fmt.clear))
		print_info("Use `{}! <command>{}` to run the command in a shell".format(fmt.bold,fmt.clear))

	def emptyline(self):
		self.onecmd("?")
### Commands ###

	def do_use(self, arg):
		"Use a module"
		pass

	def do_shell(self, arg):
		"Executes the command in the shell"
		if len(arg.split()) == 0 :
			print_info("Enter a command to be executed `{}! <command>{}`".format(fmt.bold,fmt.clear))
			return
		if arg.split()[0] == '!' :
			print_status('Spawning a bash instance ...')
			print_info('Type `exit` to go back here')
			shell = subprocess.run('bash')
			print_success('Welcome back here !')
		else :
			try:
				shell = subprocess.run(arg.split(), stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip()
				print('{}[{} Ouput of `{}` {}]{}'.format(fmt.ylw,fmt.clear,arg,fmt.ylw,fmt.clear))
				for line in shell.splitlines() :
					print("    "+line)
			except FileNotFoundError:
				print_error("'{}{}{}' isn't a shell command".format(fmt.bold, arg.split()[0], fmt.clear))
			except PermissionError:
				print_error("You're not allowed to do this !")

	def do_show(self, arg):
		"""WIP"""
		core.show(arg)

	def do_clear(self,arg):
		"""Clear the screen"""
		print(subprocess.run('clear',stdout=subprocess.PIPE).stdout.decode('utf-8').rstrip())

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


	def do_banner(self, arg):
		"Print the banner"
		print(self.intro)


if __name__ == '__main__':
	os.system("clear")
	try:
		sploit_shell().cmdloop()
	except KeyboardInterrupt:
		bye()
