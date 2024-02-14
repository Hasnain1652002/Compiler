from Lexical_Analyzer import tokens

I = 0

def Syntax_Analyzer(Tokens):
    global I
    if start(Tokens):
        print("Valid Syntax")
    else:
        print("Syntax Error at Line Number", Tokens['LINE NO.'][I])

## start
def start(Tks):
    global I 
    if Tks['CLASS NAME'][I] in ['#']:
        return True
    elif Tks['CLASS NAME'][I] in ['from', 'import']:
        if import_st(Tks):
            if start(Tks):
                return True
    elif Tks['CLASS NAME'][I] in ['if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '#', 'int' ,'str','char', 'float']:
        if sst(Tks):
            if start(Tks):
                return True
    elif Tks['CLASS NAME'][I] in [ 'public', 'private', '#','abstract','static','sealed','class']:
        if class_def(Tks):
            if start(Tks):
                return True
    
    else:
        return False
    
## import st
def import_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['from', 'import']:
        if from_st(Tks):
            if Tks['CLASS NAME'][I] == 'import':
                I += 1
                if im_id(Tks):
                    if as_st(Tks):
                        if Tks['CLASS NAME'][I] == ';':
                            I += 1
                            return True
    else:
        return False


def from_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['from']:
        if Tks['CLASS NAME'][I] == 'from':
            I += 1
            if from_id(Tks):
                return True
    elif Tks['CLASS NAME'][I] in ['import']:
        return True  # Epsilon production
    else:
        return False

def from_id(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            if from_id_prime(Tks):
                return True
    else:
        return False

def from_id_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['.']:
        if Tks['CLASS NAME'][I] == '.':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if from_id_prime(Tks):
                    return True
    elif Tks['CLASS NAME'][I] in ['import']:
        return True   # Epsilon production
    else:
        return False

def im_id(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            if im_id_prime(Tks):
                return True
    else:
        return False

def im_id_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['.']:
        if Tks['CLASS NAME'][I] == '.':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if im_id_prime(Tks):
                    return True
    elif Tks['CLASS NAME'][I] in ['as',';']:
        return True   # Epsilon production
    else:
        return False

def as_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['as']:
        if Tks['CLASS NAME'][I] == 'as':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                return True
    elif Tks['CLASS NAME'][I] in [';']:
        return True  # Epsilon production
    else:
        return False

## single line st
def sst(Tks):
    global I
    
    if Tks['CLASS NAME'][I] in ['if']:
        if if_else(Tks):
            return True
    elif Tks['CLASS NAME'][I] in ['for', 'while']:
        if loops(Tks):
            return True 
    elif Tks['CLASS NAME'][I] in ['try']:
        if try_st(Tks):
            return True 
    elif Tks['CLASS NAME'][I] in ['id']:
        I += 1
        if Tks['CLASS NAME'][I] in ['id']:
            I -= 1
            if dec(Tks):
                return True
        elif Tks['CLASS NAME'][I] in ['.','[','(','AO']:  
            I -= 1
            if assign_st(Tks):
                if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True
    elif Tks['CLASS NAME'][I] in [ 'return']:
        if ret(Tks):
            if Tks['CLASS NAME'][I] == ';':
                I += 1
                return True
    elif Tks['CLASS NAME'][I] in ['def']:
        if fn_def(Tks):
            return True
    # elif Tks['CLASS NAME'][I] in ['id']:
    #     if ref(Tks):
    #         if Tks['CLASS NAME'][I] == ';':
    #             I += 1
    #             return True
    elif Tks['CLASS NAME'][I] in ['pass']:
        if Tks['CLASS NAME'][I] == 'pass':
            I += 1
            if Tks['CLASS NAME'][I] == ';':
                I += 1
                return True
    elif Tks['CLASS NAME'][I] in ['continue']:
        if Tks['CLASS NAME'][I] == 'continue':
            I += 1
            if Tks['CLASS NAME'][I] == ';':
                I += 1
                return True
    elif Tks['CLASS NAME'][I] in ['break']:
        if Tks['CLASS NAME'][I] == 'break':
            I += 1
            if Tks['CLASS NAME'][I] == ';':
                I += 1
                return True
    
    elif Tks['CLASS NAME'][I] in ['int' ,'str','char', 'float']:
        if dec(Tks):
            return True  
        

    return False

## if else
def if_else(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['if']:
        if Tks['CLASS NAME'][I] == 'if':
            I += 1
            if Tks['CLASS NAME'][I] == '(':
                I += 1
                if exp(Tks):
                    if Tks['CLASS NAME'][I] == ')':
                        I += 1
                        if if_body(Tks):
                            return True

    return False

def if_body(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['{']:
        if Tks['CLASS NAME'][I] == '{':
            I += 1
            if mst(Tks):
                if Tks['CLASS NAME'][I] == '}':
                    I += 1
                    if else_nt(Tks):
                        return True

    return False

def mst(Tks):
    global I

    if Tks['CLASS NAME'][I] in  ['if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '#', 'int' ,'str','char', 'float']:
        if sst(Tks):
            if mst(Tks):
                return True
    elif Tks['CLASS NAME'][I] in [ '}' ]:
        return True  # Epsilon production
    return False

def else_nt(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['else']:
        if Tks['CLASS NAME'][I] == 'else':
            I += 1
            if body(Tks):
                return True
    elif Tks['CLASS NAME'][I] in ['if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '{', '}', 'except', '#', 'int' ,'str','char', 'float']:
        return True    # Epsilon production
    return False

def body(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['{']:
        if Tks['CLASS NAME'][I] == '{':
            I += 1
            if mst(Tks):
                if Tks['CLASS NAME'][I] == '}':
                    I += 1
                    return True

    return False

## loops
def loops(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['for']:
        if for_st(Tks):
            return True
    elif Tks['CLASS NAME'][I] in ['while']:
        if while_st(Tks):
            return True
        
    return False

def for_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['for']:
        if Tks['CLASS NAME'][I] == 'for':
            I += 1
            if loop_prime(Tks):
                return True

    return False

def while_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['while']:
        if Tks['CLASS NAME'][I] == 'while':
            I += 1
            if loop_prime(Tks):
                return True

    return False

def loop_prime(Tks):
    global I
    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if exp(Tks):
            if body(Tks):
                return True

    return False

## constant
def const(Tks):
    global I
    

    if Tks['CLASS NAME'][I] in ['int_const']:
        if Tks['CLASS NAME'][I]=='int_const':  
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['bool_const']:
        if Tks['CLASS NAME'][I]=='bool_const':  
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['float_const']:
        if Tks['CLASS NAME'][I]=='float_const':  
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['char_const']:
        if Tks['CLASS NAME'][I]=='char_const':  
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['string_const']:
        if Tks['CLASS NAME'][I]=='string_const':  
            I += 1
            return True
    return False

## function def
def fn_def(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['def']:
        if Tks['CLASS NAME'][I] == 'def':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if Tks['CLASS NAME'][I] == '(':
                    I += 1
                    if fn_def_prime(Tks):
                        if Tks['CLASS NAME'][I] == ')':
                            I += 1
                            if Tks['VALUE'][I] == '-':
                                I += 1
                                if Tks['VALUE'][I] == '>':
                                    I += 1
                                    if ret_type(Tks):
                                        if body(Tks):
                                            return True

    return False


def fn_def_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int', 'str', 'char', 'float','id']:
        if dt(Tks):
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if fn_def_double_prime(Tks):
                    return True
    elif Tks['CLASS NAME'][I] in [')']:
        return True  # Epsilon production

    return False


def fn_def_double_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in [',']:
        if Tks['CLASS NAME'][I] == ',':
            I += 1
            if dt(Tks):
                if Tks['CLASS NAME'][I] == 'id':
                    I += 1
                    if fn_def_double_prime(Tks):
                        return True
    elif Tks['CLASS NAME'][I] in [')']:
        return True  # Epsilon production

    return False

def ret_type(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int', 'str', 'char', 'float', 'None', 'list', 'dict', 'id']:
        if type_(Tks):
            return True
    return False

def type_(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int', 'str', 'char', 'float']:
        if dt(Tks):
            return True
    
    elif Tks['CLASS NAME'][I] in ['None']:
        if Tks['CLASS NAME'][I] == 'None':
            I += 1
            return True
      
    elif Tks['CLASS NAME'][I] in ['List' , 'dict']: 
        if type_prime(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            return True

    return False

def type_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in [ 'list' ]:
        if Tks['CLASS NAME'][I] == 'list':
            I += 1
            if Tks['CLASS NAME'][I] == '[':
                I += 1
                if type_double_prime(Tks):
                    if Tks['CLASS NAME'][I] == ']':
                        I += 1
                        return True

    elif Tks['CLASS NAME'][I] in ['dict']:
        if Tks['CLASS NAME'][I] == 'dict':
            I += 1
            if Tks['CLASS NAME'][I] == '[':
                I += 1
                if type_double_prime(Tks):
                    if Tks['CLASS NAME'][I] == ']':
                        I += 1
                        return True

    return False
def type_double_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int','str','char','float','none','list','dict','id']:
        if type(Tks):
            if mul_type(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            if mul_type(Tks):
                return True

    return False


def dt(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int']:
        if Tks['CLASS NAME'][I] == 'int':
            I += 1
        return True
    elif Tks['CLASS NAME'][I] in ['str']:
        if Tks['CLASS NAME'][I] == 'str':
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['char']:
        if Tks['CLASS NAME'][I] == 'char':
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['float']:
        if Tks['CLASS NAME'][I] == 'float':
            I += 1
            return True
    return False



def mul_type(Tks):
    global I

    if Tks['CLASS NAME'][I] in [',']:
        if Tks['CLASS NAME'][I] == ',':
            I += 1
            if type_double_prime(Tks):
                if Tks['CLASS NAME'][I] == []:
                    if mul_type(Tks):
                        return True

    elif Tks['CLASS NAME'][I] in [']']:
        return True  # Epsilon production

    return False

## return
def ret(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['return']:
        if Tks['CLASS NAME'][I] == 'return':
            I += 1
            if ret_prime(Tks):
                return True

    elif Tks['CLASS NAME'][I] in  ['if', 'for', 'while', 'try', 'pass', 'id', 'continue', 'break', 'return', 'def', '}']:
        return True  # Epsilon production

    return False


def ret_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['(']:
        if Tks['CLASS NAME'][I] == '(':
            I += 1
            if para(Tks):
                if Tks['CLASS NAME'][I] == ')':
                    I += 1
                    return True

    elif Tks['CLASS NAME'][I] in ['not', '(', 'id', 'int_const','float_const','string_const','char_const', 'bool_const', ';']:
        if para(Tks):
            return True

    return False


## try except
def try_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['try']:
        if Tks['CLASS NAME'][I] == 'try':
            I += 1
            if body(Tks):
                if except_st(Tks):
                    if finally_st(Tks):
                        return True

    return False


def except_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['except']:
        if Tks['CLASS NAME'][I] == 'except':
            I += 1
            if except_prime(Tks):
                if Tks['CLASS NAME'][I] == '{':
                    if body(Tks):
                        if except_double_prime(Tks):
                            return True

    return False

def except_double_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['except']:
        if except_st(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['else']:
        if else_st(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['finally', '#']:
        return True  # Epsilon production

    return False


def except_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            if as_(Tks):
                return True

    return False

def as_(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['as']:
        if Tks['CLASS NAME'][I] == 'as':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                return True

    elif Tks['CLASS NAME'][I] in ['{']:
        return True  # Epsilon production

    return False


def finally_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['finally']:
        if Tks['CLASS NAME'][I] == 'finally':
            I += 1
            if body(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['#']:
        return True  # Epsilon production

    return False

def else_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['else']:
        if Tks['CLASS NAME'][I] == 'else':
            I += 1
            if body(Tks):
                return True

    return False


## self and super
def ss(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['self']:
        if Tks['CLASS NAME'][I] == 'self':
            I += 1
            if Tks['CLASS NAME'][I] == '.':
                I += 1
                return True

    elif Tks['CLASS NAME'][I] in ['super']:
        if Tks['CLASS NAME'][I] == 'super':
            I += 1
            if Tks['CLASS NAME'][I] == '(':
                I += 1
                if Tks['CLASS NAME'][I] == ')':
                    I += 1
                    if Tks['CLASS NAME'][I] == '.':
                        I += 1
                        return True

    elif Tks['CLASS NAME'][I] in ['id']:
        return True  # Epsilon production

    return False


## assignment st
def assign_st(Tks):
    global I
    if Tks['CLASS NAME'][I] == 'id':
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            if a2(Tks):
                if assign(Tks):
                    return True
    else:
        return False


def a2(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['.']:
        if Tks['CLASS NAME'][I] == '.':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if a2(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['[']:
        if Tks['CLASS NAME'][I] == '[':
            I += 1
            if exp(Tks):
                if Tks['CLASS NAME'][I] == ']':
                    I += 1
                    if a2(Tks):
                        return True

    elif Tks['CLASS NAME'][I] in ['(']:
        if Tks['CLASS NAME'][I] == '(':
            I += 1
            if para(Tks):
                if Tks['CLASS NAME'][I] == ')':
                    I += 1
                    if a3(Tks):
                        return True

    elif Tks['CLASS NAME'][I] in ['AO',';',')',',',']','RO','MO','IO','{']:
        return True  # Epsilon production

    return False


def a3(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['.']:
        if Tks['CLASS NAME'][I] == '.':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if a2(Tks):
                    return True

    elif Tks['CLASS NAME'][I] == ['[']:
        if Tks['CLASS NAME'][I] == '[':
            I += 1
            if exp(Tks):
                if Tks['CLASS NAME'][I] == ']':
                    I += 1
                    if a2(Tks):
                        return True

    
    elif Tks['CLASS NAME'][I] in ['AO', ';']:
        return True  # Epsilon production

    return False


def assign(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['AO']:
        I -= 1
        if Tks['CLASS NAME'][I] != ')':
            I += 1
            if Tks['CLASS NAME'][I] == 'AO':
                I += 1
                if assign_prime(Tks):
                    return True
    elif Tks['CLASS NAME'][I] in [';',')',',',']','RO','MO','IO','{']:
        return True

    return False

def assign_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['and', 'DM', 'not', 'string_const', '(', 'PM', 'char_const', 'IO', 'id', 'RO', 'or', 'E', 'bool_const', 'MO', 'float_const', 'int_const', 'DM', ')', ';', '#']:

        if exp(Tks):
            return True
    elif Tks['CLASS NAME'][I] in ['[', '{']:
        if arr_dict(Tks):
            return True


def arr_dict(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['[']:
        if arr(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['{']:
        if Tks['CLASS NAME'][I] == '{':
            I += 1
            if dict(Tks):
                if Tks['CLASS NAME'][I] == '}':
                    I += 1
                    return True

    return False


def arr(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['[']:
        if Tks['CLASS NAME'][I] == '[':
            I += 1
            if para(Tks):
                if arr(Tks):
                    if Tks['CLASS NAME'][I] == ']':
                        I += 1
                        if mul_arr(Tks):
                            return True
    elif Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if para(Tks):
            return True

    elif Tks['CLASS NAME'][I] in [']',',']:
            return True  # Epsilon production

    return False


def mul_arr(Tks):
    global I

    if Tks['CLASS NAME'][I] in [',']:
        if Tks['CLASS NAME'][I] == ',':
            I += 1
            if arr(Tks):
                if mul_arr(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in [']',';']:
            return True  # Epsilon production

    return False

def dict_st(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int_const', 'float_const', 'string_const', 'char_const', 'bool_const']:
        if const(Tks):
            if Tks['CLASS NAME'][I] == ':':
                I += 1
                if exp(Tks):
                    if mul_dict(Tks):
                        return True

    return False


def mul_dict(Tks):
    global I

    if Tks['CLASS NAME'][I] in [',']:
        if Tks['CLASS NAME'][I] == ',':
            I += 1
            if dict_st(Tks):
                if mul_dict(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['}']:
        return True  # Epsilon production

    return False


# ## refernce
# def ref(Tks):
#     global I

#     if Tks['CLASS NAME'][I] in ['id']:
#         if Tks['CLASS NAME'][I] == 'id':
#                 I += 1
#                 if ref_prime(Tks):
#                     return True

#     return False


# def ref_prime(Tks):
#     global I

#     if Tks['CLASS NAME'][I] in ['.']:
#         if Tks['CLASS NAME'][I] == '.':
#             I += 1
#             if Tks['CLASS NAME'][I] == 'id':
#                 I += 1
#                 if ref_prime(Tks):
#                     return True
#     elif Tks['CLASS NAME'][I] in ['[']:
#         if Tks['CLASS NAME'][I] == '[':
#             I += 1
#             if exp(Tks):
#                 if Tks['CLASS NAME'][I] == ']':
#                     I += 1
#                     if ref_prime(Tks):
#                         return True
#     elif Tks['CLASS NAME'][I] in ['(']:
#         if Tks['CLASS NAME'][I] == '(':
#             I += 1
#             if para(Tks):
#                 if Tks['CLASS NAME'][I] == ')':
#                     I += 1
#                     if ref_double_prime(Tks):
#                         return True

#     elif Tks['CLASS NAME'][I] in [';']:
#         return True  # Epsilon production

#     return False


# def ref_double_prime(Tks):
#     global I

#     if Tks['CLASS NAME'][I] in ['.']:
#         if Tks['CLASS NAME'][I] == '.':
#             I += 1
#             if Tks['CLASS NAME'][I] == 'id':
#                 I += 1
#                 if ref(Tks):
#                     return True

#     elif Tks['CLASS NAME'][I] in [';']:
#         return True  # Epsilon production

#     return False


def para(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if exp(Tks):
            if mul_para(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['id','int_const', 'bool_const', 'char_const', 'string_const', 'float_const', '(', 'not', ']', '[',',',')']:
            return True  # Epsilon production

    return False


def mul_para(Tks):
    global I

    if Tks['CLASS NAME'][I] in [',']:
       if Tks['CLASS NAME'][I] == ',':
            I += 1
            if exp(Tks):
                if mul_para(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['id','int_const', 'bool_const', 'char_const', 'string_const', 'float_const', '(', 'not', ']', '[',';',')']:
        return True  # Epsilon production

    return False


## exp
def exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if or_exp(Tks):
            return True

    return False

def or_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if and_exp(Tks):
            if or_exp_prime(Tks):
                return True

    return False

def or_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['or']:
        if Tks['CLASS NAME'][I] == 'or':
            I += 1
            if and_exp(Tks):
                if or_exp_prime(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in [ ')', '{', ']', ';', ',']:
            return True  # Epsilon production

    return False

def and_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if in_exp(Tks):
            if and_exp_prime(Tks):
                return True

    return False


def and_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['and']:
        if Tks['CLASS NAME'][I] == 'and':
            I += 1
            if in_exp(Tks):
                if and_exp_prime(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['or', ')', '{', ']', ';', ',']:
            return True  # Epsilon production

    return False

def in_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if is_exp(Tks):
            if in_exp_prime(Tks):
                return True

    return False


def in_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['MO']:
        if Tks['CLASS NAME'][I] == 'MO':
            I += 1
            if is_exp(Tks):
                if in_exp_prime(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['and', 'or', ')', '{', ']', ';', ',']:
        return True  # Epsilon production

    return False


def is_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if RO_exp(Tks):
            if is_exp_prime(Tks):
                return True

    return False


def is_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['IO']:
        if Tks['CLASS NAME'][I] == 'IO':
            I += 1
            if RO_exp(Tks):
                if is_exp_prime(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['MO', 'and', 'or', ')', '{', ']', ';', ',']:
            return True  # Epsilon production

    return False


def RO_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if PM_exp(Tks):
            if RO_exp_prime(Tks):
                return True

    return False


def RO_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['RO']:
        if Tks['CLASS NAME'][I] == 'RO':
            I += 1
            if PM_exp(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['IO', 'MO', 'and', 'or', ')', '{', ']', ';', ',']:
        return True  # Epsilon production

    return False


def PM_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if DM_exp(Tks):
            if PM_exp_prime(Tks):
                return True

    return False

def PM_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['PM']:
        if Tks['CLASS NAME'][I] == 'PM':
            I += 1
            if DM_exp(Tks):
                if PM_exp_prime(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['RO', 'IO', 'MO', 'and', 'or',  ')', '{', ']', ';', ',']:
        return True  # Epsilon production

    return False

def DM_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if end_exp(Tks):
            if DM_exp_prime(Tks):
                return True

    return False


def DM_exp_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['DM']:
        if Tks['CLASS NAME'][I] == 'DM':
            I += 1
            if end_exp(Tks):
                if DM_exp_prime(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['*']:
        if Tks['CLASS NAME'][I] == '*':
            I += 1
            if power_exp(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['PM', 'RO', 'IO', 'MO', 'and',  'or',  ')', '{', ']', ';', ',']:
            return True  # Epsilon production

    return False


def power_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not']:
        if end_exp(Tks):
            if DM_exp_prime(Tks):
                return True
    
    elif Tks['CLASS NAME'][I] in ['*']:
        if Tks['CLASS NAME'][I] == '*':
            I += 1
            if end_exp(Tks):
                if DM_exp_prime(Tks):
                    return True

    # elif Tks['CLASS NAME'][I] in ['id', 'int_const', 'float_const', 'string_const', 'char_const', 'bool_const', '(', 'not', '*']:
    #     return True  # Epsilon production

    return False


def end_exp(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id']:
        if assign_st(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['int_const', 'float_const', 'string_const', 'char_const', 'bool_const']:
        if const(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['(']:
        if Tks['CLASS NAME'][I] == '(':
            I += 1
            if exp(Tks):
                if Tks['CLASS NAME'][I] == ')':
                    I += 1
                    return True

    elif Tks['CLASS NAME'][I] in ['not']:
        if Tks['CLASS NAME'][I] == 'not':
            I += 1
            if end_exp(Tks):
                return True

    return False


## Class def
def class_def(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['public', 'private', 'abstract', 'static', 'sealed', 'class']:
        if access_modifiers(Tks):
            if class_type(Tks):
                if Tks['CLASS NAME'][I] == 'class':
                    I += 1
                    if Tks['CLASS NAME'][I] == 'id':
                        I += 1
                        if CID(Tks):
                            if c_body(Tks):
                                return True

    return False


def access_modifiers(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['public']:
        if Tks['CLASS NAME'][I]=='public':  
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['private']:
        if Tks['CLASS NAME'][I]=='private':  
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['abstract', 'static', 'sealed', 'def','class', 'int', 'float', 'char', 'bool', 'str','id']:
        return True
    return False


def class_type(Tks):
    global I
    if Tks['CLASS NAME'][I] in ['abstract']:
        if Tks['CLASS NAME'][I] == 'abstract':
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['static']:
        if Tks['CLASS NAME'][I] == 'static':
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['sealed']:  
        if Tks['CLASS NAME'][I] == 'sealed':
            I += 1
            return True
    elif Tks['CLASS NAME'][I] in ['def','class']:
        return True  # Epsilon production

    return False


def CID(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['(']:
        if Tks['CLASS NAME'][I] == '(':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if mul_id(Tks):
                    if Tks['CLASS NAME'][I] == ')':
                        I += 1
                        return True

    elif Tks['CLASS NAME'][I] in ['{']:
        return True  # Epsilon production

    return False

def mul_id(Tks):
    global I

    if Tks['CLASS NAME'][I] in [',']:
        if Tks['CLASS NAME'][I] == ',':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if mul_id(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in [')']:
        return True  # Epsilon production

    return False


def csst(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['if']:
        if if_else(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['for', 'while']:
        if loops(Tks):
            return True
        
    elif Tks['CLASS NAME'][I] in ['try']:
        if try_st(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['self', 'super']:
        if ss(Tks):
            if assign_st(Tks):
                if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True
            
    elif Tks['CLASS NAME'][I] in ['id']:
        I += 1
        if Tks['CLASS NAME'][I] in ['id']:
            I -= 1
            if dec(Tks):
                return True
        elif Tks['CLASS NAME'][I] in ['.','[','(','AO']:  
            I -= 1
            if assign_st(Tks):
                if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True
                
    elif Tks['CLASS NAME'][I] in ['int','str','char','float','id']: 
        if dec(Tks):
            return True

    elif Tks['CLASS NAME'][I] in ['public', 'private']:
        I += 1
        if Tks['CLASS NAME'][I] in ['abstract', 'static', 'sealed']:
            I += 1
            if Tks['CLASS NAME'][I] in ['def', 'int', 'float', 'char', 'bool', 'str', 'id']:
                I -= 2
                if access_modifiers(Tks):
                    if csst_prime(Tks):
                        return True
            elif Tks['CLASS NAME'][I] in ['class']:
                I -= 2
                if class_def(Tks):
                    return True

    elif Tks['CLASS NAME'][I] in ['def', 'static', 'sealed', 'abstract']:
        if class_type(Tks):
            if fn_def(Tks):
                return True
        
    elif Tks['CLASS NAME'][I] in ['class']:
        if class_def(Tks):
            return True
        
    elif Tks['CLASS NAME'][I] in ['return']:           
        if ret(Tks):
            if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True

    elif Tks['CLASS NAME'][I] in ['pass']:      
        if Tks['CLASS NAME'][I] == 'pass':
            I += 1
            if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True

    elif Tks['CLASS NAME'][I] in ['continue']:      
        if Tks['CLASS NAME'][I] == 'continue':
            I += 1
            if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True

    elif Tks['CLASS NAME'][I] in ['break']:      
        if Tks['CLASS NAME'][I] == 'break':
            I += 1
            if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True

    return False

def csst_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['int','str','char','float','id']: 
        if dec(Tks):
            return True
    
    elif Tks['CLASS NAME'][I] in ['abstract', 'static', 'sealed', 'def']: 
        if class_type(Tks):
            if fn_def(Tks):
                return True

    return False

def c_body(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['{']:
        if Tks['CLASS NAME'][I] == '{':
            I += 1
            if c_mst(Tks):
                if Tks['CLASS NAME'][I] == '}':
                    I += 1
                    return True

    return False


def c_mst(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['if', 'for', 'while', 'try', 'pass', 'self', 'super', 'id', 'public', 'private', 'abstract', 'static', 'sealed', 'def', 'return', 'break', 'continue', 'int', 'str', 'char', 'float']:
        if csst(Tks):
            if c_mst(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['}',';']:
        return True  # Epsilon production

    return False

## Declaration

def dec(Tks):
    global I

    if Tks['CLASS NAME'][I] in [ 'int','str','char','float', 'id']:
        if dt_prime(Tks):
            if Tks['CLASS NAME'][I] == 'id':
                I += 1

                if dec_prime(Tks):
                    return True

    return False

def dt_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in [ 'int','str','char','float']:
        if dt(Tks):
            return True
        
    elif Tks['CLASS NAME'][I] in [ 'id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            return True

    return False

def dec_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['[', '{' ]:
        if LD_dec(Tks):
            return True

    elif Tks['CLASS NAME'][I] in [ 'AO', ';', ',']:
        if init_double_prime(Tks):
            if dec_double_prime(Tks):
                return True
    elif Tks['CLASS NAME'][I] in ['def', 'if', 'for', 'while', 'try', 'pass', 'id', 'abstract', 'static', 'sealed', 'self', 'super', '#']:
        return True 

    return False

def init_double_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['AO']:
        if Tks['CLASS NAME'][I] == 'AO':
            I += 1
            if init(Tks):
                return True
    elif Tks['CLASS NAME'][I] in [';', ',']:
        return True
    
    return False

def LD_dec(Tks):
    global I

    if Tks['CLASS NAME'][I] in [ '[' ]:
        if Tks['CLASS NAME'][I] == '[':
            I += 1
            if Tks['CLASS NAME'][I] == ']':
                I += 1
                if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True

    elif Tks['CLASS NAME'][I] in ['{']:
        if Tks['CLASS NAME'][I] == '{':
            I += 1
            if Tks['CLASS NAME'][I] == '}':
                I += 1
                if Tks['CLASS NAME'][I] == ';':
                    I += 1
                    return True

    return False

def init(Tks):
    global I

    if Tks['CLASS NAME'][I] in ['id']:
        if Tks['CLASS NAME'][I] == 'id':
            I += 1
            if init_double_prime(Tks):
                return True

    elif Tks['CLASS NAME'][I] in ['int_const', 'float_const', 'string_const', 'char_const', 'bool_const']:
        if const(Tks):
            return True

    return False

def dec_double_prime(Tks):
    global I

    if Tks['CLASS NAME'][I] in [';']:
        if Tks['CLASS NAME'][I] == ';':
            I += 1
            return True

    elif Tks['CLASS NAME'][I] in [',']:
        if Tks['CLASS NAME'][I] == ',':
            I += 1
            if Tks['CLASS NAME'][I] == 'id':
                I += 1
                if init_double_prime(Tks):
                    if dec_double_prime(Tks):
                        return True

    return False
