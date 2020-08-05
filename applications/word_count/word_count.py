import re
def word_count(s):
    words = re.split(r'\s\W*|\W*\s|\W*$|^\W*', s)
    counts = {}
    for w in words:
       if w:
           w = w.lower()
           if w in counts:
               counts[w] += 1
           else:
                counts[w] = 1
    return counts
  



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))