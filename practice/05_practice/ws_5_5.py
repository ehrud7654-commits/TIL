# 아래 함수를 수정하시오.
def even_elements():
    pass


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


# 아래 함수를 수정하시오.
def even_elements(numbers):

    even_list = []
    length = len(numbers)

    for i in range(length) :
        x = numbers.pop(0) #x=1을 가져오면 홀수이기 때문에 안들어가고 제거, 그리고 다음 맨 앞 숫자로 넘어감
        if x % 2 == 0 :
            even_list.extend([x])
            

    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)