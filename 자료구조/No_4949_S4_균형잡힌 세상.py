sent = input()

while sent != '.':
    sent = list(sent)
    sck = list()
    for ss in sent:
        if ss == '[':
            sck.append('[')
            continue
        if ss == '(':
            sck.append('(')
            continue
        if ss == ']':
            if len(sck) == 0:
                sck.append(ss)
                break
            if sck[-1] == '[':
                del sck[-1]
            else:
                break
        if ss == ')':
            if len(sck) == 0:
                sck.append(ss)
                break
            if sck[-1] == '(':
                del sck[-1]
            else:
                break
    if len(sck) > 0:
        print('no')
    else:
        print('yes')
    sent = input()
