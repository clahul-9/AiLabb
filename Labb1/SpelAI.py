import State, StateMachine, GameEntity

ola = GameEntity.Person(0)
ola.stateMachine.currentState = State.goHomeandSleepUntilRested()

i = 0

while i <= 50:
    ola.Update()
    i += 1
