'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title: To print the all the files in the directory problem
'''
import os

def list_files():
    """ 
    Description :
        This function is used to list all the files in the directory
    Return :
        It returns the list of files in the current directory
  """
    dir = os.getcwd()
    files = os.listdir(dir)
    return files

def main():
    dir_files = list_files()
    print(f"The files in the directory are {dir_files}")

if __name__ == "__main__":
    main()
