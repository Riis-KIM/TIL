num = int(input())

for i in range(1, num+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        for item in str(i):
            if '3' == item or '6' == item or '9' == item:
                print('-', end = '')
        print(' ', end = '')
    else:
        print(i, end = ' ')