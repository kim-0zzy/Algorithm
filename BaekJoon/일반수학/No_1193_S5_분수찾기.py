n = int(input())
i = 1
j = 2
cnt = 1


while(True):
    if (i >= n):
        break
    
    else:
        cnt +=1
        i += j
        j +=1

if cnt%2 :
    print("{1}/{0}".format( 1+ cnt-(1+i-n), 1+i-n)  )
else:
    print("{0}/{1}".format( 1+ cnt-(1+i-n), 1+i-n)  )
