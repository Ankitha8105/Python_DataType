'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To create the colon of a tuple
'''

def tuple_clone(tuple):
    """ 
    Description :
        This function is used to create the colon of a tuple
    Parameter :
        tuple = tuple elements
    Return :
        It return the coloned tuple
    """
    cloned_tuple = tuple[ : ]
    return cloned_tuple

def main():
    tuple_ele = ("Apple","Red","Graps",'Black','Green',8,7)

    cloned_ele = tuple_clone(tuple_ele)
    print(f"The Cloned elemwnts are {cloned_ele}")

if __name__ == "__main__":
    main() 