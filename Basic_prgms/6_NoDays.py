'''
    @Author: Ankitha B L
    @Date:12-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12- 11-2024
    @Title : print the number of days between Two dates problem
'''
from datetime import date

def no_days(date_1,date_2):
    """ 
    Description :
        This function is used to calculate the number of days between two days
    Parameters :
        date_1 : user entered first date
        date_2 : user entered second date
    Return :
        It returns the number of days between two dates
    """
    if(date_2>date_1):
        return (date_2 - date_1).days
    else:
        return(date_1 - date_2).days

def main():
    date1 = date(2024, 11, 10)
    date2 = date(2024, 11, 12)
    days = no_days(date1,date2)

    print(f"The number of days between {date1} and {date2} is {days}")

if __name__ == "__main__":
    main()