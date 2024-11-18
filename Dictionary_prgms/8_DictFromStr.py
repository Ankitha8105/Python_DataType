'''
    @Author: Ankitha B L
    @Date:18 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18- 11-2024
    @Title: To create a dictionary from a string problem
'''
def str_to_dict(string_name):
    """ 
    Description :
        This function is used to create a dictionary from a string
    Parameter :
        String_name : String
    Return :
        It return a created dictionary from a string
    """
    count_dict = {} 
    for char in string_name:
        if char in count_dict:
            count_dict[char] += 1 
        else:
            count_dict[char] = 1  
    return count_dict

def main():
    string = "w3resource" 
    res_dict = str_to_dict(string) 
    print(f"The resulting dictionary is {res_dict}")

if __name__ == "__main__":
    main()
