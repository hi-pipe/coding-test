# source: https://school.programmers.co.kr/learn/courses/30/lessons/138477?language=python3

from collections import deque

def solution(k, score):
    answer = []
    hall_of_fame = []
    score = deque(score)
    
    while score:
        hall_of_fame.append(score.popleft())
        hall_of_fame.sort()
        
        answer.append(min(hall_of_fame[-k:]))
    
    return answer