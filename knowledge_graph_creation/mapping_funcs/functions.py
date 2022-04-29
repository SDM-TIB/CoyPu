import re
import csv
import sys
import os
import pandas as pd
from pathlib import Path
import requests
import json

global global_dic
global_dic = {}
global functions_pool
global exactMatchDic
exactMatchDic = dict()

#####################################################################################################
########### ADD THE IMPLEMENTATION OF YOUR FUNCTIONS HERE FOLLOWING THE EXAMPLES ####################
#####################################################################################################

## For each new function that you define, add an entry as "function_name":"" to the dictionary below 
functions_pool = {"reverseString":"", "toLower":"", "replaceExactMatch":"", "falcon_UMLS_CUI_function":"", "chomp": "",
    "concat2": "", "falcon_entity_function": "", "controls_if":"", "equal":"",
    "string_replace":""}


### Non-injective, surjective
def controls_if():
    # bool_b
    # grel:param_b grel:param_true grel:param_false
    try:
        if global_dic['bool_b']:
            return global_dic['any_true']
        return global_dic['any_false']
    except:
        if 'any_false' in global_dic:
            return global_dic['any_false']
        return global_dic['any_true']

def equal():
    # valueParameter, valueParameter2, any_false
    if (global_dic["valueParameter"]==global_dic["valueParameter2"]):
        return True
    return False
        

def string_replace():
    # valueParameter, p_string_find, p_string_replace
    try:
        return str(global_dic["valueParameter"]).replace(global_dic["p_string_find"], global_dic["p_string_replace"])
    except:
        return str(global_dic["valueParameter"])

def chomp():
    try:
        return global_dic["value"].replace(global_dic["toremove"], "")
    except:
        return global_dic["value"]
    
def concat2():
    value1 = global_dic["value1"]
    value2 = global_dic["value2"]
    try :
        if bool(value1) and bool(value2):
            result = str(str(value1) + str(value2))
        else:
            result = ""
        return result
    except:
        return ""


headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}


def falcon_entity_function():
    value = global_dic["value"]
    url = "https://labs.tib.eu/falcon/falcon2/api?mode=short"
    # url = "https://labs.tib.eu/falcon/falcon2/api?mode=long"
    # headers = {"content-type": "application/json", "Accept-Charset": "UTF-8"}
    payload = '{"text":"' + value + '"}'
    r = requests.post(url, data=payload.encode("utf-8"), headers=headers)
    try:
        if r.status_code == 200:
            response = r.json()
            print(response)
            return "<http://www.wikidata.org/entity/{}>".format(
                response["entities"][0][0]
            )
            # return response["entities_wikidata"][0][1]
    except Exception as e:
        print("Error: ", e)

    return ""

### Non-injective, surjective 
def toLower(): 
    return global_dic["value"].lower()

### Bijective
def dictionaryCreation():
    directory = Path(os.path.abspath(os.path.join(os.getcwd(), os.path.dirname(__file__)))).parent.absolute()
    with open(str(directory)+"/Sources/label_cui_dictionary.csv",'r') as data:
        for row in csv.DictReader(data):
            exactMatchDic.update({row['SampleOriginLabel']:row['CUI']}) 
dictionaryCreation()

def replaceExactMatch():    
    value = global_dic["value"]                   
    if value != "":
        replacedValue = exactMatchDic[value]
    else:
        replacedValue = "" 
    return(replacedValue)

def reverseString():    
    value = str(global_dic["value"])
    if value != "":
        output = value[::-1]
    else:
        output = ""
    return(output) 


### non-injective, non-surjective
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
def falcon_UMLS_CUI_function():
    value = global_dic["value"]
    output = ""
    url = 'https://labs.tib.eu/sdm/biofalcon/api?mode=short'
    text = str(value).replace("_"," ")
    payload = '{"text":"'+text+'"}'
    r = requests.post(url, data=payload.encode('utf-8'), headers=headers)
    if r.status_code == 200:
        response=r.json()
        if len(response['entities'][1])>0:
            return response['entities'][1][0]
        else:
            return ""
    else:
        return ""


################################################################################################
############################ Static (Do NOT change this code) ##################################
################################################################################################

def execute_function(row,header,dic):
    if "#" in dic["function"]:
        func = dic["function"].split("#")[1]
    else:
        func = dic["function"].split("/")[len(dic["function"].split("/"))-1]
    if func in functions_pool:
        global global_dic
        global_dic = execution_dic(row,header,dic)
        return eval(func + "()")             
    else:
        print("Invalid function")
        print("Aborting...")
        sys.exit(1)

def execution_dic(row,header,dic):
    output = {}
    for inputs in dic["inputs"]:
        if "constant" not in inputs: 
            if isinstance(row,dict):
                output[inputs[2]] = row[inputs[0]]
            else:
                output[inputs[2]] = row[header.index(inputs[0])]
        else:
            output[inputs[2]] = inputs[0]
    return output