'''
    @Author: Ankitha B L
    @Date: 18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18-11-2024
    @Title: To convert a list into a nested dictionary of keys
'''
def list_to_nested_dict(lst):
    """ 
    Description :
        This function is used to convert a list into a nested dictionary of keys
    Parameter :
        lst : List Elements
    Return :
        It return a list of nested dictionary of keys
    """
    result = {}
    current = result
    for item in lst:
        current[item] = {}
        current = current[item]
    return result

def main():
    lst = ['a', 'b', 'c', 'd']
    print(list_to_nested_dict(lst))

if __name__ == "__main__":
    main()
