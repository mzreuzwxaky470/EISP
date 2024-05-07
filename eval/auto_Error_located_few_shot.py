import sys
import os
import json
sys.path.append('/home/user/cl/EISP')
from code_spilt import code_strip_spaces
from myAPItoken import *
from OverallLogicToken import write_result
from bs4 import BeautifulSoup
import json
import tiktoken
import re
from setproctitle import setproctitle
# model, tokenizer = init_model_and_tokenizer()

# model,tokenizer=init_model_and_tokenizer_starling_LM_7B_beta()
def few_shot_gpt35(source_code,target_code):
    few_shot_prompt =""
    with open("EISP/prompt/baseline/few_shot.txt","r") as f:
        few_shot_prompt = f.read()
    few_shot_prompt=few_shot_prompt.replace("{source_code_flag}",source_code)
    few_shot_prompt=few_shot_prompt.replace("{target_code_flag}",target_code)
    messages=[]
    messages.append({"role": "user", "content": few_shot_prompt})
    response, messages, extra_response_count=get_api_continue_response(messages)

    # response, messages, extra_response_count=Mistral_7B_v2(messages, model, tokenizer)

    assistant_reply = response["choices"][0]["message"]["content"]

    print(assistant_reply)
    # result_dict={}

    return assistant_reply
def cot_gpt(source_code,target_code):
    cot_prompt =""
    with open("EISP/prompt/baseline/cot.txt","r") as f:
        cot_prompt = f.read()
    cot_prompt=cot_prompt.replace("{source_code_flag}",source_code)
    cot_prompt=cot_prompt.replace("{target_code_flag}",target_code)
    messages=[]
    messages.append({"role": "user", "content": cot_prompt})
    response, messages, extra_response_count=get_api_continue_response(messages)

    # response, messages, extra_response_count=Mistral_7B_v2(messages, model, tokenizer)

    assistant_reply = response["choices"][0]["message"]["content"]

    print(assistant_reply)
    # result_dict={}

    return assistant_reply
def eval_dataset(method_func,result_path,data_path="EISP/data/dataset/test/test2.json"):

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
    for file_path,file_path_name in zip(file_path_list,file_path_name_list):
        tem_dict={}
        # if num>3:
        #         break
        for root, dirs, files in os.walk(file_path):
            sample_result_dict={}
            file_full_path = os.path.join(root,file_name)
            res_name=re.search(r'codex0err/(.+)$',root)
            if os.path.exists(file_full_path):
                    


                    # if file_path_name=="leetcode": continue
                    print("sample_num:",num)
                    # if num>20:
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

                    # result={}
                    result=method_func(source_code,target_code)
                    # result={}
                    sample_result_dict["result"]=result
                    tem_dict[res_name.group(1)]=sample_result_dict

        output_path="/home/user/cl/EISP/eval/result/gpt4_EISP/test.json"
        result_dict[file_path_name]=tem_dict 
        with open(output_path,'w') as f:
            json.dump(result_dict,f)   
        print("1")
        # if num>3:
        #         break
    with open(result_path,'w') as f:
        json.dump(result_dict,f)             
    print(num)
    return

# source_code=open('EISP/data/source_code.py').read()
# target_code=open('EISP/data/target_code.js').read()
# a=few_shot_gpt35(source_code,target_code)


