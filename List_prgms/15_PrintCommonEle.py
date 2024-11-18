'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To find common items from two lists problem
'''

def common_Ele(list1,list2):
    """ 
    Description :
        This function is used to find common items from two lists
    Parameters :
        list1 = First List items
        list2 = Second list items
    Return :
        It returns common elements  between two list 
    """
    common_item = []
    for item in list1:
        if item in list2:
            common_item.append(item)
    
    return common_item

def main():
    list1 = [1,2,3,4,5,6]
    list2 = [5,6,7,8]

    common_items = common_Ele(list1,list2)
    print(f"The Common Elements from the two list is {common_items}")

if __name__ == "__main__":
    main()