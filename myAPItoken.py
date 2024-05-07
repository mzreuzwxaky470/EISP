import openai
import time
from code_spilt import code_strip_spaces
import re
import tiktoken
from FewShot import *
import logging
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from torch.cuda.amp import autocast
import transformers
# from accelerate import *
# from torch import *
# 
api_key=""
api_key = ''


temp = 0.2
# temp = 0
max_tok = 300
# gpt_top_P=0.9
gpt_top_P=1.0
gpt_model = "gpt-3.5-turbo"
is_summary  = False

# log_path="EISP/log2.log"
log_path="/home/user/cl/EISP/gpt_log.log"
logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# OpenAI
openai.api_key = api_key


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

# def get_api_response(prompt,max_tokens = max_tok,n = 1,temperature = temp):
#     messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code."},
#                  {"role":"user", "content": prompt}]
#     chat_completion = openai.ChatCompletion.create(model=gpt_model, 
#                                     messages=messages_list,
#                                     max_tokens = max_tok,
#                                     n=1,
#                                     temperature=temp)
#     return chat_completion.choices[0].message.content
def get_response(prompt,max_tokens = max_tok,n = 1,temperature = temp,gpt_model="gpt-4-1106-preview"):
        # logging.info("ChatGPT prompt: " + prompt)
        messages=[]
        if {"role": "system", "content":"""
            You are ChatGPT, a large language model trained by OpenAI.
            Knowledge cutoff: 2023-12 
            Current date: 2024-03
        """} not in messages:
            messages.append({"role": "system", "content":"""
                You are ChatGPT, a large language model trained by OpenAI.
                Knowledge cutoff: 2023-12 
                Current date: 2024-03
            """})
        messages.append({"role": "user", "content": prompt})
        extra_response_count = 0
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=gpt_model,
                    messages=messages,
                    temperature=temperature,
                    top_p=gpt_top_P,
                    # max_tokens=max_tokens
                )
            except Exception as e:
                print(e)
                time.sleep(30)
                continue
            if response["choices"][0]["finish_reason"] == "stop":
                break
            else:
                messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
                messages.append({"role": "user", "content": "continue"})
                extra_response_count += 1
        logging.info("ChatGPT response: " + response["choices"][0]["message"]["content"])
        # response["choices"][0]["message"]["content"]
        # return response["choices"][0]["message"]["content"]
        return response, messages, extra_response_count
def get_api_response(prompt,max_tokens = max_tok,n = 1,temperature = temp):
        logging.info("ChatGPT prompt: " + prompt)
        messages=[]
        if {"role": "system", "content":"""
            You are ChatGPT, a large language model trained by OpenAI.
            Knowledge cutoff: 2023-12 
            Current date: 2024-03
        """} not in messages:
            messages.append({"role": "system", "content":"""
                You are ChatGPT, a large language model trained by OpenAI.
                Knowledge cutoff: 2023-12 
                Current date: 2024-03
            """})
        messages.append({"role": "user", "content": prompt})
        extra_response_count = 0
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=gpt_model,
                    messages=messages,
                    temperature=temperature,
                    top_p=gpt_top_P,
                    # max_tokens=max_tokens
                )
            except Exception as e:
                print(e)
                time.sleep(30)
                continue
            if response["choices"][0]["finish_reason"] == "stop":
                break
            else:
                messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
                messages.append({"role": "user", "content": "continue"})
                extra_response_count += 1
        logging.info("ChatGPT response: " + response["choices"][0]["message"]["content"])
        # response["choices"][0]["message"]["content"]
        # return response["choices"][0]["message"]["content"]
        return response, messages, extra_response_count
# EISPchatgpt api
def get_api_continue_response(messages,max_tokens = max_tok,n = 1,temperature = temp):
        logging.info("\nChatGPT prompt:  \n" +messages[0]['content'])
        if {"role": "system", "content":"""
            You are ChatGPT, a large language model trained by OpenAI.
            Knowledge cutoff: 2023-12 
            Current date: 2024-03
        """} not in messages:
            messages.append({"role": "system", "content":"""
                You are ChatGPT, a large language model trained by OpenAI.
                Knowledge cutoff: 2023-12 
                Current date: 2024-03
            """})
        extra_response_count = 0
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=gpt_model,
                    messages=messages,
                    temperature=temperature,
                    top_p=gpt_top_P
                )
            except Exception as e:
                print(e)
                time.sleep(30)
                continue
            if response["choices"][0]["finish_reason"] == "stop":
                break
            else:
                messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
                messages.append({"role": "user", "content": "continue"})
                extra_response_count += 1
        logging.info("\nChatGPT response: \n" + response["choices"][0]["message"]["content"])
        # response["choices"][0]["message"]["content"]
        # return response["choices"][0]["message"]["content"]
        # input_token = num_tokens_from_string(messages[0]['content'])
        # output_token = num_tokens_from_string(response["choices"][0]["message"]["content"])
        return response, messages, extra_response_count

