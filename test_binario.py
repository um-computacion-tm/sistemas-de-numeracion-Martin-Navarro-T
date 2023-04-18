import unittest
from binario2decimal import binario2decimal

class TestNumeracion(unittest.TestCase):
    def test_0(self):
        self.assertEqual(binario2decimal(0000), '0')
        
    def test_1(self):
        self.assertEqual(binario2decimal('0001'), '1')
    
    def test_2(self):
        self.assertEqual(binario2decimal('0010'), "2")

    def test_3(self):
        self.assertEqual(binario2decimal('0011'), "3")
    
    def test_4(self):
        self.assertEqual(binario2decimal('0100'), "4")
    
    def test_5(self):
        self.assertEqual(binario2decimal('0101'), "5")

    def test_6(self):
        self.assertEqual(binario2decimal('0110'), "6")
    
    def test_7(self):
        self.assertEqual(binario2decimal('0111'), "7")
    
    def test_8(self):
        self.assertEqual(binario2decimal(1000), "8") 
    
    def test_9(self):
        self.assertEqual(binario2decimal(1001), "9")
    
    def test_10(self):
        self.assertEqual(binario2decimal(1010), "10")
        
    def test_11(self):
        self.assertEqual(binario2decimal(1011), "11")
    
    def test_12(self):
        self.assertEqual(binario2decimal(1100), "12")
    
    def test_13(self):
        self.assertEqual(binario2decimal(1101), "13")
    
    def test_14(self):
        self.assertEqual(binario2decimal(1110), "14")
    
    def test_15(self):
        self.assertEqual(binario2decimal(1111), "15")
    
    def test_16(self):
        self.assertEqual(binario2decimal(10000), "16")

    def test_32(self):
        self.assertEqual(binario2decimal(100000), "32")
    
    def test_64(self):
        self.assertEqual(binario2decimal(1000000), "64")
    
    def test_128(self):
        self.assertEqual(binario2decimal(10000000), "128")
    
    def test_256(self):
        self.assertEqual(binario2decimal(100000000), "256")
    
    def test_512(self):
        self.assertEqual(binario2decimal(1000000000), "512")
    
    def test_1024(self):
        self.assertEqual(binario2decimal(10000000000), "1024")

if __name__ == '__main__':
    unittest.main()