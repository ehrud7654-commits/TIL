### **문제: 길 찾기 로봇**

"""
**시나리오:**
5x5 크기의 2차원 평면이 있고,
로봇의 시작점은 `(0, 0)`입니다.
방향 문자열 `N, S, E, W`가 리스트로 주어질 때,
순서대로 1칸씩 이동합니다.
이동 중 평면을 벗어나는 입력은 없다고 가정할 때,
최종 위치 `(r, c)`를 반환하는 함수를 작성하세요.
"""

def get_final_position(commands):
    # 시작 위치
    r, c = 0, 0

    dr = [-1,1,0,0]
    dc = [0,0,1,-1]

    directions = ['N','S','E','W']

    for cmd in commands:
        for i in range(len(directions)):
            if cmd == directions[i]:
                r += dr[i]
                c += dc[i]
                break
    return r, c


# 테스트
commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = get_final_position(commands)
print(f"최종 위치: ({end_r}, {end_c})") # 최종 위치: (0, 1)

