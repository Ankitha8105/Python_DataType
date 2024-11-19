'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to display formatted text (width=50) as output problem
'''
import textwrap

def text_formate(str_val):
    """ 
    Description :
        This function is used to display formatted text (width=50) as output
    Parameters :
        string_val = String value
    Return :
        It returns the formatted text (width=50) as output
    """
    formatted_txt = textwrap.fill(str_val,width=50,initial_indent = "   ")
    print(f"The formatted string is {formatted_txt}")    

def main():
    str_val = "This is a Example program for formatted string and to do this we need to import the text wrap module and then we need to use fill function"
    text_formate(str_val)

if __name__ == "__main__":
    main()

