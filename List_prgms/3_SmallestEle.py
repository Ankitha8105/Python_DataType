'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified Atime: 13- 11-2024
    @Title: To Find the smallest item from the list problem
'''

def smallest_item(list_ele):
    """ 
    Description :
        This function is used to Find the smallest item from the list
    Parameters :
        list_ele = List of items
    Return :
        It returns the Find the smallest item from the list
    """
    small = list_ele[0]
    for i in list_ele:
        if i < small:
            small = i
    return small

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    list_ele = []
    
    if total_val > 0:
        while len(list_ele) < total_val:
            val = int(input("Enter Item to be inserted into list :"))
            list_ele.append(val)
    
        smallest = smallest_item(list_ele)
        print(f"The smallest items in the list is {smallest}")
    else:
        print("Please Enter correct number")

if __name__ == "__main__":
    main()