def get_api_format_result(messages,max_tokens = max_tok,n = 1,temperature = 0):
        if {"role": "system", "content":"""
            You are ChatGPT, a large language model trained by OpenAI.
            Knowledge cutoff: 2023-04 
            Current date: 2024-03
        """} not in messages:
            messages.append({"role": "system", "content":"""
                You are ChatGPT, a large language model trained by OpenAI.
                Knowledge cutoff: 2023-04 
                Current date: 2024-03
            """})
        extra_response_count = 0
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model = "gpt-4-1106-preview",

                    messages=messages,
                    temperature=temperature,
                    top_p=gpt_top_P
                )
            except Exception as e:
                print(e)
                time.sleep(30)
                continue
            if response["choices"][0]["finish_reason"] == "stop":
                break
            else:
                messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
                messages.append({"role": "user", "content": "continue"})
                extra_response_count += 1
        logging.info("\nChatGPT response: \n" + response["choices"][0]["message"]["content"])
        # response["choices"][0]["message"]["content"]
        # return response["choices"][0]["message"]["content"]
        return response, messages, extra_response_count
def return_snippet_explain(code):
    code_content = "code:\n"+str(code)+"\nexplain the above code logic:\n"
    return get_api_response(code_content)
    

#，
def return_input_assign_explain(code,problem_statement):
    return 0,0,0
    
    code_content = "[Task description:]\n"+str(problem_statement)+"\n[code:]\n"+str(code)+"\n[explain the above code logic:]\n"
    
    input_token = num_tokens_from_string(code_content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code. Output nothing but understand the logic of the input variables"},
                 {"role":"user", "content": code_content},{"role":"user", "content": "Summarize the above variable logic: The variable"}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 100,
                                    n=1,
                                    temperature=temp)

    output_token = num_tokens_from_string(chat_completion.choices[0].message.content)
    return input_token,output_token,chat_completion.choices[0].message.content


def add_external_var(code,varlist,codedict):
    my_codedict = []
    #，
    for var in varlist:
        if var in codedict:
            my_codedict.append(codedict[var])
    
    #
    newcode = ""
    for c in my_codedict:
        newcode = newcode+c+"\n"
    newcode = newcode+code

    newcode = code_strip_spaces(newcode)
    
    return newcode

def return_assign_explain(code,varlist,classdict,funcdict,problem_statement,use_problem_statement):
    
    return 0,0,"0"

    if classdict == {}:
        return 0,0,""
    if use_problem_statement:
        code = "[Task description:]\n"+str(problem_statement)+"\n[code:]\n"+str(code)+code
    for v in varlist:
        if v in classdict:
            code = code+"\n"+"**The logic of class"+str(v)+" is "+str(classdict[v])+"\n"
        if v in funcdict:
            code = code+"\n"+"**The logic of function"+str(v)+" is "+str(funcdict[v])+"\n"
    code_content = "**code:\n"+str(code)+"\n**explain the above code logic:\n"

    input_token = num_tokens_from_string(code_content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code. Output nothing but understand the logic of the input variables"},
                    {"role":"user", "content": code_content},{"role":"user", "content": "Summarize the above variable logic: The variable"}]

    chat_completion = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 100,
                                    n=1,
                                    temperature=temp)
    output_token = num_tokens_from_string(chat_completion.choices[0].message.content)
    return input_token,output_token,chat_completion.choices[0].message.content
def return_snippet_explain2(code,varlist,vardict,codedict,fundict):
    return 0
    code = add_external_var(code,varlist,codedict)

    code_content = "code:\n"+str(code)+"\n The original meaning of variable:"
    #varlist = {"variable":"x1","variable_logic":"xxxxxxx"}
    for var in varlist:
        #variable_logic
        if var in vardict:
            var_content = vardict[var]
            if var_content!="":
                code_content = code_content+str(var_content)+"\n"
        #function_logic
        if var in fundict:
            var_content = fundict[var]
            code_content = code_content+"\nThe function of "+str(var)+" is "+str(var_content)+"\n"
    code_content = code_content+"\nexplain the above code logic:"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    #,{"role":"user", "content": "Summarize the above code logic:"}
    answer = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 600,
                                    n=1,
                                    temperature=temp)
    if is_summary:
    #prompt，
        messages_list2 = [{"role":"assistant", "content": answer.choices[0].message.content},{"role":"user", "content": "Summarize the above code logic:"}]
        answer2 = openai.ChatCompletion.create(model=gpt_model, 
                                        messages=messages_list2,
                                        max_tokens = 400,
                                        n=1,
                                        temperature=temp)

        return answer2.choices[0].message.content,code
    else:

        return answer.choices[0].message.content,code
    

