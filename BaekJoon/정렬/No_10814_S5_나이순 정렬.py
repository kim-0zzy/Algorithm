import sys

cyc = int(sys.stdin.readline())
word_arr = list()

for i in range(cyc):
    age, name = sys.stdin.readline().split()
    word_arr.append((int(age), i, name))
    
word_arr = sorted(word_arr)
for a, s, n in word_arr:
    print("{} {}".format(a, n))
