from triangles.commons import create_triangle_from_raw_string


def print_sorted_result(triangle_list):
    print("================= Triangles list: =================")
    for number, triangle in enumerate(sorted(triangle_list,
                                             key=lambda triangle: triangle.count_square(),
                                             reverse=True), start=1):
        print("{num}.[{name}]: {square:.2f} cm.".format(num=number,
                                                        name=triangle.name,
                                                        square=triangle.count_square()))


if __name__ == "__main__":
    triangle_list = []
    answer = "yes"

    while answer in ("yes", "y"):
        if not triangle_list:
            triangle_raw_data = input(
                "Please, enter your triangle to count its square.\n"
                "Input format is: <name>, <first_side>, <second_side>, "
                "<third_side>\n")
        else:
            triangle_raw_data = input("Please, enter your triangle: ")

        new_triangle = create_triangle_from_raw_string(triangle_raw_data)
        if new_triangle:
            triangle_list.append(new_triangle)
        answer = input("Do you want to add another triangle? ").lower()

    print_sorted_result(triangle_list)
