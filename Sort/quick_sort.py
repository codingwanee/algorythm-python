###############################################################
# 퀵 정렬 알고리즘 - 효율 따지지 않고 원리 이해를 위한 버전
# 그룹을 둘로 나눠 재귀호출 but 병합정렬과 달리 미리 기준(pivot)과 비교
###############################################################
def solution(lst):
    n = len(lst)

    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return lst

    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = lst[-1] # 편의상 리스트의 마지막 값을 기준값으로 정함(좋은 기준을 정하는 법에 대해서는 따로 공부)
    g1 = []
    g2 = []
    for i in range(0, n-1): # 마지막 값은 기준 값이므로 제외
        if lst[i] < pivot:
            g1.append(lst[i]) # pivot보다 작은 값은 g1으로 분류
        else:
            g2.append(lst[i]) # pivot보다 큰 값은 g2로 분류

    # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return solution(g1) + [pivot] + solution(g2)

###############################################################
# 일반적인 삽입 퀵 알고리즘
###############################################################
def quick_sort(lst, start, end):
    # 종료 조건: 정렬 대상이 한 개 이하이면 정렬할 필요가 없음
    if end - start <= 0:
        return

    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = lst[end]    # 편의상 리스트의 마지막 값을 기준 값으로 정함
    i = start

    for j in range(start, end):
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[end] = lst[end], lst[i]

    # 재귀 호출 부분
    quick_sort(lst, start, i-1)
    quick_sort(lst, i+1, end)

# 리스트 전체(0 ~ len(lst)-1)를 대상으로 재귀 호출 함수 호출
def main(lst):
    quick_sort(lst, 0, len(lst) - 1)

d = [6, 3, 8, 8, 1, 2, 4, 7, 1]
main(d)
print(d)