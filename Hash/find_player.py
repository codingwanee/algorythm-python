import numpy as np


def solution(participant, completion):
    answer = ''

    dic = {}

    for com in completion:
        hv = hash(com)
        dic[hv] = 0

    for com in completion:
        hv = hash(com)
        dic[hv] += 1

    for part in participant:
        hv = hash(part)
        if dic[hv] == 0:
            answer = part
            break
        else:
            dic[hv] -= 1

    return answer

A=["leo", "kiki", "eden"]
B=["eden", "kiki"]

print(solution(A,B))

def solution_wanee(participant, completion):
    answer = ''
    dic = {} # 해시함수를 이용할 dictionary 타입 변수 선언

    for par in participant:
        hv = hash(par)
        dic[hv] = 0

    for com in completion:
        hv = hash(com)
        dic[hv] += 1

    for par in participant:
        hv = hash(par)
        if dic[hv] == 0:
            answer = par
            break

    return answer


def solution(participant, completion):
    temp = {}  # key,value를 가진 딕셔너리 이용
    # 딕셔너리에 참가자 이름(key)과 해당 이름 사람수(value) 넣기
    for i in participant:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1

    # 완주자 이름(key)의 value가 1이면 지우기, 동명이인이면 -1
    for i in completion:
        if temp[i] == 1:
            del temp[i]
        else:
            temp[i] -= 1

    # 딕셔너리를 리스트로 바꾸고 가장 첫번째꺼 리턴(어차피 하나뿐)
    return list(temp.keys())[0]