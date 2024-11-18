'''
    @Author: Ankitha B L
    @Date:18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18- 11-2024
    @Title: program to iteration over sets problem
'''

def create_set(set_ele):
    """ 
    Description :
        This function is used to iteration over sett
    Parameters :
        set_ele = set of items
    Return :
        It returns the set items
    """
    for item in set_ele:
        print(item,end = " ")

def main():
    set_ele = {1,3,4,5,2,1,3,2}
    create_set(set_ele)

if __name__ =="__main__":
    main()