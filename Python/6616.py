def solution(N, what): #6616번 <문자열 암호화>
    copy = []
    for x in what:
        copy.append(x)

    if N > len(what):
        print(''.join(s for s in what))
        return

    x = 0
    for i in range(0, len(what)):
        j = 0
        while(i+N*j < len(what)):
            if(x == len(what)):
                print(''.join(s for s in copy))
                return
            copy[i+N*j] = what[x]
            x += 1; j += 1
    
while(True):
    N = int(input())
    if (N == 0):
        break
    else:
        string = input()
        string = string.replace(" ","")
        string = string.upper()
        solution(N, list(string))
    N -= 1