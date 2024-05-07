import openai
import time
from code_spilt import code_strip_spaces
import re
import tiktoken

api_key = ''
temp = 0.2
max_tok = 300
gpt_model = "gpt-3.5-turbo"
is_summary  = False



# OpenAI
openai.api_key = api_key


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def get_api_response(prompt,max_tokens = max_tok,n = 1,temperature = temp):
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": prompt}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = max_tok,
                                    n=1,
                                    temperature=temp)
    return chat_completion.choices[0].message.content


def return_snippet_explain(code):
    code_content = "code:\n"+str(code)+"\nexplain the above code logic:\n"
    return get_api_response(code_content)
    

#，
def return_input_assign_explain(code,problem_statement,use_problem_statement):
    if use_problem_statement:
        code_content = "[Task description:]\n"+str(problem_statement)+"\n[code:]\n"+str(code)+"\n[explain the above code logic:]\n"
    else:
        code_content = "code:\n"+str(code)+"\nexplain the above code logic:\n"

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code. Output nothing but understand the logic of the input variables"},
                 {"role":"user", "content": code_content},{"role":"user", "content": "Summarize the above variable logic: The variable"}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 100,
                                    n=1,
                                    temperature=temp)


    return chat_completion.choices[0].message.content


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

def return_assign_explain(code,varlist,classdict,funcdict):
    if classdict == {}:
        return ""
    for v in varlist:
        if v in classdict:
            code = code+"\n"+"The logic of class"+str(v)+" is "+str(classdict[v])+"\n"
        if v in funcdict:
            code = code+"\n"+"The logic of function"+str(v)+" is "+str(funcdict[v])+"\n"
    code_content = "code:\n"+str(code)+"\nexplain the above code logic:\n"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code. Output nothing but understand the logic of the input variables"},
                    {"role":"user", "content": code_content},{"role":"user", "content": "Summarize the above variable logic: The variable"}]

    chat_completion = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 100,
                                    n=1,
                                    temperature=temp)

    return chat_completion.choices[0].message.content
def return_snippet_explain2(code,varlist,vardict,codedict,fundict):
    
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
    

def return_snippet_explain3(code,dependencies,codeStructure):
    varlist = dependencies
    vardict = codeStructure.get_snippet_logic()
    codedict = codeStructure.get_assign_code()
    fundict = codeStructure.get_function_logic()
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
    code_content = code_content+"\nexplain the above code logic(If it contains an output or input(print\input), explain them):"


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

#、，
def update_snippet_logic(background,snippet,code_snippet,origin_logic):

    code_content = "Code snippet:\n"+str(code_snippet)+"\nCode snippet logic explain: \n"+str(background)+"\n"+"\nThe origin logic of \""+str(snippet)+"\":"+str(origin_logic)+"\nExplain the meaning of "+str(snippet)+" is from the above code snippet(If snippet's logic is not provided in the given code snippet, output the origin logic):"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and code's background, I'll Extract the part of the background information about the code snippet (no further explanation is needed)."},
                 {"role":"user", "content": code_content}]
    answer = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=temp)

    return answer.choices[0].message.content

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
def return_func_explain(func):
    code_content = "Code function snippets:\n"+str(func)+"\nExplain the logical function of the above code function(If it contains an output(print), explain it together):\n"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 400,
                                    n=1,
                                    temperature=temp)

    return chat_completion.choices[0].message.content




#“”“”，“”
def return_output_explain(code,dependencies_list,snippet_list,func_dict):
    #

    code_content = "The program output is:\n"+str(code)+"\nExplain what the output of the program is:\n"
    
    #
    for var in dependencies_list:
        if var in snippet_list:
            code_content = code_content+str(snippet_list[var])+"\n"
    #
    for var in dependencies_list:
        if var in func_dict:
            code_content = code_content+"\nThe function of "+str(var)+" is: "+str(func_dict[var])+"\n"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and variable logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=temp)

    return chat_completion.choices[0].message.content

