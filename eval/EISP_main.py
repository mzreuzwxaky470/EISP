import sys
import os
import json
sys.path.append('/home/user/cl/EISP')
from code_spilt import code_strip_spaces
from myAPItoken import *
from OverallLogicToken import *
from bs4 import BeautifulSoup
import json
import tiktoken
import re
from auto_Error_located_few_shot  import *
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from torch.cuda.amp import autocast
from setproctitle import setproctitle

# setproctitle("cl")
model=None
tokenizer=None
# model, tokenizer = init_model_and_tokenizer_starling_LM_7B_beta()
pipeline_=init_llam3_70b_4bit()

def eval_map(result_path,data_path="EISP/data/dataset/test/test2.json"):

    file_path_list=["EISP/data/dataset/evalex/leetcode/py_js_codex0err",
     "EISP/data/dataset/evalex/humanevalx/py_js_codex0err",
     "EISP/data/dataset/evalex/gfg/py_js_codex0err"
     ]
    
    file_path_name_list=["leetcode",
     "humanevalx",
     "gfg"
     ]

    sample_dict={}
    with open(data_path,'r') as f:
        sample_dict=json.load(f)
    result_dict={}
    file_name="injects.json"
    num=0
    num_error=0
    for file_path,file_path_name in zip(file_path_list,file_path_name_list):
        tem_dict={}

        for root, dirs, files in os.walk(file_path):
            sample_result_dict={}
            file_full_path = os.path.join(root,file_name)
            res_name=re.search(r'codex0err/(.+)$',root)

            if os.path.exists(file_full_path) and res_name.group(1) in sample_dict[file_path_name]:
            # if os.path.exists(file_full_path):
                    print("sample_num:",num)
                    # if num>3:
                    #     break
                    num+=1
                    source_path=os.path.join(root,"source.py")
                    target_path=os.path.join(root,"target.js")
                    source_code=""
                    target_code=""
                    injects={}
                    with open(source_path,'r') as f:
                        source_code=f.read()
                    with open(target_path,'r') as f:
                        target_code=f.read()
                    with open(file_full_path, 'r') as f:
                        injects = json.load(f)
                    sample_result_dict["source_code"]=source_code
                    sample_result_dict["target_code"]=target_code
                    sample_result_dict["injects"]=injects


                    Gen_Code = code_strip_spaces(source_code)
                    Gen_Code = code_srtip_main(Gen_Code)
                    Gen_Code=Gen_Code.split("\n")
                    Gen_Code=[i+'\n' for i in Gen_Code ]
                    source_code=""
                    for i in Gen_Code:
                        if "def" in i:

                            source_code=source_code.join(Gen_Code[Gen_Code.index(i):])
                            break


                    result=""
                    try:
                        map_result=map_code(source_code,target_code,model,tokenizer)
                        # map_result=map_code(source_code,target_code)
                        python_extracted,js_extracted=get_map(map_result,source_code,target_code)

                        if len(python_extracted)==0 or len(js_extracted)==0:
                            num_error+=1
                            result=num_error

                        python_extracted,rest=get_py_map(source_code,python_extracted)
                        if len(python_extracted)==0:
                            logging.error(""+'\n'+source_code)
                        loc_code(source_code,"define",python_extracted,js_extracted)
                        
                        pass
                    except Exception as e:
                        print(f"An error occurred: {e}")

                    sample_result_dict["result"]=result
                    tem_dict[res_name.group(1)]=sample_result_dict

        output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/test.json"
        result_dict[file_path_name]=tem_dict 

        with open(output_path,'w') as f:
            json.dump(result_dict,f)   
        # if num>3:
        #         break
    with open(result_path,'w') as f:
        json.dump(result_dict,f)             

    return

