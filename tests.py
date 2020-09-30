import unittest
import statistics


class TestCases(unittest.TestCase):
    def mediaIntersecao(self, primeiro_array, segundo_array):
        intersecao_array = []

        for valor in primeiro_array:
            if valor in segundo_array and valor not in intersecao_array:
                intersecao_array.append(valor)

        if len(intersecao_array) == 0:
            intersecao_array.append(0)

        return statistics.mean(intersecao_array)


    def test_mediaIntersecao_tam_maior_que_zero(self):
        self.assertEqual(1.5, self.mediaIntersecao([1, 2, 9], [1, 2, 3]))

    def test_mediaIntersecao_tam_igual_a_zero(self):
        self.assertEqual(0, self.mediaIntersecao([1, 5, 7, 3, 6], [2, 9, 8]))


if __name__ == '__main__':
    unittest.main()
