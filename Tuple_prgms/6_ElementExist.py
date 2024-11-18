'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To check whether an element exists within a tuple
'''

def tuple_exist(tuple_items,ele):
    """ 
    Description :
        This function is used to check whether an element exists within a tuple
    Parameter :
        tuple_items = tuple elements
        ele = Element to Search
    Return :
        It return that Element is Exists or not
    """
    flag=False
    if ele in tuple_items:
        flag = True
    if flag:
        return "Exists"
    else:
        return "Not Exists"

def main():
    tuple_ele = ("Apple",7,"Red","black",9.7,"Red",'Black',7,'Green',9.8)
    ele = "Red"
    result = tuple_exist(tuple_ele,ele)
    print(f"The Element {ele} is {result}")

if __name__ == "__main__":
    main()