'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to takes input from the user and displays that input back in upper and lower cases problem
'''

def lower_upper_case(string_val):
    """ 
    Description :
        This function is used to takes input from the user and displays that input back in upper and lower cases
    Parameters :
        string_val = String value
    Return :
        It returns the string in lower case and in upper case
    """
    str_lower = string_val.lower()
    str_upper = string_val.upper()
    return str_lower,str_upper

def main():
    str_val = input("Enter the String :")
    res_lower,res_upper = lower_upper_case(str_val)
    print(f"The String {str_val} in lower case {res_lower} and in upper case {res_upper}")

if __name__ == "__main__":
    main()