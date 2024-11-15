'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title: To Access the environment variables problem
'''
import os

def acess_variable():
    """ 
    Description :
        This function is used to key value pair of all the environemnt variables
    Return :
        It returns the list of key value pair of all the environemnt variables
    """
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def main():
    acess_variable()

if __name__ == "__main__":
    main()
    