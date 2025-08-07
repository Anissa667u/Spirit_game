from .event import Event 

class Spirits:
    def __init__(self, id, name, level, energy, mood, age, element, stats, history = None):
        self._id = id
        self._name = name
        self._level = level
        self._energy = energy
        self._mood = mood
        self._age = age
        self._element = element
        self._stats = stats #Экземпляр класса ниид , дописать геттер и сеттер
        self._history = history or [] #список объектов ивент, дописать геттер и сеттер 

    def __str__(self):
        return f"Вашего духа зовут {self._name} | Level {self._level} | Energy {self._energy} | Mood {self._mood} | Age {self._age} | Element | {self._element} "

    def to_dict(self):
        return{
            "id" : self._id,
            "name" : self._name,
            "level" : self._level,
            "energy" : self._energy,
            "mood" : self._mood,
            "age" : self._age,
            "element" : self._element,
            "stats" : self._stats.to_dict() ,
            "history" : [e.to_dict() for e in self.history],
        }


    @property
    def id(self):
        return self._id 

    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @level.setter #лейвел может только расти 
    def level(self, new_level):
        if new_level > self._level:
            self._level = new_level
    
    @property
    def energy(self):
        return self._energy
    
    @energy.setter 
    def energy(self, new_energy):
        if new_energy >= 0:
            self._energy = new_energy 
    
    @property
    def mood(self):
        return self._mood
    
    @mood.setter
    def mood(self, new_mood):
        if new_mood != self._mood:
            self._mood = new_mood

    @property 
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age >= 0 and new_age != self._age:
            self._age = new_age

    
    @property 
    def element(self):
        return self._element 
    
    @property
    def stats(self):
        return self._stats
    
    @property
    def history(self):
        return self._history
    
    def feed(self):
        self._energy += 5 
        self._stats.hunger -=3
        self._history.append(Event(1, "feed", "Enegry +5, Hunger -3"))
        print(f"{self._name} покушал. Энергия: {self._energy}, уровень голода; {self._stats.hunger}")

    def sleep(self):
        self._energy += 5
        self._stats.sleepiness -= 3 
        self.history.append(Event(2, "Sleep", "Energy +5, Speepiness -3"))
        print(f"{self._name} поспал. Энергия: {self._energy}, уровень сонливости: {self._stats.sleepiness}")
    
    def meditate(self):
        self._energy += 5
        self._stats.happieness += 5 
        self._history.append(Event(3, "Meditate", "Energy +5, Happieness +5"))
        print(f"{self._name} помедитировал. Энергия: {self._energy}, уровень счастья: {self._stats.happieness}")


    def play(self): #Позже можно добавить куча игр но щас это неважно 
        print('''Выберите игру которую хотите сыграть: 
              1 - игра по математике 
              2 - игра по географий''')
        choice = int(input())
        if choice == 1:
            ans = int(input("Сколько будет 2 + 2?"))
            if ans == 4: 
                print("правильно")
                self._energy += 5 
                self._stats.happieness += 9
                self._history.append(Event(5, "Play: Math", "Energy +5, Happieness +9"))
                print(f"Уровень энергий духа вырос до {self._energy}, а уровень счастья до {self._happieness}") 
            else:
                print("Неправильно")

        if choice == 2:
            ans = input("Столица Казахстана...")
            if ans == "Астана":
                print("правильно")
                self._energy += 5 
                self._stats.happieness += 9
                self._history.append(Event(5, "Play: Geography", "Energy +5, Happieness +9"))
                print(f"Уровень энергий духа вырос до {self._energy}!") 
            else:
                print("Неправильно")

    def evolve(self):
        self._energy += 20
        self._stats.happieness += 20
        self._level += 1
        self._history.append(Event(4, "Evolve", "Energy +20, Happieness +20"))
        print(f"{self._name} эволюционировал. Теперь его уровень {self._level}") 
