'''
    @Author: Ankitha B L
    @Date:14-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 14- 11-2024
    @Title: To find the repeated items of a tuple
'''

def repeated_ele(tuple_ele):
    """ 
    Description :
        This function is used to find the repeated items of a tuple
    Parameter :
        tuple_ele = tuple elements
    Return :
        It return the repeated items from the tuple
    """
    repeat_ele = []
    for i in range(0,len(tuple_ele)):
        for j in range(i+1,len(tuple_ele)):
            if tuple_ele[i] == tuple_ele[j]:
                repeat_ele.append(tuple_ele[i])
                
    tuple_repeat = tuple(repeat_ele)
    return tuple_repeat

def main():
    tuple_ele = ("Apple",7,"Red","black",9.7,"Red",'Black',7,'Green',9.8)

    result = repeated_ele(tuple_ele)
    print(f"The tuple After Remvoing Duplicates are {result}")

if __name__ == "__main__":
    main()