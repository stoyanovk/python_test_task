def get_degrees(obj):
    degrees = {}
    for key in obj.keys():
        degrees[obj[key]] = key
    return degrees


def direction(facing, turn):
    directions = {
        "N": 0,
        "NE": 45,
        "E": 90,
        "SE": 135,
        "S": 180,
        "SW": 225,
        "W": 270,
        "NW": 315,
    }
    degrees = get_degrees(directions)

    if not directions.get(facing):
        print(f'facing must be one of next key {list(directions.keys())}')
        return

    if not degrees.get(turn % 360):
        print('turn must divide by 45 without remainder')
        return

    facing_direction = (directions.get(facing) + turn) % 360
    return degrees.get(facing_direction)


print(direction("S", 180))
print(direction("SE", -45))
print(direction("W", 495))
print(direction("WZ", 495))
print(direction("W", 123))
