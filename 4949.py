from collections import deque #4949번 <균형잡힌 세상>
while True:
    s = input()
    if s=='.': #맨 마지막에 . 하나가 종료 요청
        break
    
    tmp = True
    stack = deque()
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i ==')':
            if not stack or stack[-1]=='[': #스택이 비어있거나
                tmp = False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif i ==']':
            if not stack or stack[-1]=='(': #스택이 비어있거나
                tmp = False
                break
            elif stack[-1]=='[':
                stack.pop()

    if tmp == True and not stack:
        print('yes')
    else:
        print('no')