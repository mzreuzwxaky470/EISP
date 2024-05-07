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

setproctitle("cl")
model=None
tokenizer=None
# model, tokenizer = init_model_and_tokenizer()


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


                    map_result=map_code(source_code,target_code)
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
    print(":",num)
    print(":",num_error)
    return

def EISP(source_code,target_code):

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


    map_result=map_code(source_code,target_code,model,tokenizer)
    python_extracted,js_extracted=get_map(map_result,source_code,target_code)

    code_struct=None
    res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
    
    if res=="":
        res="yes"

    return res

def EISP_indecomposition(source_code,target_code):
    res=""
    res,input_token,output_token=locate_error(source_code,target_code)
    if res=="":
        res="yes"

    return res

def EISP_without_AIchain(source_code,target_code):

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
    map_result=map_code(source_code,target_code,model,tokenizer)
    python_extracted,js_extracted=get_map(map_result,source_code,target_code)

    code_struct=None
    res = OverAllLogic(source_code,code_struct,python_extracted,js_extracted)
    if res=="":
        res="yes"




    return res
def EISP_main():

    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_EISP/dataset/human_gfg/gpt3.5.json"
    eval_dataset(EISP,few_shot_gpt4_turbo_result_path)

    output_path="EISP/eval/result/gpt4_EISP/dataset/human_gfg/gpt3.5_format.json"
    Standardised_output_format(few_shot_gpt4_turbo_result_path,output_path)

def EISP_main_indecomposition():

    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_EISP/EISP_main_indecomposition_result/gpt3.5.json"
    eval_dataset(EISP_indecomposition,few_shot_gpt4_turbo_result_path)

    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt4_EISP/EISP_main_indecomposition_result/gpt3.5_format.json"
    Standardised_output_format(file_path,output_path)


    output_path="EISP/eval/result/gpt4_EISP/EISP_main_indecomposition_result/gpt3.5_format.json"
    evaluations(output_path)

def EISP_main_without_AIchain():

    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_EISP/EISP_main_without_AIchain_result/gpt3.5.json"
    eval_dataset(EISP_without_AIchain,few_shot_gpt4_turbo_result_path)

    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt4_EISP/EISP_main_without_AIchain_result/gpt3.5_format.json"
    Standardised_output_format(file_path,output_path)


    output_path="EISP/eval/result/gpt4_EISP/EISP_main_without_AIchain_result/gpt3.5_format.json"
    evaluations(output_path)
def EISP_main_without_kb():

    few_shot_gpt4_turbo_result_path="/home/user/cl/EISP/eval/result/gpt4_EISP/EISP_main_without_kb_result /gpt3.5.json"
    eval_dataset(EISP,few_shot_gpt4_turbo_result_path)

    file_path=few_shot_gpt4_turbo_result_path
    output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/EISP_main_without_kb_result /gpt3.5_format.json"
    Standardised_output_format(file_path,output_path)


    output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/EISP_main_without_kb_result /gpt3.5_format.json"
    evaluations(output_path)
    return

def locate_error2(source_code,target_code):
    messages=[]
    input_token=0
    output_token=0

    prompt1=get_prompt("located_error_prompt1.txt")
    prompt1 = prompt1.replace("{python code flag}",source_code)
    prompt1 = prompt1.replace("{javascript code flag}",target_code)
    messages.append({"role": "user", "content": prompt1})
    response, messages, extra_response_count=get_api_continue_response(messages)

    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    javascript_reference_document=get_knowledge_base(response["choices"][0]["message"]["content"])



    print(javascript_reference_document+"\n"+"---------")

    assistant_reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": assistant_reply})


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

    messages=[]
    prompt3=get_prompt("located_error_prompt3.txt")
    prompt3 = prompt3.replace("{api and operator comparison}",assistant_reply)
    prompt3=prompt3.replace("{javascript reference document}",javascript_reference_document)
    messages.append({"role": "user", "content": prompt3})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
        
    assistant_reply3 = response["choices"][0]["message"]["content"]


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

    # messages=[]
    prompt5=get_prompt("located_error_prompt5.txt")
    prompt5 = prompt5.replace("{reference document flag}",assistant_reply3)
    messages.append({"role": "user", "content": prompt5})
    response, messages, extra_response_count = get_api_continue_response(messages)
    input_token += num_tokens_from_string(messages[0]['content'])
    output_token += num_tokens_from_string(response["choices"][0]["message"]["content"])
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})


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
    # test()

    # 1, need to choose 3.5 or 4
    EISP_main() #dataset








