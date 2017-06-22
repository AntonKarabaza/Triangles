from triangles.triangle import TriangleFromString, Triangles


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

        try:
            triangle_list.append(TriangleFromString(triangle_raw_data))
        except ValueError:
            print("Side lengths have to be an integer or float numbers!")
        except Exception:
            print("Wrong parameters number to build triangle!")

        answer = input("Do you want to add another triangle? ").lower()

    Triangles(*triangle_list).print_in_square_desc_order()
