'''
    @Author: Ankitha B L
    @Date:18 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18- 11-2024
    @Title: To print a dictionary in table format problem
'''

def dict_to_table(dict_ele):
    """ 
    Description :
        This function is used to print a dictionary in table format
    Parameter :
        dict_ele : Dictionary Elements
    Return :
        It return a dictionary in table format
    """
    print(f"{'Key':<15} {'Value':<15}")
    print(f"-*30")

    for key,values in dict_ele.items():
        print(f"{key:<15} {values:<15}")

def main():
    dic = {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
    dict_to_table(dic)

if __name__ == "__main__":
    main()