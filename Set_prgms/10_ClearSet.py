'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to clear a set problem
'''

def clear_set(set_ele):
    """ 
    Description :
        This function is used to clear a set
    Parameters :
        set_ele :set Elements
    Return :
        It returns the Empty set
    """
    empty_set = set_ele.clear()
    print(f"The Elements in the Set is cleared")

def main():
    set_items = {"Hii",'fruits',2,6,8,2,1.1}
    clear_set(set_items)

if __name__ == "__main__":
    main()
