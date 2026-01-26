# 아래 함수를 수정하시오.
def find_min_max(numbers):
    
    # num_max = numbers[0]
    # for num in numbers :
    #     if num > num_max :
    #         num_max = num

    # num_min = numbers[0]
    # for num in numbers :
    #     if num < num_min :
    #         num_min = num

    # return num_min, num_max


    num_min = numbers[0]
    num_max = numbers[0]
    for num in numbers :
        if num < num_min :
            num_min = num
        
        if num > num_max :
            num_max = num

    return num_min, num_max
        

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
