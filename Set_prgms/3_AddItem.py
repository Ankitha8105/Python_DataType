'''
    @Author: Ankitha B L
    @Date:18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18- 11-2024
    @Title: To add member(s) in a set problem
'''

def add_to_set(set_ele):
    """ 
    Description :
        This function is used to add member(s) in a set
    Parameters :
        set_ele = set of items
    Return :
        It returns the set items after adding
    """
    ele1 = 8
    ele2 = 3

    set_ele.add(ele1)
    set_ele.add(ele2)

    return set_ele

def main():
    set_item = {1,2,1,6,4,2,5}
    res_ele = add_to_set(set_item)
    print(f"The set After adding elements {res_ele}")

if __name__ == "__main__":
    main()