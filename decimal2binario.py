import unittest

def decimal2binario(decimal, bits=0):
    """Convierte un número decimal a binario con un ancho de bits determinado"""
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    while len(binario) < bits:
        binario = "0" + binario
    return binario


if __name__ == '__main__':
    unittest.main()