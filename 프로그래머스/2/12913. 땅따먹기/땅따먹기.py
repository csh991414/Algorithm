'''
핵심 : 완전탐색으로 풀게 되면 시간초과라 불가.
그리디로 접근했지만, 안되는 반례가 존재.
따라서, dp테이블로 접근 (동적프로그래밍)
아래로 행이 내려가면서, 이전행을 다음행에다가 더하는느낌으로
1번째 행의 1열을 제외한 것중에 최댓값을 2행 1열에 더하고,
1번째 행의 2열을 제외한 것중에 최댓값을 2행 2열에 더하고, 이런식으로 진행.


'''


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]
            #2번째 줄부터 시작하여 1번째 줄에서의 max값을 2번째줄에 더해준다.
# max(land[i -1][: j] + land[i - 1][j + 1:]) -> 하나 이전의 리스트중에서 j열을 제외하는방법이고, 이 중에 max를찾는법이다. 가운데 더하기는 리스트의 결합의 더하기를 의미함... 지린다..
    '''for i in range(len(land)):
        print(land[i])'''
    return max(land[-1])