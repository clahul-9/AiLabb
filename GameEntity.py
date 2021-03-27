from State import*

class baseGameEntity:
    #privet
    _m_iNextValidID = int()
    _myID = int()
    def _SetID(self,value):
        if value >= self._m_iNextValidID:
            self._myID=value
            _m_iNextvalidId =+ 1

    def __init__(self, id):#ctor
        self._SetID(id)
        
    #public
    def __del__(self):#dtor
        pass

    def Update(self):
        pass

    def get_ID(self):
        return self._myID

class GaneEntity1(baseGameEntity):
     stat1 = int()
     currentState = State()

     def Update(self):
        self.currentState.Execute()

class Person(baseGameEntity):
    money = int()
    energi = int()
    hunger = int()
    thirst = int()
    place = string()
    def __init__(self, id):#ctor
        self._SetID(id)
        money = 0
        energi = 9
        hunger = 5
        thirst = 5
        place = None