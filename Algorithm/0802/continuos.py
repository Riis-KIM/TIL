T = int(input())

for test_case in range(1, T+1):

    length = int(input())
    arr = input()

    max_count = 0
    count = 0


    for i in range(length):
        if arr[i] == '1':
            count+=1
            if i == length-1:
                if max_count < count:
                    max_count = count
        else:
            if max_count < count:
                max_count = count
            count=0
    print(f'#{test_case} {max_count}')











    # while i <= length:
    #     if arr[i] == '1' and i < length:
    #         count += 1
    #         i += 1
    #         if i == length:
    #             if max_count < count:
    #                 max_count = count
    #             break
    #     else:
    #         if max_count < count:
    #             max_count = count
    #         count = 0
    #         i += 1
    # print(f'#{test_case} {max_count}')