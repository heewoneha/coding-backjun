def postfix(l):
    st = []
    answer = ''

    for x in l:
        
        if (x >= 'A') and (x <= 'Z'):
            answer += x

        else:
            if x == '(':
                st.append(x)

            elif (x == '*') or (x == '/'):
                while (st and (st[-1] == '*' or st[-1] == '/')):
                    answer += st.pop()
                st.append(x)

            elif (x == '+') or (x == '-'):
                while (st and st[-1] != '('):
                    answer += st.pop()
                st.append(x)

            elif x == ')':
                while (st and st[-1] != '('):
                    answer += st.pop()
                st.pop() # 앞 괄호 빼기


    while st:
        answer += st.pop()

    print(answer)

postfix(list(input()))