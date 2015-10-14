#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar un fichero SMILL
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.lista = []
        self.dic = {"root-layout": ['height', 'width', 'background-color'],
                    "region": ['id', 'top', 'bottom', 'left', 'right'],
                    "img": ['src', 'region', 'begin', 'dur'],
                    "audio": ['src', 'begin', 'dur'],
                    "textstream": ['src', 'region']}

    def startElement(self, name, attrs):
        """
        Método que el parsel llama cuando se encuentra una etiqueta de inicio
        """
        if name in self.dic:
            self.atributos = {}
            for item in self.dic[name]:
                self.atributos[item] = attrs.get(item, "")
            self.crear_lista(name, self.atributos)

    def get_tags(self):
        return self.lista

    def crear_lista(self, nombre, atributos):
        etiqueta = []
        etiqueta.append(nombre)
        etiqueta.append(atributos)
        self.lista.append(etiqueta)
        return self.lista


def print_list(list):
    for element in list:
        print(element)

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
    print_list(cHandler.get_tags())
