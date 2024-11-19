'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to find maximum and the minimum value in a set problem
'''

def max_min_set(set_ele):
    """ 
    Description :
        This function is used to find maximum and the minimum value in a set
    Parameters :
        set_ele :set Elements
    Return :
        It returns the maximum and the minimum value in a set
    """
    sort_ele = sorted(set_ele)
    print(f"The Maximum element is {sort_ele[-1]}")
    print(f"The Minimum element is {sort_ele[0]}")

def main():
    set_item = {1,3,5,67,2,3,1,11,87}
    max_min_set(set_item)

if __name__ == "__main__":
    main()