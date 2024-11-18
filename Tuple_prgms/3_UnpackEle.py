'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To unpack a tuple in several variables problem
'''

def unpack_tuple(tuple_ele):
    """ 
    Description :
        This function is used to unpack a tuple in several variables
    Parameter :
        tuple_ele = tuple elements
    Return :
        It return the unpacked tuple variables
    """
    x,y,z = tuple_ele
    return x,y,z

def main():
    tuple_ele = ("Red","Green","Yellow")
    a,b,c = unpack_tuple(tuple_ele)
    print(f"The items in the tuple are :{a},{b},{c}")

if __name__ == "__main__":
    main()