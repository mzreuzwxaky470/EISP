import requests
from bs4 import BeautifulSoup
import sys
import os
import json
sys.path.append('/home/user/cl/EISP')
import tiktoken
import re
def fetch_python_docs(url):
    """
    Fetch and print the text of all paragraphs from a given python documentation page.
    
    :param url: URL of the documentation page to fetch
    """

    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        

        for paragraph in soup.find_all('p'):
            print(paragraph.text)
    else:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")


def fetch_string_methods(url):
    """
    Fetch and print the names of all String methods from the given MDN documentation page.
    
    :param url: URL of the MDN JavaScript String reference page
    """

    res=[]
    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        

        method_list = soup.find_all('a')
        link_set=set()
        for link in method_list:

            link=link.get('href')

            flag=url.split("https://developer.mozilla.org")[1]

            if flag in link:
                link_set.add(link)
        # print(len(link_set))
        front_="https://developer.mozilla.org"
        for i in link_set:
            if '.txt'in i or (front_+i)==url:
                continue
            res.append(front_+i)
            # print(front_+i)

    else:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
    return res
def search_describe(url):
    describe_dict={}

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        method_list = soup.find(id='content')
        api_name=""
        api_describe=""
        if method_list:
            api_name=method_list.find('header').h1.text
            # content=method_list.find_all(class_="section-content")
            content = method_list.find('section', {'aria-labelledby': 'description'})

            
            if content:
                for con in content:
                    if con.text=='Description':
                        continue
                    api_describe+=con.text+' '
                print(api_name+'1')
                print(api_describe.strip())
                if api_describe.strip()=='':
                    content2=method_list.find('div', class_='section-content')
                    for con in content2:
                        api_describe+=con.text+' '
                    print(api_name)
                    print(api_describe)
                
            else:
                content2=method_list.find('div', class_='section-content')
                for con in content2:

                    api_describe+=con.text+' '
                print(api_name)
                print(api_describe)
        return api_name,api_describe
    else:
        print(f"Failed to retrieve content from {url}, status code: {response.status_code}")
        return 


if __name__ == "__main__":

    url1 = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/anchor'
    
    url2 = 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol'


