'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To iterate over dictionaries using for loops problem
'''

def iterate_dict(dict_items):
    """ 
    Description :
        This function is used to iterate over dictionaries using for loops
    Parameter :
        dict_items : Dictionary elements
    Return :
        It return reversed tuple
    """
    for item in dict_items:
        print(f"{item} : {dict_items.get(item)}",end = ' , ')

def main():
    dict_item = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    iterate_dict(dict_item)

if __name__ == "__main__":
    main()