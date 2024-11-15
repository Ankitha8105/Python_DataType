'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title: checking file exists or not problem
'''
import os

def file_exists():
    """ 
    Description :
        This function is used to check file exists or not
    Return :
        It returns true if file exists or returns false
    """
    if(os.path.exists("basic.txt")):
        return "Exists"
    else:
        return "Not Exists"
    
def main():
    res = file_exists()
    print(f"The file is {res}")

if __name__ == "__main__":
    main()