import os
import sys
import re
import json
from code_spilt import *
from code_match import get_type
#
from myAPItoken import *
from code_extra import extract_dependencies,add_assign
#，”“，
TH = 2
from BufferClass import CodeStructure
import sys

model = None
tokenizer =None
# 
map_threshold = 3
prompt_path="EISP/prompt"
input_tokens = 0
output_tokens = 0
dependencies=[]
js_map_code_saved=""

# 
def map_code(source_code,target_code,model_=None,tokenizer_=None):
    global model, tokenizer
    model=model_
    tokenizer=tokenizer_
    map_prompt=""
    with open(os.path.join(prompt_path, "map_prompt.txt"), "r", encoding="utf-8") as f:
            map_prompt = f.read()
    map_prompt = map_prompt.replace("{pycode flag}",source_code)
    map_prompt = map_prompt.replace("{jscode flag}",target_code)
    # response, messages, extra_response_count=Mistral_7B_v2_prompt(map_prompt, model, tokenizer)
    response, messages, extra_response_count=get_api_response(map_prompt)
    return response["choices"][0]["message"]["content"]
# kb
def get_knowledge_base(str):
    with open("/home/user/cl/EISP/data/knoeledge_base/kb.json",'r') as f:
        kb = json.load(f)
    res=""
    for knowledge in kb:
        tem_kb=knowledge
        if "()" in knowledge:
            tem_kb=knowledge.replace("()","")
        if tem_kb in str and tem_kb!="":

            # if tem_kb==""

            res+=knowledge.strip()+": "+kb[knowledge].strip()+'\n'
    return res
# 
def get_map(map_result,source_code=None,target_code=None):
    lines = map_result.split("\n")
    py_pattern  = r"^(.*?)#"
    js_pattern  = r"^(.*?)//"
    pattern_code = py_pattern
    pattern_num=r"stmt\s*(\d+)"

    python_extracted = [] #，pop，
    js_extracted = []
    extracted=python_extracted
    position=map_result.find("### JavaScript")
    global js_map_code_saved
    if(position!=-1):
        js_map_code_saved=map_result[position:]
    for line in lines:
        pattern_code = py_pattern
        tem_list=[]
        if "### JavaScript" in line:
            extracted=js_extracted
            
        if "stmt" not in line and ("# ---" or "// ---") not in line:
            continue
        match_code = re.match(pattern_code,line)
        match_num=re.findall(pattern_num,line)
        if match_code:
            # print(match_code.group(1).strip())
            tem_list.append(match_code.group(1).strip())
            # extracted.append((match_code.group(1).strip(), match_code.group(2)))
        else:
            # ，
            pattern_code=js_pattern
            match_code = re.match(pattern_code,line)
            if match_code:
                # print(match_code.group(1).strip())
                tem_list.append(match_code.group(1).strip())
            else:
                # ,，
                print("map_match_Error: ",line)
                # tem_list.append("Error: "+line)
        if match_num:
            # print([int(num) for num in match_num])
            tem_list.append([int(num) for num in match_num])
            # extracted.append(match_num)
        extracted.append(tem_list)
    flag=0
    for i in range(len(python_extracted)):
        if len(python_extracted[i])<2:
            flag=1
        
    #     print(python_extracted[i])
    # print("-------------------------------------------------")
    for i in range(len(js_extracted)):
        if len(js_extracted[i])<2:
            flag=1
        # print(js_extracted[i])
    if len(python_extracted)==0 or len(js_extracted)==0:
        flag=1

    if flag==1:
        print("get_map error")
        # ，
        # res=map_code(source_code,target_code)
        # python_extracted,js_extracted=get_map(res,source_code,target_code)

    for  i in python_extracted:
        if(len(i)<2):
            python_extracted.pop(python_extracted.index(i))
    for  i in js_extracted:
        if(len(i)<2):

            
            js_extracted.pop(js_extracted.index(i))
    return python_extracted,js_extracted
def get_prompt(prompt_name):
    prompt_path="EISP/prompt"
    prompt=""
    with open(os.path.join(prompt_path, prompt_name), "r", encoding="utf-8") as f:
            prompt = f.read()
    return prompt
