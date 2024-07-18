def solution(board, moves):
    answer = 0
    stack=[]
    
    for i in range(len(moves)):
        for j in range(len(board[0])):
            if board[j][moves[i] -1 ] == 0:
                continue
            else:
                stack.append(board[j][moves[i] -1 ])
                if len(stack) >1 and stack[-1] == stack[-2]:
                    k=stack.pop()
                    stack.pop()
                    #print(k)
                    answer+=2
                #print(j,moves[i] - 1,board[j][moves[i] -1 ])
                board[j][moves[i] -1 ] = 0
                break
            
    print(stack)
    
    return answer