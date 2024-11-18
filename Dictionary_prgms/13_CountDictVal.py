'''
    @Author: Ankitha B L
    @Date: 18-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18-11-2024
    @Title: To Count the total number of items in dictionary values that are lists problem
'''
def count_items_in_list_values(dictionary):
    """
    Description:
        Count the total number of items in dictionary values that are lists.
    Parameters:
        dictionary : The dictionary to check.
    Returns:
        int: The total count of items in list-type values.
    """
    return sum(len(value) for value in dictionary.values() if isinstance(value, list))


def main():
    my_dict = {
        'a': [1, 2, 3],
        'b': 'hello',
        'c': [4, 5],
        'd': 100
    }

    result = count_items_in_list_values(my_dict)
    print("Total number of items in list values:", result)

if __name__ == "__main__":
    main()