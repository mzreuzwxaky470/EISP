map_result="""
### Python to JavaScript Translation Matching

#### Python Code (myAtoi)
```python
from typing import *   # --- py myAtoi stmt 1
def f_gold(s: str) -> int:   # --- py myAtoi stmt 2
    if not s:   # --- py myAtoi stmt 3
        return 0   # --- py myAtoi stmt 4
    n = len(s)   # --- py myAtoi stmt 5
    if n == 0:   # --- py myAtoi stmt 6
        return 0   # --- py myAtoi stmt 7
    i = 0   # --- py myAtoi stmt 8
    while s[i] == ' ':   # --- py myAtoi stmt 9
        i += 1   # --- py myAtoi stmt 10
        if i == n:   # --- py myAtoi stmt 11
            return 0   # --- py myAtoi stmt 12
    sign = -1 if s[i] == '-' else 1   # --- py myAtoi stmt 13
    if s[i] in ['-', '+']:   # --- py myAtoi stmt 14
        i += 1   # --- py myAtoi stmt 15
    res, flag = 0, (2**31 - 1) // 10   # --- py myAtoi stmt 16
    while i < n:   # --- py myAtoi stmt 17
        if not s[i].isdigit():   # --- py myAtoi stmt 18
            break   # --- py myAtoi stmt 19
        c = int(s[i])   # --- py myAtoi stmt 20
        if res > flag or (res == flag and c > 7):   # --- py myAtoi stmt 21
            return 2**31 - 1 if sign > 0 else -(2**31)   # --- py myAtoi stmt 22
        res = res * 10 + c   # --- py myAtoi stmt 23
        i += 1   # --- py myAtoi stmt 24
    return sign * res   # --- py myAtoi stmt 25
```

#### JavaScript Code (myAtoi)
```javascript
"use strict";   // --- js myAtoi stmt 1
function f_gold(s) {   // --- py myAtoi stmt 2
    if (!s) return 0;   // --- py myAtoi stmt 3, py myAtoi stmt 4
    var n = s.length;   // --- py myAtoi stmt 5
    if (n == 0) return 0;   // --- py myAtoi stmt 6, py myAtoi stmt 7
    var i = 0;   // --- py myAtoi stmt 8
    while (s[i] == ' ') {   // --- py myAtoi stmt 9
        i++;   // --- py myAtoi stmt 10
        if (i == n) return 0;   // --- py myAtoi stmt 11, py myAtoi stmt 12
    }
    var sign = s[i] == '-' ? -1 : 1;   // --- py myAtoi stmt 13
    if (s[i] == '-' || s[i] == '+') i++;   // --- py myAtoi stmt 14, py myAtoi stmt 15
    var res = 0;   // --- py myAtoi stmt 16 (part 1)
    var flag = (Math.pow(2, 31) - 1) / 10;   // --- py myAtoi stmt 16 (part 2)
    while (i < n) {   // --- py myAtoi stmt 17
        if (isNaN(s[i])) break;   // --- py myAtoi stmt 18, py myAtoi stmt 19 (adjusted for JS isNaN function)
        var c = parseInt(s[i]);   // --- py myAtoi stmt 20
        if (res > flag || (res == flag && c > 7)) {   // --- py myAtoi stmt 21
            if (sign > 0) return Math.pow(2, 31) - 1;   // --- py myAtoi stmt 22 (part 1)
            else return -(Math.pow(2, 31));   // --- py myAtoi stmt 22 (part 2)
        }
        res = res * 10 + c;   // --- py myAtoi stmt 23
        i++;   // --- py myAtoi stmt 24
    }
    return sign * res;   // --- py myAtoi stmt 25
}
```

"""
map_result="""

response: ### Python
### myAtoi 
from typing import *
def f_gold(s: str) -> int:   # --- py stmt 1
    if not s:   # --- py stmt 2
        return 0   # --- py stmt 3
    n = len(s)   # --- py stmt 4
    if n == 0:   # --- py stmt 5
        return 0   # --- py stmt 6
    i = 0   # --- py stmt 7
    while s[i] == ' ':   # --- py stmt 8
        i += 1   # --- py stmt 9
        if i == n:   # --- py stmt 10
            return 0   # --- py stmt 11
    sign = -1 if s[i] == '-' else 1   # --- py stmt 12
    if s[i] in ['-', '+']:   # --- py stmt 13
        i += 1   # --- py stmt 14
    res, flag = 0, (2**31 - 1) // 10   # --- py stmt 15
    while i < n:   # --- py stmt 16
        if not s[i].isdigit():   # --- py stmt 17
            break   # --- py stmt 18
        c = int(s[i])   # --- py stmt 19
        if res > flag or (res == flag and c > 7):   # --- py stmt 20
            return 2**31 - 1 if sign > 0 else -(2**31)   # --- py stmt 21
        res = res * 10 + c   # --- py stmt 22
        i += 1   # --- py stmt 23
    return sign * res   # --- py stmt 24

### JavaScript
"use strict";
function f_gold(s) {   // --- py stmt 1
    if (!s) return 0;   // --- py stmt 2
    var n = s.length;   // --- py stmt 4
    if (n == 0) return 0;   // --- py stmt 6
    var i = 0;   // --- py stmt 7
    while (s[i] == ' ') {   // --- py stmt 8
        i++;   // --- py stmt 9
        if (i == n) return 0;   // --- py stmt 11
    }
    var sign = -1;   // --- py stmt 12
    if (s[i] == '-') sign = -1;   // --- py stmt 12
    else sign = 1;   // --- py stmt 12
    if (s[i] == '-' || s[i] == '+') i++;   // --- py stmt 13
    var res = 0;   // --- py stmt 15
    var flag = (Math.pow(2, 31) - 1) / 10;   // --- py stmt 15
    while (i < n) {   // --- py stmt 16
        if (!s[i].isDigit()) break;   // --- py stmt 17
        var c = parseInt(s[i]);   // --- py stmt 19
        if (res > flag || (res == flag && c > 7)) return Math.pow(2, 31) - 1;   // --- py stmt 21
        if (sign < 0) return -(Math.pow(2, 31));   // --- py stmt 21
        res = res * 10 + c;   // --- py stmt 22
        i++;   // --- py stmt 23
    }
    return sign * res;   // --- py stmt 24
}

"""
python_code = '''
from typing import *   # --- py stmt 1
def f_gold(s: str) -> int:   # --- py stmt 2
    if not s:   # --- py stmt 3
        return 0   # --- py stmt 4
    n = len(s)   # --- py stmt 5
    if n == 0:   # --- py stmt 6
        return 0   # --- py stmt 7
    i = 0   # --- py stmt 8
    while s[i] == ' ':   # --- py stmt 9
        i += 1   # --- py stmt 10
        if i == n:   # --- py stmt 11
            return 0   # --- py stmt 12
    sign = -1 if s[i] == '-' else 1   # --- py stmt 13
    if s[i] in ['-', '+']:   # --- py stmt 14
        i += 1   # --- py stmt 15
    res, flag = 0, (2**31 - 1) // 10   # --- py stmt 16
    while i < n:   # --- py stmt 17
        if not s[i].isdigit():   # --- py stmt 18
            break   # --- py stmt 19
        c = int(s[i])   # --- py stmt 20
        if res > flag or (res == flag and c > 7):   # --- py stmt 21
            return 2**31 - 1 if sign > 0 else -(2**31)   # --- py stmt 22
        res = res * 10 + c   # --- py stmt 23
        i += 1   # --- py stmt 24
    return sign * res   # --- py stmt 25(), js wss stmt 26(ww)
'''
import re
lines = map_result.split("\n")
py_pattern = r"^(.*?)#"
js_pattern = r"^(.*?)//"
pattern_code = py_pattern
pattern_num=r"stmt\s*(\d+)"

python_extracted = [] #，pop，
js_extracted = []
extracted=python_extracted
for line in lines:
    tem_list=[]
    print(line)
    if "### JavaScript" in line:
        extracted=js_extracted
        pattern_code = js_pattern
    if "stmt" not in line and ("# ---" or "// ---") not in line:
        continue
    match_code = re.match(pattern_code,line)
    match_num=re.findall(pattern_num,line)
    if match_code:
        # print(match_code.group(1).strip())
        tem_list.append(match_code.group(1).strip())
        # extracted.append((match_code.group(1).strip(), match_code.group(2)))
    else:
        print("now_Error: ",line)
        tem_list.append("Error: "+line)
    if match_num:
        # print([int(num) for num in match_num])
        tem_list.append([int(num) for num in match_num])
        # extracted.append(match_num)
    extracted.append(tem_list)
for i in range(len(python_extracted)):
    print(python_extracted[i])
print("-------------------------------------------------")
for i in range(len(js_extracted)):
        print(js_extracted[i])
print(type(python_extracted))