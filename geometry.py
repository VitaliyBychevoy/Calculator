import math

class Round():

    def __init__(self, diameter: float = None):
        self.diameter = diameter

    def perimeter_round(self, diameter: float) -> float:
        self.set_diameter(diameter_1 = diameter)
        return self.perimeter()
        
    def perimeter(self) -> float:
        if type(self.diameter) not in [float, int]:
            raise ValueError("Діаметр має бути числом")
        elif self.diameter < 0:
            raise ValueError("Від'ємне число")
        else:
            return round(self.diameter * 3.1415, 2)

    def set_diameter(self, diameter_1: float) -> None:
        self.diameter = diameter_1

#Напівколо
class Incomplete_circle():

    def __init__(self, diameter: float = None, height: float = None) -> None:
        self.diameter = diameter
        self.height = height
        self.lenght = None

    def set_diameter(self, new_diameter: float) -> None:
        self.diameter = new_diameter

    def get_diameter(self) -> float:
        return self.diameter

    def set_height(self, new_height: float) -> None:
        self.height = new_height

    def get_height(self) -> float:
        return self.height

    def get_h_form_height(self, diameter: float, height: float) -> float:
        self.set_diameter(new_diameter = diameter)
        d = self.get_diameter()
        
        self.set_height(new_height=height)
        h = self.get_height()

        return round(h - (d * 0.5), 1)

    def lenght_chold(self, diameter: float, height: float) -> float:
        self.set_diameter(new_diameter = diameter)
        d = self.get_diameter()
        
        self.set_height(new_height=height)
        h = self.get_height()
        
        t = self.get_h_form_height(d, h)
        lenght = 2 * ((((d * 0.5) ** 2) - (t ** 2)) ** 0.5)
        return round(lenght, 4)      


    #Висота більша за радіус
    def perim_in_circle(self, diameter: float, height: float) -> float:
        self.set_diameter(new_diameter = diameter)
        d = self.get_diameter()
        
        self.set_height(new_height=height)
        h_1 = self.get_height()
        
        c = d * 3.1415 
        h = self.get_h_form_height(d, h_1)
        l = self.lenght_chold(d, h_1)
        r = d * 0.5
        a_2_rad = math.acos(h / r)
        a_rad = a_2_rad * 2
        a = a_rad * 180 / 3.1415
        x = (3.1415 * r * a ) / 180
        return round((l + c - x), 2) 

    #Висота дорівнює радіусу
    def perim_half_round(self, diameter: float, height: float) -> float:
        self.set_diameter(new_diameter = diameter)
        d = self.get_diameter()

        p = (d * 3.1415 * 0.5) + d
        return round(p, 2)

    def chold_length(self, diameter: float, height: float) -> float:
        self.set_diameter(new_diameter = diameter)
        d = self.get_diameter()
        
        self.set_height(new_height=height)
        h_1 = self.get_height()

        r = d * 0.5
        h = diameter - h_1
        l = self.lenght_chold(d, h)
        return round(l, 4) 

    #Висота меньша за радіус
    def perim_half_round_height_less_radius(self, diameter: float, height: float) -> float:

        self.set_diameter(new_diameter = diameter)
        d = self.get_diameter()
        
        self.set_height(new_height=height)
        h_1 = self.get_height()

        r = d * 0.5
        h = d - h_1
        l = self.chold_length(d, h)
        k = r - h_1
        a_rad = 2 * (math.acos((k / r)))
        a = a_rad * 180 / 3.1415
        c = (3.1415 * r * a) / 180
        p = l + c
        return round(p, 2)

#Квадрат
class Square():

    def __init__(self, side:float = None):
        self.side = side

    def set_side(self, new_side: float) -> None:
        self.side = new_side

    def get_side(self) -> float:
        return self.side

    def perimeter_square(self, side: float) -> float:
        self.set_side(new_side=side)
        s = self.get_side()
        return round(s * 4, 2)

    def circumscribed_circle_diameter(self, side: float) -> float:
        self.set_side(new_side=side)
        s = self.get_side()
        return round(0.707 * s, 1)

