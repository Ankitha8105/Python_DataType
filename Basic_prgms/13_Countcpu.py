'''
    @Author: Ankitha B L
    @Date:13-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 13- 11-2024
    @Title: Count the number of cpu's using problem
'''
import os

def count_cpu():
    """ 
    Description :
        This function is used count the number of cpu's using
    Return :
        It returns the number of cpu's using
  """
    num = os.cpu_count()
    return num

def main():
    count = count_cpu()
    print(f"The number of cpu's using are {count}")

if __name__ == "__main__":
    main()