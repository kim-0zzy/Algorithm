import sys
import math

while(True):
    limit = int(input())
    if limit == 0:
        break
    prime_list = [1] * (2 * limit + 1)
    prime_list[0] = 0
    prime_list[1] = 0

    for i in range(2, int(math.sqrt(len(prime_list))+1) ):
        if prime_list[i] :
            
            for j in range(i + i, len(prime_list), i):
                prime_list[j] = 0


    print(sum (prime_list[ limit+1 : (limit*2)+1] ) )
        
