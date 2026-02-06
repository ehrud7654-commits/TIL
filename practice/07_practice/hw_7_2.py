# 아래 클래스를 수정하시오.
class StringRepeater:

    def __init__(self, number, string):
        self.number = number
        self.string = string

    def repeat_string(self):
        for _ in range(self.number):
            print(self.string)
    


repeater1 = StringRepeater(3, 'Hello')
repeater1.repeat_string()


# # 아래 클래스를 수정하시오.
# class StringRepeater:
#     pass


# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")
