'''
Created on Aug 3, 2017

@author: sureshsagiraju
'''
import itertools
import datetime

from payment_algo import *


class ParkingTicket(object):
    '''
    class for parking ticket 
    '''
    new_ticket_number = itertools.count().next

    def __init__(self, vehicle_number, parking_space, hours_of_parking):
        '''
        constructor
        '''
        self._vehicle_number = vehicle_number
        self._parking_space = parking_space
        self._hours_of_parking = hours_of_parking
        self._arrival_time = datetime.datetime.now()
        self._ticket_number = ParkingTicket.new_ticket_number()

    def get_ticket_number(self):
        '''
        returns  parking ticket number
        '''
        return self._ticket_number

    def get_arrival_time(self):
        '''
        returns arrival time of vehicle
        '''
        return self._arrival_time

    def get_hours_of_parking(self):
        '''
        returns the number of hours the ticket is bought for
        '''
        return self._hours_of_parking


class ParkingTicketer(object):
    '''
    class for parking ticketer
    '''

    def __init__(self,):
        '''
        constructor
        '''
        self._tickets = {}
        self._total_revenue = 0

    def get_ticket(self, vehicle_number, parking_space, hours_of_parking):
        '''
        creates a ticket and calculates payment and gemerates ticker number
        '''
        ticket_object = ParkingTicket(
            vehicle_number, parking_space, hours_of_parking)
        ticket_number = ticket_object.get_ticket_number()
        weekno = datetime.datetime.today().weekday()
        if weekno < 5:
            bill = PaymentAlgorithm(
                weekday_rates).calculate_payment(hours_of_parking)
        else:
            bill = PaymentAlgorithm(
                weekend_rates).calculate_payment(hours_of_parking)
        self._total_revenue += bill
        self._tickets[ticket_number] = ticket_object
        return ticket_number

    def park_exit_overstay_check(self, ticket_number):
        '''
        checks for overstay penality during exit
        '''
        ticket_object = self._tickets[ticket_number]
        arrival_time = ticket_object.get_arrival_time()
        current_time = datetime.datetime.now()
        diff = current_time - arrival_time
        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        if hours > ticket_object.get_hours_of_parking():
            penality_hours = ticket_object.get_hours_of_parking() - hours
            bill = PaymentAlgorithm(
                overstay_penality).calculate_payment(penality_hours)
            self._total_revenue += bill

    def get_total_revenue(self):
        '''
        returns the total revenue
        '''
        return self._total_revenue


if __name__ == '__main__':
    # my quick unit test area
    pass
