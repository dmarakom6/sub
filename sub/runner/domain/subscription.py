# s = Subscription("netflix.com", {'cost': Decimal("13.00"), 'frequency':relativedelta(months=1)})

from datetime import date

class Subscription:
    
    def __init__(self, name, options):
        self.name = name

        self.cost = options['cost']
        self.frequency = options['frequency']
        self.starts_on = options.get('starts_on', date.today()) #in case starts_on doesn't exist, return today's date
        self.ends_on = options.get('ends_on', None) #in case ends_on doesn't exist


    def __str__(self):
        ends_on = "" if self.ends_on is None else self.ends_on
        active = '●' if self.is_active() else '○'
        return f"{active} {self.name}   {self.cost} / {self.frequency}   {self.starts_on} - {ends_on}"
        # TODO: format frequency, align columns (str.ljust, str.rjust)

    def __repr__(self):
        return self.__str__()


    def is_active(self):
        return self.starts_on <= date.today() and (self.ends_on is None or self.ends_on > date.today())

    def cancel(self, ends_on=None):
        """
        Sets subscription end date or updates it.
        """

        self.ends_on = date.today() if ends_on is None else ends_on        
    


        
