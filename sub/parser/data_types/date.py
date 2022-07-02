import dateparser
from analyzer import analyze

#

def parse(val_start, val_end):

    """
    Parses the date given by the user. Courtesy of the dateparser module.
    """


    # date when the subscription started
    starts_on = dateparser.parse('today').date() if val_start is None else dateparser.parse(val_start).date()

    # expiration date
    ends_on = None if val_end is None else dateparser.parse(val_end).date()



    return starts_on, ends_on