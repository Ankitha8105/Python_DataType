'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To remove an item from a tuple
'''
def remove_ele(tuple_ele,ele_remove):
    """ 
    Description :
        This function is used to remove an item from a tuple
    Parameter :
        tuple_ele = tuple elements
        ele_remove = element to remove
    Return :
        It return tuple after removing element
    """
    unique_list = []
    for item in tuple_ele:
        if (item != ele_remove):
            unique_list.append(item)
    unique_tuple = tuple(unique_list)
    return unique_tuple

def main():
    tuple_ele = ('abc',111,'alpha',4.0,"Hii")
    ele = 'Hii'

    tuple_items = remove_ele(tuple_ele,ele)
    print(f"The Tuple after removing {ele} is {tuple_items}")

if __name__ == "__main__":
    main()