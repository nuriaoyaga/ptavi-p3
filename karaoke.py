#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


def abrirfichero():
    try:
        fich = open(sys.argv[1], 'r')
        return fich
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    except FileNotFoundError:
        sys.exit("Not file with this name")

def print_list(lista):
    pass


if __name__ == '__main__':
    fichero = abrirfichero()
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(fichero)
    print(cHandler.get_tags())
