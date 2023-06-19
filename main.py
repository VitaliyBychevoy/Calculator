import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as gui
from PyQt5 import QtCore

import geometry as g

material = {
    "Алюміній": 0.5,
    "Мідь": 0.57,
    "Сталь звичайна": 1,
    "Сталь нержавіюча": 1.5
 }

exceptable_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']

zero = ['0', '0,0', '0.0', '', '.', ',']

error_value_style: str = "background-color: red; color: white; border-radius: 10px;"
valide_value_style: str = "background-color: green; color: white; border-radius: 10px;"
error_width_1: int = 150
error_width_2: int = 210
valid_width: int = 150

message_width: int = 150

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 450, 300)
        self.setWindowTitle("Cluster force")


        gui.QFontDatabase.addApplicationFont("fonts/Kareliac bold.otf")
        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.perimeter_lalel = QLabel("Периметр", self)
        self.perimeter_lalel.setGeometry(10, 50, 100, 20)
        self.perimeter_lalel.setStyleSheet("color: lightgreen;")
        self.perimeter_lalel.setFont(font_1)

        #Значення периметра
        self.perimeter_velue = QLineEdit("0.0", self)
        self.perimeter_velue.setGeometry(120, 50, 70, 20)
        self.perimeter_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.perimeter_velue.setStyleSheet(
            "background-color: lightgreen;"
            "color: #008CBA;"
            "border: 2px solid blue;"
            "border-radius: 10px; text-align: center;"
            )
        self.perimeter_velue.setFont(font_3)


        #Розмірність периметра
        self.mm_label_perimeter = QLabel("мм", self)
        self.mm_label_perimeter.setGeometry(195, 50, 70, 20)
        self.mm_label_perimeter.setStyleSheet("color: lightgreen;")
        self.mm_label_perimeter.setFont(font_1)

        #Статус введенного периметра
        self.message_perimeter = QLabel(None, self)
        self.message_perimeter.setGeometry(230, 50, 150, 20)
        self.message_perimeter.setFont(font_4)
        if self.perimeter_velue.text() in zero:
            self.message_perimeter.setText("Відсутнє значення")
            self.message_perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.message_perimeter.setGeometry(230, 50, message_width, 20)

            self.message_perimeter.setStyleSheet(error_value_style)

        #ТОВЩИНА
        #Заголовок товщини       
        self.thickness_label = QLabel("Товщина", self)
        self.thickness_label.setGeometry(10, 75, 100, 20)
        self.thickness_label.setStyleSheet("color: coral;")
        self.thickness_label.setFont(font_1)

        #Значення товщини
        self.thickness_velue = QLineEdit("0.0", self)
        self.thickness_velue.setGeometry(120, 75, 70, 20)
        self.thickness_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.thickness_velue.setStyleSheet("background-color: coral; color: #008CBA; border: 2px solid blue; border-radius: 10px; text-align: center;")
        self.thickness_velue.setFont(font_3)

        #Розмірність товщини
        self.mm_label_thickness = QLabel("мм", self)
        self.mm_label_thickness.setGeometry(195, 75, 50, 20)
        self.mm_label_thickness.setStyleSheet("color: coral;")
        self.mm_label_thickness.setFont(font_1)
        
        #Статус введенної товщини
        self.message_thickness = QLabel(None, self)
        self.message_thickness.setGeometry(230, 75, message_width, 20)
        self.message_thickness.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)      
        self.message_thickness.setFont(font_4)
        if self.thickness_velue.text() in zero:
            self.message_thickness.setText("Відсутнє значення")
            self.message_thickness.setStyleSheet(error_value_style)

        #МАТЕРІАЛ
        #Заголовок матеріала
        self.material_label = QLabel("Матеріал", self)
        self.material_label.setGeometry(10, 100, 100, 20)
        self.material_label.setStyleSheet("color: Yellow;")
        self.material_label.setFont(font_1)

        #Список матеріалів
        # усі літери і у назвах матеріалу англійські
        self.material = QComboBox(self)
        self.material.addItem("Сталь звичайна") 
        self.material.addItem("Сталь нержавіюча")
        self.material.addItem("Алюміній")
        self.material.addItem("Мідь")
        self.material.setGeometry(120, 100, 320, 20)
        self.material.setStyleSheet("color: MediumAquaMarine; background-color: Yellow; border: 2px solid blue; ")
        self.material.setFont(font_4)

        #ОТВОРИ
        #Заголовок отворів
        self.amount_holes_label = QLabel("Отворiв", self)
        self.amount_holes_label.setGeometry(10, 125, 100, 20)
        self.amount_holes_label.setStyleSheet("color: MediumAquaMarine;")
        self.amount_holes_label.setFont(font_1)

        #Список отворів
        self.amount_holes = QComboBox(self)
        for i in range(1, 37):
            self.amount_holes.addItem(str(i))
        self.amount_holes.setGeometry(120, 125, 60, 20)
        self.amount_holes.setStyleSheet("color: Olive; background-color: MediumAquaMarine; border: 2px solid blue;")
        self.amount_holes.setFont(font_3)

        #КНОПКА ДЛЯ РОЗРАХУВАННЯ ЗУСИЛЛЯ
        self.btn = QPushButton("Розрахувати зусилля", self)
        self.btn.setGeometry(120, 150, 320, 40)
        self.btn.setStyleSheet(
        "color: white; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(127,255,212), stop:1 rgb(100,149,237));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )

        self.btn.clicked.connect(self.calculate_tonage_new)


        #ОТРИМАНЕ ЗУСИЛЛЯ
        #Заголовок зусилля
        self.force_result_label = QLabel("Зусилля", self)
        self.force_result_label.setGeometry(10, 195, 100, 25)
        self.force_result_label.setFont(font_0)
        self.force_result_label.setStyleSheet(
            "color: #F0F8FF;"
        )

        #Значеня зусилля
        self.force_result_value = QLineEdit('?', self)
        self.force_result_value.setGeometry(120, 195, 100, 25)
        self.force_result_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)    
        self.force_result_value.setFont(font_0)
        self.force_result_value.setStyleSheet(
        "border-radius: 10px;"
        "border: 2px solid rgb(0, 255, 255);"
        "color: #660099;"
        )

        #Розмірність зусилля
        self.tonage_label_force = QLabel("тонн(и)", self)
        self.tonage_label_force.setGeometry(230, 195, 100, 20)
        self.tonage_label_force.setFont(font_0)
        self.tonage_label_force.setStyleSheet(
            "color: #F0F8FF;"
        )

        #ФОРМІ
        #Заголовок форми
        self.force_result_label = QLabel("Форма", self)
        self.force_result_label.setGeometry(10, 20, 80, 20)
        self.force_result_label.setStyleSheet("color: Cornsilk;")
        self.force_result_label.setFont(font_1)

        #Cписок форм
        self.shape = QComboBox(self)
        self.shape.addItem("")
        self.shape.addItem("Коло")
        self.shape.addItem("Напівколо")
        self.shape.addItem("Квадрат")
        self.shape.addItem("Квадрат з однаковими радіусами")
        self.shape.addItem("Квадрат з різними радіусами")
        self.shape.addItem("Квадрат у колі")
        self.shape.addItem("Прямокутник")
        self.shape.addItem("Прямокутник з однаковими радіусами")
        self.shape.addItem("Прямокутник з різними радіусами")
        self.shape.addItem("Шестигранник")
        self.shape.addItem("Овал з паралельними сторонами")
        self.shape.addItem("Трикутник рівносторонній")
        self.shape.addItem("Трикутник рівнобедрений")        
        self.shape.setGeometry(120, 20, 320, 25)
        self.shape.currentTextChanged.connect(self.shape_handler)
        self.shape.setStyleSheet(
            "color: DarkGreen; "
            "background-color: Cornsilk; "
            "border: 2px solid blue; "
            )
        self.shape.setFont(font_2)

    def paintEvent(self, a0: gui.QPaintEvent) -> None:
        painter = gui.QPainter(self)
        pixmap = gui.QPixmap("img/main_1.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    #Розрахунок навантаження
    def calculate_tonage_new(self):
        coeff_material = self.coefficient_material()
        
        perimetr_list = self.check_number_new(self.perimeter_velue.text())
        thickness_list = self.check_number_new(self.thickness_velue.text()) 

        self.message_perimeter.setText(perimetr_list[1])
        self.message_thickness.setText(thickness_list[1])

        if perimetr_list[1][-1] == "л":
            self.message_perimeter.setGeometry(230, 50, 210, 20)
        
        if thickness_list[1][-1] == "л":
            self.message_thickness.setGeometry(230, 75, 210, 20)

        if perimetr_list[0] != 0 and thickness_list[0] != 0:
            result = 0.0352 * coeff_material
            result = result * perimetr_list[0]
            result = result * thickness_list[0]
            result = round(result * float(self.amount_holes.currentText()), 2)
            self.perimeter_velue.setText(str(round(perimetr_list[0], 1)))
            self.thickness_velue.setText(str(round(thickness_list[0], 2)))
            self.message_perimeter.setStyleSheet(valide_value_style)
            self.message_thickness.setStyleSheet(valide_value_style)
            self.force_result_value.setText(str(result))
        else:
            self.force_result_value.setText("?")

        if perimetr_list[0] == 0 :
            self.message_perimeter.setStyleSheet(error_value_style)
        else:
            self.message_perimeter.setStyleSheet(valide_value_style)
            self.message_perimeter.setGeometry(230, 50, perimetr_list[2], 20)

        if thickness_list[0] == 0:
            self.message_thickness.setStyleSheet(error_value_style)
        else:
            self.message_thickness.setStyleSheet(valide_value_style)
            self.message_thickness.setGeometry(230, 75, thickness_list[2], 20)


    #Функція вертає коефіцієнт матеріала
    def coefficient_material(self) -> float:
        coeff = 0.0
        coeff = material[self.material.currentText()]
        return coeff

    #Перевіряємо числові дані, які вводив користувач 
    def check_number_new(self,item_string: str) -> list:

        result = [0, " Валідне значення", 150]
        item_string = item_string.strip()

        count_dot, count_comma = item_string.count('.'), item_string.count(',')

        if count_dot >= 1 and count_comma  >= 1:
            result[0]  = 0
            result[1] = " Або . або ,"
            result[2] = 150             
            return result            
        elif count_dot > 1 and count_comma  == 0:
            result[0]  = 0
            result[1] = "Забагато крапок"
            result[2] = 150
            return result
        elif count_comma > 1 and count_dot == 0:
            result[0]  = 0
            result[1] = "Забагато ком"
            result[2] = 150
            return result
        elif item_string in zero:
            result[0] = 0
            result[1] = "Відсутнє значення"
            result[2] = 150
            return result
        else:
            for letter in item_string:
                if letter not in exceptable_number:
                    result[0] = 0
                    message = f'"{letter}" э некоректний символ'
                    result[1] = message
                    result[2] = 210
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
                result[2] = 150
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
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.image_round = gui.QPixmap("img/Round.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(40, 30, 290, 300)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        self.window_shape.setStyleSheet("background-color: white;")
        self.window_shape.setFixedSize(370, 500)

        #ДІАМЕТР
        #Заголовок диаметра
        self.diameter_lalel = QLabel("D", self.window_shape)
        self.diameter_lalel.setGeometry(15, 350, 15, 20)
        self.diameter_lalel.setStyleSheet("color: #7B68EE;")
        self.diameter_lalel.setFont(font_1)

        #Значення диаметра
        self.diameter_velue = QLineEdit("0.0", self.window_shape)
        self.diameter_velue.setGeometry(35, 350, 80, 20)
        self.diameter_velue.setFont(font_3)
        self.diameter_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.diameter_velue.setStyleSheet(
            "background-color: #7B68EE;"
            "color: #FFFFE0;"
            "border: 2px solid blue;"
            "border-radius: 10px; text-align: center;"
            )

        #Розмірність диаметра
        self.mm_label_d = QLabel("мм", self.window_shape)
        self.mm_label_d.setGeometry(120, 350, 70, 20)
        self.mm_label_d.setFont(font_1)
        self.mm_label_d.setStyleSheet("color: #7B68EE;")

        #Статус діаметра         
        self.message_diameter = QLabel(None, self.window_shape)
        self.message_diameter.setGeometry(150, 350, 150, 20)


        if self.diameter_velue.text() in zero:
            self.message_diameter.setText("Відсутнє значення")
            self.message_diameter.setFont(font_4)
            self.message_diameter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_diameter.setStyleSheet(error_value_style)


        #Кнопка розрахунку
        self.btn_d = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_d.setGeometry(10, 380, 350, 30)
        self.btn_d.clicked.connect(self.perim_round)
        self.btn_d.setStyleSheet(
        "color: #E6E6FA;"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(106,90,205), stop:1 rgb(0,255,255));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )
        #ПЕРИМЕТР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметр кола", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_d_peremeter.setStyleSheet("color: YellowGreen;")
        self.Label_d_peremeter.setFont(font_1)
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.perimeter.setStyleSheet("color: YellowGreen;")
        self.perimeter.setFont(font_1)
        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeret.setStyleSheet("color: YellowGreen;")
        self.mm_result_perimeret.setFont(font_1)
        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(34,139,34), stop:1 rgb(127,255,0));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )

        self.window_shape.show()
    #Периметер кола  
    def perim_round(self):

        diameter_list_d = self.check_number_new(self.diameter_velue.text())
        self.message_diameter.setText(diameter_list_d[1])

        if diameter_list_d[0] == 0:
            self.message_diameter.setGeometry(150, 350, diameter_list_d[2], 20)
            self.message_diameter.setStyleSheet(error_value_style)
            self.perimeter.setText("?")
        else:
            self.perimeter.setText(str(g.Perimeter.round(float(diameter_list_d[0]))))
            self.diameter_velue.setText(str(round(diameter_list_d[0], 2)))
            self.message_diameter.setGeometry(150, 350, diameter_list_d[2], 20)
            self.message_diameter.setStyleSheet(valide_value_style)
    #КІНЕЦЬ КОЛО

    #НАПІВКОЛО
    def half_round_heandler(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setStyleSheet("background-color: white;")
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.window_shape.setFixedSize(370, 500)

        #ДІАМЕТР
        #Заголовок диаметра
        self.diameter_hr_lalel = QLabel("D", self.window_shape)
        self.diameter_hr_lalel.setGeometry(15, 290, 15, 20)
        self.diameter_hr_lalel.setStyleSheet("color: #5F9EA0;")
        self.diameter_hr_lalel.setFont(font_1)

        #Значення диаметра
        self.diameter_hr_velue = QLineEdit("0.0", self.window_shape)
        self.diameter_hr_velue.setGeometry(35, 290, 80, 20)
        self.diameter_hr_velue.setFont(font_3)
        self.diameter_hr_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.diameter_hr_velue.setStyleSheet(
            "background-color: #5F9EA0;"
            "color: #191970;"
            "border: 2px solid blue;"
            "border-radius: 10px; text-align: center;"
            )

        #Розмірність диаметра
        self.mm_label_d_hr = QLabel("мм", self.window_shape)
        self.mm_label_d_hr.setGeometry(120, 290, 70, 20)
        self.mm_label_d_hr.setStyleSheet("color: #5F9EA0;")
        self.mm_label_d_hr.setFont(font_1)


        #Статус діаметра         
        self.message_diameter_hr = QLabel(None, self.window_shape)
        self.message_diameter_hr.setGeometry(150, 290, 150, 20)
        if self.diameter_hr_velue.text() in zero:
            self.message_diameter_hr.setText("Відсутнє значення")
            self.message_diameter_hr.setFont(font_4)
            self.message_diameter_hr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_diameter_hr.setStyleSheet(error_value_style)      

        #Висота
        #Заголовок висоти
        self.height_hr_lalel = QLabel("H", self.window_shape)
        self.height_hr_lalel.setGeometry(15, 320, 15, 20)
        self.height_hr_lalel.setStyleSheet("color: #D2691E;")
        self.height_hr_lalel.setFont(font_1)

        #Значення висоти
        self.height_hr_velue = QLineEdit("0.0", self.window_shape)
        self.height_hr_velue.setGeometry(35, 320, 80, 20)
        self.height_hr_velue.setFont(font_3)
        self.height_hr_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.height_hr_velue.setStyleSheet(
            "background-color: #D2691E;"
            "color: #00FFFF;"
            "border: 2px solid #FFFF00;"
            "border-radius: 10px; text-align: center;"
            )
        
        #Розмірність висоти
        self.mm_label_h_hr = QLabel("мм", self.window_shape)
        self.mm_label_h_hr.setGeometry(120, 320, 70, 20)
        self.mm_label_h_hr.setStyleSheet("color: #D2691E;")
        self.mm_label_h_hr.setFont(font_1)

        #Статус висоти         
        self.message_height_hr = QLabel(None, self.window_shape)
        self.message_height_hr.setGeometry(150, 320, 150, 20)

        if self.height_hr_velue.text() in zero:
            self.message_height_hr.setText("Відсутнє значення")
            self.message_height_hr.setFont(font_4)
            self.message_height_hr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_height_hr.setStyleSheet(error_value_style)         

        self.image_half_round = gui.QPixmap("img/Half_round_1.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(12, 10, int(250 * 1.387 ), 250)
        self.image_lable.setPixmap(self.image_half_round )
        self.image_lable.setScaledContents(True)

        #Кнопка розрахунку
        self.btn_perim = QPushButton("Розрахувати периметр та довжину хорди", self.window_shape)
        self.btn_perim.clicked.connect(self.perim_half_round_height)
        self.btn_perim.setGeometry(10, 350, 350, 30)
        self.btn_perim.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 140, 0), stop:1 rgb(128, 0, 128));"
        "border-radius: 10px;"
        "font-size: 14px;"
        "font-weight: bold;"
        )

        #ХОРДА
        #Заголовок хорди
        self.lenght_hr_lalel = QLabel("Хорда L", self.window_shape)
        self.lenght_hr_lalel.setGeometry(15, 390, 150, 20)
        self.lenght_hr_lalel.setStyleSheet("color: #4682B4;")
        self.lenght_hr_lalel.setFont(font_1)

        #Значення хорди
        self.lenght_hr_velue = QLabel("0.0", self.window_shape)
        self.lenght_hr_velue.setGeometry(165, 390, 90, 20)
        self.lenght_hr_velue.setStyleSheet("color: #4682B4;")
        self.lenght_hr_velue.setFont(font_1)

        #Розмірність хорди
        self.mm_label_length_hr = QLabel("мм", self.window_shape)
        self.mm_label_length_hr.setGeometry(255, 390, 50, 20)
        self.mm_label_length_hr.setStyleSheet("color: #4682B4;")
        self.mm_label_length_hr.setFont(font_1)

        #ПЕРИМЕТР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_d_peremeter.setStyleSheet("color: #800080;")
        self.Label_d_peremeter.setFont(font_1)

        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet("color: #800080;")
        self.perimeter.setFont(font_1)

        #Розмірність периметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeret.setStyleSheet("color: #800080;")
        self.mm_result_perimeret.setFont(font_1)

        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)
        self.btn_add_perimeter.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(32, 178, 170), stop:1 rgb(186, 85, 211));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )

        self.window_shape.show()

    #Периметер напівкільця
    def perim_half_round_height(self):

        diameter_list = self.check_number_new(self.diameter_hr_velue.text())
        height_list = self.check_number_new(self.height_hr_velue.text())

        self.message_diameter_hr.setText(diameter_list[1])
        self.message_height_hr.setText(height_list[1])

        self.message_diameter_hr.setGeometry(145, 290, diameter_list[2], 20)
        self.message_diameter_hr.setStyleSheet(error_value_style)
        self.message_height_hr.setGeometry(145, 320, height_list[2], 20)
        self.message_height_hr.setStyleSheet(error_value_style)
        self.lenght_hr_velue.setText("?")
        self.perimeter.setText("?")

        if diameter_list[0] != 0:
            self.message_diameter_hr.setGeometry(150, 290, diameter_list[2], 20)
            self.message_diameter_hr.setStyleSheet(valide_value_style)
            self.diameter_hr_velue.setText(str(round(diameter_list[0], 2)))
        if height_list[0] != 0:
            self.message_height_hr.setGeometry(150, 320, height_list[2], 20)
            self.message_height_hr.setStyleSheet(valide_value_style)
            self.height_hr_velue.setText(str(round(height_list[0], 2)))

        if diameter_list[0] != 0 and height_list[0] != 0:
            if diameter_list[0] <= height_list[0]:
                self.message_diameter_hr.setText("Замалий розмір D")
                self.message_diameter_hr.setGeometry(150, 290, 190, 20)
                self.message_diameter_hr.setStyleSheet(error_value_style)
                self.message_height_hr.setText("Завеликий розмір H")
                self.message_height_hr.setGeometry(150, 320, 190, 20)
                self.message_height_hr.setStyleSheet(error_value_style)
            else:
                if height_list[0] > (diameter_list[0] / 2):
                    #Висота більша за радіус
                    self.perimeter.setText(str(g.Incomplete_circle.perim_in_circle(diameter_list[0], height_list[0])))
                    l = round(g.Incomplete_circle.lenght_chold(diameter_list[0], height_list[0]), 2)
                    self.lenght_hr_velue.setText(str(l))
                elif height_list[0] == (diameter_list[0] / 2):
                    #Висота дорівнює радіусу
                    self.perimeter.setText(str(g.Incomplete_circle.perim_half_round(diameter_list[0], height_list[0])))
                    self.lenght_hr_velue.setText(str(height_list[0] * 2))
                elif height_list[0] < (diameter_list[0] / 2):
                    #Висота меньша за радіус
                    l = round(g.Incomplete_circle.lenght_chold(diameter_list[0], height_list[0]), 2)
                    self.lenght_hr_velue.setText(str(l))
                    p = round((g.Incomplete_circle.perim_half_round_height_less_radius(diameter_list[0], height_list[0])), 2)
                    self.perimeter.setText(str(p))
    #КІНЕЦЬ НАПІВКОЛО 

    #КВАДРАТ
    #Вікно квадрата
    def square(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.window_shape.setStyleSheet("background-color: white;")
        self.window_shape.setFixedSize(370, 500)

        self.image_round = gui.QPixmap("img/square.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(52, 30, int(260 / 1.023), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        
        #Сторона
        #Заголовок сторони
        self.side_lalel = QLabel("A", self.window_shape)
        self.side_lalel.setGeometry(15, 350, 15, 20)
        self.side_lalel.setStyleSheet("color: #5F9EA0;")
        self.side_lalel.setFont(font_1)

        #Значення диаметра
        self.side_velue = QLineEdit("0.0", self.window_shape)
        self.side_velue.setGeometry(35, 350, 80, 20)
        self.side_velue.setFont(font_3)
        self.side_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_velue.setStyleSheet(
            "background-color: #5F9EA0;"
            "color: #00FFFF;"
            "border: 2px solid #00FF00;"
            "border-radius: 10px; text-align: center;"
            )
        
        #Розмірність диаметра
        self.mm_label_side = QLabel("мм", self.window_shape)
        self.mm_label_side.setGeometry(120, 350, 70, 20)
        self.mm_label_side.setStyleSheet("color: #5F9EA0;")
        self.mm_label_side.setFont(font_1)

        #Статус сторони       
        self.message_side = QLabel(None, self.window_shape)
        self.message_side.setGeometry(150, 350, 150, 20)
        if self.side_velue.text() in zero:
            self.message_side.setText("Відсутнє значення")
            self.message_side.setFont(font_4)
            self.message_side.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side.setStyleSheet(error_value_style)         
     
        #Кнопка розрахунку
        self.btn_s = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_s.clicked.connect(self.perim_square)
        self.btn_s.setGeometry(10, 380, 350, 30)
        self.btn_s.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 140, 0), stop:1 rgb(128, 0, 128));"
        "border-radius: 10px;"
        "font-size: 14px;"
        "font-weight: bold;"
        )

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_s_peremeter.setStyleSheet("color: #800080;")
        self.Label_s_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet("color: #800080;")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeret.setStyleSheet("color: #800080;")
        self.mm_result_perimeret.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(32, 178, 170), stop:1 rgb(186, 85, 211));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )

        self.window_shape.show()

    #Периметр квадрата
    def perim_square(self) -> None:
        square_list = self.check_number_new(self.side_velue.text())
        self.message_side.setText(square_list[1])

        self.message_side.setGeometry(150, 350, square_list[2], 20)

        if square_list[0] == 0:
            self.message_side.setStyleSheet(error_value_style)   
            self.perimeter.setText("?")
        else:
            self.side_velue.setText(str(round(square_list[0], 2)))
            self.message_side.setStyleSheet(valide_value_style)      
            self.perimeter.setText(str(g.Perimeter.square(float(square_list[0]))))                        
    #КІНЕЦЬ КВАДРАТ

    #КВАДРАТ З ОДНАКОВИМИ РАДІУСАМИ
    #Вікно квадрата з однаковими радіусами
    def square_one_radius(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.window_shape.setStyleSheet("background-color: white;")

        self.image_round = gui.QPixmap("img/square_one_radius.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(34, 30, int(260 * 1.16), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        self.window_shape.setFixedSize(370, 500)

        #Сторона 
        #Заголовок сторони
        self.side_one_round_square_lalel = QLabel("A", self.window_shape)
        self.side_one_round_square_lalel.setGeometry(15, 320, 15, 20)
        self.side_one_round_square_lalel.setStyleSheet("color: #5F9EA0;")
        self.side_one_round_square_lalel.setFont(font_1)

        #Значення сторони
        self.side_one_round_square_velue = QLineEdit("0.0", self.window_shape)
        self.side_one_round_square_velue.setGeometry(35, 320, 80, 20)
        self.side_one_round_square_velue.setFont(font_3)
        self.side_one_round_square_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_one_round_square_velue.setStyleSheet(
            "background-color: #5F9EA0;"
            "color: #00FFFF;"
            "border: 2px solid #00FF00;"
            "border-radius: 10px; text-align: center;"
            )
        
        #Розмірність сторони
        self.mm_label_side_one_round_square = QLabel("мм", self.window_shape)
        self.mm_label_side_one_round_square.setGeometry(120, 320, 70, 20)
        self.mm_label_side_one_round_square.setStyleSheet("color: #5F9EA0;")
        self.mm_label_side_one_round_square.setFont(font_1)

        #Статус сторони       
        self.message_side_one_round_square = QLabel(None, self.window_shape)
        self.message_side_one_round_square.setGeometry(150, 320, 150, 20)
        if self.side_one_round_square_velue.text() in zero:
            self.message_side_one_round_square.setText("Відсутнє значення")
            self.message_side_one_round_square.setFont(font_4)
            self.message_side_one_round_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_one_round_square.setStyleSheet(error_value_style)  

        #Радіус
        #Заголовок радіуса
        self.radius_one_round_square_lalel = QLabel("R", self.window_shape)
        self.radius_one_round_square_lalel.setGeometry(15, 350, 15, 20)
        self.radius_one_round_square_lalel.setStyleSheet("color: #8A2BE2;")
        self.radius_one_round_square_lalel.setFont(font_1)

        #Значення радіуса
        self.radius_one_round_square_velue = QLineEdit("0.0", self.window_shape)
        self.radius_one_round_square_velue.setGeometry(35, 350, 80, 20)
        self.radius_one_round_square_velue.setFont(font_3)
        self.radius_one_round_square_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.radius_one_round_square_velue.setStyleSheet(
            "background-color: #8A2BE2;"
            "color: #00FFFF;"
            "border: 2px solid #00FF00;"
            "border-radius: 10px; text-align: center;"
            )

        #Розмірність радіуса
        self.mm_label_radius_one_round_square = QLabel("мм", self.window_shape)
        self.mm_label_radius_one_round_square.setGeometry(120, 350, 70, 20)
        self.mm_label_radius_one_round_square.setStyleSheet("color: #8A2BE2;")
        self.mm_label_radius_one_round_square.setFont(font_1)

        #Статус радіуса       
        self.message_radius_one_round_square = QLabel(None, self.window_shape)
        self.message_radius_one_round_square.setGeometry(150, 350, 150, 20)
        if self.radius_one_round_square_velue.text() in zero:
            self.message_radius_one_round_square.setText("Відсутнє значення")
            self.message_radius_one_round_square.setFont(font_4)
            self.message_radius_one_round_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_radius_one_round_square.setStyleSheet(error_value_style)    

        #Кнопка розрахунку
        self.btn_square_one_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_square_one_radius.clicked.connect(self.perim_square_one_radius)
        self.btn_square_one_radius.setGeometry(10, 380, 350, 30)
        self.btn_square_one_radius.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 140, 0), stop:1 rgb(128, 0, 128));"
        "border-radius: 10px;"
        "font-size: 14px;"
        "font-weight: bold;"
        )
        
        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.label_square_one_radius_peremeter = QLabel("Периметр", self.window_shape)
        self.label_square_one_radius_peremeter.setGeometry(15, 420, 150, 20)
        self.label_square_one_radius_peremeter.setStyleSheet("color: #4682B4;")
        self.label_square_one_radius_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet("color: #4682B4;")
        self.perimeter.setFont(font_1)

        #Розмірність периметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeret.setStyleSheet("color: #4682B4;")
        self.mm_result_perimeret.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(32, 178, 170), stop:1 rgb(186, 85, 211));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )

        self.window_shape.show()
    
    #Периметер квадрата з однаковими радіусами
    def perim_square_one_radius(self):

        side_list_qor = self.check_number_new(self.side_one_round_square_velue.text())
        radius_list_qor = self.check_number_new(self.radius_one_round_square_velue.text())

        self.message_side_one_round_square.setText(side_list_qor[1])
        self.message_side_one_round_square.setGeometry(150, 320, side_list_qor[2], 20)
        self.message_radius_one_round_square.setText(radius_list_qor[1])        
        self.message_radius_one_round_square.setGeometry(150, 350, radius_list_qor[2], 20)

        if side_list_qor[0] == 0:
            self.message_side_one_round_square.setStyleSheet(error_value_style)
        
        if radius_list_qor[0] == 0:
            self.message_radius_one_round_square.setStyleSheet(error_value_style)

        if side_list_qor[0] != 0 and radius_list_qor[0] != 0:
            if side_list_qor[0] - (2 * radius_list_qor[0]) < 0:
                self.message_radius_one_round_square.setText("Завеликий радіус")
                self.message_side_one_round_square.setText("Замала сторона")
                self.message_radius_one_round_square.setStyleSheet(error_value_style)
                self.message_side_one_round_square.setStyleSheet(error_value_style)
                self.perimeter.setText("?")
            else:
                print(side_list_qor[0], " ", type(side_list_qor[0]))
                print(radius_list_qor[0], " ", type(radius_list_qor[0]))
                self.perimeter.setText(str(g.Perimeter.square_one_radius(side_list_qor[0], radius_list_qor[0])))
                self.message_side_one_round_square.setStyleSheet(valide_value_style)
                self.message_radius_one_round_square.setStyleSheet(valide_value_style)
        else:
            self.perimeter.setText("?")
        pass
    #КІНЕЦЬ КВАДРАТ З ОДНАКОВИМИ РАДІУСАМИ

    #КВАДРАТ З РІЗНИМИ РАДІУСАМИ
    #Вікно квадрата з різними радіусами
    def square_four_radius(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 600, 700)


        self.image_round = gui.QPixmap("img/square_four_radiuses.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 1.336), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

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
            self.message_r1_square.setFont(font_4)
            self.message_r1_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r1_square.setStyleSheet(error_value_style) 


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
        self.message_r2_square.setGeometry(140, 110, 150, 20)
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
        self.r4_square_lalel.setGeometry(15, 550, 30, 20)
        self.r4_square_lalel.setStyleSheet("color: #2E2B5F;")
        self.r4_square_lalel.setFont(font_1)

        #Значення радіуса
        self.r4_square_velue = QLineEdit("0.0", self.window_shape)
        self.r4_square_velue.setGeometry(50, 550, 80, 20)
        self.r4_square_velue.setFont(font_3)
        self.r4_square_velue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r4_square_velue.setStyleSheet(
            "background-color: #2E2B5F;"
            "color: white;"
            "border: 2px solid #00FF00;"
            "border-radius: 10px; text-align: center;"
            )

        #Розмірність радіуса
        self.mm_label_r4 = QLabel("мм", self.window_shape)
        self.mm_label_r4.setGeometry(130, 550, 70, 20)
        self.mm_label_r4.setStyleSheet("color: #2E2B5F;")
        self.mm_label_r4.setFont(font_1)

        #Статус радіуса       
        self.message_r4_square = QLabel(None, self.window_shape)
        self.message_r4_square.setGeometry(160, 550, 150, 20)
        if self.r4_square_velue.text() in zero:
            self.message_r4_square.setText("Відсутнє значення")  
            self.message_r4_square.setFont(font_4)
            self.message_r4_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r4_square.setStyleSheet(error_value_style)           
        
        #Кнопка розрахунку
        self.btn_square_four_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_square_four_radius.clicked.connect(self.perim_square_four_radius)
        self.btn_square_four_radius.setGeometry(10, 580, 350, 30)
        self.btn_square_four_radius.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 140, 0), stop:1 rgb(128, 0, 128));"
        "border-radius: 10px;"
        "font-size: 14px;"
        "font-weight: bold;"
        )

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_sfr_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_sfr_peremeter.setGeometry(15, 620, 150, 20)
        self.Label_sfr_peremeter.setStyleSheet("color: #8B00FF;")
        self.Label_sfr_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 620, 90, 20)
        self.perimeter.setStyleSheet("color: #8B00FF;")
        self.perimeter.setFont(font_1)
        
        #Розмірність приметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(255, 620, 50, 20)
        self.mm_result_perimeret.setStyleSheet("color: #8B00FF;")
        self.mm_result_perimeret.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 650, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(
        "color: #FFEFD5; "
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(32, 178, 170), stop:1 rgb(186, 85, 211));"
        "border-radius: 10px;"
        "font-size: 16px;"
        "font-weight: bold;"
        )

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
            if s1 < 0 or s2 < 0 or s3 < 0 or s4 < 0:
                if s1 < 0:
                    self.perimeter.setText('?')
                    self.message_r1_square.setText("Завеликий радіус")
                    self.message_r2_square.setText("Завеликий радіус")
                if s2 < 0:
                    self.perimeter.setText('?')
                    self.message_r2_square.setText("Завеликий радіус")
                    self.message_r3_square.setText("Завеликий радіус")
                if s3 < 0:
                    self.perimeter.setText('?')
                    self.message_r3_square.setText("Завеликий радіус")
                    self.message_r4_square.setText("Завеликий радіус")
                if s4 < 0:
                    self.perimeter.setText('?')
                    self.message_r4_square.setText("Завеликий радіус")
                    self.message_r1_square.setText("Завеликий радіус")
            else:
                #self.mm_result_perimeret.setGeometry(170, 230, 20, 20)
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
    
    #КВАДРАТ УКОЛІ
    #Вікно квадрата у колі
    def square_in_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        self.image_round = gui.QPixmap("img/square_in_round.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 1.045), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        #Сторона квадрата у колі
        #Заголовок сторони
        self.side_sir_lalel = QLabel("A", self.window_shape)
        self.side_sir_lalel.setGeometry(10, 50, 10, 20)

        #Значення сторони
        self.side_sir_velue = QLineEdit("0.0", self.window_shape)
        self.side_sir_velue.setGeometry(25, 50, 40, 20)

        #Розмірність сторони
        self.mm_label_sir = QLabel("мм", self.window_shape)
        self.mm_label_sir.setGeometry(70, 50, 40, 20)

        #Статус сторони       
        self.message_side_sir = QLabel(None, self.window_shape)
        self.message_side_sir.setGeometry(100, 50, 150, 20)
        if self.side_sir_velue.text() in zero:
            self.message_side_sir.setText("Відсутнє значення")

        #Діаметер
        #Заголовок 
        self.diameter_sir_lalel = QLabel("D", self.window_shape)
        self.diameter_sir_lalel.setGeometry(10, 80, 10, 20)

        #Значення діаметра
        self.diameter_sir_value = QLineEdit("0.0", self.window_shape)
        self.diameter_sir_value.setGeometry(25, 80, 40, 20)

        #Розмірність діаметра
        self.mm_label_diameter_sir = QLabel("мм", self.window_shape)
        self.mm_label_diameter_sir.setGeometry(70, 80, 40, 20)

        #Статус діаметра    
        self.message_diameter_sir = QLabel(None, self.window_shape)
        self.message_diameter_sir.setGeometry(100, 80, 150, 20)
        if self.diameter_sir_value.text() in zero:
            self.message_diameter_sir.setText("Відсутнє значення")

        #Кнопка розрахунку
        self.btn_perimeter = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_perimeter.setGeometry(10, 110, 200, 25)
        self.btn_perimeter.clicked.connect(self.perim_sir)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_sfr_peremeter = QLabel("Периметр квадрата", self.window_shape)
        self.Label_sfr_peremeter.setGeometry(15, 140, 120, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(130, 140, 40, 20)
        
        #Розмірність приметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(160, 140, 20, 20)


        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 170, 200, 25)
        self.btn_add_perimeter.clicked.connect(self.add_value)

        self.window_shape.show()
    
    #Периметер квадрата у колі
    def perim_sir(self) -> None:

        list_side_sir = self.check_number_new(self.side_sir_velue.text())
        list_diameter = self.check_number_new(self.diameter_sir_value.text())

        self.message_side_sir.setText(list_side_sir[1])
        self.message_diameter_sir.setText(list_diameter[1])
        
        if list_diameter[0] != 0 and list_side_sir[0] != 0:
            if (list_side_sir[0] / 0.707106) <= list_diameter[0]:
                self.message_side_sir.setText("Замала сторона")
                self.message_diameter_sir.setText("Завеликий діаметер")
                self.perimeter.setText("?")
            else:
                self.perimeter.setText(str(g.Square_in_round.perimeter_square_in_round(list_side_sir[0], list_diameter[0])))  
                self.perimeter.setGeometry(125, 140, 40, 20)
        else:
            self.perimeter.setText("?")
    #КІНЕЦЬ КВАДРАТ УКОЛІ

    #ПРЯМОКУТНИК
    #вікно прямокутника
    def rectangle(self, shape: str) -> None:        
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(120, 10, 200, 20)

        self.image_round = gui.QPixmap("img/rectangle.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 0.823), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

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
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(50, 10, 200, 20)

        self.image_round = gui.QPixmap("img/rectangle_one_radius.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 0.948), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

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
        self.Label_s_peremeter_req = QLabel("Периметр квадрата", self.window_shape)
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
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(80, 10, 200, 20)

        self.image_round = gui.QPixmap("img/rectangle_four_radius.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 1.186), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
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
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        self.image_round = gui.QPixmap("img/hexagon.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 0.872), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

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
        self.Label_d_peremeter = QLabel("Периметр кола", self.window_shape)
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
    #КІНЕЦЬ ШЕСТИГАРННИК

    #ОВАЛ
    #Вікно овала
    def oblong(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)


        self.image_round = gui.QPixmap("img/oblong.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(200 / 0.577), 200)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

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
        self.btn_oblong = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_oblong.setGeometry(10, 110, 200, 20)
        self.btn_oblong.clicked.connect(self.perim_oblong)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр квадрата", self.window_shape)
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
    #КІНЕЦЬ ОВАЛ

    #ТРИКУТНИК РІВНОСТОРОННІЙ
    #Вікно трикутника рівносоторонній
    def equilateral_triangle(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        self.image_round = gui.QPixmap("img/Triangle_60.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 1.325), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

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
        self.btn_eq_tr_a = QPushButton("Розрахувати периметр", self.window_shape)
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
        self.btn_eq_tr_h = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_eq_tr_h.setGeometry(10, 140, 200, 20)
        self.btn_eq_tr_h.clicked.connect(self.perim_eq_riangle_h)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр квадрата", self.window_shape)
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
    #КІНЕЦЬ ТРИКУТНИК РІВНОСТОРОННІЙ

    #РІВНОБЕДРЕНИЙ ТРИКУТНИК
    #Вікно рівнобедреного трикутника
    def isosceles_triangle(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()
        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(950, 200, 600, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

        self.image_round = gui.QPixmap("img/Treangle_.jpg")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(230, 30, int(260 * 0.955), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
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
        self.btn_perim_is_tr_a_b = QPushButton("Розрахувати периметр (по А, В)", self.window_shape)
        self.btn_perim_is_tr_a_b.setGeometry(10, 120, 200, 20)
        self.btn_perim_is_tr_a_b.clicked.connect(self.perim_is_tr_a_b)

        #Кнопка розрахунку через сторону А та сторону H
        self.btn_perim_is_tr_a_h = QPushButton("Розрахувати периметр (по А, Н)", self.window_shape)
        self.btn_perim_is_tr_a_h.setGeometry(10, 150, 200, 20)
        self.btn_perim_is_tr_a_h.clicked.connect(self.perim_is_tr_a_h)

        #Кнопка розрахунку через сторону B та сторону H
        self.btn_perim_is_tr_b_h = QPushButton("Розрахувати периметр (по B, Н)", self.window_shape)
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
            self.message_perimeter.setStyleSheet(valide_value_style)
            self.message_perimeter.setText("Валідне значення")
            self.message_perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        if self.perimeter_velue.text() in zero:
            self.message_perimeter.setText("Відсутнє значення")
            self.message_perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.message_perimeter.setGeometry(230, 50, 150, 20)
            self.message_perimeter.setStyleSheet(error_value_style)

    #КІНЕЦЬ РІВНОБЕДРЕНИЙ ТРИКУТНИК

if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    gui.QFontDatabase.addApplicationFont("fonts/Kareliac bold.otf")
    gui.QFontDatabase.addApplicationFont("fonts/v_CCYadaYadaYadaInt.ttf")
    gui.QFontDatabase.addApplicationFont("fonts/Aver_Bold_Italic.ttf")
    gui.QFontDatabase.addApplicationFont("fonts/v_WhizBang.ttf")
    font_0 = gui.QFont("KareliaC", 16)
    font_1 = gui.QFont("v_CCYadaYadaYadaInt", 14)
    font_2 = gui.QFont("Aver", 11)
    font_3 = gui.QFont("v_CCYadaYadaYadaInt", 12)
    font_4 = gui.QFont("v_WhizBang", 10)
    main_window = MainWindow()
    main_window.setFixedSize(450, 230)
    main_window.show()
    sys.exit(my_app.exec_())