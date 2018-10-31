import unittest
from Encoder.encoder import encode_extended_Golay


class TestParser(unittest.TestCase):

    def test_encode_extended_Golay(self):
        self.assertEqual(encode_extended_Golay('101010101010'), '101010101010010010111100')


if __name__ == '__main__':
    unittest.main()
