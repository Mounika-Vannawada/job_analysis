import re

def word_count(word, text):
    text = text.lower()
    print(text)
    count = re.findall( r'{}'.format(word), text)
    print(count)
    return len(count)


cnt = word_count("Python", "python, java, python")
print(cnt)