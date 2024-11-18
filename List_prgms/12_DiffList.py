'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To get the difference between the two lists problem
'''
def diff_list(list1,list2):
    """ 
    Description :
        This function is used to get the difference between the two lists
    Parameters :
        list1 = First List items
        list2 = Second list items
    Return :
        It returns the difference between the two lists
    """
    set1 = set(list1)
    set2 = set(list2)

    set_diff = set1.difference(set2)

    list_diff = list(set_diff)
    return list_diff

def main():
    list1 = [1,2,3,4,5,6]
    list2 = [4,5,6,7,8,9,0]

    list_diff = diff_list(list1,list2)

    print(f"The Difference between the {list1} and {list2} is {list_diff}")

if __name__ == "__main__":
    main()