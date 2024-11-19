'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to lowercase first n characters in a string problem
'''

def str_to_lowercase(string_val,n):
    """ 
    Description :
        This function is used to lowercase first n characters in a string
    Parameters :
        string_val : String value
        n : Number upto lowercase the string
    Return :
        It returns the string which lowercase first n characters in a string
    """
    if(len(string_val) >= n):
        res_str = string_val[:n].lower()+string_val[n:]
        return res_str
    else:
        print("Please enter correct string")

def main():
    string_val = input("Enter the String :")
    n = 4
    result_str = str_to_lowercase(string_val,n)
    print(f"The Final string is {result_str}")

if __name__ == "__main__":
    main()
