'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to count occurrences of a substring in a string problem
'''

def count_substring(string_val):
    """ 
    Description :
        This function is used to count occurrences of a substring in a string
    Parameters :
        string_val = String value
    Return :
        It returns the occurrences of a substring in a string
    """
    try:
        sub_string = string_val[4:7]
        count = string_val.count(sub_string)
        print(f"The number of times {sub_string} present is {string_val} is {count}")
    except BaseException:
        print("Enter valid range")

def main():
    string_val = "How Are you Are You"
    count_substring(string_val)

if __name__ == "__main__":
    main()