def eval_map_llam3(result_path,data_path="/home/user/cl/EISP/data/dataset/test/test2.json"):

    file_path_list=["/home/user/cl/EISP/data/dataset/evalex/leetcode/py_js_codex0err",
     "/home/user/cl/EISP/data/dataset/evalex/humanevalx/py_js_codex0err",
     "/home/user/cl/EISP/data/dataset/evalex/gfg/py_js_codex0err"
     ]
    
    file_path_name_list=["leetcode",
     "humanevalx",
     "gfg"
     ]

    sample_dict={}
    with open(data_path,'r') as f:
        sample_dict=json.load(f)
    result_dict={}
    file_name="injects.json"
    num=0
    num_error=0
    for file_path,file_path_name in zip(file_path_list,file_path_name_list):
        tem_dict={}
        # if num>3:
        #         break
        for root, dirs, files in os.walk(file_path):
            sample_result_dict={}
            file_full_path = os.path.join(root,file_name)
            res_name=re.search(r'codex0err/(.+)$',root)

            if os.path.exists(file_full_path) and res_name.group(1) in sample_dict[file_path_name]:
            # if os.path.exists(file_full_path):
                    print("sample_num:",num)
                    # if num>3:
                    #     break
                    num+=1
                    source_path=os.path.join(root,"source.py")
                    target_path=os.path.join(root,"target.js")
                    source_code=""
                    target_code=""
                    injects={}
                    with open(source_path,'r') as f:
                        source_code=f.read()
                    with open(target_path,'r') as f:
                        target_code=f.read()
                    with open(file_full_path, 'r') as f:
                        injects = json.load(f)
                    sample_result_dict["source_code"]=source_code
                    sample_result_dict["target_code"]=target_code
                    sample_result_dict["injects"]=injects


                    Gen_Code = code_strip_spaces(source_code)
                    Gen_Code = code_srtip_main(Gen_Code)
                    Gen_Code=Gen_Code.split("\n")
                    Gen_Code=[i+'\n' for i in Gen_Code ]
                    source_code=""
                    for i in Gen_Code:
                        if "def" in i:

                            source_code=source_code.join(Gen_Code[Gen_Code.index(i):])
                            break


                    map_result=map_code(source_code,target_code,pipeline__=pipeline_)
                    python_extracted,js_extracted=get_map(map_result,source_code,target_code)
                    result="result_yes"
                    if len(python_extracted)==0 or len(js_extracted)==0:
                        num_error+=1
                        result="result_no"+str(num_error)

 
                    python_extracted,rest=get_py_map(source_code,python_extracted)
                    if len(python_extracted)==0:
                        logging.error("python_extracted"+'\n'+source_code)
                        if "result_no" not in result:
                            num_error+=1
                            result="result_no"+str(num_error)
                    # loc_code(source_code,"define",python_extracted,js_extracted)
                    


                    sample_result_dict["result"]=result+map_result
                    tem_dict[res_name.group(1)]=sample_result_dict

        output_path="/home/user/cl/EISP/eval/result/map/gpt35.json"
        result_dict[file_path_name]=tem_dict 

        with open(output_path,'w') as f:
            json.dump(result_dict,f)   
        # if num>3:
        #         break
    with open(result_path,'w') as f:
        json.dump(result_dict,f)             

    return

def EISP(source_code,target_code):
    # modify_target_code(target_code)

    Gen_Code = code_strip_spaces(source_code)
    Gen_Code = code_srtip_main(Gen_Code)
    Gen_Code=Gen_Code.split("\n")
    Gen_Code=[i+'\n' for i in Gen_Code ]
    source_code=""
    for i in Gen_Code:
        if "def" in i:

            source_code=source_code.join(Gen_Code[Gen_Code.index(i):])
            break
    if source_code=="":
        source_code=Gen_Code
    res=""

    try:
        map_result=map_code(source_code,target_code,model,tokenizer)
        # python_extracted,js_extracted=get_map(map_result,source_code,target_code)

        # code_struct=None
        # res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)

        pass
    except Exception as e:
         print(f"An error occurred: {e}")
    res,input_token,output_token=locate_error(source_code,target_code)
    # map_result=map_code(source_code,target_code,model,tokenizer)
    # python_extracted,js_extracted=get_map(map_result,source_code,target_code)

    # code_struct=None
    # res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
    
    if res=="":
        res="yes"


    # res=summary_incorrect_lines(res,source_code,target_code)

    # Incorrect line of code: sum += Math.floor(value / 3) + (0 if value % 3 == 0 else 1);
    # Incorrect explanation: The ternary operator syntax is incorrect for JavaScript. It should be written as sum += Math.floor(value / 3) + (value % 3 == 0 ? 0 : 1);"

    return res
