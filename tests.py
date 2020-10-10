import unittest
import mediaIntersecao


# Suite de testes
class TestCases(unittest.TestCase):

    def test_mediaIntersecao_tam_maior_que_zero(self):
        self.assertEqual(1.5, mediaIntersecao.mediaIntersecao([1, 2, 9], [1, 2, 3]))

    def test_mediaIntersecao_tam_igual_a_zero(self):
        self.assertEqual(0, mediaIntersecao.mediaIntersecao([1, 5, 7, 3, 6], [2, 9, 8]))


if __name__ == 'main':
    unittest.main()

