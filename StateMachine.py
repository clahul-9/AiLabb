from State import *
from GameEntity import*

class StateMachine:
    _CurrentState = State()
    _PreviusState = State()
    _Globalstate = State()
    #public
    def __init__(self, owner):
        self._Owner= baseGameEntity(owner.get_ID())
        _CurrentState = None
        _PreviusState = None
        _Globalstate = None

    def Update(self):
        if self._Globalstate:
            self._Globalstate.Execute()
        if self._CurrentState:
            self._CurrentState.Execute()

    def ChangeState(self, newState):
        self._PreviusState = _CurrentState
        self._CurrentState.Exit()
        self._CurrentState = newState
        self._CurrentState.Enter()


