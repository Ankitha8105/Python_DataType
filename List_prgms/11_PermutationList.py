'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To generate all permutations of a list in Python problem
'''
def generate_permu(list_items):
    """ 
    Description :
        This function is used to generate all permutations of a list in Python
    Parameters :
        list_items = List items  
    Return :
        It returns all permutations of a list
    """
    
    for i in range(0,len(list_items)):
        for j in range(i,len(list_items)):
            copy_list = list_items[:]
            temp = copy_list[j]
            copy_list[j] = copy_list[i]
            copy_list[i] = temp

            print(copy_list)

def main():
    list_items = [1,6,7]

    generate_permu(list_items)

if __name__ == "__main__":
    main()