#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile
from multiprocessing import Pool, Queue
from itertools import product
import os
import zlib
import time
import sys

def print_error(string):
    print('\033[91m[-]\033[0m ' + string)


def print_status(string):
    print('\033[94m[*]\033[0m ' + string)


def print_success(string):
    print('\033[92m[+]\033[0m ' + string)


def print_info(string):
    print('\033[93m[?]\033[0m ' + string)

def f_init(q):
    extract_file.q = q

def extract_file(tuple):
    passwords, zipPath = tuple
    i=0
    with zipfile.ZipFile(zipPath) as zipf:
        for password in passwords:
            try:
                zipf.extractall(pwd=password)
                print("\n\n")
                print_success('Found password {}\n'.format(password.decode(encoding='UTF-8')))
                raise AssertionError
            except (RuntimeError,zipfile.BadZipfile) as e:
                pass
            except zlib.error:
                zipf = zipfile.ZipFile(zipf.filename)
            except KeyboardInterrupt :
                extract_file.q.put(i)
            # update the bar
            i+=1
            sys.stdout.write("\r\033[94m[*]\033[0m Progress : " + str(i) + " (" + str(round(i / len(passwords),2)) + "% )")
            sys.stdout.flush()

def poolManager(passwords,zipPath):
    start_time = time.time()
    q = Queue()
    with Pool(None, f_init, [q]) as pool:
        try :
            pool.map(extract_file, ((passwords,zipPath),))
        except AssertionError: # Savage way to terminate process (line 14-15)
            pool.terminate()
            eltime = time.time() - start_time
            print_success("Time elapsed : {}min {}sec".format(round(eltime//60),round(eltime%60)))
        except KeyboardInterrupt:
            pool.terminate()
            eltime = time.time() - start_time
            print("\n\n")
            print_error("You stopped the programm !")
            print_info("Time {}min {}sec".format(round(eltime//60),round(eltime%60)))
            print_info("Ratio : {}/s".format(round(q.get()/eltime)))
            exit(0)


def main():
    WORKING_DIR = os.path.dirname(os.path.realpath(__file__))+"/.."
    WORKING_DIR = os.path.normpath(WORKING_DIR)
    #os.chdir(WORKING_DIR+"/spf")
    os.system('clear')
    while 1 :
        print("    1. Dictionary Attack")
        print("    2. Brute Force Attack")
        i = input("Choose an attack :")
        if i == "1" :
            dictionaryAttack()
            break
        elif i == "2" :
            bruteForceAttack()
            break
        else :
            os.system("clear")
            print("Choose an attack by typing its number")


def dictionaryAttack():
    while 1 :
        zipPath = input("Zip File to crack : ").strip().replace("\\","")
        try :
            zipfile.ZipFile(zipPath.strip())
            break
        except (zipfile.BadZipfile) :
            os.system('clear')
            print_error("Be sure to enter a valid path to a zipfile !")
    os.system('clear')
    print_success("Zip file selected successfully")
    print("")
    while 1 :
        dictionaryPath = input("The dictionary file : ").strip().replace("\\","")
        try :
            open(dictionaryPath, 'rb')
            break
        except FileNotFoundError :
            os.system('clear')
            print_error("Be sure to enter a valid path to a dictionary !")

    print_status("Reading the dictionary")
    with open(dictionaryPath, 'rb') as pass_file:
        passwords = [i.strip() for i in pass_file]
        print_status("Trying all the provided passwords ...")
        poolManager(passwords,zipPath)


if __name__ == '__main__':
    main()
