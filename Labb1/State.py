import Enum
import random
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

        if agent.thirst >= 5:
            agent.whatToDo()

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

        if agent.hunger >= 5:
            agent.whatToDo()

    def Exit(self, agent):
        print(agent.get_ID + ": I am full, time to leave the Resturant.")


class goHomeandSleepUntilRested(State):
    def Enter(self, agent):
        if agent.place != Enum.PlaseEnum.HOME:
            agent.place = Enum.PlaseEnum.HOME
            print(agent.get_ID+": I sure am tierd, time to go home")

    def Execute(self, agent):
        agent.thirst -= 1
        agent.energi += 1
        print(agent.get_ID + "ZZZ")

        if agent.energi >= 8:
            agent.whatToDo()

    def Exit(self, agent):
        print(agent.get_ID + "Time to get going whit the day")


class goToOfficeAndProgram(State):
    def Enter(self, agent):
        if agent.place != Enum.PlaseEnum.OFFICE:
            agent.place = Enum.PlaseEnum.OFFICE
            print(agent.get_ID + "Time to go to the office")

    def Execute(self, agent):
        agent.energi -= 1
        agent.thirst -= 1
        agent.money += 1

        print(agent.get_ID + "Tap tap tap, ah an Error")
        agent.whatToDo()

    def Exit(self, agent):
        print(agent.get_ID + "That is enough programing for now, time to leave the office")

class goToFactoryandFixMachines(State):
    def Enter(self, agent):
        if agent.place != Enum.PlaseEnum.FACTORY:
            agent.place = Enum.PlaseEnum.FACTORY
            print(agent.get_ID + "Time to go to the factory")

    def Execute(self, agent):
        agent.energi -= 1
        agent.hunger -= 1
        agent.money += 1

        print(agent.get_ID + "fixing machines")
        agent.whatoDo()

    def Exit(self, agent):
        print(agent.get_ID + "All machines are fixed, time to leave")


class goToStoreAndBuySomethingNice(State):
    def Enter(self, agent):
        if agent.place != Enum.PlaseEnum.STORE:
            agent.place = Enum.PlaseEnum.STORE
            print(agent.get_ID + "I have enough money to go shopping, to the shop")

    def Execute(self, agent):
        i = random.randint(1,5)
        agent.money = agent.money - i
