import uuid
import pandas as pd

scopeCount    : int        = 0
defTable     : list[dict] = []
scopeTable : list[dict] = []
memTables    : dict       = {}
stack         : list       = [] 
CCR : str = ""
CCN : str = ""

def to_dataFrame(data):
    a = pd.DataFrame(data)
    a = pd.DataFrame.from_dict(data)
    a = pd.DataFrame.from_records(data)

    print(a)

def createDataTable() -> str:
    
    key : str = str(uuid.uuid4())

    memTables[key] = []

    return key


def insertDT(name:str,type:str,accessModifier:str,category:str,parent:str,link:str) -> bool:
    if name not in [i["Name"] for i in defTable]:
    
        defTableEntry : dict = {
                        "Name":name,
                        "Type":type,
                        "Access Modifier":accessModifier,
                        "Category":category,
                        "Parent":parent,
                        "Link":link
                        }
        defTable.append(defTableEntry)
        return True
    else:
        return False


def insertST(name:str,type:str, scope:int) -> bool:
    # scope = stack[-1]
    if {"Name":name,"Scope":scope,"Type":type.split("->")[0]} not in [{"Name":i["Name"],"Scope":i["Scope"],"Type":i["Type"].split("->")[0]} for i in scopeTable]:
    
        scopeTableEntry : dict= {
                       "Name":name,
                       "Type":type,
                       "Scope":scope
                       }
        scopeTable.append(scopeTableEntry)
        return True
    else:
        return False



def insertMTFN(name:str,type:str,accessModifier:str,typeModifier:str,link:str) -> bool:
    if {"Name":name,"Type":type} not in [{"Name":i["Name"],"Type":i["Type"]} for i in memTables[link]]:
    
        dataTableEntry : dict = {
                    "Name":name,
                    "Type":type,
                    "Access Modifier":accessModifier,
                    "Type Modifier":typeModifier,
                }
        memTables[link].append(dataTableEntry)
        return True
    else:
        return False





def lookupDT(name:str) -> dict:
    for i in defTable:
        if i["Name"] == name:
            return i
    else:
        return None


def lookupST(name:str,scopes:int) -> dict:
    for scope in range(scopes,-1,-1):
        for i in scopeTable:
            if i["Name"] == name and i["Scope"] == scope :
                return i
        else:
            return None

def lookupMTATT(name:str,link:str) -> dict:
    for i in memTables[link]:
        if i["Name"] == name:
            return i
    else:
        return None


def lookupMTFN(name:str,type:str,link:str) -> dict:
    for i in memTables[link]:
        if i["Name"] == name and i["Type"].split("->")[0] == type.split("->")[0]:
            return i
    else:
        return None


def CompatibilityBinary(leftType:str,rightType:str,operator:str) -> str :
    binaryTypeRules = {
            ('int', 'int', '+'):       'int',
            ('int', 'int', '*'):       'int',
            ('int', 'int', '/'):       'float',
            ('int', 'int', '%'):       'float',
            ('int', 'float', '+'):     'float',
            ('float', 'int', '+'):     'float',
            ('float', 'float', '+'):   'float',
            ('str', 'str', '+'): 'str',
            ('int', 'int', '-'):       'int',
            ('bool', 'bool', 'and'):   'bool',
            ('bool', 'bool', 'or'):    'bool',
            ('int', 'int', '=='):      'bool',
            ('int', 'int', '>='):      'bool',
            ('int', 'int', '<='):      'bool',
            ('int', 'int', '>'):       'bool',
            ('int', 'int', '<'):       'bool',
            ('int', 'int', '!='):      'bool',
            ('float', 'float', '=='):  'bool',
            ('float', 'float', '>='):  'bool',
            ('float', 'float', '<='):  'bool',
            ('float', 'float', '>'):   'bool',
            ('float', 'float', '<'):   'bool',
            ('float', 'float', '!='):  'bool',
            ('str', 'str', '=='):'bool',
            ('bool', 'bool', '=='):    'bool',
            ('int', 'int'  , '='):     'int',
            ('bool', 'bool', '='):     'bool',
            ('float','float', '='):    'float',
            ('str', 'str', '='): 'str',
            
    }
    returnedDataType = binaryTypeRules.get((leftType, rightType, operator), 'Unknown')  
    if returnedDataType == "Unknown":
        return ""
    else:
        return returnedDataType

 
def CompatibilityUnary(operandType:str,operand:str) -> str :
    unaryTypeRules = {

            ('bool','!')    : 'bool'
        }
    
    returnedDataType = unaryTypeRules.get((operandType,operand), 'Unknown')   
    if returnedDataType == "Unknown":
        return ""
    else:
        return "returnedDataType"



def createScope() -> bool:
    global scopeCount
    scopeCount+=1
    stack.append(scopeCount)
    return True


def destroyScope() -> bool:
    stack.pop()



# insertST('a','int->int',1)
# insertST('b','str',1)
# a = createDataTable()
# insertDT('a','private', 'public','none', 'none', a)
# insertMTFN('a','ax','zsx','saa', a)
# print(lookupMTATT('a', a))
# to_dataFrame(scopeTable)
# to_dataFrame(defTable)
