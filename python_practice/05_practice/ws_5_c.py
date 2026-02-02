original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

for char in original_word :
    arr.extend(char)

print(arr)


def restructure_word(word,arr) :
    for i in word :
        if i.isdecimal() == True :
            num = int(i)
            for _ in range(num) :
                arr.pop()
        else :
            arr.remove(i)

    return arr


result = restructure_word(word, arr)

print(result)

sentence = ''.join(result)

print(sentence)

# def restructure_word(word, arr):
#     pass

# original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
# word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
# arr = []

# result = restructure_word(word, arr)




# # extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)  # [1, 2, 3, 4, 5, 6]

# isdecimal() : 가장 엄격한 기준을 적용, 오직 일반적인 십진수 숫자(0-9)만 True로 인식
# print('isdecimal() 메서드 예시:')
# print('"12345".isdecimal():', '12345'.isdecimal())
# print('"123.45".isdecimal():', '123.45'.isdecimal())
# print('"-123".isdecimal():', '-123'.isdecimal())
# print('"Ⅳ".isdecimal():', 'Ⅳ'.isdecimal())
# print('"½".isdecimal():', '½'.isdecimal())
# print('"²".isdecimal():', '²'.isdecimal())
# print()