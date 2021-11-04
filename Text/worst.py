# 최악의 경우 O(nm)이 걸리는 문자열 검색

t = input('Text: ')
p = input('Pattern: ')

for i in range(len(t) - len(p)):
    for j in range(len(t)):
        if t[i+j] == p[j]:
            j+=1
        else:
            break
