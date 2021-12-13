# Another way of solving this problem without 
# using the OrderedDict provided by python
# would be to create a list along with the
# dictionary and iterate over that list in
# which the words will be stored in order
from collections import OrderedDict

n = int(input())
words = OrderedDict()

for i in range(n):
    word = str(input())
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

print(len(words.keys()))
print(' '.join(str(words[word]) for word in words))
