from urllib.request import urlopen
with urlopen('http://sixty-north.com/c/t.txt') as story:
    print("Get from URL")
    print(story)
    story_words = []
    for line in story:
        line_words = 