def EISP_llama3(source_code,target_code):
    # modify_target_code(target_code)

    Gen_Code = code_strip_spaces(source_code)
    Gen_Code = code_srtip_main(Gen_Code)
    Gen_Code=Gen_Code.split("\n")
    Gen_Code=[i+'\n' for i in Gen_Code ]
    source_code=""
    for i in Gen_Code:
        if "def" in i:

            source_code=source_code.join(Gen_Code[Gen_Code.index(i):])
            break
    if source_code=="":
        source_code=Gen_Code
    res=""

    except_flag=0
    try:
        map_result=map_code(source_code,target_code,pipeline__=pipeline_)
        python_extracted,js_extracted=get_map(map_result,source_code,target_code)

        code_struct=None
        pass
    except Exception as e:
         except_flag=1
         print(f"An error occurred: {e}")
    if except_flag==0:
        res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
    # res,input_token,output_token=locate_error(source_code,target_code)
    # map_result=map_code(source_code,target_code,model,tokenizer)
    # python_extracted,js_extracted=get_map(map_result,source_code,target_code)
    # # DFSAST，
    # code_struct=None
    # res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
    
    if res=="":
        res="yes"
    print("：",res)

    # res=summary_incorrect_lines(res,source_code,target_code)

    # 
    # gpt，No.
    # Incorrect line of code: sum += Math.floor(value / 3) + (0 if value % 3 == 0 else 1);
    # Incorrect explanation: The ternary operator syntax is incorrect for JavaScript. It should be written as sum += Math.floor(value / 3) + (value % 3 == 0 ? 0 : 1);"

    return res
def EISP_indecomposition(source_code,target_code):
    res=""
    res,input_token,output_token=locate_error(source_code,target_code)
    if res=="":
        res="yes"
    print("：",res)
    return res
# locate_error_fewshotlocate_error
def EISP_without_AIchain(source_code,target_code):
    # modify_target_code(target_code)
    # 
    # pythonimport
    Gen_Code = code_strip_spaces(source_code)
    Gen_Code = code_srtip_main(Gen_Code)
    Gen_Code=Gen_Code.split("\n")
    Gen_Code=[i+'\n' for i in Gen_Code ]
    source_code=""
    for i in Gen_Code:
        if "def" in i:
        # i
            source_code=source_code.join(Gen_Code[Gen_Code.index(i):])
            break
    if source_code=="":
        source_code=Gen_Code
    res=""
    map_result=map_code(source_code,target_code,model,tokenizer)
    python_extracted,js_extracted=get_map(map_result,source_code,target_code)
    # DFSAST，
    code_struct=None
    res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
    if res=="":
        res="yes"
    print("：",res)

    # res=summary_incorrect_lines(res,source_code,target_code)

    return res
def EISP_main():
    # eval_dataset，few_shot_gpt4_turbo_result_path
    few_shot_gpt4_turbo_result_path="/home/user/cl/EISP/eval/result/gpt4_EISP/starling_LM_7B_beta/gpt3.5.json"
    eval_dataset(EISP,few_shot_gpt4_turbo_result_path)
    # ，
    file_path=few_shot_gpt4_turbo_result_path
    output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/starling_LM_7B_beta/gpt3.5_format.json"
    # Standardised_output_format(file_path,output_path)

    # 
    output_path="EISP/eval/result/gpt4_EISP/starling_LM_7B_beta/gpt3.5.json"
def EISP_main_llama3():
    # eval_dataset，few_shot_gpt4_turbo_result_path
    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_EISP/llama3_70b/2.json"
    eval_dataset(EISP_llama3,few_shot_gpt4_turbo_result_path)
    # ，
    # file_path=few_shot_gpt4_turbo_result_path
    # output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/llama3_70b/1_format.json"
    # Standardised_output_format(file_path,output_path)

def EISP_main_indecomposition():
    # eval_dataset，few_shot_gpt4_turbo_result_path
    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_EISP/EISP_main_indecomposition_result/gpt3.5.json"
    eval_dataset(EISP_indecomposition,few_shot_gpt4_turbo_result_path)
    # ，
    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt4_EISP/EISP_main_indecomposition_result/gpt3.5_format.json"
    Standardised_output_format(file_path,output_path)

    # 
    output_path="EISP/eval/result/gpt4_EISP/EISP_main_indecomposition_result/gpt3.5_format.json"
    evaluations(output_path)
