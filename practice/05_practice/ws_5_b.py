# # isupper
# string1 = 'HELLO'
# string2 = 'Hello'
# print(string1.isupper())  # True
# print(string2.isupper())  # False



data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.

for alpha in data_1 :
    if alpha.isupper() or alpha == ' ' :
        print(alpha, end='')


# # find
# text = 'banana'
# print(text.find('a'))  # 1
# print(text.find('z'))  # -1

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

words_to_find = ['내','힘','들','다']

for word in words_to_find :
    index = data_2.find(word)
    if index != -1 : #못찾으면 -1 반환하므로 
        arr.append(index)

print(arr)

arr.sort()
print(arr)

# print(data_2[5] + data_2[12] + data_2[29] + data_2[37])
print(data_2[5], data_2[12], data_2[29], data_2[37], sep='')




