#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
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


def get_list(fich):
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(fich)
    list = cHandler.get_tags()
    return list


def print_list(lista):
    linea = ""
    for elem in lista:
        linea = linea + elem[0]
        atributos = elem[1].items()
        for nombre, valor in atributos:
            linea = linea + '\t' + nombre + ' = ' + '"' + valor + '"'
        linea = linea + '\n'
    print (linea)


def to_json(list):
    with open('karaoke.json', 'w') as fichero_json:
        json.dump(list, fichero_json, sort_keys=True, indent=4, separators=(' ', ': '))


if __name__ == '__main__':
    fichero = abrirfichero()
    lista = get_list(fichero)
    print_list(lista)
    to_json(lista)
