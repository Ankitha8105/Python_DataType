'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to takes input from the user and displays that input back in upper and lower cases problem
'''

def sort_input_str(string_vals):
    """ 
    Description :
        This function is used to takes input from the user and displays that input back in upper and lower cases
    Parameters :
        string_val = String value
    Return :
        It returns the string in lower case and in upper case
    """
    words = [words.strip() for words in string_vals.split(',')]
    sorted_list = sorted(set(words))
    sorted_str = ' , '.join(sorted_list)
    return sorted_str

def main():
    str_vals = input("Enter comma separated sequence of strings :")
    sorted_str = sort_input_str(str_vals)
    print(f"The Sorted String Values are : {sorted_str}")

if __name__ == "__main__":
    main()