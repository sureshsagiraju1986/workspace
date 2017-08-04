'''
Created on Aug 3, 2017

@author: sureshsagiraju
'''
from abc import ABCMeta
import itertools


class ParkingSpace(object):
    '''
    class for parking space
    '''
    __metaclass__ = ABCMeta
    new_space_number = itertools.count().next

    def __init__(self):
        '''
        constructor
        '''
        self._number = ParkingSpace.new_space_number()
        self._is_occupied = False

    def park(self):
        '''
        sets the variable indicating parked
        '''
        self._is_occupied = True

    def un_park(self):
        '''
        unsets variable indicating unparked
        '''
        self._is_occupied = False

    def is_occupied(self):
        '''
        returns the occupied status of the parking space
        '''
        return self._is_occupied

    def get_space_number(self):
        '''
        returns the parking space number
        '''
        return self._number


class NormalParkingSpace(ParkingSpace):

    def __init__(self,  *args, **kw):
        '''
        constructor
        '''
        super(NormalParkingSpace, self).__init__(*args, **kw)


class CompactParkingSpace(ParkingSpace):

    def __init__(self,  *args, **kw):
        '''
        constructor
        '''
        super(CompactParkingSpace, self).__init__(*args, **kw)


class LargeParkingSpace(ParkingSpace):

    def __init__(self,  *args, **kw):
        '''
        constructor
        '''
        super(LargeParkingSpace, self).__init__(*args, **kw)


if __name__ == '__main__':
    # my quick unit test area
    for x in [NormalParkingSpace(), NormalParkingSpace(), CompactParkingSpace(), LargeParkingSpace()]:
        print x
        print x.get_space_number()
        print x.is_occupied()
