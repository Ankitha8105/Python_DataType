'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to use of frozensets problem
'''

def frozen_set(set1,set2):
    """ 
    Description :
        This function is used to use of frozensets
    Parameters :
        set1 :First set Elements
        set2 :Second set Elements
    Return :
        It returns the frozen_set methods
    """
    copy_set = set1.copy()
    print(f"The copies frozen set elements are {copy_set}")

    union_set = set1.union(set2)
    print(f"The Union of two frozen sets is {union_set}")

    intersection_set = set1.intersection(set2)
    print(f"The intersection of two frozen sets is {intersection_set}")

    diff_set = set2.difference(set1)
    print(f"The difference of two frozen sets is {diff_set}")

def main():
    set1 = ["Hii",'fruits',2,6,8,2,1.1]
    frozen_set1 = frozenset(set1)
    set2 = [4,'Hello',8.0,1,'Mango',2,3,5]
    frozen_set2 = frozenset(set2)
    frozen_set(frozen_set1,frozen_set2)

if __name__ == "__main__":
    main()