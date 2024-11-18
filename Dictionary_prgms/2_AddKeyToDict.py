'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To add a key to a dictionary problem
'''

def add_Key_dict(dict_items):
    """ 
    Description :
        This function is used to add a key to a dictionary
    Parameters :
        list_items = List items  
    Return :
        It returns key added dictionary
    """
    dict_items[2] = 30
    return dict_items

def main():
    dict_ele =  {0: 10, 
                 1: 20}
    res_dict = add_Key_dict(dict_ele)
    print(res_dict)

if __name__ == "__main__":
    main()