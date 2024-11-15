'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title : Find the given value present in the list or not problem
'''
def con_val(val,list):
    """ 
    Description :
        This function is used to find the given element present in the list
    Parameters :
        val : value to find
        list : list of elements
    Return :
        It returns Val is present in the list or not
    """
    return val in list

def main():
    val = int(input("Enter the value to find :"))
    list = [1,5,8,3]

    value = con_val(val,list)
    if value:
        print(f"{val} is present in the {list}")
    else:
        print(f"{val} is not present in the {list}")

if __name__ == "__main__":
    main()