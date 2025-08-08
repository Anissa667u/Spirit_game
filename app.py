from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel
from spirit import Spirits 
from event import Event
from need import Need

app = FastAPI(title = 'Spirit Game API', version='0.1.0')

class NeedOut(BaseModel):
    hunger: int 
    happieness: int 
    sleepiness: int     
class SpiritOut(BaseModel):
    id: int
    name: str 
    level: int 
    energy: int 
    mood: str 
    age: int 
    element: str 
    stats: NeedOut 
    
_spirit = Spirits(
    id=1, 
    name = "Ersimol" , 
    level = 1 , 
    energy = 10, 
    mood = "neutral" , 
    age = 0 , 
    element = "air", 
    stats = Need(spirit_id = 1, hunger = 3 , happieness = 10, sleepiness = 2),
    history = []
)

def to_spirit_out(s: Spirits) -> SpiritOut:
    return SpiritOut(
        id = s.id,
        name = s.name, 
        energy= s.energy,
        mood = s.mood, 
        age = s.age, 
        element = s.element, 
        stats = NeedOut(
            hunger = s.stats.hunger,
            happieness = s.stats.happieness, 
            sleepiness= s.stats.sleepiness
        )
    )
    
@app.get("/spirit", response_model=SpiritOut)
def get_spirit():
    return to_spirit_out(_spirit)

@app.post("/spirit/feed", response_model=SpiritOut)
def feed():
    _spirit.feed()
    return to_spirit_out(_spirit)

@app.post("/spirit/sleep", response_model=SpiritOut)
def sleep():
    _spirit.sleep()
    return to_spirit_out(_spirit)

@app.post("/spirit/meditate", response_model=SpiritOut)
def meditate():
    _spirit.meditate()
    return to_spirit_out(_spirit)

class PlayIn(BaseModel):
    # потом добавлю мини игры
    game: str | None = None

'''@app.post("/spirit/play", response_model=SpiritOut)
def play(body: PlayIn = PlayIn()):
    # потом посмотрим
    _spirit.play()
    return to_spirit_out(_spirit) '''

@app.post("/spirit/evolve", response_model=SpiritOut)
def evolve():
    _spirit.evolve()
    return to_spirit_out(_spirit)