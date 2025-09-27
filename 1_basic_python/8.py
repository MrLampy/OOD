class TorKham:
    def __init__(self):
        self.words = []
        self.original_words = []
    
    def play(self):
        initial = []
        answer = []
        if len(self.words[0]) == 2:
            if self.original_words[0][0] == 'P':
                    initial.append(self.original_words[0][1])
                    answer.append(f'\'{self.original_words[0][1]}\' -> {initial}')
            for i in range(1,len(self.original_words)):
            # print(self.original_words[i])
                if(len(self.words[i]) == 2) and self.original_words[i][0] in ['P', 'R', 'X']:
                    if self.original_words[i][0] == 'P':
                            if len(initial) == 0:
                                initial.append(self.original_words[i][1])
                                answer.append(f"\'{self.original_words[i][1]}\' -> {initial}")
                    if len(self.words[i-1]) == 2:
                        if self.original_words[i][0] == 'P':
                            if self.words[i-1][1][-2:] == self.words[i][1][:2]:
                                initial.append(self.original_words[i][1])
                                answer.append(f"\'{self.original_words[i][1]}\' -> {initial}")
                            else:
                                answer.append(f"\'{self.original_words[i][1]}\' -> game over")
                                break
                elif self.original_words[i][0] == 'X':
                    break
                elif self.original_words[i][0] ==  'R':
                    answer.append("game restarted")
                    initial = []
                else:
                    answer.append(f"\'{self.original_words[i][0]} {self.original_words[i][1]}\' is Invalid Input !!!")
                    break
        elif self.original_words[0][0] ==  'R':
            answer.append("game restarted")
            for i in range(1,len(self.original_words)):
                # print(self.original_words[i])
                if(len(self.words[i]) == 2) and self.original_words[i][0] in ['P', 'R', 'X']:
                    if self.original_words[i][0] == 'P':
                            if len(initial) == 0:
                                initial.append(self.original_words[i][1])
                                answer.append(f"\'{self.original_words[i][1]}\' -> {initial}")
                    if len(self.words[i-1]) == 2:
                        if self.original_words[i][0] == 'P':
                            if self.words[i-1][1][-2:] == self.words[i][1][:2]:
                                initial.append(self.original_words[i][1])
                                answer.append(f"\'{self.original_words[i][1]}\' -> {initial}")
                            else:
                                answer.append(f"\'{self.original_words[i][1]}\' -> game over")
                                break
                elif self.original_words[i][0] == 'X':
                    break
                elif self.original_words[i][0] ==  'R':
                    answer.append("game restarted")
                    initial = []
                else:
                    answer.append(f"\'{self.original_words[i][0]} {self.original_words[i][1]}\' is Invalid Input !!!")
                    break
        else:
            answer.append(f"\'{self.original_words[i][0]} {self.original_words[i][1]}\' is Invalid Input !!!")
        return answer



torkham = TorKham()

print("*** TorKham HanSaa ***")

Original = input("Enter Input : ")
use_original = [i.split(' ') for i in Original.split(",")]
# print(use_original[0][0])
S = [i.split(" ") for i in Original.lower().split(',')]
torkham.words = S
torkham.original_words = use_original
result = torkham.play()
for line in result:
    print(line)