'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title: print the elements present in list_1 not in list_2 problem
'''
def diff(set_1,set_2):
    """ 
    Description :
        This function is used to find the elements present in set 1 not in set 2
    Parameters :
        set_1 : first set elements
        list : second set elements
    Return :
        It returns elements present in set 1 not in set 2
    """
    return set_1.difference(set_2)

def main():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    set1 = set(color_list_1)
    set2 = set(color_list_2)

    diff_val = diff(set1,set2)

    print(f"The elements present in set 1 are {diff_val}")

if __name__ == "__main__":
    main()
