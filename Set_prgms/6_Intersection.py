'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title:  Python program to create an intersection of sets problem
'''

def intersection_set(set1,set2):
    """ 
    Description :
        This function is used to create an intersection of sets
    Parameters :
        set1 :First set Elements
        set2 :second set Elements
    Return :
        It returns the intersection of sets
    """
    inter_set = set1.intersection(set2)
    return inter_set

def main():
    set1 = {1,2,3,42,7,2,1,42}
    set2 = {2,7,42,1,11,43}
    res_set = intersection_set(set1,set2)
    print(f"The Intersection Set is {res_set}")

if __name__ == "__main__":
    main()