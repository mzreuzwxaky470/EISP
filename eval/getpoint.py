#
import json
file = "/home/user/Automatic-Code-Evaluation/eval/result/others/GPT-4-turbo-COT.json"
point_file = "/home/user/Automatic-Code-Evaluation/eval/result/others/GPT-4-turbo-COT.txt"
#
point = []
with open(file, "r") as f:
    for line in f:
        print("gpt：",line)
        p = input("")
        with open(point_file, "a") as f:
            f.write(p+"\n")
        