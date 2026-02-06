def ordered_difference_sets(set1, set2):
    new_set1 = set1 - set2
    new_set2 = set2 -set1
    
    if len(new_set1) > len(new_set2) :
        return new_set2, new_set1
    elif len(new_set1) == len(new_set2) :
        return new_set1, new_set2
    else :
        return new_set1, new_set2
    

def ordered_difference_sets(set1, set2):
    diffs = [set1 - set2, set2 - set1]
    return tuple(sorted(diffs, key=len))



# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})


