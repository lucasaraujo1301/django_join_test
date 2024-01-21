import datetime


def get_expiration_date_default():
    """
    The get_expiration_date_default function returns a datetime.date object that is one day in the future from when
    the function is called. This function will be used as the default value for the expiration_date field of our model.

    :return: A date object that is two days after the current date
    :doc-author: Trelent
    """
    return datetime.date.today() + datetime.timedelta(days=1)
