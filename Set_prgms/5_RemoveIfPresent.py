'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to remove an item from a set if it is present in the set problem
'''

def remove_if_present(set_ele,ele):
    """ 
    Description :
        This function is used to remove an item from a set if it is present in the set
    Parameters :
        set_ele : set of items
        ele : Element to remove
    Return :
        It returns the set items after deleting Element
    """
    if ele in set_ele:
        set_ele.remove(ele)
        print(f"The element {ele} is deleted from the {set_ele}")
    else:
        print(f"The element {ele} is not present in the {set_ele}")

def main():
    set_ele = {1,5,'hello',4.3,5,2}
    ele = 5
    remove_if_present(set_ele,ele)

if __name__ == "__main__":
    main()
