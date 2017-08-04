'''
Created on Aug 3, 2017

@author: sureshsagiraju
'''

import types


class PaymentAlgorithm(object):
    '''
    Class to calculate payments based of various strategies
    '''

    def __init__(self, func=None):
        '''
        constructor
        '''
        if func:
            self.calculate_payment = types.MethodType(func, self)

    def calculate_payment(self, hours):
        '''
        default calcualtion, flat rate per hour
        '''
        return hours * 5


def weekend_rates(self, hours):
    '''
    calculation based on weekend rates
    '''
    if hours < 2:
        return 10
    elif hours >= 2 and hours < 6:
        return 20
    elif hours >= 6 and hours < 12:
        return 30
    elif hours >= 12:
        return 40


def weekday_rates(self, hours):
    '''
    calculation based on weekday rates
    '''
    if hours < 2:
        return 5
    elif hours >= 2 and hours < 6:
        return 10
    elif hours >= 6 and hours < 12:
        return 15
    elif hours >= 12:
        return 20


def overstay_penality(self, hours):
    '''
    calcualtion for overstayed hours
    '''
    return hours * 10


if __name__ == '__main__':
    # my quick unit test area
    print PaymentAlgorithm().calculate_payment(10)
    print PaymentAlgorithm(weekday_rates).calculate_payment(12)
    print PaymentAlgorithm(weekend_rates).calculate_payment(12)