#Квадрат з радіусом
class Square_One_Radius():
    
    def __init__(self,side: float = None, radius: float = None) -> None:
        self.side = side
        self.radius = radius

    def set_side(self, new_side: float) -> None:
        self.side = new_side

    def get_side(self) -> float:
        return self.side
    
    def set_radius(self, new_radius) -> None:
        self.radius = new_radius

    def get_radius(self) -> float:
        return self.radius
    
    def perimeter_square_one_radius(self, side: float, radius: float) -> float:
        self.set_side(new_side=side)
        s = self.get_side()

        self.set_radius(new_radius=radius)
        r = self.get_radius()

        return round((2 * 3.1415 * r) + (4 * (s - (r * 2))), 2)

#Квадрат з 4 радіусами
class Square_four_Radius():

    def __init__(
            self,
            side: float = None,
            r1: float = None,
            r2: float = None,
            r3: float = None,
            r4: float = None
            ) -> None:
        self.side = side
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        
    def set_side(self, new_side: float) -> None:
        self.side = new_side
    
    def get_side(self) -> float:
        return self.side
    
    def set_r1(self, new_r: float) -> None:
        self.r1 = new_r

    def get_r1(self) -> float:
        return self.r1

    def set_r2(self, new_r: float) -> None:
        self.r2 = new_r

    def get_r2(self) -> float:
        return self.r2

    def set_r3(self, new_r: float) -> None:
        self.r3 = new_r

    def get_r3(self) -> float:
        return self.r3
    
    def set_r4(self, new_r: float) -> None:
        self.r4 = new_r

    def get_r4(self) -> float:
        return self.r4

    def perimeter_square_four_radius(self,
            side: float, 
            r1: float, 
            r2: float, 
            r3: float, 
            r4: float
            ) -> None:
        
        self.set_side(new_side=side)
        s = self.get_side()

        self.set_r1(new_r=r1)
        r1 = self.get_r1()

        self.set_r2(new_r=r2)
        r2 = self.get_r2()

        self.set_r3(new_r=r3)
        r3 = self.get_r3()

        self.set_r4(new_r=r4)
        r4 = self.get_r4()

        s1 = s - r1 - r2
        s2 = s - r2 - r3
        s3 = s - r3 - r4
        s4 = s - r4 - r1

        arc1 = r1 * 2 * 3.1415 * 0.25
        arc2 = r2 * 2 * 3.1415 * 0.25
        arc3 = r3 * 2 * 3.1415 * 0.25
        arc4 = r4 * 2 * 3.1415 * 0.25
        return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 1)

#Квадрат у колі
class Square_in_round():

    def __init__(self, side_sir: float = None, diameter_sir: float = None) -> None:
        self.side_sir = side_sir
        self.diameter_sir = diameter_sir

    def set_side_sir(self, new_side:float = None) -> None:
        self.side_sir = new_side
    
    def get_side_sir(self) -> float:
        return self.side_sir
    
    def set_diameter_sir(self, new_diameter) -> None:
        self.diameter_sir = new_diameter

    def get_diameter_sir(self) -> float:
        return self.diameter_sir

    def perimeter_square_in_round(self, side_sir: float, diameter_sir: float) -> float:

        self.set_side_sir(new_side=side_sir)
        s = self.get_side_sir()

        self.set_diameter_sir(new_diameter=diameter_sir)
        d = self.get_diameter_sir()

        m = round((((d ** 2) - (s ** 2)) ** 0.5), 4)
        c = round(d * 3.1415, 4)
        k_1 = m / 2
        l_ab = round((math.asin(k_1/(d * 0.5)) * 2) * (d / 2), 2)
        p =  round(((4 * m) + (c - (4 * l_ab))), 2)
        return p


#Прямокутник
class Rectangle():

    def __init__(self, side_1: float = None, side_2: float = None) -> None:
        self.side_a = side_1
        self.side_b = side_2 
        
    def set_side_a(self, new_side_a: float) -> None:
        self.side_a = new_side_a

    def get_side_a(self) -> float:
        return self.side_a
    
    def set_side_b(self, new_side_b: float) -> None:
        self.side_b = new_side_b

    def get_side_b(self) -> float:
        return self.side_b
    
    def perimeter_rectangle(self, side_a: float, side_b: float) -> float:

        self.set_side_a(new_side_a=side_a)
        s_a = self.get_side_a()

        self.set_side_b(new_side_b=side_b)
        s_b = self.get_side_b()

        return round((s_a * 2) + (s_b * 2), 2)