def return_snippet_explain3(code,dependencies,codeStructure,problem_statement,use_problem_statement):

    return 0,0,"0",code
    varlist = dependencies
    vardict = codeStructure.get_snippet_logic()
    codedict = codeStructure.get_assign_code()
    fundict = codeStructure.get_function_logic()
    code = add_external_var(code,varlist,codedict)
    if use_problem_statement:
        code_content = "[Task description:]\n"+str(problem_statement)
    else:
        code_content = ""
    code_content = code_content+"**code:\n"+str(code)+"\n **The original meaning of variable:"
    #varlist = {"variable":"x1","variable_logic":"xxxxxxx"}
    for var in varlist:
        #variable_logic
        if var in vardict:
            var_content = vardict[var]
            if var_content!="":
                code_content = code_content+str(var_content)+"\n"
        #function_logic
        if var in fundict:
            var_content = fundict[var]
            code_content = code_content+"\n**The function of "+str(var)+" is "+str(var_content)+"\n"
    code_content = code_content+"\n**explain the above code logic(If it contains an output or input(print\input), explain them):"
    input_token = num_tokens_from_string(code_content)

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    #,{"role":"user", "content": "Summarize the above code logic:"}
    answer = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 600,
                                    n=1,
                                    temperature=temp)
    output_token = num_tokens_from_string(answer.choices[0].message.content)
    if is_summary:
    #prompt，
        messages_list2 = [{"role":"assistant", "content": answer.choices[0].message.content},{"role":"user", "content": "Summarize the above code logic:"}]
        answer2 = openai.ChatCompletion.create(model=gpt_model, 
                                        messages=messages_list2,
                                        max_tokens = 400,
                                        n=1,
                                        temperature=temp)
        output_token = num_tokens_from_string(answer2.choices[0].message.content)
        return input_token,output_token,answer2.choices[0].message.content,code
    else:

        return input_token,output_token,answer.choices[0].message.content,code

#、，
def update_snippet_logic(background,snippet,code_snippet,origin_logic):

    return 0,0,"0"
    code_content = return_UpdateLogic_FW()

    code_content = code_content+"**Code snippet:\n"+str(code_snippet)+"\n**Code snippet logic explain: \n"+str(background)+"\n"+"\nThe origin logic of \""+str(snippet)+"\":\n"+str(origin_logic)+"\n**Explain the meaning of "+str(snippet)+" is from the above code snippet(If snippet's logic is not provided in the given code snippet, output the origin logic):"

    input_token = num_tokens_from_string(code_content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and code's background, I'll Extract the part of the background information about the code snippet (no further explanation is needed)."},
                 {"role":"user", "content": code_content}]
    answer = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=temp)

    output_token = num_tokens_from_string(answer.choices[0].message.content)
    return input_token,output_token,answer.choices[0].message.content

"""
<OpenAIObject at 0x7f91087a33d0> JSON: {
  "index": 0,
  "message": {
    "role": "assistant",
    "content": "The code snippet is an implementation of the selection sort algorithm. \n\nThe outer loop iterates `n` times, where `n` is the number of elements in the sequence. This loop is responsible for selecting the minimum element from the unsorted portion of the list and placing it in its correct position in the sorted portion of the list.\n\nInside the outer loop, the variable `min_idx` is initialized to `i`, which represents the current position in the list. This variable keeps track of the index of the minimum element found so far.\n\nThe inner loop starts from `i+1` and iterates until `n`. This loop is responsible for finding the minimum element in the unsorted portion of the list. It compares each element with the current minimum element (`a[min_idx]`) and updates `min_idx` if a smaller element is found.\n\nAfter the inner loop completes, the minimum element is swapped with the element at position `i` using a tuple assignment. This ensures that the minimum element is placed in its correct position in the sorted portion of the list.\n\nFinally, the `count` variable is incremented to keep track of the number of iterations performed.\n\nOverall, the code snippet sorts the list `a` in ascending order using the selection sort algorithm."
  },
  "finish_reason": "stop"
}
"""

