'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title: Find the Histogram from the list problem
'''

def histogram(list):
    """ 
    Description :
        This function is used to how many times each integer present in the list
    Parameters :
        list : list of elements
    Return :
        It returns count of each element in the list
    """
    count_l=[]
    
    for i in range(0,len(list)):
        count = 0
        for j in range(i,len(list)):
            if(list[i] == list[j]):
                count += 1
        count_l.append(count)

    print(count_l)

def main():
    list = [1,3,5,3,1,1,8,9,7,8]
    histogram(list)

if __name__ == "__main__":
    main()