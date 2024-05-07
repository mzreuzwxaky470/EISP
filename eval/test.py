# point_file = "/home/user/Automatic-Code-Evaluation/eval/result/GPT3.5Point.txt"
# #
# with open(point_file, "r") as f:
#     point = []
#     for line in f:
#         line = line.strip('\n')
#         point.append(line)
#     print(point)
#     print(len(point))
import json
file_path1="/home/user/cl/EISP/eval/result/gpt4_EISP/llama3_70b/100/1_format.json"
file_path2="/home/user/cl/EISP/eval/result/gpt4_EISP/llama3_70b/379/2_format.json"
file_path3="/home/user/cl/EISP/eval/result/gpt4_EISP/llama3_70b/1_format.json"
with open(file_path1, "r") as f:
    result_dict1 = json.load(f)
with open(file_path2, "r") as f:
    result_dict2 = json.load(f)

result_dict1["leetcode"].update(result_dict2["leetcode"])
result_dict1["humanevalx"].update(result_dict2["humanevalx"])
result_dict1["gfg"].update(result_dict2["gfg"])
print(len(result_dict1["leetcode"]))
print(len(result_dict1["humanevalx"]))
print(len(result_dict1["gfg"]))
with open(file_path3,'w') as f:
            json.dump(result_dict1,f)  