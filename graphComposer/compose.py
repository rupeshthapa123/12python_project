import string
import random
import re
import os
from graph import Graph, Vertex

def get_words_from_text(text_path):
    """
    It takes a text file, removes punctuation, and returns a list of words
    
    :param text_path: the path to the text file
    :return: A list of words
    """
    with open(text_path, 'rb') as f:
        text = f.read().decode("utf-8")

        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('','', string.punctuation))
    
    words = text.split()
    return words

def make_graph(words):
    """
    We're going to take a list of words, and create a graph where each word is a vertex, and each edge
    is the probability of going from one word to another
    
    :param words: A list of words
    :return: A graph object
    """
    g = Graph()

    previous_word = None

    for word in words:
        word_vertex = g.get_vertex(word)

        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex
    
    g.generate_probability_mappings()

    return g

def compose(g, words, length=50):
    """
    > Given a graph, a list of words, and a length, return a list of words of the given length, where
    each word is chosen randomly from the list of words, and the next word is chosen randomly from the
    list of words that follow the current word in the graph
    
    :param g: the graph
    :param words: a list of words to use as the starting point for the composition
    :param length: the length of the composition, defaults to 50 (optional)
    :return: A list of words
    """
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    
    return composition

def main(artist):
    """
    > We're going to take all the words from all the songs in the `songs` directory, make a graph out of
    them, and then use that graph to generate a new song
    
    :param artist: the artist you want to generate lyrics for
    :return: A string of words
    """
    # words from text
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # for song lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    g = make_graph(words)
    composition = compose(g, words, 100)
    return ' '.join(composition)

# This is a common pattern in Python. It allows you to run the main function of your program by
# entering `python filename.py` in the command line.
if __name__ == '__main__':
    print(main('taylor_swift'))

