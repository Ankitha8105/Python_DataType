'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To split a list based on first character of word problem
'''

def split_list(list_ele):
    """ 
    Description :
        This function is used to split a list based on first character of word
    Parameters :
        list_ele = First List items
    Return :
        It returns split a list based on first character of word
    """
    result = { }
    for item in list_ele:
        first_char = item[0]
        if first_char not in result:
            result[first_char] = []
            result[first_char].append(item)

    return result

def main():
    list_ele = ['abc','jhg','xyz','acb','xx','ji']
    solution = split_list(list_ele)
    print(f"The list is {solution}")

if __name__ == "__main__":
    main()
        
    