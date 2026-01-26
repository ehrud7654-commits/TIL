#이거 리스트 컴프리헨션 으로 출력해보기!

N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.

# for char in data_1 :
#     arr_1.append(char)

# print(arr_1)

for i in range(N) :
    arr_1.append(data_1[i])

print(arr_1)

#리스트 컴프리헨션: arr_1 = [data_1[i] for i in range[N]]


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.

arr_2 = data_2.split() #문자열의 리스트


for i in arr_2 :
    if int(i) % 2 : # Falsy/Trusy
        print(i)


# for i in arr_2 :
#     if int(i) % 2 == 1 : #문자열 -> 숫자형(정수)로 바꿔서 숫자 연산
#         print(i)


#리스트 컴프리헨션
# odds = [int[i] for i in arr_2 if int(i) % 2]
# for i in odds :
#     print(i)