#、，
def return_overall_explain(code,code_structure,structure_code_dict,structure_logic_dict):
    code_content = "code:\n"+str(code)+"\n"
    for s in code_structure:
        code_con = "code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
        code_content = code_content+code_con
    code_content = code_content+"\nExplain the logic of the above code in three part separately:Code Input: XXX\\n Code Logic: XXX\\n Code Output: XXX\\n(If the code has no inputs or outputs then point out there is no input or output):\n"

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
    code_content = "code:\n"+str(code)+"\n"
    for s in code_structure:
        code_con = "code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
        code_content = code_content+code_con
    code_content1 = code_content+"\nExplain the input part of the above code:Code Input(If the code has no inputs then point out there is no input):\n"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content1}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    input_logic = chat_completion.choices[0].message.content


    code_content1 = code_content+"\nExplain the logic part of the above code:Code Logic(Do not explain the input and output of the code):\n"

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                    {"role":"user", "content": code_content1}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    logic_logic = chat_completion.choices[0].message.content


    code_content1 = code_content+"\nExplain the output part of the above code:Code Output(If the code has no outputs then point out there is no output):\n"

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                    {"role":"user", "content": code_content1}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)
    output_logic = chat_completion.choices[0].message.content
 

    
    return input_logic,logic_logic,output_logic


#“”，、、
def return_snippet_overall_explain(code,code_structure,structure_code_dict,structure_logic_dict):
    code_content = "code:\n"+str(code)+"\n"
    for s in code_structure:
        code_con = "code snippet:\n"+str(structure_code_dict[s])+"\nlogic explain:\n"+str(structure_logic_dict[s])+"\n"+"----------"
        code_content = code_content+code_con
    code_content = code_content+"\nBriely explain the logic of the above code(Explain only the general logical function, not the sentence-by-sentence explanation):\n"

    
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant, given a code snippet and logic, I'll provide a logical explanation of the code."},
                 {"role":"user", "content": code_content}]
    chat_completion = openai.ChatCompletion.create(model=gpt_model, 
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)


    return chat_completion.choices[0].message.content


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
                
def return_logic_different3(codeNetinput,codeNetlogic,codeNetoutput,geninput,genlogic,genoutput,task_description,use_problem_statemen):

    content = "**task Description:"+str(task_description)+"\n**This is the logic of input part of the correct code:"
    content = content+"\n"+str(codeNetinput)
    content = content+"\n**This is the logic of input part of the generated code:"
    content = content+"\n"+str(geninput)
    content = content+"\n**Compare the difference in \"input\" between the correct code and the generated code, explain the functional differences.(If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\"):"
    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]

    input_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)

    content = "**task Description:"+str(task_description)+"\n**This is the logic of the correct code:"
    content = content+"\n"+str(codeNetlogic)
    content = content+"\n**This is the logic of the generated code:"
    content = content+"\n"+str(genlogic)
    #content = content+"\n**Weather the generated code complete the task, compare the difference in between the correct code and the generated code(may be logically incorrect). explain the functional differences(No need to compare inputs or outputs. If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\"):"
    content = content+"**Determine whether the generated code has completed the task by referring to the logic of the correct code(do not  compare other aspects such as readability, user experience.....)  explain the effect differences(No need to compare inputs or outputs between two codes. If the same effect is achieved, then output:\"The function of the input part of the two codes is the same\"):"


    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    logic_diff = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 800,
                                    n=1,
                                    temperature=0)

    content = "**task Description:"+str(task_description)+"**This is the logic of output part of the correct code:"
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

    return input_diff.choices[0].message.content,logic_diff.choices[0].message.content,output_diff.choices[0].message.content
                
    

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
    content = content+"**This is the difference between the correct code and the generated code given by experts ( just score the differences according to the Problem description and Evaluation Criteria):\n"+str(code_compare)+"\n"+str(Criteria)+"\n**Please give the generated code a score based on the above criteria and explain why:**"

    messages_list = [{"role":"system", "content": "I'm a code analysis assistant"},
                    {"role":"user", "content": content}]
    
    chat_completion = openai.ChatCompletion.create(model=gpt_model,
                                    messages=messages_list,
                                    max_tokens = 200,
                                    n=1,
                                    temperature=0)
    return chat_completion.choices[0].message.content


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




    






