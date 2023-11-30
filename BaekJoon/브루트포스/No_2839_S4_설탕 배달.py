deliv = int(input())
count = 0
minus_cnt = 0
while (minus_cnt <= 11):
    
    if deliv <= 4 and deliv != 3 and deliv != 0:
        count = -1
        break
    
    if deliv % 5 == 0:

        count = count + deliv //5
        deliv = deliv%5

    else:
        deliv -= 3
        count +=1
        
    minus_cnt +=1

print(count)
