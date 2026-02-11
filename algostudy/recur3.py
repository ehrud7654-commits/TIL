def f(i,N,V):
    if i == N: # V를 못찾은 경우
        return 0
    elif A[i] == V:
        return 1
    else:
        f(i+1, N, v)

N = 3
A = [3, 7, 6]
v = 2

ans =f(0,N,V)