#，
def return_func_explain(func,problem_statement,use_problem_statement):

    return 0,0,"0"

    if use_problem_statement:
        code_content = "[Task description:]\n"+str(problem_statement)
    else:
        code_content = ""
    code_content = code_content+"Code function snippets:\n"+str(func)+"\nExplain the logical function of the above code function:\n"

    input_token = num_tokens_from_string(code_content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 400,
                                    n=1,
                                    temperature=temp)
    output_token = num_tokens_from_string(chat_completion.choices[0].message.content)
    return input_token,output_token,chat_completion.choices[0].message.content




#“”“”，“”
def return_output_explain(code,dependencies_list,snippet_list,func_dict,problem_statement,use_problem_statement):

    return 0,0,"0"
    #
    if use_problem_statement:
        code_content = "[Task description:]\n"+str(problem_statement)
    else:
        code_content = ""
    code_content = code_content+"The program output is:\n"+str(code)+"\nExplain what the output of the program is:\n"
    
    #
    for var in dependencies_list:
        if var in snippet_list:
            code_content = code_content+str(snippet_list[var])+"\n"
    #
    for var in dependencies_list:
        if var in func_dict:
            code_content = code_content+"\nThe function of "+str(var)+" is: "+str(func_dict[var])+"\n"



    input_token = num_tokens_from_string(code_content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and variable logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=temp)
    output_token = num_tokens_from_string(chat_completion.choices[0].message.content)
    return input_token,output_token,chat_completion.choices[0].message.content

#、，
def return_overall_explain(code,code_structure,structure_code_dict,structure_logic_dict,problem_statement,use_problem_statement):
    if use_problem_statement:
        code_content = "[Task description:]\n"+str(problem_statement)
    else:
        code_content = ""
    code_content = code_content+"\n**code:\n"+str(code)+"\n"
    for s in code_structure:
        code_con = "**code snippet:\n"+str(structure_code_dict[s])+"\n**logic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
        code_content = code_content+code_con
    code_content = code_content+"\n**Explain the logic of the above code in three part separately:Code Input: XXX\\n Code Logic: XXX\\n Code Output: XXX\\n(If the code has no inputs or outputs then point out there is no input or output):\n"

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)


    return chat_completion.choices[0].message.content

#、，
def return_overall_explain2(code,code_structure,structure_code_dict,structure_logic_dict):
    code_content = "**complete code::\n"+str(code)+"\n"+"**following is an expert explanation of each snippet of the code:\n"

    input_code_content = code_content
    for s in code_structure:
        #input，
        if "input" in structure_code_dict[s]:
            code_con = "---------Input code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
            input_code_content = input_code_content+code_con
    code_content1 = input_code_content+"\nAccording to the above experts’ explanation of the code, explain all the input of  above code(If the code has no inputs then point out there is no input, do not explain other part of code except input)Code Input:\n"
    input_token = num_tokens_from_string(code_content1)

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content1}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    input_logic = chat_completion.choices[0].message.content
    output_token = num_tokens_from_string(input_logic)


    logic_code_content = code_content
    for s in code_structure:
        #
        if "input" in structure_code_dict[s]:
            continue
        if "print" in structure_code_dict[s]:
            continue
        code_con = "---------code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
        logic_code_content = logic_code_content+code_con
    code_content1 = logic_code_content+"\nExplain the logic part of the above code:Code Logic(Do not explain the input and output of the code)no more than 300 words:\n"
    input_token = input_token + num_tokens_from_string(code_content1)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                    {"role":"user", "content": code_content1}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    logic_logic = chat_completion.choices[0].message.content
    output_token = output_token + num_tokens_from_string(logic_logic)


    output_code_content = code_content
    for s in code_structure:
        #output，
        if "print" in structure_code_dict[s]:
            code_con = "---------Output code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
            output_code_content = output_code_content+code_con
    code_content1 = output_code_content+"\n**According to the above experts’ explanation of the code, briefly explain the output(print) of  the complete code and explain the meaning of the output values. (If the code has no outputs then point out there is no output, do not explain other part of code. If there are multiple outputs, explain them all )no more than 100 words:\n"
    input_token = input_token + num_tokens_from_string(code_content1)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                    {"role":"user", "content": code_content1}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0.2)
    output_logic = chat_completion.choices[0].message.content
    output_token = output_token + num_tokens_from_string(output_logic)

    
    return input_token,output_token,input_logic,logic_logic,output_logic


