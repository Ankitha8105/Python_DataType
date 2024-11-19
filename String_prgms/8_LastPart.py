'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to get the last part of a string before a specified character problem
'''
def get_last_part_before_character(string, character):
    """ 
    Description :
        This function is used to get the last part of a string before a specified character
    Parameters :
        string_val : String value
        character : specified character 
    Return :
        It returns the get a string before a specified character
    """
    parts = string.split(character)
    if len(parts) > 1:
        return character.join(parts[:-1])  
    else :
        return string

def main():
    input_string = "https://www.w3resource.com/python-exercises"
    specified_character = "/"

    result = get_last_part_before_character(input_string, specified_character)
    print("The last part before the specified character is:", result)

if __name__ == "__main__":
    main()
