import math

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

    def hexagon_h(h: float) -> float:
        return round(h * 0.5 / 0.866 * 6, 2)
    
    def hexagon_d(d: float) -> float:
        return round(d * 0.5 * 6 , 2)
        
    def oblong(side_a: float, side_b: float) -> float:
        return round((((side_a - side_b) * 2)+ (side_b * 3.1415)), 2)

class Hexagon():

    #Сторона шестикутника по описаному діаметру кола
    def a_hexagon_d(d: float) -> float:
        return round(d * 0.5, 2)
    
    #Сторона шестикутника по відстані проміж паралельними сторонами
    def a_hexagon_h(h: float) -> float:
        return round(0.57735 * h, 2)

    #Відстань проміж паралельними сторонами по стороні
    def h_hexagon_a(a: float) -> float:
        return round((a / 0.57735), 2)

    #Відстань проміж паралельними сторонами по описаному діаметру кола
    def h_hexagon_d(d: float) -> float:
        return round((d * 0.866), 2)
    
    #Діаметр описаного кола по стороні
    def d_hexagon_a(a: float) -> float:
        return round((a * 2), 2)

    #Діаметр описаного кола по відстані проміж паралельними сторонами
    def d_hexagon_h(h: float) -> float:
        return round((h / 0.866), 2)
    

class Equilateral_triangle():

    def perim_eq_tr_side(side: float) -> float:
        return round((3 * side), 2)

    def perim_eq_tr_height(height: float) -> float:
        return round((height / 0.866) * 3, 2)

    def side_eq_tr_height(height: float) -> float:
        return round((height / 0.866) , 2)

    def height_eq_tr_side(side: float) -> float:
        return round((side * 0.866), 2)


class Isosceles_triangle():

    def perim_is_tr_side_a_b(side_a: float, side_b: float) -> float:
        return round((2 * side_a + side_b), 2)
    
    def perim_is_tr_height_side_b(height: float, side_b: float) -> float:
        return round(2 * ((height ** 2 + (side_b * 0.5) ** 2) ** 0.5) + side_b, 2)
    
    def perim_is_tr_side_a_height(side_a: float, height: float) -> float:
        return round((side_a * 2) + 2 * (((side_a ** 2) - (height ** 2)) ** 0.5), 2)
    
    def height_is_tr_side_a_b(side_a:  float, side_b: float) -> float:
        return round((((side_a ** 2) - ((side_b * 0.5) ** 2)) ** 0.5), 2)
    
    def side_a_is_tr_side_b_height(side_b: float, height: float) -> float:
        return round( ((height ** 2) + ((side_b * 0.5) ** 2)) ** 0.5 , 2)
    
    def side_b_is_tr_side_a_height(side_a: float, height: float) -> float:
        return round(2 * (((side_a ** 2) - (height** 2)) ** 0.5) , 2)


class Square_in_round():

    def perimeter_square_in_round(side_sir: float, diameter_sir: float) -> float:
        m = round((((diameter_sir ** 2) - (side_sir ** 2)) ** 0.5), 4)
        c = round(diameter_sir * 3.1415, 4)
        k_1 = m / 2
        l_ab = round((math.asin(k_1/(diameter_sir * 0.5)) * 2) * (diameter_sir / 2), 2)
        p =  round(((4 * m) + (c - (4 * l_ab))), 2)
        return p 
    

class Incomplete_circle():

    def get_h_form_height(diameter: float, height: float) -> float:
        return round(height - (diameter * 0.5), 2)

    def lenght_chold(diameter: float, height: float) -> float:
        h = Incomplete_circle.get_h_form_height(diameter, height)
        lenght = 2 * ((((diameter * 0.5) ** 2) - (h ** 2)) ** 0.5)
        return round(lenght, 2)
    
    def perim_in_circle(diameter: float, height: float):
        c = diameter * 3.1415
        h = Incomplete_circle.get_h_form_height(diameter, height)
        x = ((0.5 * diameter * 8 * ((diameter * diameter) - h)) +  (4 * ((0.5 * diameter) - h))) ** 0.5
        l = Incomplete_circle.lenght_chold(diameter, height)
        return round((l + c - x), 2 )





