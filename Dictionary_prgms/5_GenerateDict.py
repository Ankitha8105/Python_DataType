'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x) problem
'''

def generate_dict(x):
    """ 
    Description :
        This function is used to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
    Parameter :
        x : Number of Dictionary elements
    Return :
        It return dictionary in the from of (x, x*x)
    """
    dict_ele = { }
    for i in range(1,x+1):
        dict_ele[i] = i*i
    return dict_ele
    dict
def main():
    n = int(input("Enter Number of Elements to generate dictionary :"))
    ele_dict = generate_dict(n)
    print(f"The Dictionary elemens are {ele_dict}")

if __name__ == "__main__":
    main()