# ，prompt 
def locate_error(source_code,target_code):
# def locate_error_(source_code,target_code):
    messages=[]
    input_token=0
    output_token=0

    if source_code=="" or target_code=="":
        print("source_code or target_code is empty"+'\n'+source_code+'------------------\n'+target_code)
        logging.error("source_code or target_code is empty"+'\n'+source_code+'------------------\n'+target_code)
        res=""
        return res,input_token,output_token

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

    # javascript_reference_document=""


    # print(javascript_reference_document+"\n"+"---------")
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
    

    res=response["choices"][0]["message"]["content"]
    # print("******prompt:*********")
    # print(prompt1)
    # print("******")
    # print(prompt2)
    # print("******")
    # print(prompt3)
    # print("******")
    # print(prompt4)
    # print("******")
    # print(prompt5)
    # print("******")
    # print(prompt6)

    if "yes" in response["choices"][0]["message"]["content"].lower():
        res=""

    return res,input_token,output_token
# LLM
def locate_error_v2(source_code,target_code):
# def locate_error(source_code,target_code):
    # 

    messages=[]
    input_token=0
    output_token=0

    if source_code=="" or target_code=="":
        print("source_code or target_code is empty"+'\n'+source_code+'------------------\n'+target_code)
        logging.error("source_code or target_code is empty"+'\n'+source_code+'------------------\n'+target_code)
        res=""
        return res,input_token,output_token

    # FQN
    prompt1=get_prompt("located_error_prompt1.txt")
    prompt1 = prompt1.replace("{python code flag}",source_code)
    prompt1 = prompt1.replace("{javascript code flag}",target_code)
    messages.append({"role": "user", "content": prompt1})
    response, messages, extra_response_count = Mistral_7B_v2(messages, model, tokenizer)
    # response, messages, extra_response_count=get_api_continue_response(messages)
    #token
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    javascript_reference_document=get_knowledge_base(response["choices"][0]["message"]["content"])

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
    response, messages, extra_response_count = Mistral_7B_v2(messages, model, tokenizer)
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
    response, messages, extra_response_count = Mistral_7B_v2(messages, model, tokenizer)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
        
    assistant_reply3 = response["choices"][0]["message"]["content"]

    # ，
    messages=[]
    prompt4=get_prompt("located_error_prompt4.txt")
    prompt4 = prompt4.replace("{python code flag}",source_code)
    prompt4 = prompt4.replace("{javascript code flag}",target_code)

    messages.append({"role": "user", "content": prompt4})
    response, messages, extra_response_count = Mistral_7B_v2(messages, model, tokenizer)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
        
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})
    # ，，，
    # messages=[]
    prompt5=get_prompt("located_error_prompt5.txt")
    prompt5 = prompt5.replace("{reference document flag}",assistant_reply3)
    messages.append({"role": "user", "content": prompt5})
    response, messages, extra_response_count = Mistral_7B_v2(messages, model, tokenizer)
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
    response, messages, extra_response_count = Mistral_7B_v2(messages, model, tokenizer)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    

    res=response["choices"][0]["message"]["content"]
    if "yes" in response["choices"][0]["message"]["content"].lower():
        res=""

    return res,input_token,output_token
# ai-chain，fewshot
def locate_error_fewshot(source_code,target_code):
# def locate_error(source_code,target_code):
    few_shot_prompt =""
    with open("/home/user/cl/EISP/prompt/baseline/few_shot.txt","r") as f:
        few_shot_prompt = f.read()
    few_shot_prompt=few_shot_prompt.replace("{source_code_flag}",source_code)
    few_shot_prompt=few_shot_prompt.replace("{target_code_flag}",target_code)
    messages=[]
    messages.append({"role": "user", "content": few_shot_prompt})
    response, messages, extra_response_count=get_api_continue_response(messages)
    # assistant
    assistant_reply = response["choices"][0]["message"]["content"]
    if "yes" in response["choices"][0]["message"]["content"].lower():
        assistant_reply=""
    input_token=[]
    output_token=[]
    return assistant_reply,input_token,output_token
