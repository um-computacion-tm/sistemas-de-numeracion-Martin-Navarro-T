import unittest

def binario2decimal(binario):
    decimal = 0 
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal 

if __name__ == '__main__':
    unittest.main()