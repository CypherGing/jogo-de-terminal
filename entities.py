import os, json, nen


class Entity:
    def __init__(self,
                 name: str,
                 age: int,
                 sex: str,
                 strenght: int,
                 dexterity: int,
                 constituition: int,
                 agility: int,
                 intelligence: int,
                 perception: int,
                 aura: int,
                 ) -> None:
        
        # Informações Básicas
        self.name = name
        self.age = age
        self.sex = sex

        # Atributos Base
        self.strenght = strenght
        self.dexterity = dexterity
        self.constituition = constituition
        self.agility = agility
        self.intelligence = intelligence
        self.perception = perception
        self.aura = aura
    

    def new_character(self):
    
        saves = r"saves"
        saves_count = len([arquivo for arquivo in os.listdir(saves) if os.path.isfile(os.path.join(saves, arquivo))])
        save_number = 0
        if saves_count >= 0:
            save_number = saves_count + 1

        new_game_name = f"character00{save_number}.json"
        
        new_game = {"char_basic_info": {
                    
                    "name": self.name,
                    "age": self.age,
                    "sex": self.sex,
                    },

                    "char_atributes": {
                            
                        'strenght': self.strenght,
                        'dexterity': self.dexterity,
                        'constituition': self.constituition,
                        'agility': self.agility,
                        'intelligence': self.intelligence,
                        'perception': self.perception,
                        'aura': self.aura
                        },

                    "char_stats": {
                            
                        'sanity': self.perception+self.intelligence,
                        'health': 5*self.constituition+15,
                        'nen': self.aura*5,
                        'force': self.agility+self.constituition+self.strenght,
                        'inventory': 1+self.constituition+self.strenght/2
                    }
                }
        

        with open(f"saves/{new_game_name}", 'w', encoding='utf-8') as newgame_json:
            json.dump(new_game, newgame_json, ensure_ascii=False, indent=4)

        print(f"Novo jogo salvo em: saves/{new_game_name}")
        print(new_game["char_basic_info"])
        return new_game_name

        
        

#hero = Entity("Rebeca Calhau", 27, "Feminino", 4, 4, 4, 4, 4, 4, 4).new_character()
#nen.nen_talent(hero, nen.roll_nentype())
