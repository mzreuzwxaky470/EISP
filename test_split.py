from OverallLogicToken import *
#
from myAPItoken import *
from code_extra import extract_dependencies,add_assign
#，”“，
from BufferClass import CodeStructure

input_tokens = 0
output_tokens = 0
task=0
# problem_statement = open('EISP/problem_statement.txt').read()
use_problem_statement = False

#problem_statement
# problem_statement = problem_statement.replace(" ","")
problem_statement=""
pre_logic = ""
source_code=open('EISP/data/source_code.py').read()
target_code=open('EISP/data/target_code.js').read()

# source_code="""
# i = i // 10;
# """
# target_code="""
# i = i / 10;
# """
# 
# locate_error(source_code,target_code)

# map_result=map_code(source_code,target_code)
# python_extracted,js_extracted=get_map(map_result)

# python_extracted=['w']
# js_extracted=[]
# code_struct=None
# codeNet_input,codeNet_logic,codeNet_output = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
# print("：",codeNet_logic)
code_test="""
for i, c in enumerate(s):
    res.append(c)
    t += 1
    if t == cnt:
        t = 0
        cnt = k
        if i != len(s) - 1:
            res.append('-')
    elif t < cnt:
        res.append('-')
    else:
        cnt = k
    if t != cnt:
        t = 0
        cnt = k
        if a != len(s) - 1:
            res.append('-')
"""
# loc_code(code_test,'w',)
python_extracted=[
['def f_gold(s: str) -> int:', [1]],
['if not s:', [2]],
['return 0', [3]],
['n = len(s)', [4]],
['if n == 0:', [5]],
['return 0', [6]],
['i = 0', [7]],
["while s[i] == ' ':", [8]],
['i += 1', [9]],
['if i == n:', [10]],
['return 0', [11]],
["sign = -1 if s[i] == '-' else 1", [12]],
["if s[i] in ['-', '+']:", [13]],
['i += 1', [14]],
['res, flag = 0, (2**31 - 1) // 10', [15]],
['while i < n:', [16]],
['if not s[i].isdigit():', [17]],
['break', [18]],
['c = int(s[i])', [19]],
['if res > flag or (res == flag and c > 7):', [20]],
['return 2**31 - 1 if sign > 0 else -(2**31)', [21]],
['res = res * 10 + c', [22]],
['i += 1', [23]],
['return sign * res', [24]]
]
# b="i += 1\nres, flag = 0, (2**31 - 1) // 10"
# python_extracted,rest_py_code=get_py_map(b,python_extracted)
# print(python_extracted)
# print(rest_py_code)

source_code="""
def f_gold(s: str) -> int:
    if not s:
        return 0
    n = len(s)
    if n == 0:
        return 0
    i = 0
    while s[i] == ' ':
        i += 1
    if i == n:
        return 0
    sign = -1 if s[i] == '-' else 1
    if s[i] in ['-', '+']:
        i += 1
    res, flag = 0, (2**31 - 1) // 10
    while i < n:
        if not s[i].isdigit():
            break
        c = int(s[i])
        if res > flag or (res == flag and c > 7):
            return 2**31 - 1 if sign > 0 else -(2**31)
        res = res * 10 + c
        i += 1
    return sign * res

"""
code_struct=None
js_extracted=[['function f_gold(s) {', [1]],
['if (!s) return 0;', [2,3]],
['var n = s.length;', [4]],
['if (n == 0) return 0;', [5,6]],
['var i = 0;', [7]],
["while (s[i] == ' ') {", [8]],
['i++;', [9]],
['if (i == n) return 0;', [11]],
['var sign = -1;', [12]],
["if (s[i] == '-') sign = -1;", [12]],
['else sign = 1;', [12]],
["if (s[i] == '-' || s[i] == '+') i++;", [13]],
['var res = 0;', [15]],
['var flag = (Math.pow(2, 31) - 1) / 10;', [15]],
['while (i < n) {', [16]],
['if (!s[i].isDigit()) break;', [17]],
['var c = parseInt(s[i]);', [19]],
['if (res > flag || (res == flag && c > 7)) return Math.pow(2, 31) - 1;', [21]],
['if (sign < 0) return -(Math.pow(2, 31));', [21]],
['res = res * 10 + c;', [22]],
['i++;', [23]],
['return sign * res;', [24]]]
res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
print("：",res)