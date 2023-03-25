'''
    Dado uma string S, retorne True se todos os caracteres forem únicos e False caso exista algum duplicado.

    Valores em minúsculo e maiúsculo são considerados os mesmos.

    EX:
        >>>is_unique("Lucas")
        True
        
        >>>is_unique("LucasS")
        False
'''

import sys

def is_unique(string: str) -> bool:                                             #faz o que pede, porém faz lento
    count = 0

    for index, character in enumerate(string):
        for second_index, second_character in enumerate(string):
            if character == second_character and index != second_index:
                return False
            count += 1
    
    print("Total count:", count)
    return True


#outro formato de resolução
'''
def is_unique(string: str) -> bool:                                             #troca performace por mais espaço, pois o dicionário vai exigir mais espaço em memória para guardar a quantidade de caracteres
    character_seen = {}

    for character in string:
        if character_seen.get(character):
            return False
        character_seen[character] = True
        
    return True
'''


if __name__ == "__main__":
    try:
        string = sys.argv[1]
    except IndexError:
        string = "Lucas"

    print(f"is_unique({string}) ->", is_unique(string))