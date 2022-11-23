# source: https://school.programmers.co.kr/learn/courses/30/lessons/136798

'''
각 기사는 자신의 기사 번호의 약수 개수에 해당하는 공격력을 가진 무기 구매.
협약에 의해 공격력의 제한수치가 있어, 제한수치보다 큰 공격력을 가진 무기를 구매해야 하면 협약에서 정한 공격력을 가진 무기 구매.
'''

def solution(number, limit, power):
    answer = 0
    
    divisor_number = [0] * (number + 1)
    
    for i in range(1, number + 1):
        j = 1
        
        while i * j < number + 1:
            divisor_number[i * j] += 1
            j += 1
            
    for i in range(1, number + 1):
        if divisor_number[i] > limit:
            answer += power
        else:
            answer += divisor_number[i]
    
    return answer