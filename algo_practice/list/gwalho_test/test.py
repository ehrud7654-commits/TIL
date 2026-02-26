T = int(input())

pairs = {
    ')': '(',
    '}': '{'
}

for tc in range(1, T+1):

    arr = input()
    stack = []
    valid = True

    for ch in arr:
        if ch in '({':
            stack.append(ch)
        elif ch in ')}':
            if not stack or stack[-1] != pairs[ch]:
                valid = False
                break
            stack.pop()

    if stack:
        valid = False





