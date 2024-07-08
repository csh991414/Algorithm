def solution(babbling):
    answer = 0
    patterns = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        i = 0
        prev_pattern = ""
        valid = True
        
        while i < len(word):
            matched = False
            for pattern in patterns:
                if word[i:i+len(pattern)] == pattern:
                    if pattern == prev_pattern:
                        valid = False
                        break
                    prev_pattern = pattern
                    i += len(pattern)
                    matched = True
                    break
            if not matched:
                valid = False
                break
        
        if valid:
            answer += 1
    
    return answer
