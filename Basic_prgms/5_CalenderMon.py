'''
    @Author: Ankitha B L
    @Date:11 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 11 - 11-2024
    @Title : print Calnder month problem
'''
import calendar

def cal_mon(yy,mm):
    """ 
    Description :
        This function is used to display month of the calender
    Parameters :
        yy : year
        mm : month
    Return :
        It returns the  months calender
    """
    print(calendar.month(yy,mm))

def main():
    yy = int(input("Enter the year :"))
    mm = int(input("Enter the month :"))
    cal_mon(yy,mm)

if __name__ == "__main__":
    main()