import sys

cyc = int(sys.stdin.readline())
word_arr = list()

for i in range(cyc):
    a = input()
    word_arr.append((len(a), a))

word = list(set(word_arr))
word.sort()
for i in range(len(word)):
    print(word[i][1])
