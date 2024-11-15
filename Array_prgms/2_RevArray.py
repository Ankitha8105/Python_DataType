'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title:Reverse the Elements or items in an Array problem
'''
import array

def rev_array(arr_ele):
    """ 
    Description :
        This function is used to Reverse the Array Elements
    Parameters :
        arr_ele = Array Elements
    Return :
            It returns the Reversed Array elements
    """
    print("Elements Before Reverse",end = ' ')
    for i in range(0,len(arr_ele)):
        print(arr_ele[i],end=' ')
    
    print()

    print("Elements after Reverse" , end = " ")
    arr_ele.reverse()
    for i in range(0,len(arr_ele)):
        print(arr_ele[i],end=' ')
    
def main():
    arr = array.array('i',[8,7,4,6,3,1,2,0])
    rev_array(arr)

if __name__ == "__main__":
    main()
