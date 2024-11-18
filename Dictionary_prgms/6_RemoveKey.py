'''
    @Author: Ankitha B L
    @Date:16-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 16-11-2024
    @Title: To remove a key from a dictionary problem
'''

def remove_key(dict_items,key):
    """ 
    Description :
        This function is used to remove a key from a dictionary
    Parameter :
        dict_items : Dictionary elements
    Return :
        It return dictionary in the from of (x, x*x)
    """
    dict_items.pop(key)
    return dict_items

def main():
    dict_ele = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    key = 4
    res_dict = remove_key(dict_ele,key)
    print(f"The Dictionary Elements After removing are {res_dict}")

if __name__ == "__main__":
    main()


