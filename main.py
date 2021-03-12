import os
import random
import time
def listen_command():
    return input('Ваша команда: ')

def do_this_command(message):
    message = message.lower()
    if 'привет петя' in message:
        say_message('Привет, Дамир!')
    elif 'пока петя' in message:
        say_message('Пока, Дамир')
        exit()
    else:
        say_message('Команда не распознана!')
def say_message(message):
    print(f"Голосовой ассистент: {message}")

if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)

