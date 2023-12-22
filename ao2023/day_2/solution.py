max_red, max_blue, max_green = 12, 14, 13


def impossible(cube_sets):
    for cube_set in cube_sets.split(';'):
        for cube in cube_set.split(','):
            number, color = cube.split()
            if color == 'red' and int(number) > max_red:
                return True
            elif color == 'blue' and int(number) > max_blue:
                return True
            elif color == 'green' and int(number) > max_green:
                return True
    return False


def find_min_cubes(cube_sets):
    red, blue, green = None, None, None
    for cube_set in cube_sets.split(';'):
        for cube in cube_set.split(','):
            number, color = cube.split()
            if color == 'red' and (red is None or int(number) > red):
                red = int(number)
            elif color == 'blue' and (blue is None or int(number) > blue):
                blue = int(number)
            elif color == 'green' and (green is None or int(number) > green):
                green = int(number)
    return red, blue, green


if __name__ == '__main__':
    possible = list()
    min_cubes = list()
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            game, cube_sets = line.split(':')
            game_number = game.split()[1]

            min_cubes.append(find_min_cubes(cube_sets))

            if not impossible(cube_sets):
                possible.append(int(game_number))

        print(f'Sum of IDs: {sum(possible)}')
        print(f'Sum of the power of min cube sets: {sum(red * blue * green for red, blue, green in min_cubes)}')
