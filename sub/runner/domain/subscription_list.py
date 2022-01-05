# sl = SubscriptionList() => empty subscription list
# sl.add(name, options) => add a subscription to the list

from .subscription import Subscription

class SubscriptionList:

    def __init__(self):
        self.subscriptions = []

    def add(self, name, options):
        """
        Records a new subscription in a Subscription() type variable
        """
        self.subscriptions.append(Subscription(name, options))
