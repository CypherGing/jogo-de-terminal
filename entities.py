

class Entity:
    def __init__(self,
                 name: str,
                 raca: str,
                 age: int,
                 max_age,
                 sex: str,
                 appearance: str,
                 current_sanity: int,
                 max_sanity: int,
                 current_health: int,
                 max_health: int,
                 current_nen: int,
                 max_nen: int,
                 current_force: int,
                 max_force: int,
                 strenght: int,
                 dexterity: int,
                 constituition: int,
                 agility: int,
                 intelligence: int,
                 perception: int,
                 aura: int

                 ) -> None:
        
        # Informações Básicas
        self.name = name
        self.raca = raca
        self.age = age
        self.max_age = age
        self.sex = sex
        self.appearence = appearance

        # Status Atual
        self.current_sanity = current_sanity
        self.max_sanity = max_sanity
        self.current_health = current_health
        self.max_health = max_health
        self.current_nen = current_nen
        self.max_nen = max_nen
        self.current_force = current_force
        self.max_force = max_force

        # Atributos Base
        self.strenght = strenght
        self.dexterity = dexterity
        self.constituition = constituition
        self.agility = agility
        self.intelligence = intelligence
        self.perception = perception
        self.aura = aura

        

heroi = Entity("Joseph Joestar", "Humano", 22, "Masculino", "Bonitão")
print(heroi.name)