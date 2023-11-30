sent = list(input())
count = 0
z_count = 0

before_sent = sent[0]
for i in range(1,len(sent)):


    if sent[i] ==  '=':
        if i >= 2 :
            if sent[i-2] == 'd' and sent[i-1] == 'z':
                count -= 2
                continue
            
        if i >= 1:
            if sent[i-1] == 'c' or sent[i-1] == 'z' or sent[i-1] == 's' :
                count -= 1
                continue

    elif sent[i] == '-':
        if sent[i-1] == 'c' or sent[i-1] == 'd' :
            count -= 1
            continue

    elif sent[i] == 'j':
        if sent[i-1] == 'l' or sent[i-1] == 'n' :
            count -= 1

print(len(sent) + count)
