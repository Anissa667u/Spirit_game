class Need:
    def __init__(self, spirit_id, hunger = 0, happieness = 10 , sleepiness = 0):
        self._spirit_id = spirit_id
        self._hunger = hunger
        self._happieness = happieness
        self._sleepiness = sleepiness

    def __str__(self):
        return f"Hunger {self._hunger} | Happieness {self._happieness} | Sleepiness {self._sleepiness}"

    def to_dict(self):
        return {
            "spirit_id" : self._spirit_id,
            "hunger" : self._hunger, 
            "happieness" : self._happieness,
            "sleepiness" : self._sleepiness,
        }

    @property
    def spirit_id(self):
        return self._spirit_id 

    @property 
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, new_hunger):
        if new_hunger >= 0 and new_hunger != self._hunger:
            self._hunger = new_hunger 
    
    @property 
    def happieness(self):
        return self._happieness 
    
    @happieness.setter 
    def happieness(self, new_happieness):
        if new_happieness >= 0 and new_happieness != self._happieness:
            self._happieness = new_happieness
    
    @property 
    def sleepiness(self):
        return self._sleepiness 
    
    @sleepiness.setter
    def sleepiness(self, new_sleep):
        if new_sleep >= 0 and new_sleep != self._sleepiness:
            self._sleepiness = new_sleep
    
  
