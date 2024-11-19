'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to create a union of sets problem
'''

def union_set(set1,set2):
    """ 
    Description :
        This function is used to create a union of sets
    Parameters :
        set1 :First set Elements
        set2 :second set Elements
    Return :
        It returns the union of sets
    """
    set_union_ele = set1.union(set2)
    return set_union_ele

def main():
    set1 = {"Hii",'fruits',2,6,8,2,1}
    set2 = {4,'Hello',8.0,1,'Mango',2,3,5}
    res_set = union_set(set1,set2)
    print(f"The Union of set elements are {res_set}")

if __name__ == "__main__":
    main()