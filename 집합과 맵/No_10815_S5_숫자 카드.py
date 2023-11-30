import sys

my_card_count = int(sys.stdin.readline())
my_card_list = sys.stdin.readline().split()

not_my_card_count = int(sys.stdin.readline())
not_my_card_list = sys.stdin.readline().split()


card_dict = {}
for i in range(my_card_count):
    card_dict[my_card_list[i]] = 0

for j in range(not_my_card_count):
    if not_my_card_list[j] in card_dict:
        print(1, end=" ")
    else:
        print(0, end=" ")
