#!/usr/local/bin/python3
import sys
import os
from importlib import util

# import termcolor
_spec = util.spec_from_file_location(
    "colorama",
    "/usr/local/lib/python3.5/site-packages/termcolor.py"
)
termcolor = util.module_from_spec(_spec)
_spec.loader.exec_module(termcolor)

cprint = termcolor.cprint
colored = termcolor.colored

PREFIX = '.'

class Creator:
    def __init__(self, mod_name):
        self.mod_name = mod_name

    def create_filename(self):
        self.filename = '{}{}'.format(PREFIX, self.mod_name)

    def write(self, lines):
        f = open(self.filename, 'w')
        f.writelines(lines)

    def serialize(self, module):
        self.create_filename()
        self.write(module.ZKERO_LINES)

def show_zkero_list():
    for f in os.listdir():
        if f.startswith('zkero_') and f.endswith('.py'):
            print(
                'zkero_'
                + colored(f.replace('zkero_', '', 1).replace('.py', ''), 'green')
                + '.py'
            )


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        cprint('Kerror 0: Command is crazy', 'red')
        print(
'''Command List:
    ./zmanage.py list
    ./zmanage.py build [filename]''')
        exit(1)

    command = sys.argv[1]
    if command == 'list':
        show_zkero_list()
        exit(0)

    if command != 'build' or len(sys.argv) <=2 or len(sys.argv) > 3:
        cprint('Kerror 0: Command is crazy', 'red')
        print(
'''Command List:
    ./zmanage.py list
    ./zmanage.py build [filename]''')
        exit(1)

    filename = sys.argv[2]

    if not '.py' in filename:
        cprint('Kerror 1: This is not Python file!', 'red')
        exit(1)
    if not filename.startswith('zkero_'):
        cprint("Kerror 2: 'zkero_' must be needed to this filename for prefix.", 'red')
        exit(1)

    mod_name = filename.replace('.py', '')
    try:
        mod = __import__(mod_name)
    except Exception as e:
        cprint('Kerror 3: module cannot be imported!', 'red')
        cprint(e, 'red')
        exit(1)

    print('🐟  module ' + colored(mod.__name__, 'green') + ' was imported.')

    creator = Creator(mod_name=mod_name)
    creator.serialize(mod)

    cprint('😃  Success! It was written.', 'cyan')
    print('🐷  '+ colored(creator.filename, 'red') + ' was edited.')
