import unittest

#agregar tildes

def contar_vocales(mi_string):
    
    nuevo_string = mi_string.lower()
    resultado = {}
    
    for letra in mi_string:
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
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

# agregar mayusculas y minusculas

unittest.main()
