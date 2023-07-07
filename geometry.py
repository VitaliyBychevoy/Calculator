import math

# class Perimeter():

#     def square(side: float) -> float:
#         return round(side * 4, 1)

#     def square_one_radius(side: float, radius: float) -> float:
#         return round((2 * 3.1415 * radius) + (4 * (side - (radius * 2))), 1)

#     def square_four_radius(
#             side: float, 
#             r1: float, 
#             r2: float, 
#             r3: float, 
#             r4: float
#             ) -> None:
#         s1 = side - r1 - r2
#         s2 = side - r2 - r3
#         s3 = side - r3 - r4
#         s4 = side - r4 - r1

#         arc1 = r1 * 2 * 3.1415 * 0.25
#         arc2 = r2 * 2 * 3.1415 * 0.25
#         arc3 = r3 * 2 * 3.1415 * 0.25
#         arc4 = r4 * 2 * 3.1415 * 0.25

#         return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 1)
        
#     def square_in_round():
#         pass

#     def rectangle(side_a: float, side_b: float) -> float:
#         return round((side_a * 2) + (side_b * 2), 2)

#     def rectangle_one_radius(side_a: float, side_b: float, radius: float) -> float:
#         return round((radius * 2 * 3.1415) + ((side_a - (2 * radius)) * 2) + ((side_b - (2 * radius)) * 2), 1)

#     def rectangle_four_radius(
#             side_1: float,
#             side_2: float, 
#             r1: float, 
#             r2: float, 
#             r3: float, 
#             r4: float
#     ):
#         s1 = side_1 - r1 - r2
#         s2 = side_2 - r2 - r3
#         s3 = side_1 - r3 - r4
#         s4 = side_2 - r4 - r1

#         arc1 = r1 * 2 * 3.1415 * 0.25
#         arc2 = r2 * 2 * 3.1415 * 0.25
#         arc3 = r3 * 2 * 3.1415 * 0.25
#         arc4 = r4 * 2 * 3.1415 * 0.25

#         return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 1)
   
#     def hexagon_a(a: float) -> float:
#         return round(a * 6, 1)

#     def hexagon_h(h: float) -> float:
#         return round(h * 0.5 / 0.866 * 6, 1)
    
#     def hexagon_d(d: float) -> float:
#         return round(d * 0.5 * 6 , 1)
        
#     def oblong(side_a: float, side_b: float) -> float:
#         return round((((side_a - side_b) * 2)+ (side_b * 3.1415)), 1)

class Round():

    def perimeter_round(diameter: float) -> float:
        return round(diameter * 3.1415, 2)

#Напівколо
class Incomplete_circle():

    def get_h_form_height(diameter: float, height: float) -> float:
        return round(height - (diameter * 0.5), 1)

    def lenght_chold(diameter: float, height: float) -> float:
        h = Incomplete_circle.get_h_form_height(diameter, height)
        lenght = 2 * ((((diameter * 0.5) ** 2) - (h ** 2)) ** 0.5)
        return round(lenght, 4)

    #Висота більша за радіус
    def perim_in_circle(diameter: float, height: float) -> float:
        c = diameter * 3.1415
        h = Incomplete_circle.get_h_form_height(diameter, height)
        l = Incomplete_circle.lenght_chold(diameter, height)
        r = diameter * 0.5
        a_2_rad = math.acos(h / r)
        a_rad = a_2_rad * 2
        a = a_rad * 180 / 3.1415
        x = (3.1415 * r * a ) / 180 
        return round((l + c - x), 2)

    #Висота дорівнює радіусу
    def perim_half_round(diameter: float, height: float) -> float:
        p = (diameter * 3.1415 * 0.5) + diameter
        return round(p, 2)

    def chold_length(diameter: float, height: float) -> float:
        r = diameter * 0.5
        h = diameter - height
        l = Incomplete_circle.lenght_chold(diameter, h)
        return round(l, 4) 

    #Висота меньша за радіус
    def perim_half_round_height_less_radius(diameter: float, height: float) -> float:
        r = diameter * 0.5
        h = diameter - height
        l = Incomplete_circle.chold_length(diameter, h)
        k = r - height
        a_rad = 2 * (math.acos((k / r)))
        a = a_rad * 180 / 3.1415
        c = (3.1415 * r * a) / 180
        p = l + c
        return round(p, 2)

#Квадрат
class Square():

    def perimeter_square(side: float) -> float:
        return round(side * 4, 2)

    def circumscribed_circle_diameter(side: float) -> float:
        return round(0.707 * side, 1)

#Квадрат з радіусом
class Square_One_Radius():
    
    def perimeter_square_one_radius(side: float, radius: float) -> float:
        return round((2 * 3.1415 * radius) + (4 * (side - (radius * 2))), 2)

#Квадрат з 4 радіусами
class Square_four_Radius():

    def perimeter_square_four_radius(
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

        return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 1)

#Квадрат у колі
class Square_in_round():

    def perimeter_square_in_round(side_sir: float, diameter_sir: float) -> float:
        m = round((((diameter_sir ** 2) - (side_sir ** 2)) ** 0.5), 4)
        c = round(diameter_sir * 3.1415, 4)
        k_1 = m / 2
        l_ab = round((math.asin(k_1/(diameter_sir * 0.5)) * 2) * (diameter_sir / 2), 2)
        p =  round(((4 * m) + (c - (4 * l_ab))), 2)
        return p

#Прямокутник
class Rectangle():
    def perimeter_rectangle(side_a: float, side_b: float) -> float:
        return round((side_a * 2) + (side_b * 2), 2)

#Прямокутник з одним радіусом
class Rectangle_One_Radius():
    
    def parimeter_rectangle_one_radius(side_a: float, side_b: float, radius: float) -> float:
        return round((radius * 2 * 3.1415) + ((side_a - (2 * radius)) * 2) + ((side_b - (2 * radius)) * 2), 2)

#Прямокутник з 4 радіусами
class Rectangel_Four_Radius():
    def perimeter_rectangle_four_radius(
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

#Шестикутник
class Hexagon():

    def perimeter_hexagon_a(a: float) -> float:
        return round(a * 6, 2)
    
    def perimeter_hexagon_h(h: float) -> float:
        return round(h * 0.5 / 0.866 * 6, 2)
    
    def perimeter_hexagon_d(d: float) -> float:
        return round(d * 0.5 * 6 , 2)

    #Сторона шестикутника по описаному діаметру кола
    def a_hexagon_d(d: float) -> float:
        return round(d * 0.5, 1)
    
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
    
#Овал
class Oblong():

    def perimeter_oblong(side_a: float, side_b: float) -> float:
        return round((((side_a - side_b) * 2)+ (side_b * 3.1415)), 2)

#Рівносторонній трикутник
class Equilateral_triangle():

    def perim_eq_tr_side(side: float) -> float:
        return round((3 * side), 2)

    def perim_eq_tr_height(height: float) -> float:
        return round((height / 0.866) * 3, 2)

    def side_eq_tr_height(height: float) -> float:
        return round((height / 0.866) , 2)

    def height_eq_tr_side(side: float) -> float:
        return round((side * 0.866), 2)

#Рівнобедрений трикутник
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

if __name__ == '__main__':
    pass