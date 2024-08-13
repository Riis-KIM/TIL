T = int(input())

for test_case in range(1, T+1):

    word = input()

    i = 0
    ball = 0
    while i < len(word):
        if word[i] == '(':
            if word[i+1] == '|' or word[i+1] ==')':
                ball += 1
                i += 2
        elif word[i] == ')' and word[i-1] != '.':
            if word[i  1] == '|' or word[i - 1] == '(':
                ball += 1
                i += 1
        else:
            i += 1

    print(f'#{test_case} {ball}')
