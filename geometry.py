class Perimeter():
    
    def round(diameter: float) -> float:
        return round(diameter * 3.1415, 2)

    def halfround():
        pass

    def square(side: float) -> float:
        return round(side * 4, 2)

    def square_one_radius(side: float, radius: float) -> float:
        return round((2 * 3.1415 * radius) + (4 * (side - (radius * 2))), 2)

    def square_four_radius(
            side: float, 
            r1: float, 
            r2: float, 
            r3: float, 
            r4: float
            ) -> None:
        s1 = side - r1 - r2
        s2 = side - r2 - r3
        s3 = side - r3 - r4
        s4 = side - r4 - r1

        arc1 = r1 * 2 * 3.1415 * 0.25
        arc2 = r2 * 2 * 3.1415 * 0.25
        arc3 = r3 * 2 * 3.1415 * 0.25
        arc4 = r4 * 2 * 3.1415 * 0.25

        return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 2)
        
    def square_in_round():
        pass

    def rectangle(side_a: float, side_b: float) -> float:
        return (side_a * 2) + (side_b * 2)

    def rectangle_one_radius(side_a: float, side_b: float, radius: float) -> float:
        return round((radius * 2 * 3.1415) + ((side_a - (2 * radius)) * 2) + ((side_b - (2 * radius)) * 2), 2)

    def rectangle_four_radius(
            side_1: float,
            side_2: float, 
            r1: float, 
            r2: float, 
            r3: float, 
            r4: float
    ):
        s1 = side_1 - r1 - r2
        s2 = side_2 - r2 - r3
        s3 = side_1 - r3 - r4
        s4 = side_2 - r4 - r1

        arc1 = r1 * 2 * 3.1415 * 0.25
        arc2 = r2 * 2 * 3.1415 * 0.25
        arc3 = r3 * 2 * 3.1415 * 0.25
        arc4 = r4 * 2 * 3.1415 * 0.25

        return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 2)

    def rectangle_in_round():
        pass
        
    def hexagon_a(a: float) -> float:
        return round(a * 6, 2)
    
    def a_hexagon_d(d: float) -> float:
        return round(d * 0.5, 2)
    
    def a_hexagon_h(h: float) -> float:
        return round(0.57735 * h, 2)

    def hexagon_h(h: float) -> float:
        return (((h * 0.5) / 0.866) * 6, 2)
    
    def h_hexagon_a(a: float) -> float:
        return round(a / 0.57735, 2)

    def h_hexagon_d(d: float) -> float:
        return round(d * 0.866, 2)
    
    def hexagon_d(d: float) -> float:
        return(d * 0.5 * 6 , 2)
        
    def d_hexagon_a(a: float) -> float:
        return (a * 2, 2)

    def d_hexagon_h(h: float) -> float:
        return(h / 0.866, 2)