# locate_error_fewshotlocate_error
def EISP_main_without_AIchain():
    # eval_dataset，few_shot_gpt4_turbo_result_path
    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_EISP/EISP_main_without_AIchain_result/gpt3.5.json"
    eval_dataset(EISP_without_AIchain,few_shot_gpt4_turbo_result_path)
    # ，
    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt4_EISP/EISP_main_without_AIchain_result/gpt3.5_format.json"
    Standardised_output_format(file_path,output_path)

    # 
    output_path="EISP/eval/result/gpt4_EISP/EISP_main_without_AIchain_result/gpt3.5_format.json"
    evaluations(output_path)
def EISP_main_without_kb():
    # eval_dataset，few_shot_gpt4_turbo_result_path
    few_shot_gpt4_turbo_result_path="/home/user/cl/EISP/eval/result/gpt4_EISP/EISP_main_without_kb_result /gpt3.5.json"
    eval_dataset(EISP,few_shot_gpt4_turbo_result_path)
    # ，
    file_path=few_shot_gpt4_turbo_result_path
    output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/EISP_main_without_kb_result /gpt3.5_format.json"
    Standardised_output_format(file_path,output_path)

    # 
    output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/EISP_main_without_kb_result /gpt3.5_format.json"
    evaluations(output_path)
def test(source_code,target_code):
    prompt="""
python code="
### licenseKeyFormatting 
from typing import *
def f_gold(s: str, k: int) -> str:
    s = s.replace('-', '').upper()
    res = []
    cnt = (len(s) % k) or k
    t = 0
    for i, c in enumerate(s):
        res.append(c)
        t += 1
        if t == cnt:
            t = 0
            cnt = k
            if i != len(s) - 1:
                res.append('-')
    return ''.join(res)

                             "
javascript code="
function f_gold(s, k) {
    s = s.replace('-', '').toUpperCase();
    let res = [];
    let cnt = (s.length % k) || k;
    let t = 0;
    for (let i = 0; i < s.length; i++) {
        res.push(s[i]);
        t += 1;
        if (t == cnt) {
            t = 0;
            cnt = k;
            if (i != s.length - 1) {
                res.push('-');
            }
        }
    }
    return res.join('');
}


"
task:You are an experienced python and JavaScript developer, please compare and analyze the logic of the above two pieces of code  and determine whether the logic of the JavaScript code and the Python code is completely equivalent. Let's think step-by-step.  Please note that there is no need to correct code that is logically different!

"""
    prompt2="""
reference document="   
Removing Dashes and Converting to Upper Case:

Both the Python and JavaScript codes start by removing all hyphens ('-') from the input string s and converting all characters to uppercase. This is achieved in Python with s.replace('-', '').upper() and in JavaScript with s.replace('-', '').toUpperCase(). This step is correctly translated.
Initialization of Variables:

Both codes initialize a result container (res), a counter for the current segment length (cnt), and a temporary counter (t). The purpose of these variables is to build the formatted license key in segments of length k, except possibly the first segment, which might be shorter. The initialization logic is correctly translated from Python to JavaScript.
Calculating Initial Segment Length:

The calculation of the initial segment length (cnt) is based on the remainder of the division of the string's length by k. If the remainder is 0, it uses k as the initial segment length. This is correctly implemented in both languages with (len(s) % k) or k in Python and (s.length % k) || k in JavaScript.
Iterating Over Characters:

Both codes iterate over the characters of the cleaned-up string. They add each character to the result container and increment the temporary counter t after each character. This logic is consistent between the two languages.
Segment Delimiter Insertion:

When t equals cnt, indicating that the current segment is complete, both codes reset t to 0 and set cnt to k for subsequent segments. If the current character is not the last character in the string, a delimiter ('-') is appended to the result container. This logic ensures that a delimiter is not added after the last segment, and it is correctly implemented in both codes.
Joining and Returning the Result:

Finally, both codes join the characters (and any inserted delimiters) in the result container into a single string and return it. The Python code does this with return ''.join(res), and the JavaScript code uses return res.join('').


- In Python, `str.replace(old, new)` replaces all occurrences of the substring `old` with `new`. If `old` is not found, the string is returned unchanged.
   - In JavaScript, `string.replace(searchValue, newValue)` replaces only the first occurrence of `searchValue` with `newValue` unless `searchValue` is a regular expression with the global (`g`) flag.

   
String Manipulation: Both Python and JavaScript code begin by removing any hyphens from the string (s) and converting it to uppercase. This is done using the replace() and toUpperCase() functions in Python and JavaScript respectively. The logic here is equivalent in both languages.

Variable Initialization: The variables res, cnt, and t are initialized in both Python and JavaScript. Again, the logic here is equivalent in both languages.

Determining cnt: In both codes, cnt is set to either (len(s) % k) or k. This logic checks if the length of the string (s) modulo k is non-zero. If it's zero, it sets cnt to k, otherwise, it sets cnt to (len(s) % k). This logic seems to be correctly translated from Python to JavaScript.   
   
   "

Task: You are an experienced Python and JavaScript developer, please re-determine if the logic of the JavaScript code and Python code are not equal in some detail based on the above reference document! Please note that there is no need to correct code that is logically different! Let's re-think step-by-step.
"""
    messages=[]
    messages.append({"role": "user", "content": prompt})
    response, messages, extra_response_count=get_api_continue_response(messages)
     # assistant
    assistant_reply = response["choices"][0]["message"]["content"]
    # assistant
    messages=[]
    messages.append({"role": "assistant", "content": assistant_reply})
    messages.append({"role": "user", "content": prompt2})
    response, messages, extra_response_count=get_api_continue_response(messages)
    prompt6=get_prompt("located_error_prompt61.txt")
    messages=[]

