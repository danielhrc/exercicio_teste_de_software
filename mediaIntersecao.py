# Código implementado
def mediaIntersecao(primeiro_array, segundo_array):
    intersecao_array = []
    media = 0

    for valor in primeiro_array:
        if valor in segundo_array and valor not in intersecao_array:
            intersecao_array.append(valor)

    if len(intersecao_array) != 0:
        for value in intersecao_array:
            media = value + media
        media = media/len(intersecao_array)

    return media
