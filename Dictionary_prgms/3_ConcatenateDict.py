'''
    @Author: Ankitha B L
    @Date:15-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 15- 11-2024
    @Title: To concatenate following dictionaries to create a new one problem
'''

def concatenate_dict(dic1,dic2,dic3):
    """ 
    Description :
        This function is used to concatenate following dictionaries to create a new one
    Parameter :
        dic1 : First Dictionary elements
        dic2 : Second Dictionary elements
        dic3 : Third Dictionary elements
    Return :
        It return reversed tuple
    """
    new_dict = { }
    items1 = dic1.items()
    items2 = dic2.items()
    items3 = dic3.items()
    new_dict.update(items1)
    new_dict.update(items2)
    new_dict.update(items3)
    
    print(new_dict)
        
def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    concatenate_dict(dic1,dic2,dic3)

if __name__ == "__main__":
    main()