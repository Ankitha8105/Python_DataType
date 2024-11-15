'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title: running external command in python file problem
'''
import subprocess

def run_command():
  """ 
    Description :
        This function is used to run the external command in python
    Return :
        It returns the list of files in the current directory
  """
  result = subprocess.run('dir',shell= True, capture_output=True, text=True)
  print(result.stdout)

if __name__ == "__main__": 
  run_command()
    