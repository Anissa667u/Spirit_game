from datetime import datetime 

class Event:
    def __init__(self, id, action_name: str , effect: str):
        self._id = id
        self._timestamp = datetime.now()
        self._action_name = action_name
        self._effect = effect 

    def __str__(self):
        return f"[{self._timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self._action_name}: {self._effect}"

    
    def to_dict(self):
        return {
            "id" : self._id,
            "timestamp" : self._timestamp.isoformat(),
            "action_name" : self._action_name, 
            "effect" : self._effect, 
        }

    @property
    def id(self):
        return self._id