#     res="""
#     Based on the reference document provided, let's re-examine the logic of the Python and JavaScript code snippets in more detail:

# 1. **String `replace()` Method**:
#    - In Python, the `replace()` method mutates the original string in place, replacing the specified substring with the new one. This means that the original string `s` is modified directly.
#    - In JavaScript, the `replace()` method does not mutate the original string but returns a new string with the replacement. This behavior differs from Python, where the original string would be modified in place.

# 2. **Global Replacement**:
#    - JavaScript's `replace()` method replaces a string pattern only once by default. To perform a global search and replace, a regular expression with the `g` flag or `replaceAll()` should be used.
#    - In Python, the `replace()` method replaces all occurrences of the specified substring by default. There is no need for additional flags or methods to perform a global replacement.

# Considering the above points, there is a slight difference in behavior between the Python and JavaScript code snippets due to how the `replace()` method works in each language. In Python, the original string is mutated in place, while in JavaScript, a new string is returned with the replacement. This difference in behavior should be noted when comparing the two code snippets.

# """

    prompt6 = prompt6.replace("{python code flag}",source_code)
    prompt6 = prompt6.replace("{javascript code flag}",target_code)
    prompt6=prompt6.replace("{reference document flag}",response["choices"][0]["message"]["content"])
    response, messages, extra_response_count=get_api_response(prompt6)
def test_summary_difference():
    str="""
    similar APIs and operators="
In the provided Python and JavaScript code snippets, the following operators and API methods are used:

Python:

String  method: replace()str.replace()
String  method: upper()str.upper()
Logical OR operator: or
JavaScript:

String  method: replace()String.prototype.replace()
String  method: toUpperCase()String.prototype.toUpperCase()
Logical OR operator: ||"
javascript reference document="String.prototype.replace()": "This method does not mutate the string value it's called on. It returns a new string.\nA string pattern will only be replaced once. To perform a global search and replace, use a regular expression with the g flag, or use replaceAll() instead.\nIf pattern is an object with a Symbol.replace method (including RegExp objects), that method is called with the target string and replacement as arguments. Its return value becomes the return value of replace(). In this case the behavior of replace() is entirely encoded by the @@replace method \u00e2\u0080\u0094 for example, any mention of \"capturing groups\" in the description below is actually functionality provided by RegExp.prototype[@@replace].\nIf the pattern is an empty string, the replacement is prepended to the start of the string.\njs\"xxx\".replace(\"\", \"_\"); // \"_xxx\"\n\nA regexp with the g flag is the only case where replace() replaces more than once. For more information about how regex properties (especially the sticky flag) interact with replace(), see RegExp.prototype[@@replace](). "

Task: You are an experienced python and JavaScript developer, compare the logic and behavioral differences between similar APIs and operators in JavaScript and Python, based on the JavaScript reference document above. Let's take this step-by-step analysis and focus on the differences in logic and usage that may exist between the two languages when implementing similar functionality.

"""
    messages=[]
    messages.append({"role": "user", "content": str})
    response, messages, extra_response_count=get_api_continue_response(messages)
     # assistant
    assistant_reply = response["choices"][0]["message"]["content"]
    # assistant
    messages.append({"role": "assistant", "content": assistant_reply})
    print(response["choices"][0]["message"]["content"]+'\n')
    print('---------------------')
    return
