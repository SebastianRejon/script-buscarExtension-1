import os
def extensionesBack():
    """
    Exhibe los docuementos con extesi�n ".bak" que se encuentren
    en el directorio de ejecuci�n.

    Args:
        no recibe argumentos

    Returns:
        mensaje por pantalla
    """
    extension=".bak"
    ruta=os.getcwd()
    lista=os.listdir()
    print("* DOCUMENTOS BAK *")
    for i in lista:
            (print("- "+i)) if i[-4:]==extension else()
                  
if __name__=="__main__":
    extensionesBack()
os.system("Pause")