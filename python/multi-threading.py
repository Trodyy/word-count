import threading
from collections import Counter

def count_words(text_part, result, index):
    words = text_part.split()
    result[index] = Counter(words)

text = open("../test.txt").read()
parts = text.split("\n\n")
result = [None] * len(parts)
threads = []

for i, part in enumerate(parts):
    t = threading.Thread(target=count_words, args=(part, result, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

final_count = Counter()
for r in result:
    final_count.update(r)

print(final_count)
