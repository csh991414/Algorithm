def solution(a, b):
    
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    months = [31, 29, 31,30,31,30,31,31,30,31,30,31]
    days=5
    for i in range(a-1):
        days += months[i]
    days += b
    
    answer = day[days%7-1]
    
    
    
    return answer