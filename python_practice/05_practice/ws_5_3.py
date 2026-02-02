# 아래 함수를 수정하시오.
def sort_tuple():
    new_tuple = ()
    pass
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)

# sort메서드 활용
def sort_tuple(numbers):
    my_list = list(numbers)
    my_list.sort()

    return tuple(my_list)


result = sort_tuple((5, 2, 8, 1, 3))
print(result)

#sorted() 활용
def sort_tuple(numbers):
    list(numbers)
    new_tuple = sorted(numbers)
    my_tuple = tuple(new_tuple)

    return my_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)



# def sort_tuple(numbers):
#     lst = list(numbers)   # 1️⃣ 튜플 → 리스트

#     n = len(lst)
#     for i in range(n):
#         for j in range(n - 1):
#             if lst[j] > lst[j + 1]:   # 2️⃣ 앞이 크면
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]  # 3️⃣ 자리 교환

#     return tuple(lst)