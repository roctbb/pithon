import sys
import os
import subprocess
import uuid


def run(code, data, core_path = "pithon.core"):
    try:
        core=""
        try:
            core = open(core_path).read()
        except:
            return "Не найден файл pithon.core"

        replace_dict = {}


        lines = core.split("\n")
        for line in lines:
            words = line.split('$')
            replace_dict[words[1]] = words[0]

        for command in replace_dict:
            if code.find(replace_dict[command]) != -1:
                return "Неизвестная команда {0}".format(replace_dict[command]) 

        for command in replace_dict:
            code = code.replace(command, replace_dict[command])

        code = code.replace('поплавок ', '')
        filename = "tmp/"+str(uuid.uuid4())+".py"
        with open(filename, 'w') as tfile:
            tfile.write(code)
        process = subprocess.Popen(['python3', filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        process.stdin.write(data.encode('utf-8'))
        process.stdin.close()
        process.wait(timeout=3)
        errors = process.stderr.read().decode('utf-8')
        if len(errors)>0:
            return errors
        return process.stdout.read().decode('utf-8')
    except Exception as e:
        return str(e)


