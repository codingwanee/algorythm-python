# discard()
# add()
# clear()

def find_same(a):
    n = len(a)
    result = set()

    for i in range(0, n-1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same(name))

# 주어진 list의 중복을 제거하기 위해 set()로 변환해줌
def honeytip(name):
    a = set(name)
    return a

print(honeytip(name))

