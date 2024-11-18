'''
    @Author: Ankitha B L
    @Date:18 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 18- 11-2024
    @Title: To print all unique values in a dictionary problem
'''
def distinct_dic(dict_ele):
    """ 
    Description :
        This function is used to print all unique values in a dictionary
    Parameter :
        dict_ele : Dictionary elements
    Return :
        It return all unique values in a dictionary
    """
    unique_val = set() 
    for dic in dict_ele:
        for key, value in dic.items():
            unique_val.add(value)  
    return unique_val

def main():
    dic = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
           {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    res_dic = distinct_dic(dic)
    print(f"Unique Values: {res_dic}")

if __name__ == "__main__":
    main()
