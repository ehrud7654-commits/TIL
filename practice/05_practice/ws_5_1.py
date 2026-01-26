# 아래 함수를 수정하시오.
def reverse_string(sentence):
    sen_list = list(sentence)
    sen_list.reverse()
    
    return ''.join(sen_list)


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH 