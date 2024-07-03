import json
def load_data(file_path):
    """"" loads json file"""
    with open(file_path, "r") as handle:
     return json.load(handle)


animals_data = load_data("animals_data.json")

for fox_info_dictionary in animals_data:
    name = fox_info_dictionary["name"]
    diet = fox_info_dictionary["characteristics"]["diet"]
    first_location = fox_info_dictionary["locations"][0]
    print(f"Name: {name}\nDiet: {diet}\nLocation: {first_location}")
    if "type" in fox_info_dictionary["characteristics"]:
        fox_type = fox_info_dictionary["characteristics"]["type"]
        print(f"Type: {fox_type}")
    print("")