#“”，、、
def return_snippet_overall_explain(code,code_structure,structure_code_dict,structure_logic_dict):
    code_content = "code:\n"+str(code)+"\n"
    for s in code_structure:
        code_con = "code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
        code_content = code_content+code_con
    code_content = code_content+"\nBriely explain the logic of the above code(Explain only the general logical function, not the sentence-by-sentence explanation):\n"

    input_token = num_tokens_from_string(code_content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    output_token = num_tokens_from_string(chat_completion.choices[0].message.content)

    return input_token,output_token,chat_completion.choices[0].message.content


#
def return_logic_different(gen_logic,codeNet_logic,task_description,use_problem_statement):
    content = ""
    if use_problem_statement:
        content = content+"**task Description:\n"+str(task_description)
    content = content+"\n**The logical function of the correct code is:\n"+str(codeNet_logic)
    content = content+"\n**The logical function of the generated code is:\n"+str(gen_logic)

    if use_problem_statement:
        content = content+"\n****Compare the different between the correct code above with that of the generated code and evaluate whether the generated code fulfills the logical function of the task. Compare the inputs, logic, and outputs of the code separately(Regardless of the method used to achieve it, unless the task explicitly requires it). Lets's think step by step and figure it out:\n"
    else:
        content = content+"\n****Compare the different between the correct code above with that of the generated code and evaluate whether the generated code achieved the same effect as the correct code, lets's think step by step and figure it out:\n"
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    chat_completion = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)

    return chat_completion.choices[0].message.content

def return_logic_different2(gen_logic,codeNet_logic,task_description,use_problem_statement):
    gen_logics = gen_logic.split("\n")
    codeNet_logics = codeNet_logic.split("\n")
    gen_input_logic = ""
    gen_logic_logic = ""
    gen_output_logic = ""
    codeNet_input_logic = ""
    codeNet_logic_logic = ""
    codeNet_output_logic = ""

    for i in range(len(gen_logics)):
        if "Code Input" in gen_logics[i]:
            gen_input_logic = gen_logics[i]
        if "Code Logic" in gen_logics[i]:
            gen_logic_logic = gen_logics[i]
        if "Code Output" in gen_logics[i]:
            gen_output_logic = gen_logics[i]

    for i in range(len(codeNet_logics)):
        if "Code Input" in codeNet_logics[i]:
            codeNet_input_logic = codeNet_logics[i]
        if "Code Logic" in codeNet_logics[i]:
            codeNet_logic_logic = codeNet_logics[i]
        if "Code Output" in codeNet_logics[i]:
            codeNet_output_logic = codeNet_logics[i]

    content = "**task Description:"+str(task_description)+"\n**This is the logic of input part of the correct code:"
    content = content+"\n"+str(codeNet_input_logic)
    content = content+"\n**This is the logic of input part of the generated code:"
    content = content+"\n"+str(gen_input_logic)
    content = content+"\n**Compare the difference in \"input\" between the correct code and the generated code, explain the functional differences.(If the same functionality is implemented, then output:\"The function of the input part of the two codes is the same\"):"

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    input_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)

    content = "**task Description:"+str(task_description)+"\n**This is the logic of the correct code:"
    content = content+"\n"+str(codeNet_logic_logic)
    content = content+"\n**This is the logic of the generated code:"
    content = content+"\n"+str(gen_logic_logic)
    content = content+"\n**Compare the difference in \"logic\" between the correct code and the generated code(may be logically incorrect), explain the functional differences(No need to compare inputs or outputs).(If the same functionality is implemented, then output: \"Two codes have the same functionality\"):"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    logic_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)


    content = "**task Description:"+str(task_description)+"**This is the logic of output part of the correct code:"
    content = content+"\n"+str(codeNet_output_logic)
    content = content+"\n**This is the logic of output part of the generated code:"
    content = content+"\n"+str(gen_output_logic)
    content = content+"\n**Compare the difference in \"output\" between the correct code and the generated code, explain the functional differences. If the same functionality is implemented, then output:\"The function of the input part of the two codes is the same\")"
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]

    output_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)

    return input_diff.choices[0].message.content,logic_diff.choices[0].message.content,output_diff.choices[0].message.content
                
