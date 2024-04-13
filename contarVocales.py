import unittest

#agregar tildes

def quitar_tildes(palabra):
    
    dict_tildes = {
        "á": "a",
        "é": "e", 
        "í": "i", 
        "ó": "o", 
        "ú": "u"}
    
    for letra in palabra:

        if letra in "áéíóú":
            palabra = palabra.replace(letra, dict_tildes.get(letra))
    
    return palabra


def contar_vocales(mi_string):
    
    nuevo_string = mi_string.lower()
    nuevo_string = quitar_tildes(nuevo_string)

    resultado = {}


    for letra in nuevo_string:
        
        if letra in 'aeiou':
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1    

    return resultado


class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        resultado = contar_vocales('zzz')
        self.assertEqual(resultado, {})

    def test_a(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})
    
    def test_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})
    
    def test_casAnOva(self):
        resultado = contar_vocales('casAnOva')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    
    def test_HeLAdO(self):
        resultado = contar_vocales('HeLAdO')
        self.assertEqual(resultado, {'e': 1, 'a': 1, 'o': 1})

    def test_última(self):
        resultado = contar_vocales('última')
        self.assertEqual(resultado, {'u': 1, 'i': 1, 'a': 1})
    
    def test_cAnción(self):
        resultado = contar_vocales('cAnción')
        self.assertEqual(resultado, {'a': 1, 'i': 1, 'o': 1})
    



unittest.main()

#palabra = str(input("Inserte una palabra: "))
#print(contar_vocales(palabra))
