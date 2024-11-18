'''
    @Author: Ankitha B L
    @Date:18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18- 11-2024
    @Title: To remove item(s) from set problem
'''

def remove_from_set(set_ele):
    """ 
    Description :
        This function is used to remove item(s) from set
    Parameters :
        set_ele = set of items
    Return :
        It returns the set items after removing
    """
    try:
        set_ele.remove(8)
        set_ele.remove(1)
    except KeyError:
        print("Please remove only set present elements")

    return set_ele

def main():
    set_item = {1,2,1,6,4,2,5}
    res_ele =remove_from_set(set_item)
    print(f"The set After adding elements {res_ele}")

if __name__ == "__main__":
    main()