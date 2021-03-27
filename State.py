class State:
    def Enter(self):
        pass
    def Execute(self):
        pass
    def Exit(self):
        pass

    def __del__(self):
        pass

class State1(State):
    def Enter(self):
        print("entering State 1")
    def Execute(self):
        print("executeing State 1")
    def Exit(self):
        print("Exiting State 1")


class State2(State):
    def Enter(self):
        print("entering State 2")
    def Execute(self):
        print("executeing State 2")
    def Exit(self):
        print("Exiting State 2")

class gotoBarAndDrink(State):
    def Enter(self):
        if self.place != "bar":
            self.place = "bar"
            print( "entering bar")
    def Execute(self):
        print(" ")