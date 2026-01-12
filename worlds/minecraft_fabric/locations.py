
# Vanilla Start Locations (can be done with start items)
vanilla_start_locations = [
    "Stone Age",
    "Monster Hunter",
    "Light as a Rabbit",
    "The Parrots and the Bats",
    "You've Got a Friend in Me",
    "Whatever Floats Your Goat!",
    "Best Friends Forever",
    "A Seedy Place"
]

def get_location_table():
    table = {}
    table.update(add_locations(table, vanilla_start_locations))
    return table

def add_locations(table: dict[str, int], locations: list[str]):
    return {
        name: (index + len(table) + 1) for index, name in enumerate(locations)
    }

location_table = get_location_table()