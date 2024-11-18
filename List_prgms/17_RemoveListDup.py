'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To remove duplicates from a list of lists problem
'''

def remove_duplicate(list_ele):
    """ 
    Description :
        This function is used to remove duplicates from a list of lists.
    Parameters :
        list_ele = First List items
    Return :
        It return the list of remove duplicates from a list of lists 
    """
    distinct_ele = []
    set_ele = set()
    for items in list_ele:
        tuple_item = tuple(items)
        if tuple_item not in set_ele:
            distinct_ele.append(items)
            set_ele.add(tuple_item)

    return distinct_ele

def main():
    list_ele = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

    result = remove_duplicate(list_ele)
    print(f"The list After removing duplicates is :{result}")

if __name__ == "__main__":
    main()
    