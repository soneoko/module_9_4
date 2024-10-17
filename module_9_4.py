first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'w', encoding='utf-8')
        for i in data_set:
            if isinstance(i, list):
                file.write('[')
                for j in range(0, len(i) - 1):
                    if isinstance(i[j], str):
                        file.write("'" + i[j] + "', ")
                    else:
                        file.write(str(i[j]) + ", ")
                file.write("'" + i[-1] + "'")
                file.write(']' + '\n')
            else:
                file.write(i + '\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        import random
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())