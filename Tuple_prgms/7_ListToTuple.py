'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To convert a list to a tuple.
'''
def list_tuple(list_items):
    """ 
    Description :
        This function is used to convert a list to a tuple
    Parameter :
        list_items = List elements
    Return :
        It return tuple elements
    """
    tuple_ele = tuple(list_items)
    return tuple_ele

def main():
    list_ele = [8,2,"Morning",9.0,16,8.4,2]

    tuple_items = list_tuple(list_ele)
    print(f"The tuple items are {tuple_items}")

if __name__ == "__main__":
    main()
