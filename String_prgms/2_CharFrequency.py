'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to count the number of characters (character frequency) in a String problem
'''

def character_freq(string_var):
    """ 
    Description :
        This function is used to count the number of characters (character frequency) in a String
    Parameters :
        string_var = string variable
    Return :
        It returns the frequency of each character in a string
    """
    count_dict = { }
    for character in string_var:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def main():
    string_val = 'google.com'
    res_dict =  character_freq(string_val)
    print(f"The character frequency is {res_dict}")

if __name__  == "__main__":
    main()

