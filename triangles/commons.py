from triangles.triangle import Triangle


def pars_number(number_to_parse):
    try:
        return int(number_to_parse)
    except ValueError:
        return float(number_to_parse)


def create_triangle_from_raw_string(triangle_raw_data):
    parsed_data = []
    splitted_data = [splitted_data.strip() for splitted_data in triangle_raw_data.split(",")]

    if len(splitted_data) != 4:
        print("Wrong arguments number to build triangle!")
        return
    try:
        parsed_data.append(splitted_data[0])
        parsed_data.append(pars_number(splitted_data[1]))
        parsed_data.append(pars_number(splitted_data[2]))
        parsed_data.append(pars_number(splitted_data[3]))
    except ValueError:
        print("Side lengths have to be an integer or float numbers!")
        return

    return Triangle(*parsed_data)