def return_logic_different3(codeNetinput,codeNetlogic,codeNetoutput,geninput,genlogic,genoutput,task_description,use_problem_statement):

    if use_problem_statement:    
        content = "**task Description:"+str(task_description)+"\n**This is the logic of input part of the correct code:"
    else:
        content = ""
    content = content+"\n"+str(codeNetinput)
    content = content+"\n**This is the logic of input part of the generated code:"
    content = content+"\n"+str(geninput)
    content = content+"\n**Compare the difference in \"input\" between the correct code and the generated code, explain the functional differences.(If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\")In 200 words:"
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    input_token = num_tokens_from_string(content)
    input_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    output_token = num_tokens_from_string(input_diff.choices[0].message.content)
    if use_problem_statement:    
        content = "**task Description:"+str(task_description)+"\n**This is the logic of the correct code:"
    else:
        content = "**This is the logic of the correct code:"
    content = content+"\n"+str(codeNetlogic)
    content = content+"\n**This is the logic of the generated code:"
    content = content+"\n"+str(genlogic)
    #content = content+"\n**Weather the generated code complete the task, compare the difference in between the correct code and the generated code(may be logically incorrect). explain the functional differences(No need to compare inputs or outputs. If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\"):"
    content = content+"**Determine whether the generated code has completed the task by referring to the logic of the correct code(do not  compare other aspects such as readability, user experience.....)  Explain the difference in final effects, regardless of how they were achieved(No need to compare inputs or outputs between two codes. If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\"):"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    logic_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    input_token = input_token + num_tokens_from_string(content)
    output_token = output_token + num_tokens_from_string(logic_diff.choices[0].message.content)

    if use_problem_statement:
        content = "**task Description:"+str(task_description)+"**This is the logic of output part of the correct code:"
    else:
        content = "**This is the logic of output part of the correct code:"
    content = content+"\n"+str(codeNetoutput)
    content = content+"\n**This is the logic of output part of the generated code:"
    content = content+"\n"+str(genoutput)
    content = content+"\n**Compare the logic difference in \"output\" between the correct code and the generated code, explain the functional differences(if there have difference). If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\")"
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    output_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    input_token = input_token + num_tokens_from_string(content)
    output_token = output_token + num_tokens_from_string(output_diff.choices[0].message.content)
    return input_token,output_token,input_diff.choices[0].message.content,logic_diff.choices[0].message.content,output_diff.choices[0].message.content
                
    

def return_code_point(code_compare,corr_code,gen_code,problem_description):
    Criteria="""
    Evaluation Criteria
    0: Functionality cannot be achieved - The generated code is completely irrelevant to the task description.
    1: Logic Error - The generated code is relevant to the task description, but has serious logic problems.
    2: Partial logic functionality realized - Generated code may be able to perform some of the functionality, but does not cover all functional situations or has incomplete inputs and outputs.
    3: Functionality is realized but are insufficient. Implementation is less efficient than correct code, with higher time and space complexity.
    4: Functionality is fully implemented - the generated code has the same functionality and logic as the correct code, and has the same execution efficiency, with complete inputs and outputs.
    """
    #content = "**Correct code:\n"+str(corr_code)+"\n**Generated code:\n"+str(gen_code)+"\n"
    content = "**Problem description:\n"+str(problem_description)
    #You don't have to analyze the code any further,
    content = content+"**This is the difference between the correct code and the generated code given by experts ( just score the differences according to the Problem description and Evaluation Criteria):\n"+str(code_compare)+"\n"+str(Criteria)
    if gpt_model == "gpt-3.5":
        content = content+"\n**Please give the generated code a score based on the above criteria and explain why:**"
    else:
        content = content+"**Please give the generated code a score based on the above criteria and expert explaination(If experts believe that the logic is the same, then the generated code is logically and efficiently the same as the correct code, and there is no need to use the specific code for further analysis.)In 200 words:"
    input_token = num_tokens_from_string(content)
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    print(content)
    chat_completion = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=0)
    output_token = num_tokens_from_string(chat_completion.choices[0].message.content)
    return input_token,output_token,chat_completion.choices[0].message.content


def get_task_summary(task):
    content = "**task description:\n"+str(task)+"**Do not generate any code, just generate a brief overview of the above task for me(less than 200 words.Unless necessary, try not to exceed):"
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    chat_completion = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=0)
    return chat_completion.choices[0].message.content

# 、
def init_model_and_tokenizer():
    torch.cuda.empty_cache()
    model_name = "mistralai/Mistral-7B-Instruct-v0.2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # 
    model = AutoModelForCausalLM.from_pretrained(model_name, resume_download=True).half()
    
    if torch.cuda.device_count() > 1:
        model = torch.nn.DataParallel(model)
        print(f"Using {torch.cuda.device_count()} GPUs!")
    else:
        print("Using single GPU or CPU")
    
    model.to(torch.device("cuda"))
    return model, tokenizer
# 
def Mistral_7B_v2_prompt(prompt, model, tokenizer):
    messages = [
        {"role": "user", "content": prompt}
    ]
    logging.info("\Mistral_7B_v2 prompt:  \n" + messages[0]['content'])
    
    with autocast():  # 
        encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt").to(torch.device("cuda"))
        
        # 
        generated_ids = model.module.generate(encodeds, max_new_tokens=1000, do_sample=True) if hasattr(model, 'module') else model.generate(encodeds, max_new_tokens=1000, do_sample=True)
    
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    decoded[0]=decoded[0].split("[/INST]")[1]
    response = {"choices": [{"message": {"content": decoded[0]}}]}
    print(decoded[0])
    logging.info("\Mistral_7B_v2 response: \n" + response["choices"][0]["message"]["content"])

    return response, messages, 1
