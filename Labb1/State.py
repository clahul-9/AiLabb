class State:
    def Enter(self, agent):
        pass
    def Execute(self, agent):
        pass
    def Exit(self):
        pass

    def __del__(self):
        pass

class State1(State):
    def Enter(self, agent):
        print("entering State 1")
    def Execute(self, agent):
        print("executeing State 1")
    def Exit(self):
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
        if self.place != "bar":
            self.place = "bar"
            print( "entering bar")
    def Execute(self, agent):
        agent.thirst += 1
        print("Ahh, god drinck")

class gotoTheResturantAndEat(State):
    pass

class goHomeandSleepUntilRested(State):
    pass

class goToOfficeAndProgram(State):
    pass

class goToFactoryandFixMachines(State):
    pass

class goToStoreAndBuySomethingNice(State):
    pass