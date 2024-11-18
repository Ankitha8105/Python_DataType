'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To print a specified list after removing the 0th, 4th and5th elements problem
'''
def remove_ele(list_items):
    """ 
    Description :
        This function is used to print a specified list after removing the 0th, 4th and5th elements
    Parameters :
        list_items = List items  
    Return :
        It returns specified list after removing the 0th, 4th and 5th elements
    """
    list_items.pop(0)
    list_items.pop(3)
    list_items.pop(3)
    return list_items

def main():
    list_ele = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

    removed_list = remove_ele(list_ele)

    print(f"List Elements After removing elements at specified index :{removed_list}")

if __name__ == "__main__":
    main()