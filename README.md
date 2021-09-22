# Sleeping-Barber-Problem
Sleeping Barber Problem for inter-process communication and synchronization among multiple OS processes with semaphores.
Problem Statement
A barbershop consists of a waiting room with n chairs, and the barber room containing the barber chair. If there are no customers to be served, the barber goes to sleep. If a customer enters the barbershop and all chairs are occupied, then the customer leaves the shop. If the barber is busy, but chairs are available, then the customer sits in one of the free chairs. If the barber is asleep, the customer wakes up the barber. Write a program to coordinate the barber and the customers.
To make the problem a little more concrete, the following information is added:
• Customer threads should invoke a function named getHairCut.
• If a customer thread arrives when the shop is full, it can invoke balk, which does not return.
• Barber threads should invoke cutHair.
• When the barber invokes cutHair, there should be exactly one thread invoking getHairCut concurrently.

Semaphores:
semCustomerReady: This semaphores ensures that cutHair function can only be invoked on customers that are ready to get their hair cut done, such that only one customer can invoke getHairCut at a particular time.
semWaitingRoom: This semaphore allows only limited customers to enter the waiting room.
semBarberChair: This semaphore ensures mutual exclusion on barber such that only one customer approaches the barber chair for hair cut at a particular time.

Functions:
Class BarberShop includes
1. CustomerThread()
2. BarberThread()
Class allFunction includes
1. cutHair()
2. getHairCut()
3. balk()
4. sleep()
5. wakeUp()