def Standardised_output_format(file_path,output_path):
    with open(file_path,'r') as f:
        result_dict=json.load(f)
    num=0
    for key in result_dict:
        for key2 in result_dict[key]:
            print(num)
            num+=1
            result_i=result_dict[key][key2]["result"]
            # print(result_i)
            if "YES" in result_i.upper():
                result_dict[key][key2]["format_result"]="YES"
                result_dict[key][key2]["incorrect_code"]=[]
                result_dict[key][key2]["Explanation"]=[]
                print(1)
                continue

            format_pormpt=""
            with open("EISP/prompt/baseline/format_prompt.txt",'r') as f:
                    format_pormpt=f.read()
            format_pormpt=format_pormpt.replace("{database function flag}",result_i)
            format_result=""
            messages=[]
            messages.append({"role": "user", "content": format_pormpt})
            response, messages, extra_response_count=get_api_format_result(messages)       
            format_result=response["choices"][0]["message"]["content"]

            incorrect_code = re.findall(r"Incorrect Line of Code\*\*\*: (.*?)\*\*\*", format_result)
            incorrect_code=[i.strip() for i in incorrect_code]

            incorrect_code=list(set(incorrect_code))
            # Explanation = re.findall(r"Corrected Explanation\*\*\*: (.*?)\*\*\*", format_result)
            # print("incorrect_code::::::",incorrect_code)
            # print('------')
            # print(Explanation)
            result_dict[key][key2]["format_result"]=format_result
            result_dict[key][key2]["incorrect_code"]=incorrect_code
            # result_dict[key][key2]["Explanation"]=Explanation
    
    with open(output_path,'w') as f:
        json.dump(result_dict,f)
    return



def evaluations_sem(file_path,category_file_path,dataset_category=""):
    with open(file_path,'r') as f:
        result_dict=json.load(f)
    

    suc_num=0

    Total_errors=0

    Total_code_lines=0

    sus_lines_dict={}
    sus_lines_error_dict={}
    sus_lines_solved_error_dict={}
    Average_ratio=0
    for key in result_dict:
        if dataset_category!="" and key!=dataset_category:
            continue

        category_path=category_file_path
        category_path=category_path.replace("{category}",key)
        category_error_total=[]
        with open(category_path,'r') as f:
                category_error_total=f.readlines()
                category_error_total=[i.strip() for i in category_error_total ]
        f.close()

        for key2 in result_dict[key]:
            

            code_lines=0

            result_dict[key][key2]["incorrect_code"]=[i.strip() for i in result_dict[key][key2]["incorrect_code"]]
            result_dict[key][key2]["incorrect_code"]=list(set(result_dict[key][key2]["incorrect_code"]))


            for incorrect_code_i in result_dict[key][key2]["incorrect_code"]:
                code_lines+=1

            codeline_num=result_dict[key][key2]["target_code"].count("\n") 


            falg2=1
            inject_num=0

            solved_error_num=0

            for inject in result_dict[key][key2]["injects"]:

                inject_sum=inject["replacement"].split("\n")
                inject_sum=[i.strip() for i in inject_sum if i.strip()!=""]
                
                error_tag=key2+'.'+str(inject_num)
                inject_num+=1

                if error_tag not in category_error_total:
                    continue

                Total_errors+=1

                if len(result_dict[key][key2]["incorrect_code"])==0:
                    continue

                flag=0
                for inject_i in inject_sum:
                    incorrect_code_str="".join(result_dict[key][key2]["incorrect_code"])
                    if (inject_i!="{" and inject_i!="}") and inject_i not in incorrect_code_str:
                        flag=1
                        break

                if flag==0:
                    solved_error_num+=1
                    suc_num+=1
                    falg2=0

            if falg2==0:

                if str(len(result_dict[key][key2]["incorrect_code"])) in sus_lines_dict:
                    sus_lines_dict[str(len(result_dict[key][key2]["incorrect_code"]))]+=1
                    sus_lines_error_dict[str(len(result_dict[key][key2]["incorrect_code"]))]+=len(result_dict[key][key2]["injects"])
                    sus_lines_solved_error_dict[str(len(result_dict[key][key2]["incorrect_code"]))]+=solved_error_num
                else:
                    sus_lines_dict[str(len(result_dict[key][key2]["incorrect_code"]))]=1
                    sus_lines_error_dict[str(len(result_dict[key][key2]["incorrect_code"]))]=len(result_dict[key][key2]["injects"])
                    sus_lines_solved_error_dict[str(len(result_dict[key][key2]["incorrect_code"]))]=solved_error_num

                Total_code_lines+=code_lines

                Average_ratio+=code_lines/codeline_num


    sus_lines_sum=0
    sus_lines_solved_error_dict_sum=0
    sus_lines_error_dict_sum=0

    sus_lines_ratio_dict={}
    for key in sus_lines_dict:
        sus_lines_sum+=sus_lines_dict[key]
        sus_lines_solved_error_dict_sum+=sus_lines_solved_error_dict[key]
        sus_lines_error_dict_sum+=sus_lines_error_dict[key]
        sus_lines_ratio_dict[key]=sus_lines_dict[key]*int(key)/sus_lines_solved_error_dict[key]

    for key in sus_lines_dict:
        sus_lines_dict[key]=sus_lines_dict[key]/sus_lines_sum*100
        sus_lines_solved_error_dict[key]=sus_lines_solved_error_dict[key]/sus_lines_solved_error_dict_sum*100
        sus_lines_error_dict[key]=sus_lines_error_dict[key]/sus_lines_error_dict_sum*100


    sus_lines_error_dict=dict(sorted(sus_lines_error_dict.items(),key=lambda item: item[1]))

    sus_lines_solved_error_dict=dict(sorted(sus_lines_solved_error_dict.items(),key=lambda item: item[1]))

    sus_lines_dict=dict(sorted(sus_lines_dict.items(),key=lambda item: item[1]))
    
    print(suc_num)
    print(Total_errors)
    print(suc_num/Total_errors)
    print(Total_code_lines/suc_num)
    print(Average_ratio/suc_num)

    key1=[key for key in sus_lines_dict]
    value1=[sus_lines_dict[key] for key in sus_lines_dict]
    value2=[sus_lines_solved_error_dict[key] for key in sus_lines_dict]
    value3=[sus_lines_ratio_dict[key] for key in sus_lines_dict]
    print(key1)
    print(value1)
    print(value2)
    print(value3)

    return

