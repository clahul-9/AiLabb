
from Labb1 import State,StateMachine,GameEntity


Person = GameEntity.GaneEntity1(0)
Person.currentState = State.State2()
stateMachine = StateMachine.StateMachine(Person)

stateMachine._CurrentState = State.State2()
stateMachine.Update()
stateMachine._CurrentState = State.State1()
stateMachine.Update()
