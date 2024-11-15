'''
    @Author: Ankitha B L
    @Date:11 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 11 - 11-2024
    @Title : print numbers in from of list and tuples problem
'''
def generate_list(num):
    """ 
    Description :
        This function is used to print numbers in from of list and tuples
    Parameters :
        num:user entered numbers
    Return :
            It returns the numbers in the from of list and tuple
    """
    list_num = num.split(',')
    tuple_num = tuple(list_num)
    return list_num,tuple_num

def main():
    number = input("Enter Numbers :")
    num_list , num_tuple = generate_list(number)
    print(f"The number in list from {num_list}")
    print(f"The numbers in tuple from {num_tuple}")

if __name__ == "__main__":
    main()