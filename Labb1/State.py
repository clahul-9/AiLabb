from Labb1 import Enum
class State:
    def Enter(self, agent):
        pass
    def Execute(self, agent):
        pass
    def Exit(self, agent):
        pass

class State1(State):
    def Enter(self, agent):
        print("entering State 1")

    def Execute(self, agent):
        print("executeing State 1")

    def Exit(self, agent):
        print("Exiting State 1")

class State2(State):
    def Enter(self, agent):
        print("entering State 2")

    def Execute(self, agent):
        print("executeing State 2")

    def Exit(self, agent):
        print("Exiting State 2")

class gotoBarAndDrink(State):
    def Enter(self, agent):
        if agent.place != Enum.PlaseEnum.BAR:
            agent.place = Enum.PlaseEnum.BAR
            print(agent.get_ID + ": entering bar")

    def Execute(self, agent):
        agent.thirst += 1
        print(agent.get_ID + ": Ahh, good drink, really clenhes your thirst")
        agent.WhatToDo()

    def Exit(self, agent):
        print(agent.get_ID + ": time to leave the bar")

class gotoTheResturantAndEat(State):
    def Enter(self, agent):
        if agent.place != Enum.PlaseEnum.RESTURANT:
            agent.place = Enum.PlaseEnum.RESTURANT
            print(agent.get_ID + ": Entering the Resturant")
    def Execute(self, agent):
        agent.hunger += 1
        print(agent.get_ID + ": This food is tasty")
    def Exit(self, agent):
        print(agent.get_ID + ": I am full, time to leave the Resturant.")

class goHomeandSleepUntilRested(State):
    pass

class goToOfficeAndProgram(State):
    pass

class goToFactoryandFixMachines(State):
    pass

class goToStoreAndBuySomethingNice(State):
    pass