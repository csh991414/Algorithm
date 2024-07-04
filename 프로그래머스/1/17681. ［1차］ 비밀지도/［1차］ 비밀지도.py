def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        binum1 = format(arr1[i], 'b').zfill(n)
        binum2 = format(arr2[i], 'b').zfill(n)
        arr1[i] = binum1
        arr2[i] = binum2
        
        map_row=''
        for j in range(n):
            if binum1[j] == '1' or binum2[j] == '1':
                map_row += '#'
            else:
                map_row += ' '
        answer.append(map_row)

        
    return answer
