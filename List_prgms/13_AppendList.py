'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To append a first list to the second list problem
'''

def append_list(list1):
    """ 
    Description :
        This function is used to append a list to the second list
    Parameters :
        list1 = List items
    Return :
        It returns the extended list
    """
    list2 = [4,5,6,7,9]

    list1.extend(list2)

    return list1

def main():
    list1 = [9,1,2,3,4]

    extended_list = append_list(list1)
    print(f"The Append list is {extended_list}")

if __name__ == "__main__":
    main()