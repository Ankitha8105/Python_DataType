'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself problem
'''

def replace_char(string_var):
    """ 
    Description :
        This function is used to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
    Parameters :
        string_var = string variable
    Return :
        It returns the String After replacing
    """
    strn = string_var[1:]
    replaced_str = string_var[:1]+strn.replace('r','$')
    print(replaced_str)

def main():
    string_val = 'restart'
    replace_char(string_val)

if __name__ == "__main__":
    main()