'''
    @Author: Ankitha B L
    @Date: 15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 22-11-2024
    @Title: To sort a dictionary by value in ascending and descending order
'''

def sort_dict_by_value(dict_items):
    """ 
    Description :
        This function sorts a dictionary by its values in ascending 
        and descending order without using a lambda function.
    Parameters :
        dict_items: Dictionary to be sorted
    Return :
        Returns two dictionaries: one sorted in ascending order and the 
        other in descending order.
    """
    
    sorted_asc = dict(sorted(dict_items.items(), key=key_function))
    
   
    sorted_desc = dict(sorted(dict_items.items(), key=key_function, reverse=True))
    
    return sorted_asc, sorted_desc

def key_function(item):
    """ 
    A helper function to extract the value of a dictionary item for sorting.
    """
    return item[1]

def main():
    dict_ele = {'a': 3, 
                'b': 1, 
                'c': 2, 
                'd': 4}
    asc_dict, desc_dict = sort_dict_by_value(dict_ele)
    print("Dictionary sorted by value (ascending):", asc_dict)
    print("Dictionary sorted by value (descending):", desc_dict)

if __name__ == "__main__":
    main()