#Прямокутник з одним радіусом
class Rectangle_One_Radius():
    
    def __init__(self, side_a: float=None, side_b: float=None, radius: float=None) -> None:
        self.side_a: float = side_a
        self.side_b: float = side_b
        self.radius: float = radius

    def set_side_a(self, new_side_a: float) -> None:
        self.side_a = new_side_a

    def get_side_a(self) -> float:
        return self.side_a
    
    def set_side_b(self, new_side_b: float) -> None:
        self.side_b = new_side_b

    def get_side_b(self) -> float:
        return self.side_b
    
    def set_radius(self, new_radius: float) -> None:
        self.radius = new_radius
    
    def get_radius(self) -> float:
        return self.radius
    
    def parimeter_rectangle_one_radius(self, side_a: float, side_b: float, radius: float) -> float:

        self.set_side_a(new_side_a=side_a)
        s_a: float = self.get_side_a()

        self.set_side_b(new_side_b=side_b)
        s_b: float = self.get_side_b()

        self.set_radius(new_radius=radius)
        r: float = self.get_radius()

        return round((r * 2 * 3.1415) + ((s_a - (2 * r)) * 2) + ((s_b - (2 * r)) * 2), 2)

#Прямокутник з 4 радіусами
class Rectangel_Four_Radius():

    def __init__(
            self, 
            side_1: float = None, 
            side_2: float = None, 
            r1: float = None, 
            r2: float = None, 
            r3: float = None, 
            r4: float = None) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
    
    def set_side_1(self, new_side_1: float) -> None:
        self.side_1 = new_side_1

    def get_side_1(self) -> float:
        return self.side_1

    def set_side_2(self, new_side_2: float) -> None:
        self.side_2 = new_side_2

    def get_side_2(self) -> float:
        return self.side_2
    
    def set_r1(self, new_r1: float) -> None:
        self.r1 = new_r1

    def get_r1(self) -> float:
        return self.r1
    
    def set_r2(self, new_r2: float) -> None:
        self.r2 = new_r2

    def get_r2(self) -> float:
        return self.r2
    
    def set_r3(self, new_r3: float) -> None:
        self.r3 = new_r3

    def get_r3(self) -> float:
        return self.r3

    def set_r4(self, new_r4: float) -> None:
        self.r4 = new_r4

    def get_r4(self) -> float:
        return self.r4

    def perimeter_rectangle_four_radius(self,
            side_1: float,
            side_2: float, 
            r1: float, 
            r2: float, 
            r3: float, 
            r4: float
    ) -> float:
        
        self.set_side_1(new_side_1=side_1)
        s_1 = self.get_side_1()

        self.set_side_2(new_side_2=side_2)
        s_2 = self.get_side_2()

        self.set_r1(new_r1=r1)
        r_1 = self.get_r1()

        self.set_r2(new_r2=r2)
        r_2 = self.get_r2()

        self.set_r3(new_r3=r3)
        r_3 = self.get_r3()

        self.set_r4(new_r4=r4)
        r_4 = self.get_r4()

        s1 = s_1 - r_1 - r_2
        s2 = s_2 - r_2 - r_3
        s3 = s_1 - r_3 - r_4
        s4 = s_2 - r_4 - r_1

        arc1 = r_1 * 2 * 3.1415 * 0.25
        arc2 = r_2 * 2 * 3.1415 * 0.25
        arc3 = r_3 * 2 * 3.1415 * 0.25
        arc4 = r_4 * 2 * 3.1415 * 0.25

        return round(s1 + s2 + s3 + s4 + arc1 + arc2 + arc3 + arc4, 2)

