import pandas as pd
import re
from tabulate import tabulate
import pyfiglet

def tokens ():
    List_Of_Operators = ["+", "-", "*", "/", "%", "!", "=", "<", ">"]
    Punctuators = [";", ",", ":", "(", ")", "{", "}", "[", "]"]

    Int_const = r'^[+-]?\d+$'
    Float_const = r'^[+-]?(?:\d+\.\d*|\.\d+)(?:[eE][+-]?\d+)?$'
    string_const = r'^\".*\"$'
    char_const = r'^\'.*\'$'
    ID = r"^[a-zA-Z][a-zA-Z0-9_]*$"

    # Load keyword, operator, and punctuator data
    keyword_df = pd.read_excel("Keywords_Classify.xlsx")  # Adjust the filename as needed
    keyword = dict(zip(keyword_df["VALUE"], keyword_df["CLASS NAME"]))

    operator_df = pd.read_excel("Operators_Classify.xlsx")  # Adjust the filename as needed
    operator = dict(zip(operator_df["VALUE"], operator_df["CLASS NAME"]))

    punctuator_df = pd.read_excel("Punctuators_Classify.xlsx")  # Adjust the filename as needed
    punctuator = dict(zip(punctuator_df["VALUE"], punctuator_df["CLASS NAME"]))


    # Initialize an empty list to store the token strings
    output_tokens = []

    # Open the text file for reading
    with open("input.txt", "r") as file:
        token_list = []  # Initialize an empty list to store the tokens

        word = ""  # Initialize an empty string to store the current word
        inside_multiline_comment = False  # Flag to track whether inside a multiline comment

        lines = file.readlines()

        for index, line in enumerate(lines):
            line_token = []
            line_length = len(line)  # Get the length of the line

            i = 0
            while i < line_length:
                char = line[i]

                if inside_multiline_comment:  # Check for multi line comment
                    if char == "*" and i + 1 < line_length and line[i + 1] == "$":
                        inside_multiline_comment = False
                        i += 2  # Skip both '*' and '$'
                    else:
                        i += 1  # Skip the current character
                else:
                    if char == "$" and i + 1 < line_length and line[i + 1] == "*":
                        inside_multiline_comment = True
                        i += 2  # Skip both '$' and '*'

                    if char in [" ", "\n"]:
                        if word:
                            line_token.append(word)  # Append the previous word
                            word = ""  # Reset the word

                    elif char == "$":  # Check for single line comment
                        if word:
                            line_token.append(word)  # Append the previous word
                            word = ""  # Reset the word
                        while char != "\n":
                            if i >= line_length:
                                break
                            i += 1

                    elif char == "'":  # Check for character constant
                        if word:
                            line_token.append(word)  # Append the previous word
                            word = ""  # Reset the word
                        word += char

                        if i + 1 < line_length:  # Check if not the last character
                            next_char = line[i + 1]
                            if next_char == "\\":
                                for k in range(3):
                                    if i >= line_length:
                                        break
                                    else:
                                        i += 1
                                        char = line[i]
                                        word += char
                            else:
                                for k in range(2):
                                    if i >= line_length:
                                        break
                                    else:
                                        i += 1
                                        char = line[i]
                                        word += char

                        if word:
                            line_token.append(word)  # Append the previous word
                            word = ""  # Reset the word
                            
                    elif char == '"':  # Check for string constant
                        if word:
                            line_token.append(word)  # Append the previous word
                            word = ""  # Reset the word
                        word += char

                        while True:
                            i += 1
                            if i >= line_length:
                                break

                            char = line[i]
                            # word += char

                            if char == "\\":  # Check for escape sequence
                                if i + 1 < line_length:
                                    next_char = line[i + 1]
                                    word += next_char
                                    i += 1  # Skip the next character

                            elif char == '"':
                                word += char
                                line_token.append(word)  # Append the string constant
                                word = ""  # Reset the word
                                break
                            else:
                                word += char

                    elif char in List_Of_Operators:
                        if i + 1 < line_length:  # Check if not the last character
                            next_char = line[i + 1]
                            if char == "/":
                                if next_char == "/":
                                    if (i + 2 < line_length) and (
                                        line[i + 2] == "="
                                    ):  # Check if not the last character
                                        next_next_char = line[i + 2]
                                        if word:
                                            line_token.append(
                                                word
                                            )  # Append the previous word
                                            word = ""  # Reset the word
                                        line_token.append(char + next_char + next_next_char)
                                        i += 2
                                    else:
                                        if word:
                                            line_token.append(
                                                word
                                            )  # Append the previous word
                                            word = ""  # Reset the word
                                        line_token.append(char + next_char)
                                        i += 1  # Skip the next character
                                elif next_char == "=":
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char + next_char)
                                    i += 1
                                else:
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char)

                            elif char == "*":
                                if next_char == "*":
                                    if (i + 2 < line_length) and (
                                        line[i + 2] == "="
                                    ):  # Check if not the last character
                                        next_next_char = line[i + 2]
                                        if word:
                                            line_token.append(
                                                word
                                            )  # Append the previous word
                                            word = ""  # Reset the word
                                        line_token.append(char + next_char + next_next_char)
                                        i += 2
                                    else:
                                        if word:
                                            line_token.append(
                                                word
                                            )  # Append the previous word
                                            word = ""  # Reset the word
                                        line_token.append(char + next_char)
                                        i += 1  # Skip the next character
                                elif next_char == "=":
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char + next_char)
                                    i += 1
                                else:
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char)
                            elif char == "+":
                                # if next_char == "+":
                                #     if word:
                                #         line_token.append(word)  # Append the previous word
                                #         word = ""  # Reset the word
                                #     line_token.append(char + next_char)
                                #     i += 1  # Skip the next character
                                if next_char == "=":
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char + next_char)
                                    i += 1
                                else:
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char)

                            elif char == "-":
                                if word:
                                    line_token.append(word)  # Append the previous word
                                    word = ""  # Reset the word

                                # if (next_char.isdigit()) or (next_char == "."):  # Check if the next character is a digit
                                #     word += char  # Add the minus sign to the word
                                #     while i + 1 < line_length and (line[i + 1].isdigit() or line[i + 1] == "."):
                                #         i += 1
                                #         word += line[i]
                                if next_char == "-":
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char + next_char)
                                    i += 1  # Skip the next character
                                elif next_char == "=":
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char + next_char)
                                    i += 1
                                else:
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char)
                                    
                            elif next_char == "=":
                                if word:
                                    line_token.append(word)  # Append the previous word
                                    word = ""  # Reset the word
                                line_token.append(char + next_char)
                                i += 1  # Skip the next character
                            else:
                                if word:
                                    line_token.append(word)  # Append the previous word
                                    word = ""  # Reset the word
                                line_token.append(char)
                        else:
                            if word:
                                line_token.append(word)  # Append the previous word
                                word = ""  # Reset the word
                            line_token.append(char)

                    elif char in Punctuators:
                        if char == ":":
                            if i + 1 < line_length:  # Check if not the last character
                                next_char = line[i + 1]
                                if next_char == ":":
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char + next_char)
                                    i += 1  # Skip the next character
                                else:
                                    if word:
                                        line_token.append(word)  # Append the previous word
                                        word = ""  # Reset the word
                                    line_token.append(char)
                            else:
                                if word:
                                    line_token.append(word)  # Append the previous word
                                    word = ""  # Reset the word
                                line_token.append(char)
                        else:
                            if word:
                                line_token.append(word)  # Append the previous word
                                word = ""  # Reset the word
                            line_token.append(char)

                    elif char == ".":
                        if word and word.isdigit():
                            # If the current word is a number, continue adding digits
                            word += char
                        else:
                            if word:
                                line_token.append(word)  # Append the previous word
                                word = ""  # Reset the word
                            word += char
                        temp = ""
                        while True:
                            i += 1
                            if i >= line_length:
                                break
                            char = line[i]
                            if char in [
                                " ",
                                "\n",
                                "+", "-", "*", "/", "%", "!", "=", "<", ">",
                                ";", ",", ":", "(", ")", "{", "}", "[", "]",
                                ".",
                                "'",
                                '"',
                                "$",
                            ]:
                                i -= 1
                                break

                            else:
                                temp += char
                        if temp:
                            if temp[0].isdigit():
                                word += temp
                                temp = ""
                            else:
                                if word:
                                    line_token.append(word)  # Append the previous word
                                    word = ""  # Reset the word
                                line_token.append(temp)
                                temp = ""

                    else:
                        word += char  # Add the character to the current word

                    i += 1

            if word:  # Append the last word if it's not empty
                line_token.append(word)
                word = ""  # Reset the word after appending
            token_list.append(line_token)

    # for index, token in enumerate(token_list):
    #     print(index + 1, token)

    # output_tokens = []  # Initialize the list to store output tokens

    index = 0  # Initialize the index for token_list

    while index < len(token_list):
        token_line = token_list[index]  # Get the current line of tokens
        line_number = index + 1  # Line number corresponds to the index + 1

        for word in token_line:
            if re.match(ID, word):
                if word in keyword:
                    class_name = keyword[word]
                else:
                    class_name = "id"
            elif re.match(Int_const, word):
                class_name = "int_const"
            elif re.match(Float_const, word):
                class_name = "float_const"
            elif re.match(string_const, word):
                check = len(word)
                if word[check-2] == "/":
                    class_name = "Invalid Lexeme"
                else:
                    class_name = "string_const"
            elif re.match(char_const, word):
                class_name = "char_const"
            elif word in operator:
                class_name = operator[word]
            elif word in punctuator:
                class_name = punctuator[word]
            else:
                class_name = "Invalid Lexeme"

            output_tokens.append((class_name, word.strip("\"'") if class_name != "Invalid Lexeme" else word, line_number))

        index += 1  # Move to the next line

    # Create a pandas DataFrame from the output tokens
    df = pd.DataFrame(output_tokens, columns=["CLASS NAME", "VALUE", "LINE NO."])

    # Create a new row as a Series
    new_row = pd.Series({"CLASS NAME":"#", "VALUE":"#", "LINE NO.":index})
    # Add the new row to the DataFrame using the integer index
    df.loc[len(df)] = new_row
        
    return df

df = tokens()

print(df['CLASS NAME'][0])
print(df)
# Convert the DataFrame to a tabular format
table = tabulate(df, headers='keys', tablefmt='grid')

# Create the stylized "TOKENS" heading using pyfiglet
result = pyfiglet.figlet_format("TOKENS")

# Add the formatted heading and table to the output text
output_text = result + table

# Write the formatted text to the output file
with open("output_tokens.txt", "w") as output_file:
    output_file.write(output_text)