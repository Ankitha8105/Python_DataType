'''
    @Author: Ankitha B L
    @Date:19-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 19- 11-2024
    @Title: Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead problem
'''

def append_str(list_ele):
    """ 
    Description :
        This function is used to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead
    Parameters :
        list_ele = List of Strings
    Return :
        It returns the list of strings after modifying strings
    """
    res_list = []
    for items in list_ele:
        if (len(items) >= 3):
            if 'ing' in items:
                item = items+'ly'
            else:
                item = items+'ing'
        else:
            res_list.append(items)
            continue

        res_list.append(item)
    return res_list

def main():
    list_item = ['abc','bc','string','stand']
    result_list = append_str(list_item)
    print(f"The List after Modifying String {result_list}")

if __name__ == "__main__":
    main()