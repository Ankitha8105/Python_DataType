'''
    @Author: Ankitha B L
    @Date: 18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18-11-2024
    @Title: To Check if all keys exist in the given dictionary problem
'''
def check_keys_exist(dictionary, keys):
    """
    Description:
        Check if all keys exist in the given dictionary.
    Parameters:
        dictionary : The dictionary to check.
        keys       : List of keys to check for.
    Returns:
        bool: True if all keys exist, False otherwise.
    """
    return all(key in dictionary for key in keys)

def main():
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    keys_to_check = ['a', 'b']
    print(check_keys_exist(my_dict, keys_to_check)) 

    keys_to_check = ['a', 'd']
    print(check_keys_exist(my_dict, keys_to_check))  

if __name__ == "__main__":
    main()