def evaluations_sem_2(file_path,category_file_path):
    with open(file_path,'r') as f:
        result_dict=json.load(f)
    

    suc_num=0

    Total_errors=0

    Total_code_lines=0

    sus_lines_dict={}
    Average_ratio=0
    for key in result_dict:

        category_path=category_file_path
        category_path=category_path.replace("{category}",key)
        category_error_total=[]
        with open(category_path,'r') as f:
                category_error_total=f.readlines()
                category_error_total=[i.strip() for i in category_error_total ]
        f.close()

        
        for key2 in result_dict[key]:
            

            code_lines=0

            codeline_num=result_dict[key][key2]["target_code"].count("\n") 


            falg2=1
            inject_num=0

            for inject in result_dict[key][key2]["injects"]:

                inject_sum=inject["replacement"].split("\n")
                inject_sum=[i.strip() for i in inject_sum if i.strip()!=""]
                
                error_tag=key2+'.'+str(inject_num)
                inject_num+=1

                if error_tag not in category_error_total:
                    continue

                Total_errors+=1

                if "yes" in result_dict[key][key2]["result"].lower():
                    continue
                flag=1
                
                if inject["replacement"].strip() in result_dict[key][key2]["result"]:
                        flag=0

                if flag==0:

                    suc_num+=1
                    falg2=0
            if falg2==0:

                Total_code_lines+=code_lines

                Average_ratio+=code_lines/codeline_num


    sus_lines_dict=dict(sorted(sus_lines_dict.items(),key=lambda item: item[1]))
    sus_lines_sum=0
    for key in sus_lines_dict:
        sus_lines_sum+=sus_lines_dict[key]
    print(suc_num)
    print(Total_errors)
    print(suc_num/Total_errors)
    print(Total_code_lines/suc_num)
    print(Average_ratio/suc_num)
    print(sus_lines_dict)
    print(sus_lines_sum)
    return

def few_shot_gpt35_main():

    few_shot_gpt35_result_path="EISP/eval/result/gpt3.5_fewshot/test.json"
    eval_dataset(few_shot_gpt35,few_shot_gpt35_result_path)


    file_path="EISP/eval/result/gpt3.5_fewshot/test.json"
    output_path="EISP/eval/result/gpt3.5_fewshot/gpt35.json"
    Standardised_output_format(file_path,output_path)


    result_path="EISP/eval/result/gpt3.5_fewshot/gpt35.json"
    evaluations(result_path)
    return
