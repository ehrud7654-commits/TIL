# 아래 함수를 수정하시오.
def count_character():
    pass


result = count_character("Hello, World!", "o")
print(result)  # 2


# 아래 함수를 수정하시오.
def count_character(sentence, num):
    count = 0
    for j in sentence :
        if j == num :
            count += 1 
    
    return count

    

result = count_character("Hello, World!", "o")
print(result)  # 2
