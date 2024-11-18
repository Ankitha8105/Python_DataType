'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title: To Multiply all the items in the list problem
'''

def mul_list(list_ele):
    """ 
    Description :
        This function is used to multiplies all the items in a list.
    Parameters :
        list_ele = List of items
    Return :
        It returns the multiplication of all the items from the list
    """
    prd = 1
    for i in list_ele:
        prd *= i
    return prd

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    list_ele = []
    
    if total_val > 0:
        while len(list_ele) < total_val:
            val = int(input("Enter Item to be inserted into list :"))
            list_ele.append(val)
    
        items_mul = mul_list(list_ele)
        print(f"The multiplication of items in the list are {items_mul}")
    else:
        print("Please Enter correct number")

if __name__ == "__main__":
    main()