def locate_error2(source_code,target_code):
    messages=[]
    input_token=0
    output_token=0
    # FQN
    prompt1=get_prompt("located_error_prompt1.txt")
    prompt1 = prompt1.replace("{python code flag}",source_code)
    prompt1 = prompt1.replace("{javascript code flag}",target_code)
    messages.append({"role": "user", "content": prompt1})
    response, messages, extra_response_count=get_api_continue_response(messages)
    #token
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    javascript_reference_document=get_knowledge_base(response["choices"][0]["message"]["content"])

#     javascript_reference_document+="""
#     The % operator is overloaded for two types of operands: number and BigInt. It first coerces both operands to numeric values and tests the types of them. It performs BigInt remainder if both operands become BigInts; otherwise, it performs number remainder. A TypeError is thrown if one operand becomes a BigInt but the other becomes a number.

# For the operation n % d, n is called the dividend and d is called the divisor. The operation returns NaN if one of the operands is NaN, n is ±Infinity, or if d is ±0. Otherwise, if d is ±Infinity or if n is ±0, the dividend n is returned.

# When both operands are non-zero and finite, the remainder r is calculated as r := n - d * q where q is the integer such that r has the same sign as the dividend n while being as close to 0 as possible.

# Note that while in most languages, '%' is a remainder operator, in some (e.g. Python, Perl) it is a modulo operator. Modulo is defined as k := n - d * q where q is the integer such that k has the same sign as the divisor d while being as close to 0 as possible. For two values of the same sign, the two are equivalent, but when the operands are of different signs, the modulo result always has the same sign as the divisor, while the remainder has the same sign as the dividend, which can make them differ by one unit of d. To obtain a modulo in JavaScript, in place of n % d, use ((n % d) + d) % d. In JavaScript, the modulo operation (which doesn't have a dedicated operator) is used to normalize the second operand of bitwise shift operators (<<, >>, etc.), making the offset always a positive value.

# For BigInt division, a RangeError is thrown if the divisor y is 0n. This is because number remainder by zero returns NaN, but BigInt has no concept of NaN.

# """

    print(javascript_reference_document+"\n"+"---------")
    # assistant
    assistant_reply = response["choices"][0]["message"]["content"]
    # assistant
    messages.append({"role": "assistant", "content": assistant_reply})
    # ，FQN

    messages=[]
    prompt2=get_prompt("located_error_prompt2.txt")
    prompt2=prompt2.replace("{similar APIs and operators}",assistant_reply)
    # prompt2=prompt2.replace("{javascript reference document}",javascript_reference_document)
    messages.append({"role": "user", "content": prompt2})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
        
    assistant_reply = response["choices"][0]["message"]["content"]
    # messages.append({"role": "assistant", "content": assistant_reply})
    # ,
    messages=[]
    prompt3=get_prompt("located_error_prompt3.txt")
    prompt3 = prompt3.replace("{api and operator comparison}",assistant_reply)
    prompt3=prompt3.replace("{javascript reference document}",javascript_reference_document)
    messages.append({"role": "user", "content": prompt3})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
        
    assistant_reply3 = response["choices"][0]["message"]["content"]

    # ，
    messages=[]
    prompt4=get_prompt("located_error_prompt4.txt")
    prompt4 = prompt4.replace("{python code flag}",source_code)
    prompt4 = prompt4.replace("{javascript code flag}",target_code)

    messages.append({"role": "user", "content": prompt4})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
        
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})
    # ，，，
    # messages=[]
    prompt5=get_prompt("located_error_prompt5.txt")
    prompt5 = prompt5.replace("{reference document flag}",assistant_reply3)
    messages.append({"role": "user", "content": prompt5})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})
    # ，

    messages=[]

    prompt6=get_prompt("located_error_prompt6.txt")
    prompt6 = prompt6.replace("{python code flag}",source_code)
    prompt6 = prompt6.replace("{javascript code flag}",target_code)
    prompt6=prompt6.replace("{reference document flag}",assistant_reply)
    messages.append({"role": "user", "content": prompt6})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    
    return response["choices"][0]["message"]["content"],input_token,output_token

if __name__ == "__main__":

    EISP_main_llama3()





