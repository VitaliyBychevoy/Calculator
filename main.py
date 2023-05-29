import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as gui

import geometry as g

material = {
    "Алюміній": 0.5,
    "Мідь": 0.57,
    "Сталь звичайна": 1,
    "Сталь нержавіюча": 1.5
 }

exceptable_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']

zero = ['0', '0,0', '0.0','']

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 330, 300)
        self.setWindowTitle("Calculator")

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.perimeter_lalel = QLabel("Периметр", self)
        self.perimeter_lalel.setGeometry(10, 50, 100, 20)

        #Значення периметра
        self.perimeter_velue = QLineEdit("0.0", self)
        self.perimeter_velue.setGeometry(120, 50, 40, 20)

        #Розмірність периметра
        self.mm_label_perimeter = QLabel("мм", self)
        self.mm_label_perimeter.setGeometry(165, 50, 40, 20)

        #Статус введенного периметра
        self.message_perimeter = QLabel(None, self)
        self.message_perimeter.setGeometry(190, 50, 150, 20)
        if self.perimeter_velue.text() in zero:
            self.message_perimeter.setText("Відсутнє значення")

        #ТОВЩИНА
        #Заголовок товщини       
        self.thickness_label = QLabel("Товщина матеріала", self)
        self.thickness_label.setGeometry(10, 75, 100, 20)

        #Значення товщини
        self.thickness_velue = QLineEdit("0.0", self)
        self.thickness_velue.setGeometry(120, 75, 40, 20)

        #Розмірність товщини
        self.mm_label_thickness = QLabel("мм", self)
        self.mm_label_thickness.setGeometry(165, 75, 40, 20)
        
        #Статус введенної товщини
        self.message_thickness = QLabel(None, self)
        self.message_thickness.setGeometry(190, 75, 150, 20)
        if self.thickness_velue.text() in zero:
            self.message_thickness.setText("Відсутнє значення")

        #МАТЕРІАЛ
        #Заголовок матеріала
        self.material_label = QLabel("Оберіть матеріал", self)
        self.material_label.setGeometry(10, 100, 100, 20)

        #Список матеріалів
        self.material = QComboBox(self)
        self.material.addItem("Сталь звичайна")
        self.material.addItem("Сталь нержавіюча")
        self.material.addItem("Алюміній")
        self.material.addItem("Мідь")
        self.material.setGeometry(120, 100, 200, 20)

        #ОТВОРИ
        #Заголовок отворів
        self.amount_holes_label = QLabel("Кількість отворів", self)
        self.amount_holes_label.setGeometry(10, 125, 100, 20)

        #Список отворів
        self.amount_holes = QComboBox(self)
        for i in range(1, 21):
            self.amount_holes.addItem(str(i))
        self.amount_holes.setGeometry(120, 125, 40, 20)

        #КНОПКА ДЛЯ РОЗРАХУВАННЯ ЗУСИЛЛЯ
        self.btn = QPushButton("Розрахувати", self)
        self.btn.setGeometry(120, 150, 200, 20)
        self.btn.clicked.connect(self.calculate_tonage_new)


        #ОТРИМАНЕ ЗУСИЛЛЯ
        #Заголовок зусилля
        self.force_result_label = QLabel("Небхідне зусилля", self)
        self.force_result_label.setGeometry(10, 175, 100, 20)

        #Значеня зусилля
        self.force_result_value = QLineEdit('?', self)
        self.force_result_value.setGeometry(120, 175, 40, 20)

        #Розмірність зусилля
        self.tonage_label_force = QLabel("тонн(и)", self)
        self.tonage_label_force.setGeometry(165, 175, 40, 20)


        #ФОРМІ
        #Заголовок форми
        self.force_result_label = QLabel("Форма", self)
        self.force_result_label.setGeometry(10, 20, 40, 20)

        #Cписок форм
        self.shape = QComboBox(self)
        self.shape.addItem("")
        self.shape.addItem("Коло")
        # self.shape.addItem("Напівколо")
        self.shape.addItem("Квадрат")
        self.shape.addItem("Квадрат з однаковими радіусами")
        self.shape.addItem("Квадрат з різними радіусами")
        # self.shape.addItem("Квадрат у колі")
        self.shape.addItem("Прямокутник")
        self.shape.addItem("Прямокутник з однаковими радіусами")
        self.shape.addItem("Прямокутник з різними радіусами")
        self.shape.addItem("Шестигранник")
        self.shape.addItem("Овал з паралельними сторонами")
        self.shape.addItem("Трикутник рівносторонній")
        self.shape.addItem("Трикутник рівнобедрений")        
        self.shape.setGeometry(60, 20, 260, 25)
        self.shape.currentTextChanged.connect(self.shape_handler)

    #Розрахунок навантаження
    def calculate_tonage_new(self):
        coeff_material = self.coefficient_material()

        if self.perimeter_velue.text() == '':
            perimeter_number: str = "0.0"
            self.perimeter_velue.setText("0.0")
        else:
            perimeter_number = self.perimeter_velue.text()
        perimeter_list = self.check_number_new(perimeter_number)


        if self.thickness_velue.text() == '':
            thickness_number: str = "0.0"
            self.thickness_velue.setText("0.0")
        else:
            thickness_number = self.thickness_velue.text()
        thickness_list = self.check_number_new(thickness_number)

        self.message_perimeter.setText(perimeter_list[1])
        self.message_thickness.setText(thickness_list[1])

        if perimeter_list[0] == 0 and thickness_list[0] != 0:
            self.force_result_value.setText("?")
        elif thickness_list[0] == 0 and perimeter_list[0] != 0:
            self.force_result_value.setText("?")
        elif thickness_list[0] == 0 and perimeter_list[0] == 0:
            self.force_result_value.setText("?")
        else:
            result = 0.0352 * coeff_material
            result = result * perimeter_list[0]
            result = result * thickness_list[0]
            result = round(result * float(self.amount_holes.currentText()), 2)
            self.force_result_value.setText(str(result))
        
    #Функція вертає коефіцієнт матеріала
    def coefficient_material(self) -> float:
        coeff = 0.0
        coeff = material[self.material.currentText()]
        return coeff

    #Перевіряємо числові дані, які вводив користувач 
    def check_number_new(self,item_string: str) -> list:
        result = [0, "Валідне знячення"]
        item_string = item_string.strip()
        if item_string in zero:
            result[0] = 0
            result[1] = "Відсутнє значення"
            return result
        
        for letter in item_string:
            if letter not in exceptable_number:
                result[0] = 0
                message = f'"{letter}" э не коректний символ'
                result[1] = message
                return result
        comma_count = item_string.count(",")
        if comma_count > 1:
            result[0] = 0
            result[1] = "Забагато ком"
            return result
        
        dot_count = item_string.count(".")
        if dot_count > 1:
            result[0] = 0
            result[1] = "Забагато крапок"
            return result
        
        result[1] = "Валідне знячення"
        if "," in item_string:
            item_string = item_string.replace(",", ".")
        
        result[0] = float(item_string)
        return result

    #Обробка списку форм
    def shape_handler(self):
        shape: str = self.shape.currentText()
        if shape == "Коло":
            self.round_handler(shape)
        elif shape == "Напівколо":            
            self.half_round_heandler(shape)
        elif shape == "Квадрат":
            self.square(shape)
        elif shape == "Квадрат з однаковими радіусами":
            self.square_one_radius(shape)
        elif shape == "Квадрат з різними радіусами":
            self.square_four_radius(shape)
        elif shape == "Квадрат у колі":
            self.square_in_round(shape)
        elif shape == "Прямокутник":
            self.rectangle(shape)
        elif shape == "Прямокутник з однаковими радіусами":
            self.rectangle_one_round(shape)
        elif shape == "Прямокутник з різними радіусами":
            self.rectangle_four_round(shape)
        elif shape == "Шестигранник":
            self.hexagon(shape)
        elif shape == "Овал з паралельними сторонами":
            self.oblong(shape)
        elif shape == "Трикутник рівносторонній":
            self.equilateral_triangle(shape)
        elif shape == "Трикутник рівнобедрений":
            self.isosceles_triangle(shape)



    #КОЛО
    #Вікно для кола
    def round_handler(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(120, 10, 200, 20)

        #ДІАМЕТР
        #Заголовок диаметра
        self.diameter_lalel = QLabel("D", self.window_shape)
        self.diameter_lalel.setGeometry(10, 50, 10, 20)

        #Значення диаметра
        self.diameter_velue = QLineEdit("0.0", self.window_shape)
        self.diameter_velue.setGeometry(25, 50, 40, 20)

        #Розмірність диаметра
        self.mm_label_d = QLabel("мм", self.window_shape)
        self.mm_label_d.setGeometry(70, 50, 40, 20)

        #Статус діаметра         
        self.message_diameter = QLabel(None, self.window_shape)
        self.message_diameter.setGeometry(100, 50, 150, 20)
        if self.diameter_velue.text() in zero:
            self.message_diameter.setText("Відсутнє значення")
        
        #Кнопка розрахунку
        self.btn_d = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_d.setGeometry(10, 80, 200, 25)
        self.btn_d.clicked.connect(self.perim_round)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметер кола", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 110, 90, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(105, 110, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(140, 110, 20, 20)

        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 140, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)


        self.window_shape.show()
    #Периметер кола  
    def perim_round(self):
        if self.diameter_velue.text() in zero:
            self.diameter_velue.setText("0.0")
            self.perimeter.setText("?")
            self.message_diameter.setText("Відсутнє значення")
        else:
            diameter_list_d = self.check_number_new(self.diameter_velue.text())
            self.message_diameter.setText(diameter_list_d[1])

            if diameter_list_d[0] == 0:
                self.perimeter.setText("?")
            else:
                self.perimeter.setText(str(g.Perimeter.round(float(diameter_list_d[0]))))
    #КІНЕУЬ КОЛО

    #НАПІВКОЛО
    def half_round_heandler(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    #КВАДРАТ
    #Вікно квадрата
    def square(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(120, 10, 200, 20)
        
        #Сторона
        #Заголовок сторони
        self.side_lalel = QLabel("A", self.window_shape)
        self.side_lalel.setGeometry(10, 50, 10, 20)

        #Значення диаметра
        self.side_velue = QLineEdit("0.0", self.window_shape)
        self.side_velue.setGeometry(25, 50, 40, 20)

        #Розмірність диаметра
        self.mm_label_side = QLabel("мм", self.window_shape)
        self.mm_label_side.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_side = QLabel(None, self.window_shape)
        self.message_side.setGeometry(100, 50, 150, 20)
        if self.side_velue.text() in zero:
            self.message_side.setText("Відсутнє значення")        

        #Кнопка розрахунку
        self.btn_s = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_s.setGeometry(10, 80, 200, 25)
        self.btn_s.clicked.connect(self.perim_square)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 110, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 110, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 110, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 140, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()

    #Периметр квадрата
    def perim_square(self) -> None:
        square_list = self.check_number_new(self.side_velue.text())
        self.message_side.setText(square_list[1])

        if square_list[0] == 0:
            self.perimeter.setText("?")
        else:
            self.perimeter.setText(str(g.Perimeter.square(float(square_list[0]))))                        
    #КІНЕЦЬ КВАДРАТ

    #КВАДРАТ З ОДНАКОВИМИ РАДІУСАМИ
    #Вікно квадрата з однаковими радіусами
    def square_one_radius(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)


        #Сторона 
        #Заголовок сторони
        self.side_one_round_square_lalel = QLabel("A", self.window_shape)
        self.side_one_round_square_lalel.setGeometry(10, 50, 10, 20)

        #Значення сторони
        self.side_one_round_square_velue = QLineEdit("0.0", self.window_shape)
        self.side_one_round_square_velue.setGeometry(25, 50, 40, 20)

        #Розмірність сторони
        self.mm_label_side_one_round_square = QLabel("мм", self.window_shape)
        self.mm_label_side_one_round_square.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_side_one_round_square = QLabel(None, self.window_shape)
        self.message_side_one_round_square.setGeometry(100, 50, 150, 20)
        if self.side_one_round_square_velue.text() in zero:
            self.message_side_one_round_square.setText("Відсутнє значення")

        #Радіус
        #Заголовок радіуса
        self.radius_one_round_square_lalel = QLabel("R", self.window_shape)
        self.radius_one_round_square_lalel.setGeometry(10, 80, 10, 20)

        #Значення радіуса
        self.radius_one_round_square_velue = QLineEdit("0.0", self.window_shape)
        self.radius_one_round_square_velue.setGeometry(25, 80, 40, 20)

        #Розмірність радіуса
        self.mm_label_radius_one_round_square = QLabel("мм", self.window_shape)
        self.mm_label_radius_one_round_square.setGeometry(70, 80, 40, 20)

        #Статус радіуса       
        self.message_radius_one_round_square = QLabel(None, self.window_shape)
        self.message_radius_one_round_square.setGeometry(100, 80, 150, 20)
        if self.radius_one_round_square_velue.text() in zero:
            self.message_radius_one_round_square.setText("Відсутнє значення")

        #Кнопка розрахунку
        self.btn_square_one_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_square_one_radius.setGeometry(10, 110, 200, 25)
        self.btn_square_one_radius.clicked.connect(self.perim_square_one_radius)
        
        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.label_square_one_radius_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.label_square_one_radius_peremeter.setGeometry(15, 140, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 140, 40, 20)

        #Розмірність периметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 140, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 170, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.window_shape.show()
    
    #Периметер квадрата з однаковими радіусами
    def perim_square_one_radius(self):

        side_list_qor = self.check_number_new(self.side_one_round_square_velue.text())
        radius_list_qor = self.check_number_new(self.radius_one_round_square_velue.text())

        self.message_side_one_round_square.setText(side_list_qor[1])
        self.message_radius_one_round_square.setText(radius_list_qor[1])        

        if side_list_qor[0] != 0 and radius_list_qor[0] != 0:
            if side_list_qor[0] - (2 * radius_list_qor[0]) < 5:
                self.message_radius_one_round_square.setText("Завеликий радіус")
                self.perimeter.setText("?")
            else:
                print(side_list_qor[0], " ", type(side_list_qor[0]))
                print(radius_list_qor[0], " ", type(radius_list_qor[0]))
                self.perimeter.setText(str(g.Perimeter.square_one_radius(side_list_qor[0], radius_list_qor[0])))
                #self.perimeter.setText(str(g.Perimeter.rectangle(side_a_list[0], side_b_list[0]))) 
        else:
            self.perimeter.setText("?")
        pass
    #КІНЕЦЬ КВАДРАТ З ОДНАКОВИМИ РАДІУСАМИ

    #КВАДРАТ З РІЗНИМИ РАДІУСАМИ
    #Вікно квадрата з різними радіусами
    def square_four_radius(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        #Сторона 
        #Заголовок сторони
        self.side_four_radius_lalel = QLabel("A", self.window_shape)
        self.side_four_radius_lalel.setGeometry(10, 50, 10, 20)

        #Значення сторони
        self.side_four_radius_lalel_velue = QLineEdit("0.0", self.window_shape)
        self.side_four_radius_lalel_velue.setGeometry(25, 50, 40, 20)

        #Розмірність сторони
        self.mm_label_side_four_radius_lalel = QLabel("мм", self.window_shape)
        self.mm_label_side_four_radius_lalel.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_side_side_four_radius = QLabel(None, self.window_shape)
        self.message_side_side_four_radius.setGeometry(100, 50, 150, 20)
        if self.message_side_side_four_radius.text() in zero:
            self.message_side_side_four_radius.setText("Відсутнє значення")

        #Радіус R1
        #Заголовок радіуса
        self.r1_square_lalel = QLabel("R1", self.window_shape)
        self.r1_square_lalel.setGeometry(10, 80, 20, 20)

        #Значення радіуса
        self.r1_square_velue = QLineEdit("0.0", self.window_shape)
        self.r1_square_velue.setGeometry(25, 80, 40, 20)

        #Розмірність радіуса
        self.mm_label_r1 = QLabel("мм", self.window_shape)
        self.mm_label_r1.setGeometry(70, 80, 40, 20)

        #Статус радіуса       
        self.message_r1_square = QLabel(None, self.window_shape)
        self.message_r1_square.setGeometry(100, 80, 150, 20)
        if self.r1_square_velue.text() in zero:
            self.message_r1_square.setText("Відсутнє значення")

        #Радіус R2
        #Заголовок радіуса
        self.r2_square_lalel = QLabel("R2", self.window_shape)
        self.r2_square_lalel.setGeometry(10, 110, 20, 20)

        #Значення радіуса
        self.r2_square_velue = QLineEdit("0.0", self.window_shape)
        self.r2_square_velue.setGeometry(25, 110, 40, 20)

        #Розмірність радіуса
        self.mm_label_r2 = QLabel("мм", self.window_shape)
        self.mm_label_r2.setGeometry(70, 110, 40, 20)

        #Статус радіуса       
        self.message_r2_square = QLabel(None, self.window_shape)
        self.message_r2_square.setGeometry(100, 110, 150, 20)
        if self.r2_square_velue.text() in zero:
            self.message_r2_square.setText("Відсутнє значення")

        #Радіус R3
        #Заголовок радіуса
        self.r3_square_lalel = QLabel("R3", self.window_shape)
        self.r3_square_lalel.setGeometry(10, 140, 20, 20)

        #Значення радіуса
        self.r3_square_velue = QLineEdit("0.0", self.window_shape)
        self.r3_square_velue.setGeometry(25, 140, 40, 20)

        #Розмірність радіуса
        self.mm_label_r3 = QLabel("мм", self.window_shape)
        self.mm_label_r3.setGeometry(70, 140, 40, 20)

        #Статус радіуса       
        self.message_r3_square = QLabel(None, self.window_shape)
        self.message_r3_square.setGeometry(100, 140, 150, 20)
        if self.r3_square_velue.text() in zero:
            self.message_r3_square.setText("Відсутнє значення")

        #Радіус R4
        #Заголовок радіуса
        self.r4_square_lalel = QLabel("R4", self.window_shape)
        self.r4_square_lalel.setGeometry(10, 170, 20, 20)

        #Значення радіуса
        self.r4_square_velue = QLineEdit("0.0", self.window_shape)
        self.r4_square_velue.setGeometry(25, 170, 40, 20)

        #Розмірність радіуса
        self.mm_label_r4 = QLabel("мм", self.window_shape)
        self.mm_label_r4.setGeometry(70, 170, 40, 20)

        #Статус радіуса       
        self.message_r4_square = QLabel(None, self.window_shape)
        self.message_r4_square.setGeometry(100, 170, 150, 20)
        if self.r4_square_velue.text() in zero:
            self.message_r4_square.setText("Відсутнє значення")            
        
        #Кнопка розрахунку
        self.btn_square_four_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_square_four_radius.setGeometry(10, 200, 200, 25)
        self.btn_square_four_radius.clicked.connect(self.perim_square_four_radius)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_sfr_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_sfr_peremeter.setGeometry(15, 230, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 230, 40, 20)
        
        #Розмірність приметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 230, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 260, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()

    #Периметер квадрата з різними радіусами
    def perim_square_four_radius(self) -> None:

        side_sfr_list = self.check_number_new(self.side_four_radius_lalel_velue.text())
        r1_sfr_list = self.check_number_new(self.r1_square_velue.text())
        r2_sfr_list = self.check_number_new(self.r2_square_velue.text())
        r3_sfr_list = self.check_number_new(self.r3_square_velue.text())
        r4_sfr_list = self.check_number_new(self.r4_square_velue.text())

        self.message_side_side_four_radius.setText(side_sfr_list[1])
        self.message_r1_square.setText(r1_sfr_list[1]) 
        self.message_r2_square.setText(r2_sfr_list[1])
        self.message_r3_square.setText(r3_sfr_list[1])
        self.message_r4_square.setText(r4_sfr_list[1])

        if side_sfr_list[0] != 0 and r1_sfr_list[0] != 0 and r2_sfr_list[0] != 0 and r3_sfr_list[0] != 0 and r4_sfr_list[0] != 0:
            s1 = side_sfr_list[0] - r1_sfr_list[0] - r2_sfr_list[0]
            s2 = side_sfr_list[0] - r2_sfr_list[0] - r3_sfr_list[0]
            s3 = side_sfr_list[0] - r3_sfr_list[0] - r4_sfr_list[0]
            s4 = side_sfr_list[0] - r4_sfr_list[0] - r1_sfr_list[0]
            if s1 < 5 or s2 < 5 or s3 < 5 or s4 < 5:
                if s1 < 5:
                    self.perimeter.setText('?')
                    self.message_r1_square.setText("Завеликий радіус")
                    self.message_r2_square.setText("Завеликий радіус")
                if s2 < 5:
                    self.perimeter.setText('?')
                    self.message_r2_square.setText("Завеликий радіус")
                    self.message_r3_square.setText("Завеликий радіус")
                if s3 < 5:
                    self.perimeter.setText('?')
                    self.message_r3_square.setText("Завеликий радіус")
                    self.message_r4_square.setText("Завеликий радіус")
                if s4 < 5:
                    self.perimeter.setText('?')
                    self.message_r4_square.setText("Завеликий радіус")
                    self.message_r1_square.setText("Завеликий радіус")
            else:
                self.mm_result_perimeret.setGeometry(170, 230, 20, 20)
                self.perimeter.setText(str(g.Perimeter.square_four_radius(
                    side_sfr_list[0], 
                    r1_sfr_list[0],
                    r2_sfr_list[0],
                    r3_sfr_list[0],
                    r4_sfr_list[0]
                    )))                           
        else:
            self.perimeter.setText('?')
    #КІНЕЦЬ КВАДРАТ З РІЗНИМИ РАДІУСАМИ
    
    def square_in_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    #ПРЯМОКУТНИК
    #вікно прямокутника
    def rectangle(self, shape: str) -> None:        
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(120, 10, 200, 20)

        #Сторона A
        #Заголовок сторони
        self.side_a_lalel = QLabel("A", self.window_shape)
        self.side_a_lalel.setGeometry(10, 50, 10, 20)

        #Значення сторони
        self.side_a_velue = QLineEdit("0.0", self.window_shape)
        self.side_a_velue.setGeometry(25, 50, 40, 20)

        #Розмірність сторони
        self.mm_label_side_a = QLabel("мм", self.window_shape)
        self.mm_label_side_a.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_side_a = QLabel(None, self.window_shape)
        self.message_side_a.setGeometry(100, 50, 150, 20)
        if self.side_a_velue.text() in zero:
            self.message_side_a.setText("Відсутнє значення") 
        
        #Сторона B
        #Заголовок сторони
        self.side_b_lalel = QLabel("B", self.window_shape)
        self.side_b_lalel.setGeometry(10, 80, 10, 20)

        #Значення сторони
        self.side_b_velue = QLineEdit("0.0", self.window_shape)
        self.side_b_velue.setGeometry(25, 80, 40, 20)

        #Розмірність сторони
        self.mm_label_side_b = QLabel("мм", self.window_shape)
        self.mm_label_side_b.setGeometry(70, 80, 40, 20)

        #Статус сторони       
        self.message_side_b = QLabel(None, self.window_shape)
        self.message_side_b.setGeometry(100, 80, 150, 20)
        if self.side_b_velue.text() in zero:
            self.message_side_b.setText("Відсутнє значення") 

        #Кнопка розрахунку
        self.btn_rectangle = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_rectangle.setGeometry(10, 110, 200, 25)
        self.btn_rectangle.clicked.connect(self.perim_rectangle)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_rect_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_rect_peremeter.setGeometry(15, 140, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 140, 40, 20)
        
        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 140, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 170, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show() 

    #Периметер прямокутника
    def perim_rectangle(self):

        side_a_list = self.check_number_new(self.side_a_velue.text())
        side_b_list = self.check_number_new(self.side_b_velue.text())

        self.message_side_a.setText(side_a_list[1])
        self.message_side_b.setText(side_b_list[1])

        if side_a_list[0] != 0 and side_b_list[0] != 0:
            self.perimeter.setText(str(g.Perimeter.rectangle(side_a_list[0], side_b_list[0]))) 
        else:
            self.perimeter.setText("?")                      
    #КІНЕЦЬ ПРЯМОКУТНИК

    #ПРЯМОКУТНИК З ОДНИМ РАДІУСОМ
    #Вікно прямокутника з одним радіусом
    def rectangle_one_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(50, 10, 200, 20)

        #Сторона A
        #Заголовок сторони а
        self.side_a_lalel_req = QLabel("A", self.window_shape)
        self.side_a_lalel_req.setGeometry(10, 50, 10, 20)

        #Значення сторони а
        self.side_a_velue_req = QLineEdit("0.0", self.window_shape)
        self.side_a_velue_req.setGeometry(25, 50, 40, 20)

        #Розмірність сторони а
        self.mm_label_side_a_req = QLabel("мм", self.window_shape)
        self.mm_label_side_a_req.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_side_a_req = QLabel(None, self.window_shape)
        self.message_side_a_req.setGeometry(100, 50, 150, 20)
        if self.side_a_velue_req.text() in zero:
            self.message_side_a_req.setText("Відсутнє значення")

        #Сторона B
        #Заголовок сторони
        self.side_b_lalel_req = QLabel("B", self.window_shape)
        self.side_b_lalel_req.setGeometry(10, 80, 10, 20)

        #Значення сторони
        self.side_b_velue_req = QLineEdit("0.0", self.window_shape)
        self.side_b_velue_req.setGeometry(25, 80, 40, 20)

        #Розмірність сторони
        self.mm_label_side_b_req = QLabel("мм", self.window_shape)
        self.mm_label_side_b_req.setGeometry(70, 80, 40, 20)

        #Статус сторони       
        self.message_side_b_req = QLabel(None, self.window_shape)
        self.message_side_b_req.setGeometry(100, 80, 150, 20)
        if self.side_b_velue_req.text() in zero:
            self.message_side_b_req.setText("Відсутнє значення")

        #РАДІУС
        #Заголовок радіуса
        self.r_lalel_req = QLabel("R", self.window_shape)
        self.r_lalel_req.setGeometry(10, 110, 10, 20)

        #Значення радіуса
        self.r_velue_req = QLineEdit("0.0", self.window_shape)
        self.r_velue_req.setGeometry(25, 110, 40, 20)

        #Розмірність радіуса
        self.mm_label_r = QLabel("мм", self.window_shape)
        self.mm_label_r.setGeometry(70, 110, 40, 20)

        #Статус радіуса       
        self.message_side_r_req = QLabel(None, self.window_shape)
        self.message_side_r_req.setGeometry(100, 110, 150, 20)
        if self.r_velue_req.text() in zero:
            self.message_side_r_req.setText("Відсутнє значення")

        #Кнопка розрахунку
        self.btn_s_req = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_s_req.setGeometry(10, 140, 200, 25)
        self.btn_s_req.clicked.connect(self.req_one_radius)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter_req = QLabel("Периметер квадрата", self.window_shape)
        self.Label_s_peremeter_req.setGeometry(15, 170, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 170, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret_req = QLabel("мм", self.window_shape)
        self.mm_result_perimeret_req.setGeometry(160, 170, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter_req = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter_req.setGeometry(10, 200, 200, 25)
        self.btn_add_perimeter_req.clicked.connect(self.add_value)
        self.window_shape.show()
    
    #Периметр прямокутника с однаковими радіусами
    def req_one_radius(self):
        side_a_req_list = self.check_number_new(self.side_a_velue_req.text()) 
        side_b_req_list = self.check_number_new(self.side_b_velue_req.text())
        side_r_req_list = self.check_number_new(self.r_velue_req.text())


        self.message_side_a_req.setText(side_a_req_list[1])
        self.message_side_b_req.setText(side_b_req_list[1])
        self.message_side_r_req.setText(side_r_req_list[1])

        d = 2 * side_r_req_list[0]

        if side_a_req_list[0] != 0 and side_b_req_list[0] != 0 and side_r_req_list[0] != 0:
            if side_r_req_list[0] > side_a_req_list[0] and side_r_req_list[0] > side_b_req_list[0]:
                self.message_side_r_req.setText("Завеликий радіус")
                self.perimeter.setText("?")
            elif side_a_req_list[0] <= side_b_req_list[0] and (side_a_req_list[0] - d) < 5:
                self.message_side_r_req.setText("Завеликий радіус")
                self.perimeter.setText("?")
            elif side_b_req_list[0] <= side_a_req_list[0] and (side_b_req_list[0] - d) < 5:
                self.message_side_r_req.setText("Завеликий радіус")
                self.perimeter.setText("?")                
            else:
                print(side_a_req_list[0], " ", type(side_a_req_list[0]))
                print(side_b_req_list[0], " ", type(side_b_req_list[0]))
                print(side_r_req_list[0], " ", type(side_r_req_list[0]))
                self.perimeter.setText(str(g.Perimeter.rectangle_one_radius(side_a_req_list[0], side_b_req_list[0], side_r_req_list[0])))
        else:
            self.perimeter.setText("?")
    #КІНЕЦЬ ПРЯМОКУТНИК З ОДНИМ РАДІУСОМ

    #ПРЯМОКУТНИК З РІНИМИ РАДИУСАМИ
    #Вікно прямокутника з різними радіусами
    def rectangle_four_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(80, 10, 200, 20)

        #Сторона A
        #Заголовок сторони
        self.side_a_four_radius_lalel_rfr = QLabel("A", self.window_shape)
        self.side_a_four_radius_lalel_rfr.setGeometry(10, 30, 10, 20)

        #Значення сторони
        self.side_a_four_radius_lalel_velue = QLineEdit("0.0", self.window_shape)
        self.side_a_four_radius_lalel_velue.setGeometry(25, 30, 40, 20)

        #Розмірність сторони
        self.mm_label_side_a_four_radius_lalel = QLabel("мм", self.window_shape)
        self.mm_label_side_a_four_radius_lalel.setGeometry(70, 30, 40, 20)

        #Статус сторони       
        self.message_side_a_four_radius = QLabel(None, self.window_shape)
        self.message_side_a_four_radius.setGeometry(100, 30, 150, 20)
        if self.message_side_a_four_radius.text() in zero:
            self.message_side_a_four_radius.setText("Відсутнє значення")

        #Сторона B
        #Заголовок сторони
        self.side_b_four_radius_lalel_rfr = QLabel("B", self.window_shape)
        self.side_b_four_radius_lalel_rfr.setGeometry(10, 60, 10, 20)

        #Значення сторони
        self.side_b_four_radius_lalel_velue = QLineEdit("0.0", self.window_shape)
        self.side_b_four_radius_lalel_velue.setGeometry(25, 60, 40, 20)

        #Розмірність сторони
        self.mm_label_side_b_four_radius_lalel = QLabel("мм", self.window_shape)
        self.mm_label_side_b_four_radius_lalel.setGeometry(70, 60, 40, 20)

        #Статус сторони       
        self.message_side_b_four_radius = QLabel(None, self.window_shape)
        self.message_side_b_four_radius.setGeometry(100, 60, 150, 20)
        if self.message_side_b_four_radius.text() in zero:
            self.message_side_b_four_radius.setText("Відсутнє значення")

        #Радіус R1
        #Заголовок радіуса
        self.r1_square_lalel_rfr = QLabel("R1", self.window_shape)
        self.r1_square_lalel_rfr.setGeometry(10, 90, 20, 20)

        #Значення радіуса
        self.r1_square_velue_rfr = QLineEdit("0.0", self.window_shape)
        self.r1_square_velue_rfr.setGeometry(25, 90, 40, 20)

        #Розмірність радіуса
        self.mm_label_r1_rfr = QLabel("мм", self.window_shape)
        self.mm_label_r1_rfr.setGeometry(70, 90, 40, 20)

        #Статус радіуса       
        self.message_r1_square_rfr = QLabel(None, self.window_shape)
        self.message_r1_square_rfr.setGeometry(100, 90, 150, 20)
        if self.r1_square_velue_rfr.text() in zero:
            self.message_r1_square_rfr.setText("Відсутнє значення")

        #Радіус R2
        #Заголовок радіуса
        self.r2_square_lalel_rfr = QLabel("R2", self.window_shape)
        self.r2_square_lalel_rfr.setGeometry(10, 120, 20, 20)

        #Значення радіуса
        self.r2_square_velue_rfr = QLineEdit("0.0", self.window_shape)
        self.r2_square_velue_rfr.setGeometry(25, 120, 40, 20)

        #Розмірність радіуса
        self.mm_label_r2_rfr= QLabel("мм", self.window_shape)
        self.mm_label_r2_rfr.setGeometry(70, 120, 40, 20)

        #Статус радіуса       
        self.message_r2_square_rfr = QLabel(None, self.window_shape)
        self.message_r2_square_rfr.setGeometry(100, 120, 150, 20)
        if self.r2_square_velue_rfr.text() in zero:
            self.message_r2_square_rfr.setText("Відсутнє значення")

        #Радіус R3
        #Заголовок радіуса
        self.r3_square_lalel_rfr = QLabel("R3", self.window_shape)
        self.r3_square_lalel_rfr.setGeometry(10, 150, 20, 20)

        #Значення радіуса
        self.r3_square_velue_rfr = QLineEdit("0.0", self.window_shape)
        self.r3_square_velue_rfr.setGeometry(25, 150, 40, 20)

        #Розмірність радіуса
        self.mm_label_r3_rfr = QLabel("мм", self.window_shape)
        self.mm_label_r3_rfr.setGeometry(70, 150, 40, 20)

        #Статус радіуса       
        self.message_r3_square_rfr = QLabel(None, self.window_shape)
        self.message_r3_square_rfr.setGeometry(100, 150, 150, 20)
        if self.r3_square_velue_rfr.text() in zero:
            self.message_r3_square_rfr.setText("Відсутнє значення")

        #Радіус R4
        #Заголовок радіуса
        self.r4_square_lalel_rfr = QLabel("R4", self.window_shape)
        self.r4_square_lalel_rfr.setGeometry(10, 180, 20, 20)

        #Значення радіуса
        self.r4_square_velue_rfr = QLineEdit("0.0", self.window_shape)
        self.r4_square_velue_rfr.setGeometry(25, 180, 40, 20)

        #Розмірність радіуса
        self.mm_label_r4_rfr = QLabel("мм", self.window_shape)
        self.mm_label_r4_rfr.setGeometry(70, 180, 40, 20)

        #Статус радіуса       
        self.message_r4_square_rfr = QLabel(None, self.window_shape)
        self.message_r4_square_rfr.setGeometry(100, 180, 150, 20)
        if self.r4_square_velue_rfr.text() in zero:
            self.message_r4_square_rfr.setText("Відсутнє значення")            
        
        #Кнопка розрахунку
        self.btn_rectangle_four_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_rectangle_four_radius.setGeometry(10, 210, 200, 25)
        self.btn_rectangle_four_radius.clicked.connect(self.perim_rectangle_four_radius)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_rfr_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_rfr_peremeter.setGeometry(15, 240, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 240, 40, 20)
        
        #Розмірність приметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 240, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 270, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()             

    #Периметер прямокутника з різними радіусами
    def perim_rectangle_four_radius(self) -> None:
        list_s1 = self.check_number_new(self.side_a_four_radius_lalel_velue.text())
        list_s2 = self.check_number_new(self.side_b_four_radius_lalel_velue.text())
        list_r1 = self.check_number_new(self.r1_square_velue_rfr.text())
        list_r2 = self.check_number_new(self.r2_square_velue_rfr.text())
        list_r3 = self.check_number_new(self.r3_square_velue_rfr.text())
        list_r4 = self.check_number_new(self.r4_square_velue_rfr.text())

        self.message_side_a_four_radius.setText(list_s1[1])
        self.message_side_b_four_radius.setText(list_s2[1])
        self.message_r1_square_rfr.setText(list_r1[1])
        self.message_r2_square_rfr.setText(list_r2[1])
        self.message_r3_square_rfr.setText(list_r3[1])
        self.message_r4_square_rfr.setText(list_r4[1])

        if list_s1[0] != 0 and list_s2[0] != 0 and list_r1[0] != 0 and list_r2[0] != 0 and list_r3[0] != 0 and list_r4[0] != 0:
            s_1_rfr = list_s1[0] - list_r1[0] - list_r2[0]
            s_2_rfr = list_s2[0] - list_r2[0] - list_r3[0]
            s_3_rfr = list_s1[0] - list_r3[0] - list_r4[0]
            s_4_rfr = list_s2[0] - list_r4[0] - list_r1[0]    

            if s_1_rfr < 5 or s_2_rfr < 5 or s_3_rfr < 5 or s_4_rfr < 5:
                if s_1_rfr < 5:
                    self.perimeter.setText('?')
                    self.message_r1_square_rfr.setText(list_r1[1])
                    self.message_r2_square_rfr.setText(list_r2[1])
                if s_2_rfr < 5:
                    self.perimeter.setText('?')
                    self.message_r2_square_rfr.setText(list_r2[1])
                    self.message_r3_square_rfr.setText(list_r3[1])
                if s_3_rfr < 5:
                    self.perimeter.setText('?')
                    self.message_r3_square_rfr.setText(list_r3[1])
                    self.message_r4_square_rfr.setText(list_r4[1])
                if s_4_rfr < 5:
                    self.perimeter.setText('?')
                    self.message_r4_square_rfr.setText(list_r4[1])
                    self.message_r1_square_rfr.setText(list_r1[1])                                    
            else:
                self.mm_result_perimeret.setGeometry(170, 240, 20, 20)
                self.perimeter.setText(str(g.Perimeter.rectangle_four_radius(
                    list_s1[0], 
                    list_s2[0], 
                    list_r1[0], 
                    list_r2[0], 
                    list_r3[0], 
                    list_r4[0]
                    ))) 
        else:
            self.perimeter.setText('?')
    #КІНЕЦЬ ПРЯМОКУТНИК З РІНИМИ РАДИУСАМИ

    #ШЕСТИГАРННИК
    #Вікно шестигранника
    def hexagon(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        #Сторона 
        #Заголовок сторони
        self.hex_a_lalel = QLabel("A", self.window_shape)
        self.hex_a_lalel.setGeometry(10, 30, 10, 20)

        #Значення сторони
        self.hex_a_velue = QLineEdit("0.0", self.window_shape)
        self.hex_a_velue.setGeometry(25, 30, 40, 20)

        #Розмірність сторони
        self.mm_hex_a_lalel = QLabel("мм", self.window_shape)
        self.mm_hex_a_lalel.setGeometry(70, 30, 40, 20)

        #Статус сторони       
        self.message_hex_a = QLabel(None, self.window_shape)
        self.message_hex_a.setGeometry(100, 30, 150, 20)
        if self.hex_a_velue.text() in zero:
            self.message_hex_a.setText("Відсутнє значення")

        #Кнопка розрахунку
        self.btn_hex_a = QPushButton("Розрахувати периметр по А", self.window_shape)
        self.btn_hex_a.setGeometry(10, 55, 200, 25)
        self.btn_hex_a.clicked.connect(self.perim_hex_a)

        #Висота
        #Заголовок висоти
        self.hex_h_lalel = QLabel("H", self.window_shape)
        self.hex_h_lalel.setGeometry(10, 90, 10, 20)

        #Значення висоти
        self.hex_h_velue = QLineEdit("0.0", self.window_shape)
        self.hex_h_velue.setGeometry(25, 90, 40, 20)

        #Розмірність сторони
        self.mm_hex_h_lalel = QLabel("мм", self.window_shape)
        self.mm_hex_h_lalel.setGeometry(70, 90, 40, 20)

        #Статус сторони       
        self.message_hex_h = QLabel(None, self.window_shape)
        self.message_hex_h.setGeometry(100, 90, 150, 20)
        if self.hex_h_velue.text() in zero:
            self.message_hex_h.setText("Відсутнє значення")
        
        #Кнопка розрахунку
        self.btn_hex_h = QPushButton("Розрахувати периметр по H", self.window_shape)
        self.btn_hex_h.setGeometry(10, 115, 200, 25)
        self.btn_hex_h.clicked.connect(self.perim_hex_h)

        #Діаметр
        #Заголовок діаметра
        self.hex_d_lalel = QLabel("D", self.window_shape)
        self.hex_d_lalel.setGeometry(10, 160, 10, 20)

        #Значення висоти
        self.hex_d_velue = QLineEdit("0.0", self.window_shape)
        self.hex_d_velue.setGeometry(25, 160, 40, 20)

        #Розмірність сторони
        self.mm_hex_d_lalel = QLabel("мм", self.window_shape)
        self.mm_hex_d_lalel.setGeometry(70, 160, 40, 20)

        #Статус сторони       
        self.message_hex_d = QLabel(None, self.window_shape)
        self.message_hex_d.setGeometry(100, 160, 150, 20)
        if self.hex_d_velue.text() in zero:
            self.message_hex_d.setText("Відсутнє значення")

        #Кнопка розрахунку
        self.btn_hex_d = QPushButton("Розрахувати периметр по D", self.window_shape)
        self.btn_hex_d.setGeometry(10, 185, 200, 25)
        self.btn_hex_d.clicked.connect(self.perim_hex_d)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметер кола", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 230, 90, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(105, 230, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(140, 230, 20, 20)

        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 260, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()
    
    #Периметр шестирганника по стороні А
    def perim_hex_a(self):
        hex_a_list = self.check_number_new(self.hex_a_velue.text())
        self.message_hex_a.setText(hex_a_list[1])

        if hex_a_list[0] != 0:
            self.hex_h_velue.setText(str(g.Hexagon.h_hexagon_a(hex_a_list[0])))
            self.hex_d_velue.setText(str(g.Hexagon.d_hexagon_a(hex_a_list[0])))
            self.perimeter.setText(str(g.Perimeter.hexagon_a(hex_a_list[0])))
        else:
            self.hex_h_velue.setText("0.0")
            self.hex_d_velue.setText("0.0")
            self.perimeter.setText("?")      

    #Периметр шестирганника по відстані проміж паралельними сторонами H
    def perim_hex_h(self):
        hex_h_list = self.check_number_new(self.hex_h_velue.text())
        self.message_hex_h.setText(hex_h_list[1])

        if hex_h_list[0] != 0:
            self.hex_a_velue.setText(str(g.Hexagon.a_hexagon_h(hex_h_list[0])))
            self.hex_d_velue.setText(str(g.Hexagon.d_hexagon_h(hex_h_list[0])))
            self.perimeter.setText(str(g.Perimeter.hexagon_h(hex_h_list[0])))
        else:
            self.hex_a_velue.setText("0.0")
            self.hex_d_velue.setText("0.0")
            self.perimeter.setText("?")

    #Периметр шестирганника по діаметру описаного кола
    def perim_hex_d(self):
        hex_d_list = self.check_number_new(self.hex_d_velue.text())
        self.message_hex_d.setText(hex_d_list[1])

        if hex_d_list[0] != 0:
            self.hex_a_velue.setText(str(g.Hexagon.a_hexagon_d(hex_d_list[0])))
            self.hex_h_velue.setText(str(g.Hexagon.h_hexagon_d(hex_d_list[0])))
            self.perimeter.setText(str(g.Perimeter.hexagon_d(hex_d_list[0])))               
        else:
            self.hex_a_velue.setText("0.0")
            self.hex_h_velue.setText("0.0")
            self.perimeter.setText("?")   

    #ОВАЛ
    #Вікно овала
    def oblong(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        #Сторона A
        #Заголовок сторони а
        self.oblong_side_a_lalel = QLabel("A", self.window_shape)
        self.oblong_side_a_lalel.setGeometry(10, 50, 10, 20)

        #Значення сторони а
        self.oblong_side_a_velue = QLineEdit("0.0", self.window_shape)
        self.oblong_side_a_velue.setGeometry(25, 50, 40, 20)

        #Розмірність сторони а
        self.mm_label_oblong_side_a = QLabel("мм", self.window_shape)
        self.mm_label_oblong_side_a.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_oblong_side_a = QLabel(None, self.window_shape)
        self.message_oblong_side_a.setGeometry(100, 50, 150, 20)
        if self.oblong_side_a_velue.text() in zero:
            self.message_oblong_side_a.setText("Відсутнє значення")

        #Сторона B
        #Заголовок сторони b
        self.oblong_side_b_lalel = QLabel("B", self.window_shape)
        self.oblong_side_b_lalel.setGeometry(10, 80, 10, 20)

        #Значення сторони b
        self.oblong_side_b_velue = QLineEdit("0.0", self.window_shape)
        self.oblong_side_b_velue.setGeometry(25, 80, 40, 20)

        #Розмірність сторони b
        self.mm_label_oblong_side_b = QLabel("мм", self.window_shape)
        self.mm_label_oblong_side_b.setGeometry(70, 80, 40, 20)

        #Статус сторони       
        self.message_oblong_side_b = QLabel(None, self.window_shape)
        self.message_oblong_side_b.setGeometry(100, 80, 150, 20)
        if self.oblong_side_a_velue.text() in zero:
            self.message_oblong_side_b.setText("Відсутнє значення")
        
        #Кнопка розрахунку
        self.btn_oblong = QPushButton("Розрахувати периметер", self.window_shape)
        self.btn_oblong.setGeometry(10, 110, 200, 20)
        self.btn_oblong.clicked.connect(self.perim_oblong)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 140, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 140, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 140, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 170, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()

    #Периметер овала
    def perim_oblong(self) -> None:

        oblong_a_list = self.check_number_new(self.oblong_side_a_velue.text())
        oblong_b_list = self.check_number_new(self.oblong_side_b_velue.text())

        self.message_oblong_side_a.setText(oblong_a_list[1])
        self.message_oblong_side_b.setText(oblong_b_list[1])

        if oblong_a_list[0] <= oblong_b_list[0]:
            self.message_oblong_side_a.setText("Замале значення")
            self.message_oblong_side_b.setText("Завелике значення")
            self.perimeter.setText("?")
        else:
            if oblong_a_list[0] != 0 and oblong_b_list[0] != 0:
                self.perimeter.setText(str(g.Perimeter.oblong(oblong_a_list[0], oblong_b_list[0])))
            else:
                self.perimeter.setText("?")

    #ТРИКУТНИК РІВНОСТОРОННІЙ
    #Вікно трикутника рівносоторонній
    def equilateral_triangle(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        #Сторона A
        #Заголовок сторони а
        self.eq_tr_side_lalel = QLabel("A", self.window_shape)
        self.eq_tr_side_lalel.setGeometry(10, 50, 10, 20)
        
        #Значення сторони
        self.eq_tr_side_velue = QLineEdit("0.0", self.window_shape)
        self.eq_tr_side_velue.setGeometry(25, 50, 40, 20)

        #Розмірність сторони
        self.mm_eq_tr_side_lalel = QLabel("мм", self.window_shape)
        self.mm_eq_tr_side_lalel.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_eq_tr_side = QLabel(None, self.window_shape)
        self.message_eq_tr_side.setGeometry(100, 50, 150, 20)
        if self.eq_tr_side_velue.text() in zero:
            self.message_eq_tr_side.setText("Відсутнє значення")

        #Кнопка розрахунку через сторону А
        self.btn_eq_tr_a = QPushButton("Розрахувати периметер", self.window_shape)
        self.btn_eq_tr_a.setGeometry(10, 80, 200, 20)
        self.btn_eq_tr_a.clicked.connect(self.perim_eq_riangle_a)

        #Сторона H
        #Заголовок висоти h
        self.eq_tr_height_lalel = QLabel("H", self.window_shape)
        self.eq_tr_height_lalel.setGeometry(10, 110, 10, 20)
        
        #Значення висоти
        self.eq_tr_height_velue = QLineEdit("0.0", self.window_shape)
        self.eq_tr_height_velue.setGeometry(25, 110, 40, 20)

        #Розмірність висоти
        self.mm_eq_tr_height_lalel = QLabel("мм", self.window_shape)
        self.mm_eq_tr_height_lalel.setGeometry(70, 110, 40, 20)

        #Статус сторони       
        self.message_eq_tr_height = QLabel(None, self.window_shape)
        self.message_eq_tr_height.setGeometry(100, 110, 150, 20)
        if self.eq_tr_height_velue.text() in zero:
            self.message_eq_tr_height.setText("Відсутнє значення")

        #Кнопка розрахунку через висоту H
        self.btn_eq_tr_h = QPushButton("Розрахувати периметер", self.window_shape)
        self.btn_eq_tr_h.setGeometry(10, 140, 200, 20)
        self.btn_eq_tr_h.clicked.connect(self.perim_eq_riangle_h)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 170, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 170, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 170, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 200, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()

    #Периметер рівносторонього трикутника через сторону
    def perim_eq_riangle_a(self) -> None:
        side_a_list = self.check_number_new(self.eq_tr_side_velue.text())
        print(side_a_list[0], " ", type(side_a_list[0]))
        self.message_eq_tr_side.setText(side_a_list[1])

        if side_a_list[0] != 0:
            self.perimeter.setText(str(g.Equilateral_triangle.perim_eq_tr_side(side_a_list[0])))
            self.eq_tr_height_velue.setText(str(g.Equilateral_triangle.height_eq_tr_side(side_a_list[0])))        
        else:
            self.eq_tr_height_velue.setText("0.0")
            self.perimeter.setText("?")

    #Периметер рівносторонього трикутника через висоту
    def perim_eq_riangle_h(self) -> None:
        height_h_list = self.check_number_new(self.eq_tr_height_velue.text())

        self.message_eq_tr_height.setText(height_h_list[1])

        if height_h_list[0] != 0:
            self.perimeter.setText(str(g.Equilateral_triangle.perim_eq_tr_height(height_h_list[0])))
            self.eq_tr_side_velue.setText(str(g.Equilateral_triangle.side_eq_tr_height(height_h_list[0])))
        else:
            self.eq_tr_side_velue.setText(str(g.Equilateral_triangle.side_eq_tr_height(height_h_list[0])))
            self.perimeter.setText("?")

    #РІВНОБЕДРЕНИЙ ТРИКУТНИК
    #Вікно рівнобедреного трикутника
    def isosceles_triangle(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        #Сторона A
        #Заголовок сторони
        self.side_a_is_tr_lalel = QLabel("A", self.window_shape)
        self.side_a_is_tr_lalel.setGeometry(10, 30, 10, 20)

        #Значення сторони
        self.side_a_is_tr_velue = QLineEdit("0.0", self.window_shape)
        self.side_a_is_tr_velue.setGeometry(25, 30, 40, 20)

        #Розмірність сторони
        self.mm_side_a_is_tr_lalel = QLabel("мм", self.window_shape)
        self.mm_side_a_is_tr_lalel.setGeometry(70, 30, 40, 20)

        #Статус сторони       
        self.message_side_a_is_tr = QLabel(None, self.window_shape)
        self.message_side_a_is_tr.setGeometry(100, 30, 150, 20)
        if self.side_a_is_tr_velue.text() in zero:
            self.message_side_a_is_tr.setText("Відсутнє значення")

        #Сторона B
        #Заголовок сторони
        self.side_b_is_tr_lalel = QLabel("B", self.window_shape)
        self.side_b_is_tr_lalel.setGeometry(10, 60, 10, 20)

        #Значення сторони
        self.side_b_is_tr_velue = QLineEdit("0.0", self.window_shape)
        self.side_b_is_tr_velue.setGeometry(25, 60, 40, 20)

        #Розмірність сторони
        self.mm_side_b_is_tr_lalel = QLabel("мм", self.window_shape)
        self.mm_side_b_is_tr_lalel.setGeometry(70, 60, 40, 20)

        #Статус сторони       
        self.message_side_b_is_tr = QLabel(None, self.window_shape)
        self.message_side_b_is_tr.setGeometry(100, 60, 150, 20)
        if self.side_b_is_tr_velue.text() in zero:
            self.message_side_b_is_tr.setText("Відсутнє значення")

        #Висота H
        #Заголовок сторони
        self.height_is_tr_lalel = QLabel("H", self.window_shape)
        self.height_is_tr_lalel.setGeometry(10, 90, 10, 20)

        #Значення сторони
        self.height_is_tr_velue = QLineEdit("0.0", self.window_shape)
        self.height_is_tr_velue.setGeometry(25, 90, 40, 20)

        #Розмірність сторони
        self.mm_height_is_tr_lalel = QLabel("мм", self.window_shape)
        self.mm_height_is_tr_lalel.setGeometry(70, 90, 40, 20)

        #Статус сторони       
        self.message_height_is_tr = QLabel(None, self.window_shape)
        self.message_height_is_tr.setGeometry(100, 90, 150, 20)
        if self.height_is_tr_velue.text() in zero:
            self.message_height_is_tr.setText("Відсутнє значення")

        #Кнопка розрахунку через сторону А та сторону В
        self.btn_perim_is_tr_a_b = QPushButton("Розрахувати периметер (по А, В)", self.window_shape)
        self.btn_perim_is_tr_a_b.setGeometry(10, 120, 200, 20)
        self.btn_perim_is_tr_a_b.clicked.connect(self.perim_is_tr_a_b)

        #Кнопка розрахунку через сторону А та сторону H
        self.btn_perim_is_tr_a_h = QPushButton("Розрахувати периметер (по А, Н)", self.window_shape)
        self.btn_perim_is_tr_a_h.setGeometry(10, 150, 200, 20)
        self.btn_perim_is_tr_a_h.clicked.connect(self.perim_is_tr_a_h)

        #Кнопка розрахунку через сторону B та сторону H
        self.btn_perim_is_tr_b_h = QPushButton("Розрахувати периметер (по B, Н)", self.window_shape)
        self.btn_perim_is_tr_b_h.setGeometry(10, 180, 200, 20)
        self.btn_perim_is_tr_b_h.clicked.connect(self.perim_is_tr_b_h)


        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметер квадрата", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 210, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 210, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 210, 20, 20)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 240, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()

    #Периметер рівнобедреного трикутника через дві сторони
    def perim_is_tr_a_b(self) -> None:
        
        side_a_list = self.check_number_new(self.side_a_is_tr_velue.text())
        side_b_list = self.check_number_new(self.side_b_is_tr_velue.text())
        
        self.message_side_a_is_tr.setText(side_a_list[1])
        self.message_side_b_is_tr.setText(side_b_list[1])


        if side_a_list[0] != 0 and side_b_list[0] != 0:
            if side_a_list[0] * 2 <= side_b_list[0]:
                self.message_side_a_is_tr.setText("Завелика сторона")
                self.message_side_b_is_tr.setText("Замала сторона")
                self.height_is_tr_velue.setText("?")
                self.perimeter.setText("?")
            else:
                self.perimeter.setText(str(g.Isosceles_triangle.perim_is_tr_side_a_b(side_a_list[0], side_b_list[0])))
                self.perimeter.setGeometry(125, 210, 40, 20)
                self.height_is_tr_velue.setText(str(g.Isosceles_triangle.height_is_tr_side_a_b(side_a_list[0], side_b_list[0])))
        else:
            self.perimeter.setText("?")

    #Периметер рівнобедреного трикутника через довгу сторону та висоту
    def perim_is_tr_a_h(self) -> None:

        side_a_list = self.check_number_new(self.side_a_is_tr_velue.text())
        height_list = self.check_number_new(self.height_is_tr_velue.text())
        
        self.message_side_a_is_tr.setText(side_a_list[1]) 
        self.message_height_is_tr.setText(height_list[1])

        if side_a_list[0] != 0 and height_list[0] != 0:
            if side_a_list[0] <= height_list[0]:
                self.message_side_a_is_tr.setText("Замала сторона")
                self.message_side_b_is_tr.setText("?")
                self.message_height_is_tr.setText("Завелика сторона")
                self.perimeter.setText("?")
            else:
                self.perimeter.setGeometry(125, 210, 40, 20)
                self.perimeter.setText(str(g.Isosceles_triangle.perim_is_tr_side_a_height(side_a_list[0], height_list[0])))
                self.side_b_is_tr_velue.setText(str(g.Isosceles_triangle.side_b_is_tr_side_a_height(side_a_list[0], height_list[0])))       
        else:
            self.perimeter.setText("?")

    #Периметер рівнобедреного трикутника через коротку сторону та висоту
    def perim_is_tr_b_h(self) -> None:
        side_b_list = self.check_number_new(self.side_b_is_tr_velue.text())
        height_list = self.check_number_new(self.height_is_tr_velue.text())

        self.message_side_b_is_tr.setText(side_b_list[1]) 
        self.message_height_is_tr.setText(height_list[1])

        if side_b_list[0] != 0 and height_list[0]:
            self.perimeter.setGeometry(125, 210, 40, 20)
            self.perimeter.setText(str(g.Isosceles_triangle.perim_is_tr_height_side_b(height_list[0], side_b_list[0])))
            self.side_a_is_tr_velue.setText(str(g.Isosceles_triangle.side_a_is_tr_side_b_height(side_b_list[0], height_list[0])))  
        else:
            self.perimeter.setText("?")


    #Передаэмо з вікна форми до головного вікна периметер
    def add_value(self):
        if self.perimeter.text() != "?":
            self.perimeter_velue.setText(self.perimeter.text())


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(my_app.exec_())
