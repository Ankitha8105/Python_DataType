'''
    @Author: Ankitha B L
    @Date: 15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15-11-2024
    @Title: To check whether two lists are circularly identical problem
'''

def check_circularly_identical(list1, list2):
    """ 
    Description :
        This function is used to check whether two lists are circularly identical
    Parameters :
        list1 =First List items
        list2 = Second list items  
    Return :
        It returns two lists are circularly identical or not
    """
    
    if len(list1) != len(list2):
        return "Not Identical"
    
   
    double_list = list1 + list1


    if any(double_list[i:i+len(list2)] == list2 for i in range(len(list1))):
        return "Identical"
    else:
        return "Not Identical"
    
def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 1, 2]

    circularly_identical = check_circularly_identical(list1, list2)

    print(f"The two lists are circularly {circularly_identical}")

if __name__ == "__main__":
    main()