def few_shot_starling_LM_7B_beta(source_code,target_code):
    few_shot_prompt =""
    with open("EISP/prompt/baseline/few_shot.txt","r") as f:
        few_shot_prompt = f.read()
    few_shot_prompt=few_shot_prompt.replace("{source_code_flag}",source_code)
    few_shot_prompt=few_shot_prompt.replace("{target_code_flag}",target_code)

    single_turn_prompt = f"GPT4 Correct User: {few_shot_prompt}<|end_of_turn|>GPT4 Correct Assistant:"

    res=generate_response_starling_LM_7B_beta(single_turn_prompt,model,tokenizer)

    assistant_reply = res

    print(assistant_reply)


    return assistant_reply

def few_shot_starling_LM_7B_beta_main():

    few_shot_gpt35_result_path="/home/user/cl/EISP/eval/result/fewshot_starling_LM_7B_beta/gpt35.json"
    eval_dataset(few_shot_starling_LM_7B_beta,few_shot_gpt35_result_path)
    return

def few_shot_gpt4_turbo_main():

    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_fewshot/gpt4.json"
    eval_dataset(few_shot_gpt35,few_shot_gpt4_turbo_result_path)

    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt4_fewshot/gpt4_format.json"
    Standardised_output_format(file_path,output_path)


    output_path="EISP/eval/result/gpt4_fewshot/gpt4_format.json"
    evaluations(output_path)
def cot_gpt35_main():

    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt3.5_cot/gpt35.json"
    eval_dataset(cot_gpt,few_shot_gpt4_turbo_result_path)

    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt3.5_cot/gpt35_format.json"
    Standardised_output_format(file_path,output_path)
def cot_gpt4_main():

    few_shot_gpt4_turbo_result_path="EISP/eval/result/gpt4_cot/zero_cot/dataset/gpt35.json"
    eval_dataset(cot_gpt,few_shot_gpt4_turbo_result_path)

    file_path=few_shot_gpt4_turbo_result_path
    output_path="EISP/eval/result/gpt4_cot/zero_cot/dataset/gpt35_format.json"
    Standardised_output_format(file_path,output_path)
if __name__ == "__main__":
    # cot_gpt4_main()
    # cot_gpt35_main()
    file_path="EISP/eval/result/gpt4_cot/zero_cot/dataset/gpt35.json"
    output_path="EISP/eval/result/gpt4_cot/zero_cot/dataset/gpt35_format.json"



    # cot shot 3.5
    # result_path="/home/user/cl/EISP/eval/result/gpt3.5_cot/zero_cot/dataset/gpt35_format.json"
    # few shot 4
    # result_path="/home/user/cl/EISP/eval/result/gpt4_fewshot/dataset/gpt4_format.json"
    # cot shot 4
    # result_path="/home/user/cl/EISP/eval/result/gpt4_cot/zero_cot/dataset gpt-12/gpt35_format.json"
    # EISP gpt3.5
    result_path="/home/user/cl/EISP/eval/result/gpt4_EISP/dataset/gpt3.5_format.json"
    dataset_category=""

    result_path="/home/user/cl/EISP/eval/result/gpt4_EISP/dataset/gpt3.5_format.json"
    category_path="EISP/eval/result/category/{category}/error_total.txt"
    evaluations_sem(result_path,category_path,dataset_category)
    print("-----------------------------------------------------------")
    category_path="EISP/eval/result/category/{category}/e_sem.txt"
    evaluations_sem(result_path,category_path,dataset_category)
    print("-----------------------------------------------------------")
    category_path="EISP/eval/result/category/{category}/hid.txt"
    evaluations_sem(result_path,category_path,dataset_category)
    print("-----------------------------------------------------------")
    category_path="EISP/eval/result/category/{category}/dif.txt"
    evaluations_sem(result_path,category_path,dataset_category)




