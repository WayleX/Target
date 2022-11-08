from typing import List
import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    final_list=[]
    for i in range(3):
        list_let=[]
        for iter_1 in range(3):
            list_let.append(chr(97+random.randrange(26)))
        final_list.append(list_let)
    return final_list
