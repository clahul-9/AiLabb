import StateMachine, State
import random

class baseGameEntity:
    #privet
    _m_iNextValidID = int()
    _myID = int()
    def _SetID(self,value):
        if value >= self._m_iNextValidID:
            self._myID = value
            _m_iNextvalidId =+ 1

    def __init__(self,id):#ctor
        pass
        
    #public
    def __del__(self):#dtor
        pass

    def Update(self):
        pass

    def get_ID(self):
        return self._myID

    def whatToDo(self):
        pass



class Person(baseGameEntity):

    def __init__(self, id):#ctor
        self._SetID(id)
        self.stateMachine = StateMachine.StateMachine(self)
        self.money = 0
        self.energi = 0
        self.hunger = 0
        self.thirst = 0
        self.place = None

    def Update(self):
        self.stateMachine.Update()

    def whatToDo(self):
        if self.energi < 1:# Tierd
            self.stateMachine.ChangeState(State.goHomeandSleepUntilRested())
        elif self.thirst <= 1:#Thirsty
            self.stateMachine.ChangeState(State.gotoBarAndDrink())
        elif self.hunger <= 1:#Hungry
            self.stateMachine.ChangeState(State.gotoTheResturantAndEat())
        elif self.money > 5:#ritch/ has enogh money
            self.stateMachine.ChangeState(State.goToStoreAndBuySomethingNice())
        else: #go to work
            if self.stateMachine.currentState == State.goToOfficeAndProgram() or self.stateMachine.currentState == State.goToFactoryandFixMachines():
                pass
            else:
                i = random.randint(1,2)
                if i == 2:
                    self.stateMachine.ChangeState(State.goToFactoryandFixMachines())
                else:
                    self.stateMachine.ChangeState(State.goToOfficeAndProgram())
