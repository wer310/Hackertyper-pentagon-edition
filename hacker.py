import json
import random
from time import sleep
from colorama import Fore
from tqdm import tqdm
print(Fore.GREEN)
print("\t\t\tPENTAGON CONSOLE")

with open("commands.json") as f:
    commands = json.load(f)["commands"]

def get_output(com):
    for command in commands:
        if command["command"] == com:
            return command["output"]
    return "Команда не найдена!"

while True:
    com = input("command: ")
    if com == "exit": break
    if com == "help":
        print("-" + "\n-".join([command["command"] for command in commands]))
        continue
    if random.randint(0,100) <= 40:
        for _ in tqdm(range(random.randint(1,10))): sleep(random.randint(1,3))
    print(get_output(com.lower().strip().replace(" ", "_")))
