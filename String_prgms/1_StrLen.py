'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to calculate the length of a string problem
'''

def string_len(str_var):
    """ 
    Description :
        This function is used to calculate the length of a string
    Parameters :
        str_var = string variable
    Return :
        It returns the length of a string
    """
    str_len = len(str_var)
    return str_len

def main():
    string_val = "Hello Have u r Food"
    res = string_len(string_val)
    print(f"The length of the {string_val} is {res}")

if __name__ == "__main__":
    main()
    