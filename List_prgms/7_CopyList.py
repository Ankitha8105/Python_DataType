'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To clone or copy a list problem
'''

def copy_list(list_ele):
    """ 
    Description :
        This function is used to clone or copy a list
    Parameters :
        list_ele = List of items
    Return :
        It returns the cloned or copy of a list
    """
    copied_list = list.copy(list_ele)
    return copied_list

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    list_ele = []
    
    if total_val > 0:
        while len(list_ele) < total_val:
            val = int(input("Enter Item to be inserted into list :"))
            list_ele.append(val)
        
        print(f"List Items Before cloning :{list_ele}")

        print()

        res_list = copy_list(list_ele)
        print(f"List Items After cloning :{res_list}")
    else:
        print("Please enter correct number of items to insert")

if __name__ == "__main__":
    main()