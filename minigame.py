from random import randint, shuffle
from os import system, name


class gameofnumbers:
    def __init__(self):
        self.rounds = 0
        self.mistakes = 0
        self.start_point = 0
        self.attempts = 1
        self.points = 0
        self.end_point = None
        self.system = None
        self.difficulty = None
        self.game_flag = True
        self.mistake_flag = False
        self.answer_list = []
        self.answer = (0, 0)  # (число в системе, десятичное значение)
        self.commands = ['выход', 'статистика'] 

    def cmd_clean(self):
        system('cls' if name == 'nt' else 'clear')

    def greeting(self):
        self.cmd_clean()
        print("\nПривет! Это игра <Переведи число из системы исчисления>.")
        print("Команды : выход, статистика.\n\n")
        input("Нажмите любую клавишу для продолжения . . . ")

    def getdifficulty(self):
        self.cmd_clean()
        while 1:
            try:
                print("\nДоступно 3 уровня сложности :\n  1) числа от 0 до 15.\n  2) числа от 0 до 256.\n  3) числа от 0 до 1023 \n")
                difficulty_inp = int(input("Выберите уровень сложности : \n>>  "))
                if difficulty_inp > 0 and difficulty_inp < 4:
                    self.difficulty = difficulty_inp
                    print(f"Отлично! Уровень сложности : {self.difficulty}.\n")
                    self.set_difficulty_parameters()
                    return
                else:
                    raise Exception
            except:
                print("Введите число от 1 до 3.")
            finally:
                input("Нажмите любую клавишу для продолжения . . . ")
                self.cmd_clean()

    def set_difficulty_parameters(self):
        if self.difficulty == 1:
            self.end_point = 15
        elif self.difficulty == 2:
            self.end_point = 255
        elif self.difficulty == 3:
            self.end_point = 1023
        
    def getsystem(self):
        self.cmd_clean()
        while 1:
            try:
                print("\nДоступно 3 системы исчисления :\n << 2(bin).\n << 8(oct).\n << 16(hex) \n")
                choice = int(input("Выберите систему исчисления (ввести только число): \n>>  "))
                if choice in (2,8,16):
                    self.system = choice
                    print("Выбранна ", choice, " система исчисления.\n")
                    return
                else:
                    raise Exception
            except:
                print("Выберите систему (2, 8, 16).")
            finally:
                input("Нажмите любую клавишу для продолжения . . . ")
                self.cmd_clean()

    def show_statistic(self):
        self.cmd_clean()
        print("Ваша игровая статистика :")
        print(f"Баллов : {self.points}; Раундов сыгранно : {self.rounds}")
        print(f"Oшибок совершенно : {self.mistakes}; Система исчисления : {self.system}\n\n")
        print("Нажмите любую клавишу для выхода . . . ")

    def byebye(self):
        print("До новых встреч!")
        self.show_statistic()
        input()
        exit()
        
    def generate_count(self):
        count = randint(self.start_point,self.end_point)
        if self.system == 2:
            self.answer =( bin(count)[2::], count )
        elif self.system == 8:
            self.answer =( oct(count)[2::], count )
        elif self.system == 16:
            self.answer =( hex(count)[2::], count )

    def make_answers(self):
        self.answer_list = [self.answer[1]]
        for _ in range(4):
            temp_answer = randint(self.start_point, self.end_point)
            self.answer_list.append(temp_answer)
        shuffle(self.answer_list)
        

    def show_answers(self):
        print(f"\nВаше число : {self.answer[0]}({self.system}).")
        print(f"Варианты ответов :")

        ansswers = "  "
        for i in range(5):
            ansswers += f"{self.answer_list[i]}  "
        print(ansswers)


    def check_answer(self, user_answer : str):
        if user_answer == str(self.answer[1]):
            self.mistake_flag = False
            self.points += 1
            print(f"Отлично! Вы дали верный ответ за {self.attempts} попыток. Балл засчитан.")
            self.attempts = 1
            self.rounds += 1

        elif user_answer.lower() in self.commands:
            if user_answer.lower() == "выход":
                self.byebye()
            elif user_answer.lower() == "статистика":
                self.show_statistic()

        else:
            self.attempts += 1
            self.mistakes += 1
            self.points -= 1
            self.mistake_flag = True
            print(f"Минус балл. Попробуйте еще!")

        input()
        self.cmd_clean()

game = gameofnumbers()

game.greeting()
game.getdifficulty()
game.getsystem()
while game.game_flag:
    if game.mistake_flag is False:
        game.generate_count()
        game.make_answers()
    game.show_answers()
    user_input = input("\n>>  ")
    game.check_answer(user_input)