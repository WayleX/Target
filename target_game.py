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

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words=[]
    x=[]
    with open(f,'r') as file:
        for line in file:
            x=list(line.strip())
            x[0]=x[0].lower()
            if len(x)<4 or x.count(letters[4])==0:
                continue
            k=0
            for i in range(len(x)):
                if not(x[i] in letters):
                    k=1
            if k==1:
                continue
            k=0
            for i in range(len(x)):
                if not (x.count(x[i]) <= letters.count(x[i])):
                    k=1
            if k==0:
                words.append(line.strip().lower())
    return words
def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    words=[]
    try:
        while True:
            word=input()
            if word=="":
                break
            words.append(word)
    except:
        return words
    return words
def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    mistakes=[]
    
    for word in user_words:
        if len(word)<4 or word.count(letters[4])==0:
            continue
        for i in range(len(word)):
            if not(word[i] in letters):
                continue
        k=0
        for i in range(len(word)):
            if not (word.count(word[i]) <= letters.count(word[i])):
                k=1
        if k==1:
            continue
        if not word in words_from_dict:
            mistakes.append(word)
    return mistakes