from datetime import timedelta, date


def updateEndDate(end_date):
        """This function checks if the end date is on the Sunday or Monday
        and if it does, changes it to the date of the previous Saturday

        Parameters
        ----------
        end_date : Object of type - datetime.date
                   This is the date to check and update if needed.
        """

        if (isSunday(end_date)):
            end_date = end_date - timedelta(days=1)
        
        if (isMonday(end_date)):
            end_date = end_date - timedelta(days=2)

        return (end_date)


def isDateValid(end_date):
        """This function checks if the date that was given as the end date
        is a valid one, for example, it can not be a future date.

        Parameters
        ----------
        end_date : Object of type - datetime.date
                   This is the date to check if valid or not.
        """
        today = date.today()

        if (today < end_date):
            print("Stock.py -> __isDateValid() -> end_date not valid: future date")
            return (False)
        
        return (True)


def isSunday(date_to_check):
    """This function checks if the given date falls
    on Sunday
    
    Parameters
    ----------
    date_to_check : Object of type - datetime.date
                    The date to check if on Sunday
    0 => Monday
    1 => Tuesday
    2 => Wednesday
    3 => Thursday
    4 => Friday
    5 => Saturday
    6 => Sunday
    """
    weekday_num = date_to_check.weekday()

    if weekday_num == 6:
        return (True)
    
    return (False)


def isMonday(date_to_check):
    """This function checks if the given date falls
    on Monday
    
    Parameters
    ----------
    date_to_check : Object of type - datetime.date
                    The date to check if on Monday
    0 => Monday
    1 => Tuesday
    2 => Wednesday
    3 => Thursday
    4 => Friday
    5 => Saturday
    6 => Sunday
    """
    weekday_num = date_to_check.weekday()

    if weekday_num == 0:
        return (True)
    
    return (False)
