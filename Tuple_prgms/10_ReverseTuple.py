'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To reverse a tuple
'''
def reverse_tuple(tuple_ele):
    """ 
    Description :
        This function is used to reverse a tuple
    Parameter :
        tuple_ele = tuple elements
    Return :
        It return reversed tuple
    """
    list_ele = list(tuple_ele)
    list_ele.reverse()
    reversed_tuple = tuple(list_ele)
    return reversed_tuple

def main():
    tuple_items = ("Green","Purpule","White",8,4,2.0)

    res_tuple = reverse_tuple(tuple_items)

    print(f"The Reversed tuple is {res_tuple}")

if __name__ == "__main__":
    main()
