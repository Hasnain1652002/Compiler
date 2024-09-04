# -*- coding: utf-8 -*-
"""Language_Specification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B0Z5d7kDwHU5KIw4P-8egDbxJUUyIO-c
"""

import re

operators = ["+","-","*","/"]
conditional_operators = ["!=","==",">=","<=",">","<"]
data_type = ["int"]

patterns = {
    "declaration": r'^int\s+[_$a-zA-Z][_$a-zA-Z0-9]*\s*\=\s*[0-9]+\s*[-\+\/\*]*\s*[0-9]*',
    "condition": r'^if\s*\(\s*[_$a-zA-Z][_$a-zA-Z0-9]*\s*[<>!=]=?\s*[0-9]+\s*\)$',
    "loop": r'^LOOP\s*\(int\s+[_$a-zA-Z][_$a-zA-Z0-9]*\s*\=\s*[0-9]+\s*,\s*[_$a-zA-Z][_$a-zA-Z0-9]*\s*[<>!=]=?\s*[0-9]+\s*,\s*[_$a-zA-Z][_$a-zA-Z0-9]*[+\-]{2}\s*\)$'
}

def tokenize_variable(input):
  token = input.split("=")
  return token

def tokenize_loop(input):
  substring = re.search(r'\((.*?)\)', code).group(1)
  substrings = substring.split(',')
  token = [s.strip() for s in substrings]
  token.insert(0, 'LOOP')
  return(token)

def tokenize_condition(input):
  substring = re.search(r'\((.*?)\)', code).group(1)
  substrings = substring.split(',')
  token = [s.strip() for s in substrings]
  token.insert(0, 'if')
  return(token)

def tokenize_string(input_string):
    # Use regex to find variable name followed by comparison operator with optional whitespace
    match = re.match( r'([_$a-zA-Z][_$a-zA-Z0-9]*)\s*([<>!=]=?)\s*', input_string)
    if match:
        variable = match.group(1)
        operator = match.group(2)
        return [variable, operator]
    else:
        return None  # No match found

def tokenize_string_2(input_string):
    # Use regex to find variable name followed by comparison operator with optional whitespace
    match = re.match(r'([_$a-zA-Z][_$a-zA-Z0-9]*)\s*([+\-*/]{2})\s*', input_string)
    if match:
        variable = match.group(1)
        operator = match.group(2)
        return [variable, operator]
    else:
        return None  # No match found

def check_variable(tokenize_variable,code):
  identifier= tokenize_variable(code)
  output = identifier[0].split(" ")
  dt = output[0]
  variable = output[1]
  print(f'{dt} {variable}')
  print(f"Token part :{dt} , Class Part: 'Data Type'")
  print(f"Token part :{variable} , Class Part: 'Identifier'")
  print("----------------------------------------------")



def check_statement(tokenize_variable,code):
  statement = tokenize_variable(code)
  lst=list(statement[1])
  for i in lst:
    if i in operators:
      print(f"Data Type : {i} , Class Part: {i}")

def check_loop(tokenize_loop,code):
  loop = tokenize_loop(code)
  for i in loop:
    if i == "LOOP":
      print(i)
      print(f'Token Part:"for" , Class Part:"LOOP"')
      print("----------------------------------------------")
    if re.match(r'^int\s+[_$a-zA-Z][_$a-zA-Z0-9]*\s*\=\s*[0-9]+\s*[-\+\/\*]*\s*[0-9]*',i):
      print(i)
      check_variable(tokenize_variable,i)
      check_statement(tokenize_variable,i)
      print("----------------------------------------------")
    if re.match( r'([_$a-zA-Z][_$a-zA-Z0-9]*)\s*([<>!=]=?)\s*',i):
      variable ,operator =tokenize_string(i)
      print(i)
      print(f'Token Part:{variable} , Class Part:"Identifier"')
      print(f'Token Part:{operator} , Class Part:{operator}')
      print("----------------------------------------------")
    if re.match(r'([_$a-zA-Z][_$a-zA-Z0-9]*)\s*([+\-*/]{2})\s*',i):
      variable, operator = tokenize_string_2(i)
      print(i)
      print(f'Token Part:{variable} , Class Part:"Identifier"')
      print(f'Token Part:{operator} , Class Part:{operator}')
      print("----------------------------------------------")

def check_condition(tokenize_condition,code):
  condition = tokenize_condition(code)
  for i in condition:
    if i == "if":
      print(i)
      print(f'Token Part:"if" , Class Part:"if"')
      print("----------------------------------------------")
    if re.match( r'([_$a-zA-Z][_$a-zA-Z0-9]*)\s*([<>!=]=?)\s*',i):
      variable ,operator =tokenize_string(i)
      print(i)
      print(f'Token Part:{variable} , Class Part:"Identifier"')
      print(f'Token Part:{operator} , Class Part:{operator}')
      print("----------------------------------------------")

code = input("Enter your Statement : ")

def analyzer(patterns,code):
  for key, pattern in patterns.items():
    regex = re.compile(pattern)
    if regex.match(code):
        if key == "declaration":
          check_variable(tokenize_variable,code)
          check_statement(tokenize_variable,code)
          print("--------------------------------------------------------------")
        if key == "condition":
          check_condition(tokenize_condition,code)
          print("--------------------------------------------------------------")
        if key == "loop":
          check_loop(tokenize_loop,code)
          print("--------------------------------------------------------------")

analyzer(patterns,code)
