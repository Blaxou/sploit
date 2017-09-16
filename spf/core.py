import os

from spf import fmt
from terminaltables import DoubleTable
import configparser

def execf(filename):
    exec(compile(open(filename, "rb").read(), filename, 'exec') )#, globals, locals)



def use(s):
    print('USING ' + s)

def show(arg):
    WORKING_DIR = os.path.dirname(os.path.realpath(__file__))+"/.."
    WORKING_DIR = os.path.normpath(WORKING_DIR)
    MODULE_DIR = WORKING_DIR + "/modules/"
    os.chdir(MODULE_DIR)
    if arg == "" :
        arg = "modules"
    fmt.print_info("Showing all "+arg+" in "+MODULE_DIR)
    table_data = [[fmt.red+"Module"+fmt.blue,fmt.red+"Description"+fmt.blue]]
    for dirname, dirnames, filenames in os.walk("."):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            #print(os.path.join(dirname, subdirname))
            pass
        # print path to all filenames.
        for filename in filenames:
            if filename == "file.py":
                mod = "/".join(os.path.join(dirname, filename).split("/")[1:-1])
                dirnameString = '/'.join(dirname.split('/')[1:])
                config = configparser.ConfigParser()
                config.read(dirname+'/file.cfg')
                desc = config['main']['description'].strip('"')
                table_data.append([ fmt.ylw+dirnameString+fmt.blue, fmt.ylw+desc+fmt.blue])
    table = DoubleTable(table_data)
    print(fmt.blue + table.table)
