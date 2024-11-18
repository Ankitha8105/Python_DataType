'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To Find sorted in increasing order by the last element in each tuple from a given list of non-empty tuples problem
'''
def sort_list(list_ele):
    """ 
    Description :
        This function is used to sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
    Parameters :
        list_ele = List of items
    Return :
        It returns the sorted list in increasing order by the last element in each tuple from a given list of non-empty tuples
    """
    for i in range(0,len(list_ele)):
        for j in range(i+1,len(list_ele)):
            if(list_ele[i][1] > list_ele[j][1]):
                temp = list_ele[i]
                list_ele[i] = list_ele[j]
                list_ele[j] = temp
    return list_ele

def main():
    list_items = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_list = sort_list(list_items)

    print("Sorted List is",end=' ')
    for i in sorted_list:
        print(i)

if __name__ == "__main__":
    main()