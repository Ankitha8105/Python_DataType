'''
    @Author: Ankitha B L
    @Date:11 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 11 - 11-2024
    @Title : Reverse last name and first name problem
'''
def reverse_input(first_name,last_name):
    """ 
    Description :
        This function is used to find the reverse last name and first name
    Parameters :
        first_name = user entered First_Name
        last_name = user entered Last_Name
    Return :
            It returns the reverse of first_name and last_name
    """
    return last_name,first_name

def main():
    first_name = input("Enter the First number :")
    last_name = input("Enter the Last number :")

    lastN,firstN = reverse_input(first_name,last_name)

    print(f" The Last Name is {last_name} , First Name is {first_name}")

if __name__ == "__main__":
    main()
