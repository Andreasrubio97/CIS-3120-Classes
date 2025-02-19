class Animal:
    def __init__(self, name, food, sleep, run, hunt, fight): 
        self.__name = name
        self.__food = food
        self.__sleep = sleep
        self.__run = run
        self.__hunt = hunt
        self.__fight = fight
        print("These animals are", self.__name)

    def talk(self):
        print("Lions roar")
    
    def eat_food(self):
        print(self.__name, "eat", self.__food)
    
    def animal_sleep(self):
        print(self.__name, "sleep at", self.__sleep)
    
    def animal_run(self):
        print(self.__name, "run", self.__run)

    def animal_hunt(self):
        print(self.__name, "hunt", self.__hunt)

    def animal_fight(self):
        print(self.__name, "other", self.__fight)

    


   
    

