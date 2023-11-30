before_sent = list()
cyc = int(input())
count = 0
for i in range(0,cyc):
    sent = list(input())
    before_sent.append(sent[0])
    sent_count = 1
    for j in range(1,len(sent)):
        if (sent[j] not in before_sent):
            before_sent.append(sent[j])
            sent_count +=1
            continue

        if (sent[j] in before_sent) and (sent[j]==before_sent[-1]):
            continue

        if (sent[j] in before_sent) and (sent[j]!=before_sent[-1]):
            sent_count -=1
        

    if( len(before_sent) == sent_count ):
        count+=1
    sent_count = 0
    before_sent.clear()
print(count)
        
