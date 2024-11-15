'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title: Create an array of 5 Integer and display the array items problem
'''
import array as my_array

def display_arr():
    """ 
    Description :
        This function is used to create an array of 5 integer  
    Return :
        It returns the elements of an array
    """
    arr = my_array.array('i',[7,1,4,8,3,1])
    for i in range(0,len(arr)):
        print(arr[i],end=' ')

def main():
    display_arr()

if __name__ == "__main__":
    main()