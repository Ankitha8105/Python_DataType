'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to takes a list of words and returns the length of the longest one problem
'''

def longest_len_word(list_ele):
    """ 
    Description :
        This function is used to takes a list of words and returns the length of the longest one
    Parameters :
        list_ele = String list elements
    Return :
        It returns the length of a longest word 
    """
    longest = len(list_ele[0])
    for item in list_ele:
        if(len(item) >= longest):
            longest = len(item)
    return longest

def main():
    list_ele = ['Heyy','are','You Working','WithOrWithout','Programming','Language']
    longest_word = longest_len_word(list_ele)
    print(f"The longest word length is {longest_word} ")

if __name__ == "__main__":
    main()