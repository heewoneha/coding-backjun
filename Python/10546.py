import sys #10546 <배부른 마라토너>

n = int(sys.stdin.readline())
dic = {}

for i in range(0, 2*n-1):
    person = sys.stdin.readline().rstrip()
    if person not in dic:
        dic[person]=1
    else:
        del dic[person]
        
print(*dic) #key