import random, json

char_nen_type = 0

nen_atributes = {}


talent_value = random.randrange(1, 1000)

def roll_nentype():
    if talent_value < 1000 and talent_value >= 800:
        char_nen_type = "Reinforcement"

    elif talent_value < 800 and talent_value >= 600:
        char_nen_type = "Transmutation"

    elif talent_value < 600 and talent_value >= 400:
        char_nen_type = "Emission"

    elif talent_value < 400 and talent_value >= 200:
        char_nen_type = "Materialization"

    elif talent_value < 200 and talent_value >= 1:
        char_nen_type = "Manipulation"

    elif talent_value == 0 or talent_value == 1000:
        char_nen_type = "Specialist"
    print(char_nen_type)
    return char_nen_type



def nen_talent(character: str, char_nen_type: str):
    if char_nen_type == "Reinforcement":

        reinforcement_talent = random.randrange(80, 100)
        emission_talent = random.randrange(60, 80)
        transmutation_talent = random.randrange(60, 80)
        materialization_talent = random.randrange(10, 60)
        speacialization_talent = 0
        manipulation_talent = random.randrange(10, 60)

        user_type = ""

        potential_type = ""
        if emission_talent > transmutation_talent and reinforcement_talent < 90:
            user_type = "Hybrid"
            potential_type = "Emission"
        elif transmutation_talent > emission_talent and reinforcement_talent < 90:
            user_type = "Hybrid"
            potential_type = "Transmutation"
        else: 
            potential_type = "Reinforcement"
            user_type = "Pure"

        nen_atributes = {

        'Nen_User_type': user_type,
        'Nen_Inatte_type': char_nen_type,
        'Nen_Potential_type': potential_type,
        'reinforcement':  reinforcement_talent,
        'emission': emission_talent,
        'transmutation': transmutation_talent,
        'materialization': materialization_talent,
        'specialization': speacialization_talent,
        'manipulation': manipulation_talent,
                        }
        print(nen_atributes)

        with open(f"saves/{character}", 'r') as character_json:
            character_string = character_json.read()
            character_dict= json.loads(character_string)
        print(character_dict)

        character_dict['nen_atributes'] = nen_atributes

        with open(f'saves/{character}', 'w', encoding='utf_8') as character_json:
             json.dump(character_dict, character_json, ensure_ascii=False, indent=4)
    
    if char_nen_type == "Emission":

        reinforcement_talent = random.randrange(60, 80)
        emission_talent = random.randrange(80, 100)
        transmutation_talent = random.randrange(10, 60)
        materialization_talent = random.randrange(10, 60)
        speacialization_talent = 0
        manipulation_talent = random.randrange(60, 80)

        user_type = ""

        potential_type = ""
        if reinforcement_talent > manipulation_talent and emission_talent < 90:
            user_type = "Hybrid"
            potential_type = "Reinforcement"
        elif manipulation_talent > reinforcement_talent and emission_talent < 90:
            user_type = "Hybrid"
            potential_type = "Manipulation"
        else: 
            potential_type = "Emission"
            user_type = "Pure"

        nen_atributes = {

        'Nen_User_type': user_type,
        'Nen_Inatte_type': char_nen_type,
        'Nen_Potential_type': potential_type,
        'reinforcement':  reinforcement_talent,
        'emission': emission_talent,
        'transmutation': transmutation_talent,
        'materialization': materialization_talent,
        'specialization': speacialization_talent,
        'manipulation': manipulation_talent,
                        }
        print(nen_atributes)

        with open(f"saves/{character}", 'r') as character_json:
            character_string = character_json.read()
            character_dict= json.loads(character_string)
        print(character_dict)

        character_dict['nen_atributes'] = nen_atributes

        with open(f'saves/{character}', 'w', encoding='utf_8') as character_json:
             json.dump(character_dict, character_json, ensure_ascii=False, indent=4)

    if char_nen_type == "Transmutation":

        reinforcement_talent = random.randrange(60, 80)
        emission_talent = random.randrange(10, 60)
        transmutation_talent = random.randrange(80, 100)
        materialization_talent = random.randrange(60, 80)
        speacialization_talent = 0
        manipulation_talent = random.randrange(10, 40)

        user_type = ""

        potential_type = ""
        if reinforcement_talent > materialization_talent and transmutation_talent < 90:
            user_type = "Hybrid"
            potential_type = "Emission"
        elif materialization_talent > reinforcement_talent and transmutation_talent < 90:
            user_type = "Hybrid"
            potential_type = "Transmutation"
        else: 
            potential_type = "Transmutation"
            user_type = "Pure"

        nen_atributes = {

        'Nen_User_type': user_type,
        'Nen_Inatte_type': char_nen_type,
        'Nen_Potential_type': potential_type,
        'reinforcement':  reinforcement_talent,
        'emission': emission_talent,
        'transmutation': transmutation_talent,
        'materialization': materialization_talent,
        'specialization': speacialization_talent,
        'manipulation': manipulation_talent,
                        }
        print(nen_atributes)

        with open(f"saves/{character}", 'r') as character_json:
            character_string = character_json.read()
            character_dict= json.loads(character_string)
        print(character_dict)

        character_dict['nen_atributes'] = nen_atributes

        with open(f'saves/{character}', 'w', encoding='utf_8') as character_json:
             json.dump(character_dict, character_json, ensure_ascii=False, indent=4)

    if char_nen_type == "Manipulation":

        reinforcement_talent = random.randrange(10, 60)
        emission_talent = random.randrange(60, 80)
        transmutation_talent = random.randrange(10, 40)
        materialization_talent = random.randrange(10, 60)
        speacialization_talent = 1
        manipulation_talent = random.randrange(80, 100)

        user_type = ""

        potential_type = ""
        if emission_talent > 75 and manipulation_talent < 90:
            user_type = "Hybrid"
            potential_type = "Emission"
        else: 
            potential_type = "Transmutation"
            user_type = "Pure"

        nen_atributes = {

        'Nen_User_type': user_type,
        'Nen_Inatte_type': char_nen_type,
        'Nen_Potential_type': potential_type,
        'reinforcement':  reinforcement_talent,
        'emission': emission_talent,
        'transmutation': transmutation_talent,
        'materialization': materialization_talent,
        'specialization': speacialization_talent,
        'manipulation': manipulation_talent,
                        }
        print(nen_atributes)

        with open(f"saves/{character}", 'r') as character_json:
            character_string = character_json.read()
            character_dict= json.loads(character_string)
        print(character_dict)

        character_dict['nen_atributes'] = nen_atributes

        with open(f'saves/{character}', 'w', encoding='utf_8') as character_json:
             json.dump(character_dict, character_json, ensure_ascii=False, indent=4)

    if char_nen_type == "Materialization":

        reinforcement_talent = random.randrange(10, 60)
        emission_talent = random.randrange(10, 40)
        transmutation_talent = random.randrange(60, 80)
        materialization_talent = random.randrange(80, 100)
        speacialization_talent = 1
        manipulation_talent = random.randrange(10, 60)

        user_type = ""

        potential_type = ""
        if transmutation_talent and materialization_talent < 90:
            user_type = "Hybrid"
            potential_type = "Transmutation"
        else: 
            potential_type = "Materialization"
            user_type = "Pure"

        nen_atributes = {

        'Nen_User_type': user_type,
        'Nen_Inatte_type': char_nen_type,
        'Nen_Potential_type': potential_type,
        'reinforcement':  reinforcement_talent,
        'emission': emission_talent,
        'transmutation': transmutation_talent,
        'materialization': materialization_talent,
        'specialization': speacialization_talent,
        'manipulation': manipulation_talent,
                        }
        print(nen_atributes)

        with open(f"saves/{character}", 'r') as character_json:
            character_string = character_json.read()
            character_dict= json.loads(character_string)
        print(character_dict)

        character_dict['nen_atributes'] = nen_atributes

        with open(f'saves/{character}', 'w', encoding='utf_8') as character_json:
             json.dump(character_dict, character_json, ensure_ascii=False, indent=4)

    if char_nen_type == "Specialist":

        reinforcement_talent = random.randrange(20, 40)
        emission_talent = random.randrange(20, 60)
        transmutation_talent = random.randrange(20, 60)
        materialization_talent = random.randrange(60, 80)
        speacialization_talent = random.randrange(80, 100)
        manipulation_talent = random.randrange(60, 80)

        user_type = ""

        potential_type = ""
        if manipulation_talent > materialization_talent and speacialization_talent < 90:
            user_type = "Hybrid"
            potential_type = "Manipulation"
        elif materialization_talent > manipulation_talent and speacialization_talent< 90:
            user_type = "Hybrid"
            potential_type = "Materialization"
        else: 
            potential_type = "Specialist"
            user_type = "Pure"

        nen_atributes = {

        'Nen_User_type': user_type,
        'Nen_Inatte_type': char_nen_type,
        'Nen_Potential_type': potential_type,
        'reinforcement':  reinforcement_talent,
        'emission': emission_talent,
        'transmutation': transmutation_talent,
        'materialization': materialization_talent,
        'specialization': speacialization_talent,
        'manipulation': manipulation_talent,
                        }
        print(nen_atributes)

        with open(f"saves/{character}", 'r') as character_json:
            character_string = character_json.read()
            character_dict= json.loads(character_string)
        print(character_dict)

        character_dict['nen_atributes'] = nen_atributes

        with open(f'saves/{character}', 'w', encoding='utf_8') as character_json:
             json.dump(character_dict, character_json, ensure_ascii=False, indent=4)

# nen_talent("character001.json", roll_nentype())

