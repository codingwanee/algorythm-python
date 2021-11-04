###############################################################
# 삽입 정렬 알고리즘 - 효율 따지지 않고 원리 이해를 위한 버전
#
###############################################################
def ind_ins_idx(lst, v):    # 리스트 lst에서 v가 들어가야 할 위치를 돌려주는 함수
    # 이미 정렬된 리스트 lst의 자료를 앞에서부터 차례로 확인
    for i in range(0, len(lst)):
        # v 값보다 i번 위치에 있는 자료 값이 크면 v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
        if v < lst[i]:
            return i
    # 적절한 위치를 못 찾았을 때는 v가 lst의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
    return len(lst)

def ins_sort(lst):
    result = []
    while lst:
        value = lst.pop(0)
        ins_idx = find_ins_idx(result, value)

###############################################################
# 일반적인 삽입 정렬 알고리즘
###############################################################
def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        buffer = lst[i]  # i번 위치에 있는 값을 buffer에 저장
        j = i - 1     # j를 i 바로 왼쪽 위치로 저장
        while j >= 0 and lst[j] > buffer:
            lst[j+1] = lst[j]   # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동
            j -= 1
            lst[j + 1] = buffer    # 찾은 삽입 위치에 buffer를 저장


lst = [2, 4, 5, 1, 3]
insertion_sort(lst)
print(lst)