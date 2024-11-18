'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To slice a tuple
'''
def tuple_slice(tuple_ele):
    """ 
    Description :
        This function is used to slice a tuple
    Parameter :
        tuple_ele = tuple elements
    Return :
        It return sliced tuple 
    """
    sliced_tuple = tuple_ele[4:5] + tuple_ele[5:8]
    return sliced_tuple

def main():
    tuple_ele = ("Hello","I","am","Nothing","You","Are","Also","Nothing")

    result_tuple = tuple_slice(tuple_ele)
    print(f"The Sliced tuple elements are {result_tuple}")

if __name__ == "__main__":
    main()