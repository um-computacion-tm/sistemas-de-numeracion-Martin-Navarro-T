import unittest
from decimal2binario import decimal2binario

class TestNumeracion(unittest.TestCase):
    #Convierte un número decimal a binario con un ancho de bits determinado
    def test_0(self):
        self.assertEqual(decimal2binario(0, 4), '0000')
        
    def test_1(self):
        self.assertEqual(decimal2binario(1, 4), '0001')
    
    def test_2(self):
        self.assertEqual(decimal2binario(2, 4), "0010")

    def test_3(self):
        self.assertEqual(decimal2binario(3, 4), "0011")
    
    def test_4(self):
        self.assertEqual(decimal2binario(4, 4), "0100")
    
    def test_5(self):
        self.assertEqual(decimal2binario(5, 4), "0101")

    def test_6(self):
        self.assertEqual(decimal2binario(6, 4), "0110")
    
    def test_7(self):
        self.assertEqual(decimal2binario(7, 4), "0111")
    
    def test_8(self):
        self.assertEqual(decimal2binario(8, 4), "1000") 
    
    def test_9(self):
        self.assertEqual(decimal2binario(9, 4), "1001")
    
    def test_10(self):
        self.assertEqual(decimal2binario(10, 4), "1010")
        
    def test_11(self):
        self.assertEqual(decimal2binario(11, 4), "1011")
    
    def test_12(self):
        self.assertEqual(decimal2binario(12, 4), "1100")
    
    def test_13(self):
        self.assertEqual(decimal2binario(13, 4), "1101")
    
    def test_14(self):
        self.assertEqual(decimal2binario(14, 4), "1110")
    
    def test_15(self):
        self.assertEqual(decimal2binario(15, 4), "1111")
    
    def test_16(self):
        self.assertEqual(decimal2binario(16, 5), "10000")

    def test_32(self):
        self.assertEqual(decimal2binario(32, 6), "100000")
    
    def test_64(self):
        self.assertEqual(decimal2binario(64, 7), "1000000")
    
    def test_128(self):
        self.assertEqual(decimal2binario(128, 8), "10000000")
    
    def test_256(self):
        self.assertEqual(decimal2binario(256, 9), "100000000")
    
    def test_512(self):
        self.assertEqual(decimal2binario(512, 10), "1000000000")
    
    def test_1024(self):
        self.assertEqual(decimal2binario(1024, 11), "10000000000")

if __name__ == '__main__':
    unittest.main()