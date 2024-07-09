import re

def solution(dartResult):
    # 정규 표현식을 이용해 점수, 보너스, 옵션을 추출
    pattern = re.compile(r'(\d+)([SDT])([*#]?)')
    matches = pattern.findall(dartResult)
    
    scores = []
    
    for i, match in enumerate(matches):
        score, bonus, option = match
        score = int(score)
        
        if bonus == 'S':
            score = score ** 1
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
            
        if option == '*':
            score *= 2
            if i > 0:
                scores[i - 1] *= 2
        elif option == '#':
            score *= -1
            
        scores.append(score)
    
    return sum(scores)

