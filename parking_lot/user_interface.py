from cmd import Cmd

from parking_lot import ParkingLot
from vehicles import Car

pl = ParkingLot()


class ParkingCLI(Cmd):
    """
    Simple command line simulater of parking lot behvaiour.
    """

    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit

    def do_enter(self, args):
        """Simulates vehicle entering the parking queue"""
        vh = Car()
        pl.enter_parking_lot_queue(vh)

    def do_leave(self, args):
        """A parked vehicle to leave the parking Lot, should enter ticket number"""
        try:
            ticket = raw_input("Enter Ticket No:")
            pl.un_park(int(ticket))
        except KeyError:
            print "Ticket number does not exist"

    def do_show(self, args):
        """To Display the current parking lot status"""

        header = """
        -----------------------------------------------------------------
        *************************PARKING LOT ****************************
        _________________________________________________________________"""

        queue = """                                                          Queue   
                                                           -----         """

        print header
        print queue
        queue_vehicles_str = " " * 60
        queue_v_count, parking_lot_v_count = pl.get_current_occupancy_details()
        for _ in range(queue_v_count):
            queue_vehicles_str += "V "

        print queue_vehicles_str
        print " " * 35 + "_" * 40
        number_slots = pl.get_total_parking_spaces()
        total_revenue = pl.get_total_revenue()
        slot = 1
        i = 0
        while i < number_slots:
            print "------------------------"
            row = ''
            vehicle_row = ''
            ticket_row = ''
            j = 0
            while j < 4 and i < number_slots:
                row += " " + str(slot).zfill(2) + "  |"
                occupied, ticket = self.car_in_slot(slot - 1)
                if occupied:
                    vehicle_row += "  " + str("V") + "  |"
                    ticket_row += " " + str(ticket).zfill(2) + "  |"

                else:
                    vehicle_row += "  " + str(" ") + "  |"
                    ticket_row += "  " + str(" ") + "  |"
                j += 1
                i += 1
                slot += 1
            print row
            print "------------------------"
            print vehicle_row
            print ticket_row
            print "\n" * 2

        print "TOTAL SLOTS: %s OCCUPIED:%s CURRENT QUEUE: %s" % (number_slots, parking_lot_v_count, queue_v_count)
        print "CURRENT TOTAL REVENUE:%s" % (total_revenue)

    def car_in_slot(self, slot_number):
        """
        helper function to find if there is a car in slot
        """
        details = pl.get_current_occupied_spaces()
        for k in details:
            if details[k].is_occupied() and (details[k].get_space_number() == slot_number):
                return (True, k)
        return (False, None)


if __name__ == '__main__':
    prompt = ParkingCLI()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
