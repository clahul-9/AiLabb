from State import *
from StateMachine import*
from GameEntity import*



Person = GaneEntity1(0)
Person.currentState = State2()
stateMachine = StateMachine(Person)

stateMachine._CurrentState = State2()
stateMachine.Update()
stateMachine._CurrentState = State1()
stateMachine.Update()
