#Cost Parser
from decimal import Decimal, InvalidOperation

def parse(val):
    """
    Returns decimal value of parsed cost
    """
    try:
        return Decimal(val).quantize(Decimal("0.01")) #Forces Decimal to be a multiple of 0.01 - round. 
    except InvalidOperation:
        raise Exception(f"Invalid Cost: {val}")

