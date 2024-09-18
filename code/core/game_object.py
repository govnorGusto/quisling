from uu import Error

class Component:
    def __init__(self, owner):
        if not issubclass(type(owner), Game_object):
            print("ERROR: Only Game_object derived objects should own components")
            return
        self.owner = owner
        
    def update(self, delta_time : float):
        self.on_update(delta_time)

    def on_update(self, delta_time : float):
        pass

    def draw(self, delta_time : float):
        self.on_draw(delta_time)
    
    def get_game(self):
        return self.owner.game

    def on_draw(self, delta_time : float):
        pass
    
    def print(self) -> None:
        print("Component: " + str(self) + "\n" + "Owned by: " + str(self.owner))

class Game_object:
    game = None
    def __init__(self, game=None):
        if self.game == None:
            if game == None:
                raise Error("First gameobject initialized must receive a valid game reference")
            Game_object.game = game
            
        Game_object.game.add_game_object(self)
        self.components = []
    
    def update(self, delta_time : float):
        self.on_update(delta_time)        

        for component in self.components:
            component.update(delta_time)        
        
    def on_update(self, delta_time : float):
        pass
            
    def draw(self, delta_time : float):
        self.on_draw(delta_time)
        for component in self.components:
            component.draw(delta_time)
            
    def on_draw(self, delta_time : float):
        pass
            
    def add_component(self, type_to_add) -> Component:
        if not issubclass(type_to_add, Component):
            print("ERROR: Only Components-derived objects should be added as components")
            return
        self.components.append(type_to_add(self))
        return self.components[-1]
    
    def get_components(self, type_to_get) -> [Component]:
        '''Will return a list with all components of the specified class or inherited thereof'''
        out = []
        for component in self.components:
            if issubclass(component, type_to_get):
                out.append(component)
        return out
        
            
    def print(self) -> None:
        print("Game Object: " + str(self))