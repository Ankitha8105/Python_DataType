'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To takes two lists and returns True if they have at least one common member problem
'''
def common_Ele(list1,list2):
    """ 
    Description :
        This function is used to takes two lists and returns True if they have at least one common member list of words
    Parameters :
        list1 = First List items
        list2 = Second list items
    Return :
        It returns common elements present between two list or not
    """
    flag = False
    for item in list1:
        if item in list2:
            flag = True
            break

    return flag

def main():
    list1 = [1,2,3,4,5,6]
    list2 = [5,6,7,8]

    res = common_Ele(list1,list2)
    if res:
        print("Common elements present in both the lists")
    else:
        print("No common elements from both the list")

if __name__ == "__main__":
    main()