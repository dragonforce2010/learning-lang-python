# import words 
from words import *
story_words = fetch_words('http://sixty-north.com/c/t.txt')
words.print_words(story_words)