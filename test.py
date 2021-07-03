print('Первый способ: Без чтения линий. Самый простой способ')
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line)

print('Второй способ: С чтением всего файла сразу, не зацикливаясь на линиях')
with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

print('Третий способ: Все линии файла читаются и перемещаются в переменную, выводятся')
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)

print('Четвертый способ: Все линии читаются и перемещаются в список, список выводится')
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
content = []
for line in lines:
    content.append(line)
print(content)
