'''
Created on Aug 3, 2017

@author: sureshsagiraju
'''
from random import randint

from parking_space import NormalParkingSpace, CompactParkingSpace, LargeParkingSpace
from ticketing import ParkingTicketer
from vehicles import Car, MotorCycle

# Current problem have only normal parking spcaes since we have queue
# and we cannot skip queue as per problem statement, but can be expanded
# to other slots
NUMBER_OF_NORMAL_PARKING_SPACES = 16
NUMBER_OF_COMPACT_PARKING_SPACES = 0
NUMBER_OF_LARGE_PARKING_SPACES = 0
MAX_VEHICLES_IN_QUEUE = 4


class ParkingLot(object):
    '''
    class for parking lot.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._normal_parking_spaces = []
        self._compact_parking_spaces = []
        self._large_parking_spaces = []
        self.__create_spaces()
        self._parking_queue = ParkingQueue()
        self._occupied_spaces = {}
        self._ticketing = ParkingTicketer()

    def __create_spaces(self):
        '''
        Method creates parking spaces objects
        '''
        for _ in xrange(NUMBER_OF_NORMAL_PARKING_SPACES):
            self._normal_parking_spaces.append(NormalParkingSpace())
        for _ in xrange(NUMBER_OF_COMPACT_PARKING_SPACES):
            self._compact_parking_spaces.append(CompactParkingSpace())
        for _ in xrange(NUMBER_OF_LARGE_PARKING_SPACES):
            self._large_parking_spaces.append(LargeParkingSpace())

    def _get_first_empty_space(self, parking_spaces):
        '''
        Method looks for the empty slots and returns the first availabe space.
        '''
        for space in parking_spaces:
            if not space.is_occupied():
                return space
        return None

    def _park(self, vehicle, hours_of_parking):
        '''
        checks if the vehicle fits the available parking spaces
        gets a ticket
        parks the vehicle 
        This cannot be called directly since the vehicle we first enter queue.
        '''
        if vehicle.can_fit_in_normal_parking_spot():
            available_space = self._get_first_empty_space(
                self._normal_parking_spaces)
        ticket_number = self._ticketing.get_ticket(
            vehicle.get_vehicle_id(), available_space, hours_of_parking)
        self._occupied_spaces[ticket_number] = available_space
        available_space.park()

    def un_park(self, ticket_number):
        '''
        This method unparks the vehicle
        looks for any overstay penality
        looks if there are any vehicles waiting in queue and parks them 
        '''
        self._ticketing.park_exit_overstay_check(ticket_number)
        # remove form map and unmark parking space
        self._occupied_spaces[ticket_number].un_park()
        del self._occupied_spaces[ticket_number]
        # check if we have any vehicle in Queue and park it if any
        if not self._parking_queue.is_queue_empty():
            vehicle = self._parking_queue.get_next_vehicle()
            # For simplicity we are getting rnadom time between 1 tp 24 hours
            # for parking
            self._park(vehicle, randint(1, 24))

    def enter_parking_lot_queue(self, vehicle):
        '''
        This method checks if queue is full and can fit the type of vehicle
        If queue is empty and parking slots are available parks
        If parking lot is full, adds vehicle to the queue
        '''
        if self._parking_queue.is_queue_full():
            print "parking queue and lot is full cannot enter"
            return False
        if not vehicle.can_fit_in_normal_parking_spot():
            print "Cannot park this kind of vehicle in parking this lot"
            return False
        if self._parking_queue.is_queue_empty() and self._get_first_empty_space(
                self._normal_parking_spaces):
            # For simplicity we are getting rnadom time between 1 tp 24 hours
            # for parking
            self._park(vehicle, randint(1, 24))
        else:
            self._parking_queue.add_vehicle_to_queue(vehicle)
        return True

    def get_current_occupancy_details(self):
        '''
        returns number of vehicles in queue and in parking spaces
        '''
        return (self._parking_queue.get_current_number_of_vehicles_inqueue(), len(self.get_current_occupied_spaces()))

    def get_current_occupied_spaces(self):
        '''
        returns occupied spaces dictionary
        '''
        return self._occupied_spaces

    def get_total_parking_spaces(self):
        '''
        returns total number of parking spaces in the lot
        '''
        return NUMBER_OF_NORMAL_PARKING_SPACES + NUMBER_OF_COMPACT_PARKING_SPACES + NUMBER_OF_LARGE_PARKING_SPACES

    def get_total_revenue(self):
        '''
        returns current total revenue of the parking lot
        '''
        return self._ticketing.get_total_revenue()


class ParkingQueue(object):
    '''
    class for parking queue
    '''

    def __init__(self):
        '''
        constructor
        '''
        self._vehicles = []

    def get_next_vehicle(self):
        '''
        returns the next vehicle in the parking queue to be parked
        '''
        return self._vehicles.pop()

    def is_queue_empty(self):
        '''
        checks if the parking lot is empty
        '''
        return len(self._vehicles) == 0

    def add_vehicle_to_queue(self, vehicle):
        '''
        adds the vehicle to the queue
        '''
        self._vehicles.insert(0, vehicle)

    def is_queue_full(self):
        '''
        checks if the queue is full
        '''
        return len(self._vehicles) == MAX_VEHICLES_IN_QUEUE

    def get_current_number_of_vehicles_inqueue(self):
        return len(self._vehicles)


if __name__ == '__main__':
    # my quick unit test area
    lot = ParkingLot()
    for v in [Car(), MotorCycle(), MotorCycle(), Car(), MotorCycle(), Car(), MotorCycle(), Car(), MotorCycle(), Car()]:
        if lot.enter_parking_lot_queue(v):
            print "entered lot"
        else:
            print "did not enter"
    print lot.get_current_occupancy_details()
    lot.un_park(0)
    lot.un_park(1)
    lot.un_park(2)
    for v in [Car(), MotorCycle(), MotorCycle(), Car(), MotorCycle(), Car(), MotorCycle(), Car(), MotorCycle(), Car()]:
        if lot.enter_parking_lot_queue(v):
            print "entered lot"
        else:
            print "did not enter"
    print lot._occupied_spaces
    print lot._ticketing._tickets
    print lot.get_current_occupancy_details()
