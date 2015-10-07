from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar un fichero SMILL
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.

    def startElement(self, name, attrs):
        """
        Método que el parsel llama cuando se encuentra una etiqueta de inicio
        """
        if name == "root-layout":

        elif name == "":

        elif name == "":

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser() #lee linea a linea
    cHandler = ChistesHandler() #manejador "listo" sabe que hacer cuando encuentra una etiqueta
    parser.setContentHandler(cHandler) #cuando se encuentra una etiqueta llama al "listo"
    parser.parse(open("karaoke.smil"))