# 
def Mistral_7B_v2(messages, model, tokenizer):
    logging.info("\Mistral_7B_v2 prompt:  \n" + messages[0]['content'])
    
    with autocast():  # 
        encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt").to(torch.device("cuda"))
        
        # 
        generated_ids = model.module.generate(encodeds, max_new_tokens=1000, do_sample=True) if hasattr(model, 'module') else model.generate(encodeds, max_new_tokens=1000, do_sample=True)
    
    decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    decoded[0]=decoded[0].split("[/INST]")[1]
    response = {"choices": [{"message": {"content": decoded[0]}}]}
    print(decoded[0])
    logging.info("\Mistral_7B_v2 response: \n" + response["choices"][0]["message"]["content"])

    return response, messages, 1

def init_model_and_tokenizer_starling_LM_7B_beta():
    torch.cuda.empty_cache()
    tokenizer = transformers.AutoTokenizer.from_pretrained("Nexusflow/Starling-LM-7B-beta")
    model = transformers.AutoModelForCausalLM.from_pretrained("Nexusflow/Starling-LM-7B-beta", resume_download=True).half()
    primary_gpu = 'cuda:1'  # GPU 1
    
    if torch.cuda.is_available():
        # model.to(torch.device("cuda"))
        model.to(primary_gpu)
    if torch.cuda.device_count() > 1:
        # model = torch.nn.DataParallel(model)
        model = torch.nn.DataParallel(model,device_ids=[1,0])
        print(f"Using {torch.cuda.device_count()} GPUs!")
    else:
        print("Using single GPU or CPU")
    
    return model, tokenizer
# def init_model_and_tokenizer_starling_LM_7B_beta():
#     torch.cuda.empty_cache()
#     tokenizer = transformers.AutoTokenizer.from_pretrained("Nexusflow/Starling-LM-7B-beta")
#     model = transformers.AutoModelForCausalLM.from_pretrained("Nexusflow/Starling-LM-7B-beta", resume_download=True).half()
    
#     # GPU 1
#     device = torch.device("cuda:1") if torch.cuda.is_available() else torch.device("cpu")
#     model.to(device)

#     # GPU，DataParallel，
#     if torch.cuda.device_count() > 1:
#         model = torch.nn.DataParallel(model, device_ids=[1])  # GPU 1
#         print(f"Using {torch.cuda.device_count()} GPUs!")
#     else:
#         print("Using single GPU or CPU")
    
