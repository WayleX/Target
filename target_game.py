"""
target game
"""
from typing import List
import random
def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    final_list=[]
    for _ in range(3):
        list_let=[]
        for _ in range(3):
            list_let.append(chr(97+random.randrange(26)))
        final_list.append(list_let)
    return final_list

def get_words(f_line: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    words=[]
    with open(f_line,'r', encoding="utf-8") as file:
        for line in file:
            x_line=list(line.strip())
            x_line[0]=x_line[0].lower()
            if len(x_line)<4 or x_line.count(letters[4])==0:
                continue
            k=0
            for i in x_line:
                if not i in letters:
                    k=1
            if k==1:
                continue
            k=0
            for i in x_line:
                if not x_line.count(i) <= letters.count(i):
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
    except EOFError:
        return words
    return words

def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict:\
     List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    mistakes=[]
    for word in user_words:
        if len(word)<4 or word.count(letters[4])==0:
            continue
        for i in word:
            if not i in letters:
                continue
        k=0
        for i in word:
            if not word.count(i) <= letters.count(i):
                k=1
        if k==1:
            continue
        if not word in words_from_dict:
            mistakes.append(word)
    return mistakes

def results():
    """
    connects all function together
    """
    just_list=generate_grid()
    list_chr=[]
    for itera_1 in range(3):
        for i in range(3):
            list_chr.append(just_list[itera_1][i])
    print(list_chr)
    print("Enter your words:")
    full_words=get_words("en.txt",list_chr)
    user_words=get_user_words()
    count=0
    for i in user_words:
        if i in full_words:
            count+=1
    almost_words=get_pure_user_words(user_words, list_chr, full_words)
    not_guessed=[]
    for i in full_words:
        if not i in user_words:
            not_guessed.append(i)
    print(f"Number of words guessed:{count}")
    print(f"Not guessed words:{not_guessed}")
    print(f"Words with bad spelling: {almost_words}")
    with open("results.txt", 'w',encoding="utf-8") as file:
        file.write(str(count))
        file.write("\n")
        file.write(str(not_guessed))
        file.write("\n")
        file.write(str(almost_words))
        file.write("\n")
    return None
#results()
