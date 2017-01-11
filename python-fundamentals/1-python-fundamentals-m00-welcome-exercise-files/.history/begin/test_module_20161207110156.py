# import words 
from words as words import *
story_words = words.fetch_words('http://sixty-north.com/c/t.txt')
words.print_words(story_words)