# json
def write_result(result,method_name):
    file_path="EISP/eval/result"
    file_path=os.path.join(file_path,method_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path=os.path.join(file_path,"result.json")
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(file_path,'w') as f:
        json.dump(result,f)
    return


# ,js_extracted，
# source_code：python
# python_extracted：source_codepython[['def f_gold(s: str) -> int:', [1]]
# js_extracted:pythonjs，js
def loc_code(source_code,code_type,python_extracted=None,js_extracted=None):
    # print(""+code_type+'\n'+source_code)
    # print("python_extracted",python_extracted)
    # print( "js_extracted",js_extracted)
    lines = source_code.split("\n")
    lines=[line.strip() for line in lines if line.strip()!=""]
    # print("lines:",lines)
    
    tem_js_extra=[]
    tem_js_code=""
    tem_js_code_copy=""
    last_js_code=""
    for py_line in python_extracted:
        for js_line in js_extracted:
            # }，
            if py_line[1][0] in js_line[1] and js_line[0]!=last_js_code and js_line[0]!="}":
                tem_js_code=tem_js_code+js_line[0]+'\n'
                last_js_code=js_line[0]
                tem_js_extra.append(js_line)
    # print("#############tem_js_code:\n",tem_js_code)
    # js
    js_code=js_map_code_saved
#     js_code="""
#             if (a == 0) {   // --- py stmt 11
#                 break;   // --- py stmt 12
#             }
# """
    # js_codejs，
    js_code=js_code.split("\n")
    js_code=[line.strip() for line in js_code if line.strip()!=""]
    # print("js_code:",js_code)
    # js_codejs，{}
    if code_type=="define" or code_type=="judge" or code_type=="loop":
        # print("tem_js_extra:",tem_js_extra)
        num=0
        js_code_num=0
        while js_code_num<len(js_code):
            i=js_code[js_code_num]
            # ，js
            if num<len(tem_js_extra) and tem_js_extra[num][0] in i:
                tem_num_list=[label_num for label_num in tem_js_extra[num][1] if str(label_num) in i]
                if len(tem_num_list)!=len(tem_js_extra[num][1]):
                    num+=1
                    continue
                tem_js_code_copy=tem_js_code_copy+'\n'+tem_js_extra[num][0]
                # if (js_code_num+1)<len(js_code) and (js_code[js_code_num+1]=='{' or js_code[js_code_num+1]=='}'):
                #     tem_js_code_copy=tem_js_code_copy+'\n'+js_code[js_code_num+1]
                next_character_num=1

                # {}，，// --- py stmt 4

                while(js_code_num+next_character_num)<len(js_code) and (js_code[js_code_num+next_character_num].split("//")[0].strip()=='{' or js_code[js_code_num+next_character_num].split("//")[0].strip()=='}' or js_code[js_code_num+next_character_num].split("#")[0].strip()=='{' or js_code[js_code_num+next_character_num].split("#")[0].strip()=='}'):
                        if "//" in js_code[js_code_num+next_character_num]:
                            tem_js_code_copy=tem_js_code_copy+'\n'+js_code[js_code_num+next_character_num].split("//")[0].strip()
                        else:
                            tem_js_code_copy=tem_js_code_copy+'\n'+js_code[js_code_num+next_character_num].split("#")[0].strip()
                        next_character_num+=1
                num+=1
            js_code_num+=1
    # print("tem_js_code_copy:",tem_js_code_copy)
# tem_js_code_copytem_js_code
    if tem_js_code_copy!="":
        consitent_flag=0
        for i in tem_js_code:
            flag=0
            for j in tem_js_code_copy:
                if i in j:
                    flag=1
                    break
            #  tem_js_code_copy
            if flag==0:
                consitent_flag=1
                break
        if consitent_flag==0:
            tem_js_code=tem_js_code_copy

    res=""
    # print("\nfinal_tem_js_code\n"+tem_js_code)
    # 
    if source_code=="" or tem_js_code=="":
        logging.error("loc_error source_code or tem_js_code is empty"+'\n'+source_code+'------------------\n'+tem_js_code)

    res,input_token,output_token=locate_error(source_code,tem_js_code)

    return res
# python
def get_py_map(py_code,python_extracted):
    # target_code_str=target_code.split("\n").strip()
    # for i in target_code_str:
    #     print(i)
        
    # print("py_code",py_code)

    lines = py_code.split("\n")
    lines=[line.strip() for line in lines if line.strip()!=""]
    # print(lines)
    py_line=0
    line_num=0
    py_tem=0
    tem=[]
    # python
    while py_line<len(python_extracted) and line_num<len(lines):

        clean_line1=''.join(python_extracted[py_line][0].split()).replace('(', '').replace(')', '').replace(';', '')
        clean_line2=''.join(lines[line_num].split()).replace('(', '').replace(')', '').replace(';', '')
        if clean_line1==clean_line2:
            tem.append(python_extracted[py_line][1])
            py_tem+=1
            py_line=py_line+1
            line_num=line_num+1
        else:
            tem=[]
            line_num=0
            py_line=py_line+1-py_tem
            py_tem=0
    if line_num==len(lines) and len(tem)==len(lines):
        used_py_code=[]
        rest_py_code=[]
        for py_line in python_extracted:
            # print(py_line[1])
            if py_line[1] in tem:
                used_py_code.append(py_line)
            else:
                rest_py_code.append(py_line)
        return used_py_code,rest_py_code
    else:
        print("get_python_part_map error")
        return [],[]


def summary_incorrect_lines(res,source_code,target_code):

    prompt=get_prompt("summary_incorrect_lines_prompt.txt")
    prompt = prompt.replace("{python flag}",source_code)
    prompt = prompt.replace("{js code flag}",target_code)
    prompt = prompt.replace("{res flag}",res)
    response, messages, extra_response_count=get_api_response(prompt)
    # print(""+response["choices"][0]["message"]["content"])

    # prompt2=get_prompt("summary_incorrect_lines_prompt2.txt")
    # prompt2=response["choices"][0]["message"]["content"]+prompt2
    # response, messages, extra_response_count=get_api_response(prompt2)
    # print("2"+response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]



def OverAllLogic(Gen_Code,code_struct=None,python_extracted=None,js_extracted=None):
    dependencies=[]
    res=""
    problem_statement=""
    use_problem_statement = False
    #、
    global input_tokens
    global output_tokens
    Gen_Code = code_strip_spaces(Gen_Code)

    Gen_Code = code_srtip_main(Gen_Code)

                                                                                                                                                                  
    #“”,
    Gen_Code_unit = []

    temp = extract_first_level(Gen_Code)
    for i in range(len(temp)):
        Gen_Code_unit.append(temp[i])
    # print(Gen_Code_unit)
    #、”“
    #：variable_logic = {"x1":"xxxxxxx"}

    assign_code = {}
    if_main = False

    #CodeStructure
    if code_struct == None:
        code_struct = CodeStructure()
        if_main = True
    else:
        # ：[import]
        pre_code_struct = code_struct.get_code_struct()
        code_struct.delete_code_struct()
        # (import)：
        pre_struct_code = code_struct.get_structure_code()
        code_struct.delete_struct_code()
        # ：structure_name:logic
        pre_struct_logic = code_struct.get_structure_logic()
        code_struct.delete_struct_logic()
    # 
    for level in extract_first_level(Gen_Code):
        type = get_type(level)
        if type == "import":
            continue
        #code_structuretype，type1、type2、type3...
        if type in code_struct.get_code_struct():
            count = 0
            for t in code_struct.get_code_struct():
                if t.startswith(type):
                    count = count+1
            type = type+str(count)
            code_struct.add_code_struct(type)
            code_struct.add_structure(type,level)
        else:
            code_struct.add_code_struct(type)
            code_struct.add_structure(type,level)

    #bug，，
    for s in code_struct.get_code_struct():
        structure_code_dict = code_struct.get_structure_code()
        if structure_code_dict[s] == "":
            code_struct.remove_structure(s)
    a = 0
    tem_code_struct=code_struct.get_code_struct()
    structure_code_dict = code_struct.get_structure_code()
    for s in tem_code_struct:
        # print("s"+s)
        unit = structure_code_dict[s]
        s_position=tem_code_struct.index(s)
        if s.startswith("import"):
            tem_s=[]
            tem_s.append(s)
            for i in range(s_position+1,len(tem_code_struct)):
                if tem_code_struct[i].startswith("import"):
                    tem_s.append(tem_code_struct[i])
                else:
                    break
            for s in tem_s:
                unit = structure_code_dict[s]
                #import
                #：import math，math 
                #from math import sqrt, pow，sqrt、pow
                packages = re.findall(r"import\s+(.*)",unit)[0]
                
                pack = packages.split(",")
                for p in pack:
                    #key，value，
                    code_struct.add_import(p,structure_code_dict[s])
            # tem_code_structtem_s
            if len(tem_s)>1:        
                for i in range(len(tem_s)-1):
                    tem_code_struct.remove(tem_s[i])
            code=""
            for i in range(len(tem_s)):
                code=code+structure_code_dict[tem_s[i]]+"\n"
            # loc_code，
            used_py_code,python_extracted=get_py_map(code,python_extracted)

            res+=loc_code(code,'import',used_py_code,js_extracted)

            continue

        if s.startswith("input"):
            tem_s=[]
            tem_s.append(s)
            for i in range(s_position+1,len(tem_code_struct)):
                if tem_code_struct[i].startswith("input"):
                    tem_s.append(tem_code_struct[i])
                else:
                    break
            for s in tem_s:
                unit = structure_code_dict[s]
                input_token,output_token,code_logic = return_input_assign_explain(unit,problem_statement=problem_statement)
                input_tokens = input_tokens+input_token
                output_tokens = output_tokens+output_token
                #
                #：x1 = map(float, input().split())，x1、x1,y1,x2,y2 =map(float, input().split())，x1,y1,x2,y2
                #
                tempvar = unit.split("=")[0]
                #
                tempvar = tempvar.replace(" ","")

                tempvar = tempvar.split(",")

                #
                for t in tempvar:
                    #temp = {t:code_logic}
                    #snippet_logic.update(temp)
                    code_struct.add_snippet_logic(t,code_logic)


                #，x1,y1,x2,y2 =map(float, input().split())
                #

                #
                code_struct.add_structure_logic(s,code_logic)
            # tem_code_structtem_s
            if len(tem_s)>1:
                for i in range(len(tem_s)-1):
                    tem_code_struct.remove(tem_s[i])
            code=""
            for i in range(len(tem_s)):
                code=code+structure_code_dict[tem_s[i]]+"\n"
            # loc_cod，
            used_py_code,python_extracted=get_py_map(code,python_extracted)

            res+=loc_code(code,'input',used_py_code,js_extracted)

            # loc_code(code,'input',python_extracted,js_extracted)


        if s.startswith("assign") or s.startswith("other"):
            tem_s=[]
            tem_s.append(s)
            for i in range(s_position+1,len(tem_code_struct)):
                if tem_code_struct[i].startswith("assign") or tem_code_struct[i].startswith("other"):
                    tem_s.append(tem_code_struct[i])
                else:
                    break
            for s in tem_s:
                unit = structure_code_dict[s]
                #：
                #：x1 = map(float, input().split())，x1
                var = unit.split("=")[0]
                #
                var = var.replace(" ","")
                #todo:
                vars = var.split(",")
                # dependencies = extract_dependencies(unit)
                dependencies=[]
                input_token,output_token,logic = return_assign_explain(unit,dependencies,code_struct.get_class_logic(),code_struct.get_function_logic(),problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                input_tokens = input_tokens+input_token
                output_tokens = output_tokens+output_token
                for v in vars:
                    #
                    # （，）
                    code_struct.add_assign_code(v,unit)
                    #
                    code_struct.add_structure_logic(s,logic)
                    #temp = {v:logic}
                    #snippet_logic.update(temp)
                    code_struct.add_snippet_logic(v,logic)
            # tem_code_structtem_s
            if len(tem_s)>1:
                for i in range(len(tem_s)-1):
                    tem_code_struct.remove(tem_s[i])
            code=""
            for i in range(len(tem_s)):
                code=code+structure_code_dict[tem_s[i]]+"\n"
            # loc_cod，
            used_py_code,python_extracted=get_py_map(code,python_extracted)
            res+=loc_code(code,'assign or other',used_py_code,js_extracted)
            
            # print("tem_code_struct：",tem_code_struct)
            continue

        if s.startswith("define"):
            #，def()
            func_name = re.search(r"def(.*?)\(", unit).group(1)
            #
            func_name = func_name.replace(" ","")
                
            # dependencies = extract_dependencies(unit)
            # for d in dependencies:
            #     import_dict = code_struct.get_import()
            #     if d in import_dict:
            #         #import，
            #         unit = import_dict[d] + "\n" + unit
            if(code_depth(unit)<=TH):
                # print("define1")
                input_token,output_token,func_logic = return_func_explain(unit,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                #
                # loc_cod，
                used_py_code,python_extracted=get_py_map(unit,python_extracted)
                res+=loc_code(unit,'define',used_py_code,js_extracted)
                # loc_code(unit,'define',python_extracted,js_extracted)
            else:
                #(“”)
                #
                # print("define2")
                new_unit = extract_second_indent(unit)
                # print("：",new_unit)
                res += OverAllLogic(new_unit,code_struct,python_extracted,js_extracted)
                #
                new_code = unit.split("\n")[0]+"**nested code block**"
                
                input_token,output_token,func_logic = return_func_explain(new_code+"nested code block logic:"+str(res),problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                # loc_cod，
                used_py_code,python_extracted=get_py_map(unit,python_extracted)
                res+=loc_code(unit,'define',used_py_code,js_extracted)
                
                # loc_code(unit,'define',python_extracted,js_extracted)
            code_struct.add_function_logic(func_name,func_logic)

            #
            code_struct.add_structure_logic(s,func_logic)
            # print(""+func_name+"：")
            # print(func_logic)
            # print("----------------------")
            #return return_snippet_explain3(new_code+"nested code block logic:"+str(sub_logic),dependencies,code_struct)

        if s.startswith("judge"):
                #“”，，

                    #
                # dependencies = extract_dependencies(unit)
                # #print(return_snippet_explain2(unit,dependencies,snippet_logic))
                # for d in dependencies:
                #     import_dict = code_struct.get_import()
                #     if d in import_dict:
                #         #import，
                #         unit = import_dict[d] + "\n" + unit

                # unit = add_assign(unit,dependencies,code_struct.get_structure_code())

                if(code_depth(unit)<=TH):
                    input_token,output_token,judge_logic,code_snippet = return_snippet_explain3(unit,dependencies,code_struct,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                    # loc_cod，
                    used_py_code,python_extracted=get_py_map(unit,python_extracted)
                    res+=loc_code(unit,'judge',used_py_code,js_extracted)
                    # loc_code(unit,'judge',python_extracted,js_extracted)

                else:
                    #
                    new_unit = extract_second_indent(unit)
                    print("：",new_unit)
                    res+= OverAllLogic(new_unit,code_struct,python_extracted,js_extracted)
                    print("----------------------")
                    #
                    new_code = unit.split("\n")[0]+"**nested code block**"
                    
                    input_token,output_token,judge_logic,code_snippet = return_snippet_explain3(new_code+"nested code block logic:"+str(res),dependencies,code_struct,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                    # loc_cod，
                    used_py_code,python_extracted=get_py_map(unit,python_extracted)
                    res+=loc_code(unit,'judge',used_py_code,js_extracted)
                    # loc_code(unit,'judge',python_extracted,js_extracted)

                code_struct.add_structure_logic(s,judge_logic)

                    #，
                    #，
                for var in dependencies:
                    if var in code_struct.get_snippet_logic():
                        #
                        ori_logic = code_struct.get_snippet_logic()[var]
                        input_token,output_token,new_logic = update_snippet_logic(judge_logic,var,code_snippet,ori_logic)

                        input_tokens = input_tokens+input_token
                        output_tokens = output_tokens+output_token

                        # print(""+var+"：")
                        # print(new_logic)
                        # print("----------------------")
                        #
                        if var in code_struct.get_snippet_logic():
                            code_struct.update_snippet_logic(var,str(new_logic))
                        else:
                            code_struct.add_snippet_logic(var,str(new_logic))

                #，
                #，
                
        if s.startswith("loop"):
            # print("loop")
            #“”，，
            #
            # dependencies = extract_dependencies(unit)
            # #print(return_snippet_explain2(unit,dependencies,snippet_logic))

            # for d in dependencies:
            #     import_dict = code_struct.get_import()
            #     if d in import_dict:
            #         #import，
            #         unit = import_dict[d] + "\n" + unit
            # ,,
            # unit = add_assign(unit,dependencies,code_struct.get_structure_code())
            if(code_depth(unit)<=TH):
                input_token,output_token,loop_logic,code_snippet = return_snippet_explain3(unit,dependencies,code_struct,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                # loc_cod，
                used_py_code,python_extracted=get_py_map(unit,python_extracted)
                res+=loc_code(unit,'loop',used_py_code,js_extracted)
                
                # loc_code(unit,'loop',python_extracted,js_extracted)
            else:
                #
                new_unit = extract_second_indent(unit)
                # print("：",new_unit)
                res+= OverAllLogic(new_unit,code_struct,python_extracted,js_extracted)
                # print("----------------------")
                #
                new_code = unit.split("\n")[0]+"\n**nested code block**\n"
                
                input_token,output_token,loop_logic,code_snippet = return_snippet_explain3(new_code+"nested code block logic:"+str(res),dependencies,code_struct,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                
                # loc_cod，
                used_py_code,python_extracted=get_py_map(unit,python_extracted)
                res+=loc_code(unit,'loop',used_py_code,js_extracted)
                # loc_code(unit,'loop',python_extracted,js_extracted)

            input_tokens = input_tokens+input_token
            output_tokens = output_tokens+output_token
            code_struct.add_structure_logic(s,loop_logic)

            #，
            #，
            for var in dependencies:
                if var in code_struct.get_snippet_logic():
                    ori_logic = code_struct.get_snippet_logic()[var]
                    input_token,output_token,new_logic = update_snippet_logic(loop_logic,var,code_snippet,ori_logic)
                    input_tokens = input_tokens+input_token
                    output_tokens = output_tokens+output_token
                    
                    # print(""+var+"：")
                    # print(new_logic)
                    # print("----------------------")
                    #
                        
                    #varsnippet_logic，
                    code_struct.update_snippet_logic(var,str(new_logic))
                
        if s.startswith("class"):

            #“”，，

            #
            # dependencies = extract_dependencies(unit)
            # #print(return_snippet_explain2(unit,dependencies,snippet_logic))

            # for d in dependencies:
            #     import_dict = code_struct.get_import()
            #     if d in import_dict:
            #         #import，
            #         unit = import_dict[d] + "\n" + unit
            #unit = add_assign(unit,dependencies,structure_code_dict)
            if(code_depth(unit)<=TH):

                # loc_cod，
                used_py_code,python_extracted=get_py_map(unit,python_extracted)
                res+=loc_code(unit,'class',used_py_code,js_extracted)
                # loc_code(unit,'class',python_extracted,js_extracted)
                input_token,output_token,class_logic,code_snippet = return_snippet_explain3(unit,dependencies,code_struct,problem_statement=problem_statement,use_problem_statement=use_problem_statement)

            else:
                #
                new_unit = extract_second_indent(unit)
                # print("：",new_unit)
                res += OverAllLogic(new_unit,code_struct,python_extracted,js_extracted)
                # print("----------------------")
                #
                new_code = unit.split("\n")[0]+"**nested code block**"
                
                input_token,output_token,class_logic,code_snippet = return_snippet_explain3(new_code+"nested code block logic:"+str(res),dependencies,code_struct,problem_statement=problem_statement,use_problem_statement=use_problem_statement)
            # input_tokens = input_tokens+input_token
            # output_tokens = output_tokens+output_token
            code_struct.add_structure_logic(s,class_logic)

            #
            class_name = re.search(r"class(.*?):", unit).group(1)
            #
            class_name = class_name.replace(" ","").replace("(","").replace(")","")

            code_struct.add_class_logic(class_name,class_logic)
            temp = {s:class_logic}
            code_struct.add_class_logic(class_name,class_logic)

        if s.startswith("output"):
            tem_s=[]
            tem_s.append(s)
            for i in range(s_position+1,len(tem_code_struct)):
                if tem_code_struct[i].startswith("output"):
                    tem_s.append(tem_code_struct[i])
                else:
                    break
            for s in tem_s:
                unit = structure_code_dict[s]
                # dependencies = extract_dependencies(unit)
                dependencies=[]
                input_token,output_token,logic = return_output_explain(unit,dependencies,code_struct.get_snippet_logic(),code_struct.get_function_logic(),problem_statement=problem_statement,use_problem_statement=use_problem_statement)
                input_tokens = input_tokens+input_token
                output_tokens = output_tokens+output_token
                code_struct.add_structure_logic(s,logic)

            # tem_code_structtem_s
            if len(tem_s)>1:
                for i in range(len(tem_s)-1):
                    tem_code_struct.remove(tem_s[i])
            code=""
            for i in range(len(tem_s)):
                code=code+structure_code_dict[tem_s[i]]+"\n"

            # loc_cod，
            used_py_code,python_extracted=get_py_map(code,python_extracted)
            res+=loc_code(code,'output',used_py_code,js_extracted)   
            # loc_code(code,'output',python_extracted,js_extracted)

    for s in code_struct.get_code_struct():
        if s =="assign":
            structure_code_dict = code_struct.get_structure_code()
            assign_code = structure_code_dict[s]
            #
            var = assign_code.split("=")[0]
            #
            var = var.replace(" ","")
            snippet_logic = code_struct.get_snippet_logic()
            if var in snippet_logic:
                var_logic = snippet_logic[var]
            
                #
                #structure_logic_dict[s] = var_logic
                code_struct.update_structure_logic(s,var_logic)
            continue
    return res


