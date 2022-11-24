# source: https://school.programmers.co.kr/learn/courses/30/lessons/135808?language=python3

'''
사과의 상태: 1점부터 k점까지

한 상자의 가격 결정 기준
- 한 상자에 사과 m개씩 담아 포장
- 가장 낮은 점수가 p점인 경우, 사과 한 상자의 가격은 p * m

가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익 계산
상자 단위로만 판매, 남는 사과는 버린다.
'''

def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    max_num_for_sale = len(score) // m * m
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            answer += min(score[i:i + m]) * m
    
    return answer