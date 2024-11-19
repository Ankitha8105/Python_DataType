'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to reverse a string problem
'''

def reverse_str(string_val):
    """ 
    Description :
        This function is used to reverse a string
    Parameters :
        string_val = String value
    Return :
        It returns the reversed string
    """
    return string_val[ ::-1]

def main():
    string_val = "SomthingBeautifull"
    res_str = reverse_str(string_val)
    print(f"The Reversed string is : {res_str}")

if __name__ == "__main__":
    main()