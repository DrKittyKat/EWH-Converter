# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:28:04 2019

@author: Raptor3200
"""
print("HI")
class EWHConverter:
    def __init__(self):
        self.setWorkInfo()
        self.mainLoop()

    def setWorkInfo(self):
        print("Please input your [money] per [hours]")
        self.money = input("Money: ")
        self.hours = input("Hours: ")
    
        print("You earn " + self.money + " dollars for every " + self.hours + "hours.")
    
    def mainLoop(self):
        while True:
            nextStep = input("What do you want to do? \n1 - convert dollars to EWH\n2 - Convert EWH to dollars\n3 - Change work info\n4 - Exit")
            if nextStep == 1:
                self.D2E()
            if nextStep == 2:
                self.E2D()
            if nextStep == 3:
                self.setWorkInfo()
            if nextStep == 4:
                break
    
    def D2E(self):
        print("This costs " + input("Dollars to convert:") / self.money * self.hours + " hours of life.")
        
    def E2D(self):
        print("This costs " + input("EWH to convert:") / self.hours * self.money + " dollars.")