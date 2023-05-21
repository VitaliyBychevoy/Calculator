class Perimeter():
    
    def round(diameter: float) -> float:
        return round(diameter * 3.1415, 2)

    def halfround():
        pass

    def square(side: float) -> float:
        return round(side * 4, 2)

    def square_one_radius():
        pass

    def square_four_radius():
        pass

    def square_in_round():
        pass

    def rectangle(side_a: float, side_b: float) -> float:
        return (side_a * 2) + (side_b * 2)

    def rectangle_one_radius(side_a: float, side_b: float, radius: float) -> float:
        a = radius * 2 * 3.1415
        b = side_a - (2 * radius)
        c = side_b - (2 * radius)
        print("a = ", a, " ", type(a))
        print("b = ", b, " ", type(b))
        print("c = ", c, " ", type(c))
        result = a + b + c
        print("resutl = ",result, " ", type(result))
        return (radius * 2 * 3.1415) + (side_a - (2 * radius)) + (side_b - (2 * radius))

    def rectangle_four_radius():
        pass

    def rectangle_in_round():
        pass

    