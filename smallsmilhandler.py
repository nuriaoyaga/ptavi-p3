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
        self.width = ""
        self.height = ""
        self.bground_color = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.begin = ""
        self.dur = ""
        self.region = ""

    def startElement(self, name, attrs):
        """
        Método que el parsel llama cuando se encuentra una etiqueta de inicio
        """
        if name == "root-layout":
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.bground_color = attrs.get('background-color', "")

        elif name == "region":
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('rigth', "")

        elif name == "img":
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.region = attrs.get('region', "")

        elif name == "audio":
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")

        elif name == "textstream":
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
