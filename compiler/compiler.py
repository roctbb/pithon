import sys
import os

code = ""
core = ""
mode = "compile"


if len(sys.argv) < 2:
    print("Запуск: pithon filename.pi")
    exit()
try:
    core = open("pithon.core").read()
except:
    print("Не найден файл pithon.core")
    exit()

try:
    code = open(sys.argv[1]).read()
except:
    print("Файл {0} не найден".format(sys.argv[1]))
    exit()

if len(sys.argv) == 4:
    if sys.argv[2] == '-mode' and sys.argv[3] == "decompile":
        mode = 'decompile'

replace_dict = {}


lines = core.split("\n")
for line in lines:
    words = line.split('$')
    if mode == "compile":
        replace_dict[words[1]] = words[0]
    if mode == "decompile":
        replace_dict[words[0]] = words[1]

for command in replace_dict:
    code = code.replace(command, replace_dict[command])

if mode == "compile":
    code = code.replace('поплавок ', '')
    exec(code)
if mode == "decompile":
    print(code)