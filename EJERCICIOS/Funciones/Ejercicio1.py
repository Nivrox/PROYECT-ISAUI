#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t
#ú “. Crea un programa principal donde se use dicha función luego del ingreso del usuario.
 
def espacios_enletras(cadena):

    letras = []
    for caracter in cadena:
        if  caracter.isalpha:
            letras.append(cadena)
            letras = " ".join(cadena)
        else:

            pass
        return letras

usuario = input("por favor ingresa una cadena de texto: ")
respuesta = espacios_enletras(usuario)
print (respuesta)