#Шестикутник
class Hexagon():

    def __init__(self, a: float = None, h: float = None, d: float = None) -> None:
        self.a = a
        self.h = h
        self.d = d

    def set_a(self, new_a: float) -> None:
        self.a = new_a

    def get_a(self) -> float:
        return self.a
    
    def set_h(self, new_h: float) -> None:
        self.h = new_h

    def get_h(self) -> float:
        return self.h

    def set_d(self, new_d: float) -> None:
        self.d = new_d

    def get_d(self) -> float:
        return self.d


    def perimeter_hexagon_a(self, a: float) -> float:
        self.set_a(new_a=a)
        a_ = self.get_a()
        return round(a_ * 6, 2)
    
    def perimeter_hexagon_h(self, h: float) -> float:
        self.set_h(new_h=h)
        h_= self.get_h()
        return round(h_ * 0.5 / 0.866 * 6, 2)
    
    def perimeter_hexagon_d(self, d: float) -> float:
        self.set_d(new_d=d)
        d_ = self.get_d()
        return round(d_ * 0.5 * 6 , 2)

    #Сторона шестикутника по описаному діаметру кола
    def a_hexagon_d(self, d: float) -> float:
        self.set_d(new_d=d)
        d_ = self.get_d()
        return round(d_ * 0.5, 1)
    
    #Сторона шестикутника по відстані проміж паралельними сторонами
    def a_hexagon_h(self, h: float) -> float:
        self.set_h(new_h=h)
        h_ = self.get_h()
        return round(0.57735 * h, 2)

    #Відстань проміж паралельними сторонами по стороні
    def h_hexagon_a(self, a: float) -> float:
        self.set_a(new_a = a)
        a_ = self.get_a()
        return round((a_ / 0.57735), 2)

    #Відстань проміж паралельними сторонами по описаному діаметру кола
    def h_hexagon_d(self, d: float) -> float:
        self.set_d(new_d=d)
        d_ = self.get_d()
        return round((d_ * 0.866), 2)
    
    #Діаметр описаного кола по стороні
    def d_hexagon_a(self, a: float) -> float:
        self.set_a(new_a=a)
        a_ = self.get_a()
        return round((a_ * 2), 2)

    #Діаметр описаного кола по відстані проміж паралельними сторонами
    def d_hexagon_h(self, h: float) -> float:
        self.set_h(new_h =h)
        h_ = self.get_h()
        return round((h_ / 0.866), 2)
    
#Овал
class Oblong():

    def __init__(self, side_a: float=None, side_b: float=None) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def set_side_a(self, new_side_a: float) -> None:
        self.side_a = new_side_a

    def get_side_a(self) -> float:
        return self.side_a

    def set_side_b(self, new_side_b: float) -> None:
        self.side_b = new_side_b

    def get_side_b(self) -> float:
        return self.side_b

    def perimeter_oblong(self, side_a: float, side_b: float) -> float:
        self.set_side_a(new_side_a=side_a)
        s_a = self.get_side_a()

        self.set_side_b(new_side_b=side_b)
        s_b = self.get_side_b()

        return round((((s_a - s_b) * 2)+ (s_b * 3.1415)), 2)

#Рівносторонній трикутник
class Equilateral_triangle():

    def __init__(self, side: float = None, height: float = None) -> None:
        self.side = side
        self.height = height

    def set_side(self, new_side: float) ->None:
        self.side = new_side
    
    def get_side(self) -> float:
        return self.side
    
    def set_height(self, new_height: float) -> None:
        self.height = new_height

    def get_height(self) -> float:
        return self.height
    


    def perim_eq_tr_side(self, side: float) -> float:
        self.set_side(new_side=side)
        s = self.get_side()
        return round((3 * s), 2)

    def perim_eq_tr_height(self, height: float) -> float:
        self.set_height(new_height=height)
        h = self.get_height()
        return round((h / 0.866) * 3, 2)

    def side_eq_tr_height(self, height: float) -> float:
        self.set_height(new_height=height)
        h = self.get_height()
        return round((h / 0.866) , 2)

    def height_eq_tr_side(self, side: float) -> float:
        self.set_side(new_side=side)
        s = self.get_side()
        return round((s * 0.866), 2)

#Рівнобедрений трикутник
class Isosceles_triangle():

    def __init__(self, side_a: float, side_b: float, height: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.height = height

    def set_side_a(self, new_side_a: float) -> None:
        self.side_a = new_side_a

    def get_side_a(self) -> float:
        return self.get_side_a

    def set_side_b(self, new_side_b: float) -> None:
        self.side_b = new_side_b

    def get_side_b(self) -> float:
        return self.get_side_b
    
    def set_height(self, new_height: float) -> None:
        self.height = new_height

    def get_height(self) -> float:
        return self.height
    

    def perim_is_tr_side_a_b(self, side_a: float, side_b: float) -> float:
        
        self.set_side_a(new_side_a=side_a)
        s_a = self.get_side_a()

        self.set_side_b(new_side_b=side_b)
        s_b = self.get_side_b()

        return round((2 * s_a + s_b), 2)
    
    def perim_is_tr_height_side_b(self, height: float, side_b: float) -> float:

        self.set_height(new_height=height)
        h = self.get_side_a()

        self.set_side_b(new_side_b=side_b)
        s_b = self.get_side_b()

        return round(2 * ((h ** 2 + (s_b * 0.5) ** 2) ** 0.5) + s_b, 2)
    
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