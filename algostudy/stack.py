# Push 연산
# append 메소드를 통해 리스트의 마지막에 데이터 삽입
s = []

def my_push(item):
    s.append(item)


# 인덱스 연산을 활용한 구현
def my_push(item, size):
    global top
    top += 1
    if top == size:
        print('Overflow!')
    else:
        stack[top] = item

# 단순한 Push 연산
# 크기가 정해진 리스트와 인덱스 연산을 활용

size = 10
stack = [0] * size
top = -1

my_push(10, size)
top += 1
stack[top] = 20

# Pop 연산
# 남은 데이터 중 가장 늦게 저장 된 데이터를 삭제하는 연산
def my_pop():
    if len(s) == 0:
        print('Underflow')
        return
    else:
        return s.pop() #리스트 s의 마지막 원소 삭제

# 인덱스 연산을 이용한 Pop 연산
# 크기가 정해진 리스트와 인덱스 활용
def my_pop():
    global top
    if top == -1:
        print('Underflow')
        return 0
    else :
        top -= 1
        return stack[top+1]
print(my_pop())

if top > -1:
    top -= 1
    print(stack[top+1])


# 연습 문제 1
# 스택을 구현한 후, 이를 이용해 3개의 데이터를 저장하고 다시 3번 꺼내어 출력

top = -1
stack = [0]* 10

top += 1        #push(1)
stack[top] = 1
top += 1        #push(2)
stack[top] = 2
top += 1        #push(3)
stack[top] = 3

top -= 1        #pop()
print(stack[top+1])
top -= 1        #pop()
print(stack[top+1])
top -= 1        #pop()
print(stack[top+1])

st = []
st.append(1)
st.append(2)
st.append(3)
print(st.pop())
print(st.pop())
print(st.pop())

# 여러 종류 괄호 풀이

def is_valid_brackers(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack