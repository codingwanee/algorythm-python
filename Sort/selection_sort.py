###############################################################
# 선택 정렬 알고리즘 - 효율 따지지 않고 원리 이해를 위한 버전
# 주어진 리스트에서 최솟값을 하나 찾아 정렬배열의 가장 끝에 삽입 x 반복
###############################################################
def find_min_idx(lst):  # 주어진 리스트에서 최솟값의 위치를 돌려주는 함수
    n = len(lst)
    min_idx = 0
    for i in range(1, n):
        if lst[i] < lst[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(lst):
    result = [] # 새 리스트를 만들어 정렬된 값을 저장
    while lst:  # 주어진 리스트에 값이 남아 있는 동안 계속
        min_idx = find_min_idx(lst) # 리스트에 남아 있는 값 중 최솟값의 위치
        value = lst.pop(min_idx)    # 찾은 최솟값을 빼내어 value에 저장
        result.append(value)        # value를 결과 리스트 끝에 추가


###############################################################
# 일반적인 선택 정렬 알고리즘
###############################################################
def selection_sort(lst):
    n = len(lst)
    for i in range(0, n-1): # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        # 찾은 최솟값을 i번 위치로
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

lst = [2, 4, 5, 1, 3]
selection_sort(lst)
print(lst)
