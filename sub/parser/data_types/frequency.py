from dateutil.relativedelta import relativedelta

UNITS = {
    'd': 'days',
    'm': 'months',
    'y': 'years'
}

#Frequency Parser
def parse(val):
    #val = 'm'
    #val = '3y'
    #val = '12d'

    [*factor, unit] = val
    factor = ''.join(factor)
    parsed_factor =  parse_factor(factor) #12
    parsed_unit = parse_unit(unit) #d
    return relativedelta(**{parsed_unit:parsed_factor})
    
#Helper functions

def parse_factor(val):

    if len(val) == 0: return 1 #Multiply by 1 if val is empty.

    try:
        return int(val)
    except:
        raise Exception(f"Invalid factor: '{val}' - not a number.")


def parse_unit(val):
    if val in UNITS:
        return UNITS[val]
    else:
        raise Exception("Invalid unit.\nValid Units: 'd', 'm', 'y'.")