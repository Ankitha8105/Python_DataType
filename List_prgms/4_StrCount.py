'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title:count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings problem
'''

def str_count(list_ele):
    """ 
    Description :
        This function is used to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
    Parameters :
        list_ele = List of items
    Return :
        It returns the count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
    """
    count = 0
    for i in list_ele:
        if(len(i)>=2):
            if(i[0] == i[-1]):
                count += 1
    return count

def main():
    total_val = int(input("Enter the Number of Elements to Store in the List :"))
    list_ele = []
    
    if total_val > 0:
        while len(list_ele) < total_val:
            val = input("Enter Item to be inserted into list :")
            list_ele.append(val)
        
        num_str = str_count(list_ele)
        print(f"The Number of String present with first and last character same is {num_str}")

    else:
        print("Enter Correct Number of Items to be inserted")

if __name__ == "__main__":
    main()
    