'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To create a tuple problem
'''
def create_tuple():
    """ 
    Description :
        This function is used to create a tuple
    Return :
        It return the tuple
    """
    tuple = (0,3,6,1,5,8)
    return tuple

def main():
    tuple_items = create_tuple()
    print(f"The Elements in the tuple are :{tuple_items}")

if __name__ == "__main__":
    main()