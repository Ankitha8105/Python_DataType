'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to create a Symmetric Difference of sets problem
'''

def symmetric_difference_set(set1,set2):
    """ 
    Description :
        This function is used to create a Symmetric difference of sets
    Parameters :
        set1 :First set Elements
        set2 :second set Elements
    Return :
        It returns the symmetric difference of sets
    """
    set_diff = set1.symmetric_difference(set2)
    return set_diff

def main():
    set1 = {"Hii",'fruits',2,6,8,2,1.1}
    set2 = {4,'Hello',8.0,1,'Mango',2,3,5}
    res_set = symmetric_difference_set(set1,set2)
    print(f"The symmetric Difference of two sets are {res_set}")

if __name__ == "__main__":
    main()
