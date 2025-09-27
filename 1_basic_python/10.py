class funString():
    def __init__(self,string = ""):
        self.text = string

    # def __str__(self):
        ### Enter Your Code Here ###

    def size(self) :
        return len(self.text)

    def changeSize(self):
            result = ""
            for char in self.text:
                if 'A' <= char <= 'Z':
                    result += chr(ord(char) + 32)
                elif 'a' <= char <= 'z':
                    result += chr(ord(char) - 32)
                else:
                    result += char
            return result

    def reverse(self):
        text = list(self.text)
        ans =''
        for i in range(len(text)-1,-1,-1):
            ans += text[i]
        return ans

    def deleteSame(self):
        text = list(self.text)
        ans = []
        final = ''
        for i in text:
            if i not in ans:
                ans.append(i)
        for i in ans:
            final += i
        return final


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())