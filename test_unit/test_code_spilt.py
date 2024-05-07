import sys
sys.path.append('/home/user/Automatic-Code-Evaluation')
from code_spilt import extract_second_indent,code_depth,code_strip_spaces

code = """
def maxTargetsToDestroy(H, W, M, targets):
    # Create a 2D boolean matrix to keep track of visited cells
    grid = [[False] * W for _ in range(H)]
    
    # Sort targets by their positions
    sorted_targets = sorted(targets, key=lambda x: (x[0], x[1]))
    
    # Place the bomb starting from the top left corner of the grid
    num_destroyed = 0
    for _, target in enumerate(sorted_targets):
        if not grid[target[0]][target[1]]:
            grid[target[0]][target[1]] = True
            
            # Destroy all targets in the same row or column as the bomb
            for i in range(target[0], target[0]+2):
                if i >= 0 and i < H:
                    for j in range(target[1], target[1]+2):
                        if j >= 0 and j < W:
                            if not grid[i][j]:
                                continue
                            elif grid[i][j] == target:
                                num_destroyed += 1
                                break
                            else:
                                break
                    
            for i in range(target[1], target[1]+2):
                if i >= 0 and i < W:
                    for j in range(target[0], target[0]+2):
                        if j >= 0 and j < H:
                            if not grid[j][i]:
                                continue
                            elif grid[j][i] == target:
                                num_destroyed += 1
                                break
                            else:
                                break
    
    return num_destroyed
"""

path = "/home/user/DatasetsConstruct/Deep.json"
#json
import json
max_depth = 0
depth = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}#
new_pair = []
with open(path, "r") as f:
    code_pair = json.load(f)
    for i in range(0,81):
        task = code_pair[i]["task_id"]
        CodenetCode = code_pair[i]["CodeNet_python_code"]
        CodenetCode = code_strip_spaces(CodenetCode)
        GenCode = code_pair[i]["Gen_python_code"]
        GenCode = code_strip_spaces(GenCode)
        #print(GenCode)
        d1 = code_depth(str(CodenetCode))
        d2 = code_depth(str(GenCode))
        if(d1>4  or d2>4):
            #json
            pair = code_pair[i]
            new_pair.append(pair)
            print("task:",task)
            print(i)
            

        depth[d1] += 1
        depth[d2] += 1
"""path = "/home/user/DatasetsConstruct/DeepCodeGPT.json"

with open(path, "w") as f:
    json.dump(new_pair,f)"""

