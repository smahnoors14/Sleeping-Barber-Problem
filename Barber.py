from threading import Thread, Event, Semaphore
import time, random

semCustomerReady = Semaphore(1)
semWaitingRoom = Semaphore(1)
semBarberChair = Semaphore(1)

customerIntervalMin = 5
customerIntervalMax = 15
haircutDurationMin = 3
haircutDurationMax = 15


class BarberShop():
    Cust = []

    def __init__(self, allfunc, chairsAvailable):
        self.barber = allfunc
        self.chairsAvailable = chairsAvailable
        print('\nShop is Open',end=" ")
        print('\nAvailable Chairs in BarberShop : {0} chair(s)'.format(chairsAvailable))

    def CustomerThread(self, customer):
        semWaitingRoom.acquire()
        print('\n{0} entered the shop and is looking for a chair'.format(customer.name))
        # check the availability of chairs in the waiting room
        if len(self.Cust) == self.chairsAvailable:
            # if full then it invokes balk()
            allFunction.balk()
            semWaitingRoom.release()
        else:
            # if chairs are available then customer sits and wait
            print('{0}: Found an empty chair, I am waiting'.format(customer.name))
            self.Cust.append(c)
            semWaitingRoom.release()
            # customer wakes up the barber
            allfunc.wakeUp()

            semCustomerReady.acquire()  # block the getHairCut() function if value = 0
            allFunction.getHairCut(c)   # customer gets haircut if semaphore = 1
            semCustomerReady.release()


    def BarberThread(self):
        while True:

            if len(self.Cust) > 0:
                c = self.Cust[0]
                del self.Cust[0]

                semBarberChair.acquire()
                self.barber.cutHair(c)
                semBarberChair.release()

            else:
                print('\nBarber: No Customers, I am going to sleep')
                allfunc.sleep()
                print('Barber wakes up!')

class allFunction:
    barberWorkingEvent = Event()

    def getHairCut(customer):
        print('\n{0}: I am ready to get a haircut'.format(customer.name))

    def balk():
        print('\nWaiting room is full, Customer is  leaving.')

    def sleep(self):
        self.barberWorkingEvent.wait()

    def wakeUp(self):
        self.barberWorkingEvent.set()

    def cutHair(self, customer):
        self.barberWorkingEvent.clear()
        print("\nBarber: I am cutting {0}'s hair".format(customer.name))
        randomHairCuttingTime = random.randrange(haircutDurationMin, haircutDurationMax + 1)
        time.sleep(randomHairCuttingTime)
        print("\n{0}'s haircut is done!".format(customer.name))

class CustomerName:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    customers = []
    customers.append(CustomerName('Customer 6'))
    customers.append(CustomerName('Customer 5'))
    customers.append(CustomerName('Customer 4'))
    customers.append(CustomerName('Customer 3'))
    customers.append(CustomerName('Customer 2'))
    customers.append(CustomerName('Customer 1'))

    allfunc = allFunction()

    barberShop = BarberShop(allfunc, chairsAvailable=1)
    Shop = Thread(target=barberShop.BarberThread)
    Shop.start()

    while len(customers) > 0:
        c = customers.pop()
        # New customer enters the barbershop
        WR = Thread(target=barberShop.CustomerThread(c))
        WR.start()
        customerInterval = random.randrange(customerIntervalMin, customerIntervalMax + 1)
        time.sleep(customerInterval)


