#10진수 2진수로 변환

print(bin(13))
print(hex(10))

#2진수, 16진수를 10진수로 변환
print(int('1101',2))
print(int('b', 16))


#비트 연산
print(bin(0b1101&0b1001))

print(13&9)

a = 5
b = 3

a = a ^ b
b = a ^ b
a = a ^ b

print(a)

#시프트 연산자 
print(0b0011<<2)      

#소수점 출력 방법
t1 = 3.141592

print(f'변수 값은 {t1:.2f}')
