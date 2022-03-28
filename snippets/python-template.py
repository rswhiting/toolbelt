#!/usr/bin/env python3
# File name: format.py
# Author: 
# Date: 
#
# Description: Basic format for Python scripts

import sys
import argparse
import logging as log

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class bvisuals:
    SUCCESS = bcolors.OKGREEN + '\u2713' + bcolors.ENDC + "  "     # Green checkmark
    FAIL = bcolors.FAIL + '\u2622' + bcolors.ENDC + "  "           # ☢ failure
    LIST = bcolors.WARNING + '\u2192' + bcolors.ENDC + "  "        # → arrow pointing
    NOTE = bcolors.OKCYAN + '\u259E' + bcolors.ENDC + "  "         # ▞ Note
    DEBUG = bcolors.WARNING + '\u26A1' + bcolors.ENDC + " "        # ⚡ Lightning bolt



def parse_arguments():
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands')
    parser.add_argument('-v', metavar='verbosity', type=int, default=4,
        help='Verbosity of logging: 0-critical, 1-error, 2-warning, 3-info, 4-debug')

    args = parser.parse_args()
    verbose = {0: log.CRITICAL, 1: log.ERROR, 2: log.WARNING, 3: log.INFO, 4: log.DEBUG}
    log.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)
    
    return args



def main(args):
    log.debug(bvisuals.SUCCESS + "Success message")
    log.debug(bvisuals.FAIL + "Fail message")
    log.debug(bvisuals.LIST + "List message")
    log.debug(bvisuals.NOTE + "Note message")
    log.debug(bvisuals.DEBUG + "Debug message")
    pass



if __name__ == '__main__':
    args = parse_arguments()
    main(args)