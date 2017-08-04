'''
Created on Aug 3, 2017

@author: sureshsagiraju
'''

import itertools
from abc import ABCMeta, abstractmethod


class Vehicle(object):
    '''
    class for Vehicle
    '''
    __metaclass__ = ABCMeta
    new_vehicle_id = itertools.count().next

    def __init__(self, vehicle_id=None):
        '''
        constructor
        '''
        if not vehicle_id:
            self._vehicle_id = Vehicle.new_vehicle_id()
        else:
            self._vehicle_id = vehicle_id

    def get_vehicle_id(self):
        '''
        gets the vehicle id
        '''
        return self._vehicle_id

    @abstractmethod
    def can_fit_in_normal_parking_spot(self):
        pass

    @abstractmethod
    def can_fit_in_compact_parking_spot(self):
        pass

    @abstractmethod
    def can_fit_in_large_parking_spot(self):
        pass


class Truck(Vehicle):
    '''
    class for Truck
    '''

    def __init__(self,  *args, **kw):
        '''
        constructor
        '''
        super(Truck, self).__init__(*args, **kw)

    def can_fit_in_normal_parking_spot(self):
        return False

    def can_fit_in_compact_parking_spot(self):
        return False

    def can_fit_in_large_parking_spot(self):
        return True


class MotorCycle(Vehicle):
    '''
    class for MotorCycle
    '''

    def __init__(self,  *args, **kw):
        '''
        constructor
        '''
        super(MotorCycle, self).__init__(*args, **kw)

    def can_fit_in_normal_parking_spot(self):
        return True

    def can_fit_in_compact_parking_spot(self):
        return True

    def can_fit_in_large_parking_spot(self):
        return True


class Car(Vehicle):
    '''
    class for Car
    '''

    def __init__(self,  *args, **kw):
        '''
        constructor
        '''
        super(Car, self).__init__(*args, **kw)

    def can_fit_in_normal_parking_spot(self):
        return True

    def can_fit_in_compact_parking_spot(self):
        return False

    def can_fit_in_large_parking_spot(self):
        return True


if __name__ == '__main__':
    # my quick unit test area
    for x in [Car(), MotorCycle(), Truck()]:
        print x.get_vehicle_id()
        print x.can_fit_in_normal_parking_spot()
        print x.can_fit_in_compact_parking_spot()
        print x.can_fit_in_large_parking_spot()
