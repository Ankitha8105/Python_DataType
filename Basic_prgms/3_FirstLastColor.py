'''
    @Author: Ankitha B L
    @Date:11 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 11 - 11-2024
    @Title : print the first and last color from the list problem
'''
def print_color(list):
    """ 
    Description :
        This function is used to find the  last color and first color from the list
    Parameters :
        list : list of colors
    Return :
        It returns the  first color and last color from the list
    """
    return list[0],list[-1]

def main():
    color_list = ["Red","Green","White" ,"Black"]

    first_index,last_index = print_color(color_list)

    print(f"The first color is {first_index} and the last color is {last_index}")

if __name__ == "__main__":
    main()