information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

c


# .items()
# information.items()


# 딕셔너리의 key와 value를 한 쌍으로 꺼내줌

# 실제로는 이런 구조예요:

# ('김시습', ['금오신화', '이생규장전', '만복자서포기'])
# ('허균', ['홍길동전', '장생전', '도문대작'])
# ...


# 즉, 튜플(tuple) 들의 묶음

# for author, book_list in information.items():
# 🔹 이 부분이 핵심
# for (key, value) in information.items():


# 이걸 변수 두 개로 나눠서 받는 것이에요.

# 그래서

# author ← key (작가 이름)

# book_list ← value (책 목록 리스트)