# 아래 함수를 수정하시오.

#내장함수 쓰기

def remove_duplicates(numbers):

    new_lst = list(set(numbers))

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)


#내장함수 안쓰기


def remove_duplicates(numbers):

    new_lst = []

    for i in numbers :
        if i not in new_lst :
            new_lst.append(i)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)