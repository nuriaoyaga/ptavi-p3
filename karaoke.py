#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class KaraokeLocal(SmallSMILHandler):
    """Clase de Karaoke """
    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(fichero)
        self.datos = cHandler.get_tags()

    def __str__(self):
        linea = ""
        for elem in self.datos:
            linea = linea + elem[0]
            atributos = elem[1].items()
            for nombre, valor in atributos:
                linea = linea + '\t' + nombre + ' = ' + '"' + valor + '"'
            linea = linea + '\n'
        return linea

    def to_json(self, fichsmil, new=''):
        """if new == '':
            new = fichsmil.split('.')[0] + '.json'"""
        with open(new, 'w') as fichero_json:
            json.dump(self.datos, fichero_json, sort_keys=True, indent=4, separators=(' ', ': '))

    def do_local(self):
        for elem in self.datos:
            atributos = elem[1]
            try:
                url = atributos['src']
                if url != "cancion.ogg":
                    filename = url[url.rfind("/") + 1:]
                    data = urllib.request.urlretrieve(url, filename)
                    atributos['src'] = "http://" + data[0]
            except KeyError as e:
                pass


def abrirfichero():
    try:
        fich = open(sys.argv[1], 'r')
        return fich
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    except FileNotFoundError:
        sys.exit("Not file with this name")


if __name__ == '__main__':
    fichero = abrirfichero()
    print(fichero)
    karaoke = KaraokeLocal(fichero)
    print(karaoke)
    #karaoke.to_json(fichero)
    karaoke.do_local()
    karaoke.to_json(fichero, 'local.json')
