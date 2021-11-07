###############################################################
# 버블 정렬 알고리즘 - 효율 따지지 않고 원리 이해를 위한 버전
# 가장 큰 값을 맨 뒤로 -> 그다음 큰 값을 맨 뒤에서 2번째로 -> 반복
###############################################################
def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break


def bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap