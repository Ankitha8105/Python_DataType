'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To remove duplicates from a list problem
'''
def remove_duplicates(list_ele):
    """ 
    Description :
        This function is used to remove duplicates from a list
    Parameters :
        list_ele = List of items
    Return :
        It returns the items after removing duplicates
    """
    list_set = set(list_ele)
    return list_set

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    list_ele = []
    
    if total_val > 0:
        while len(list_ele) < total_val:
            val = int(input("Enter Item to be inserted into list :"))
            list_ele.append(val)

        set_ele = remove_duplicates(list_ele)
        list_ele = list(set_ele)
        print(f"List After removing duplicates items :{list_ele}")


    else:
        print("Please Enter correct number of elements to insert")

if __name__ == "__main__":
    main()    