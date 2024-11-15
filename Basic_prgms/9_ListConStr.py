'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title: Concatenate all elements in list into string  problem
'''
def concat_str(list):
    string = '-'.join(list)
    return string

def main():
    list = ["Apple","orange",'kiwi','graphs']
    string = concat_str(list)
    print(f"{string}")

if __name__ == "__main__":
    main()