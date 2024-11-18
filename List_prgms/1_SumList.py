'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title: Sum all the items in the list problem
'''

def sum_list(list_ele):
    """ 
    Description :
        This function is used to add all the items in the list
    Parameters :
        list_ele = List of items
    Return :
        It returns the sum all the items from the list
    """
    sum = 0
    for i in list_ele:
        sum += i
    return sum

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    list_ele = []
    
    if total_val >= 0:
        while len(list_ele) < total_val:
            val = int(input("Enter Item to be inserted into list :"))
            list_ele.append(val)
    
        items_sum = sum_list(list_ele)
        print(f"The Sum of items in the list are {items_sum}")
    else:
        print("Please Enter Correct value")

if __name__ == "__main__":
    main()