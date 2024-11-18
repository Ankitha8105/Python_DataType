'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To find the list of words that are longer than n from a given list of words problem
'''

def longer_ele(list_items,n):
    """ 
    Description :
        This function is used to  find the list of words that are longer than n from a given list of words
    Parameters :
        list_items = List of items
        n = Length of string
    Return :
        It returns the list of words that are longer than n from a given list of words
    """
    for item in list_items:
        if (len(item) >= n):
            print(item,end=',')

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    n = int(input("Enter What length elements to display :"))
    list_ele = []
    
    if total_val > 0 and n > 0:
        while len(list_ele) < total_val:
            val = input("Enter Item to be inserted into list :")
            list_ele.append(val)

        longer_ele(list_ele,n)
    
    else:
        print("Please enter correct number")

if __name__ == "__main__":
    main()