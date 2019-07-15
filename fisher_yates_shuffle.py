from random import randint, random
from math import floor


def shuffle(the_list):
    amnt_to_shuffle = len(the_list)
    # We stop at 1 because anything * 0 is 0 and 0 is the first index in the list
    # so the final loop through would just cause the shuffle to place the first
    # element in... the first position, again.  This causes this shuffling
    # algorithm to run O(n-1) instead of O(n).
    while amnt_to_shuffle > 1:
        # Indice must be an integer not a float and floor returns a float
        i = int(floor(random() * amnt_to_shuffle))
        # We are using the back of the list to store the already-shuffled-indice,
        # so we will subtract by one to make sure we don't overwrite/move
        # an already shuffled element.
        amnt_to_shuffle -= 1
        # Move item from i to the front-of-the-back-of-the-list. (Catching on?)
        the_list[i], the_list[amnt_to_shuffle] = the_list[amnt_to_shuffle], the_list[i]
    return the_list