#     return model, tokenizer
def generate_response_starling_LM_7B_beta(prompt, model, tokenizer):
    # torch.cuda.empty_cache()
    logging.info(f"Starling-LM-7B-beta prompt:  \n{prompt}")
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # input_ids = input_ids.to(device)
    input_ids = input_ids.to('cuda:1')
    with autocast():  # 
        outputs = model.module.generate(
            input_ids,
            max_length=16384,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    response_ids = outputs[0]
    response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
    response_text=response_text.split("GPT4 Correct Assistant:")[-1]
    logging.info(f"Starling-LM-7B-beta response: \n{response_text}")
    return response_text

# def generate_response_starling_LM_7B_beta(prompt, model, tokenizer):
#     logging.info(f"Starling-LM-7B-beta prompt:  \n{prompt}")
#     # Set the device for the input tensors
#     device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")  # Assuming you want to use GPU 1
#     input_ids = tokenizer(prompt, return_tensors="pt").input_ids
#     input_ids = input_ids.to(device)
    
#     # Ensure model is on the same device as the input tensors
#     model = model.to(device)

#     # Use autocast for mixed precision
#     with autocast():
#         # If you are using DataParallel, you need to access the original model for `.generate`
#         if isinstance(model, torch.nn.DataParallel):
#             outputs = model.module.generate(
#                 input_ids,
#                 max_length=8192,
#                 pad_token_id=tokenizer.pad_token_id,
#                 eos_token_id=tokenizer.eos_token_id,
#             )
#         else:
#             outputs = model.generate(
#                 input_ids,
#                 max_length=8192,
#                 pad_token_id=tokenizer.pad_token_id,
#                 eos_token_id=tokenizer.eos_token_id,
#             )
    
#     response_ids = outputs[0]
#     response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
#     response_text = response_text.split("GPT4 Correct Assistant:")[-1]
#     logging.info(f"Starling-LM-7B-beta response: \n{response_text}")
#     return response_text
# model, tokenizer=init_model_and_tokenizer_starling_LM_7B_beta()

# prompt = "Hello, how are you?"
# single_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant:"
# response_text = generate_response_starling_LM_7B_beta(single_turn_prompt,model, tokenizer)
# print("Response:", response_text)

# ## Multi-turn conversation
# prompt = "Hello"
# follow_up_question =  "How are you today?"
# response = ""
# multi_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant: {response}<|end_of_turn|>GPT4 Correct User: {follow_up_question}<|end_of_turn|>GPT4 Correct Assistant:"
# response_text = generate_response(multi_turn_prompt)
# print("Multi-turn conversation response:", response_text)

# ### Coding conversation
# prompt = "Implement quicksort using C++"
# coding_prompt = f"Code User: {prompt}<|end_of_turn|>Code Assistant:"
# response = generate_response(coding_prompt)
# print("Coding conversation response:", response)
# import accelerate
from accelerate import infer_auto_device_map,init_empty_weights,load_checkpoint_in_model
from transformers import AutoConfig, AutoModelForCausalLM,AutoModel
from accelerate.utils import get_balanced_memory,get_max_memory
# from torch import get_balanced_memory
# def init_llam3_70b_4bit():
#     # model_id = "/home/user/.cache/.assets/models/meta-llama_meta-llama-3-8b-instruct"
#     # model_id="/home/user/.cache/.assets/models/mlx-community_meta-llama-3-70b-instruct-8bit"


#     model_path="/home/user/.cache/.assets/models/unsloth_llama-3-70b-instruct-bnb-4bit"


#     # 
#     config = AutoConfig.from_pretrained(model_path)

#     # 
#     with init_empty_weights():
#         model = AutoModelForCausalLM.from_config(config, torch_dtype=config.torch_dtype)
#     model.tie_weights()

#     # 
#     # model=AutoModel.from_pretrained(model_path,config=config, device='cpu')
#     model = AutoModelForCausalLM.from_pretrained(model_path, low_cpu_mem_usage=True, device_map="cpu")
#     tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True, legacy=False)
#     # load_checkpoint_in_model(model, model_path, device_map={"": "cpu"}, dtype=config.torch_dtype)
#     # 
#     no_split_module_classes = ["LlamaDecoderLayer"]

#     # 
#     max_memory = get_balanced_memory(
#         model,
#         max_memory=get_max_memory(max_memory=None),
#         no_split_module_classes=no_split_module_classes,
#         dtype=model.dtype,
#         low_zero=False,
#     )

#     # 
#     device_map = infer_auto_device_map(
#         model,
#         max_memory=max_memory,
#         no_split_module_classes=no_split_module_classes,
#         dtype=model.dtype
#     )
#     pipeline = transformers.pipeline(
#         "text-generation",
#         model=model,
#         tokenizer=tokenizer,
#         # model=model_id,
#         model_kwargs={"torch_dtype": torch.bfloat16},
#         # device_map="auto",
#         # device_map="cuda:1",
#         device_map=device_map,
#         # low_zero=True
#     )
#     return pipeline
def init_llam3_70b_4bit():
    # model_id = "/home/user/.cache/.assets/models/meta-llama_meta-llama-3-8b-instruct"
    # model_id="/home/user/.cache/.assets/models/mlx-community_meta-llama-3-70b-instruct-8bit"

    model_path = "/home/user/.cache/.assets/models/unsloth_llama-3-70b-instruct-bnb-4bit"

    device_map = {"model.embed_tokens": 0} | {f"model.layers.{i}": 0 for i in range(0, 41)} \
        | {f"model.layers.{i}": 1 for i in range(41, 80)} | {"model.norm": 1, "lm_head": 1}
# ,_attn_implementation="flash_attention_2"
    model = AutoModelForCausalLM.from_pretrained(model_path, low_cpu_mem_usage=True, device_map=device_map)
    tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True, legacy=False)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )
    return pipeline
def getanswer(messages,pipeline):
    logging.info(f"LLAM3-70B-4bit prompt:  \n{messages[1]['content']}")
    prompt = pipeline.tokenizer.apply_chat_template(
           messages, 
           tokenize=False, 
           max_length=1024*8,
           
           add_generation_prompt=True)
    
    terminators =[
     pipeline.tokenizer.eos_token_id,
       pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
       ]
    outputs = pipeline(
        prompt,
        # max_new_tokens=256,
        max_new_tokens=1024*8,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.2,
        top_p=1,
        )
    logging.info("LLAM3-70B-4bit response: "+outputs[0]["generated_text"][len(prompt):])
    return outputs[0]["generated_text"][len(prompt):]
