from Labb1 import GameEntity, State

class StateMachine:
    #public
    def __init__(self, owner):
        self._owner = GameEntity.baseGameEntity(owner.get_ID())
        self.currentState = None
        self._previusState = None
        self._globalState = None

    def Update(self):
        if self._globalState:
            self._globalState.Execute()
        if self.currentState:
            self.currentState.Execute()

    def ChangeState(self, newState):
        self._previusState = self.currentState
        self.currentState.Exit()
        self.currentState = newState
        self.currentState.Enter()


