'''
    @Author: Ankitha B L
    @Date: 18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18-11-2024
    @Title: To count dictionaries with 'success' as True
'''

def count_val(list_ele):
    """ 
    Description :
        This function is used to count dictionaries with 'success' as True
    Parameter :
        list_ele : List Elements
    Return :
        It return a count dictionaries with 'success' as True
    """
    count = 0
    for ele in list_ele:
        if ele.get('success') == True:  
            count += 1  
    return count

def main():
    dict_items = [{'id': 1, 'success': True, 'name': 'Lary'}, 
                  {'id': 2, 'success': False, 'name': 'Rabi'}, 
                  {'id': 3, 'success': True, 'name': 'Alex'}]  
    res_count = count_val(dict_items)  
    print(f"{res_count} dictionaries have 'success' as True")

if __name__ == "__main__":
    main()
