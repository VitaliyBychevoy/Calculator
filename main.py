import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as gui
from PyQt5 import QtCore
from PyQt5.QtWinExtras import QWinTaskbarButton

import geometry as g
import style as s

material = {
    "Алюміній": 0.5,
    "Мідь": 0.57,
    "Сталь звичайна": 1,
    "Сталь нержавіюча": 1.5
 }

#Допустимі символи
exceptable_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']

#Можливі нульові значення
zero = ['0', '0,0', '0.0', '', '.', ',']

ROUND_IMAGE_PATH = "img/Round.jpg"
HALFROUND_IMAGE_PATH = "img/Half_round_1.jpg"
SQUARE_IMAGE_PATH = "img/square.jpg"
SQUARE_ONE_RADIUS_IMAGE_PATH = "img/square_one_radius.jpg"
SQUARE_FOUR_RADIUS_IMAGE_PATH = "img/square_four_radiuses.jpg"
SQUARE_IN_ROUND_IMAGE_PATH = "img/square_in_round.jpg"
RECTANGE_IMAGE_PATH = "img/rectangle.jpg"
RECTANGLE_ONE_RADIUS_IMAGE_PATH = "img/rectangle_one_radius.jpg"
RECTANGLE_FOUR_RADIUS_IMAGE_PATH = "img/rectangle_four_radius.jpg"
HEXAGON_IMAGE_PATH = "img/hexagon.jpg"
OBLONG_IMAGE_PATH = "img/oblong.jpg"
TRIANGLE_IMAGE_PATH = "img/Triangle_60.jpg"
ISOSCELES_TRIANGLE_IMAGE_PATH = "img/Treangle_.jpg"

ICON = 'img/Cluster.png'

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 450, 350)
        self.setWindowTitle("Розрахунок зусилля для кластера")
        self.setWindowIcon(gui.QIcon(f"{ICON}"))

        #ФОРМИ
        #Заголовок форми
        self.force_result_label = QLabel("Форма", self)
        self.force_result_label.setGeometry(10, 20, 80, 30)
        self.force_result_label.setStyleSheet(f"color: {s.COLOR};")
        self.force_result_label.setFont(font_1)

        #Cписок форм
        self.shape = QComboBox(self)
        self.shape.addItem("Оберіть форму одного отвору")
        self.shape.addItem("Коло")
        self.shape.addItem("Напівколо")
        self.shape.addItem("Квадрат")
        self.shape.addItem("Квадрат з радіусом")
        self.shape.addItem("Квадрат з радіусами")
        self.shape.addItem("Квадрат у колі")
        self.shape.addItem("Прямокутник")
        self.shape.addItem("Прямокутник з радіусом")
        self.shape.addItem("Прямокутник з радіусами")
        self.shape.addItem("Шестигранник")
        self.shape.addItem("Овал з паралельними сторонами")
        self.shape.addItem("Трикутник рівносторонній")
        self.shape.addItem("Трикутник рівнобедрений")        
        self.shape.setGeometry(120, 15, 320, 30)
        self.shape.currentTextChanged.connect(self.shape_handler)
        self.shape.setStyleSheet(s.qComboBox_style_Line_Edit)
        self.shape.setFont(font_2)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.perimeter_label = QLabel("Периметр", self)
        self.perimeter_label.setGeometry(10, 50, 100, 30)
        self.perimeter_label.setStyleSheet(f"color: {s.COLOR};")
        self.perimeter_label.setFont(font_1)

        #Значення периметра
        self.perimeter_value = QLineEdit("0.0", self)
        self.perimeter_value.setGeometry(120, 50, 70, 30)
        self.perimeter_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.perimeter_value.setGeometry(120, 50, 70, 30)
        self.perimeter_value.setStyleSheet(s.line_edit_main_window_style)
        self.perimeter_value.setFont(font_3)

        #Розмірність периметра
        self.mm_label_perimeter = QLabel("мм", self)
        self.mm_label_perimeter.setGeometry(195, 50, 70, 30)
        self.mm_label_perimeter.setStyleSheet(f"color: {s.COLOR};")
        self.mm_label_perimeter.setFont(font_1)

        #Статус введенного периметра
        self.message_perimeter = QLabel(None, self)
        self.message_perimeter.setGeometry(230, 55, 150, 30)
        self.message_perimeter.setFont(font_4)
        if self.perimeter_value.text() in zero:
            self.message_perimeter.setText("Відсутнє значення")
            self.message_perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.message_perimeter.setGeometry(230, 50, s.message_width, 30)
            self.message_perimeter.setStyleSheet(s.error_value_style)

        #ТОВЩИНА
        #Заголовок товщини       
        self.thickness_label = QLabel("Товщина", self)
        self.thickness_label.setGeometry(10, 85, 100, 30)
        self.thickness_label.setStyleSheet(f"color: {s.COLOR};")
        self.thickness_label.setFont(font_1)

        #Значення товщини
        self.thickness_value = QLineEdit("0.0", self)
        self.thickness_value.setGeometry(120, 85, 70, 30)
        self.thickness_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.thickness_value.setStyleSheet(s.line_edit_main_window_style)
        self.thickness_value.setFont(font_3)

        #Розмірність товщини
        self.mm_label_thickness = QLabel("мм", self)
        self.mm_label_thickness.setGeometry(195, 85, 50, 30)
        self.mm_label_thickness.setStyleSheet(f"color: {s.COLOR};")
        self.mm_label_thickness.setFont(font_1)
        
        #Статус введенної товщини
        self.message_thickness = QLabel(None, self)
        self.message_thickness.setGeometry(230, 85, s.message_width, 30)
        self.message_thickness.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)      
        self.message_thickness.setFont(font_4)
        if self.thickness_value.text() in zero:
            self.message_thickness.setText("Відсутнє значення")
            self.message_thickness.setStyleSheet(s.error_value_style)

        #МАТЕРІАЛ
        #Заголовок матеріала
        self.material_label = QLabel("Матеріал", self)
        self.material_label.setGeometry(10, 125, 100, 20)
        self.material_label.setStyleSheet(f"color: {s.COLOR};")
        self.material_label.setFont(font_1)

        #Список матеріалів
        # усі літери і у назвах матеріалу англійські
        self.material = QComboBox(self)
        self.material.addItem("Сталь звичайна") 
        self.material.addItem("Сталь нержавіюча")
        self.material.addItem("Алюміній")
        self.material.addItem("Мідь")
        self.material.setGeometry(120, 120, 320, 30)
        self.material.setStyleSheet(s.qComboBox_style_Line_Edit)
        self.material.setFont(font_4)

        #ОТВОРИ
        #Заголовок отворів
        self.amount_holes_label = QLabel("Отворiв", self)
        self.amount_holes_label.setGeometry(10, 160, 100, 20)
        self.amount_holes_label.setStyleSheet(f"color: {s.COLOR};")
        self.amount_holes_label.setFont(font_1)

        #Список отворів
        self.amount_holes = QComboBox(self)
        for i in range(1, 37):
            self.amount_holes.addItem(str(i))
        self.amount_holes.setGeometry(120, 155, 60, 30)
        self.amount_holes.setStyleSheet(s.qComboBox_style_Line_Edit)
        self.amount_holes.setFont(font_3)

        #КНОПКА ДЛЯ РОЗРАХУВАННЯ ЗУСИЛЛЯ
        self.btn = QPushButton("Розрахувати зусилля", self)
        self.btn.setGeometry(120, 190, 320, 40)
        self.btn.setStyleSheet(s.force_button_style)
        self.btn.clicked.connect(self.calculate_tonage_new)

        #ОТРИМАНЕ ЗУСИЛЛЯ
        #Заголовок зусилля
        self.force_result_label = QLabel("Зусилля", self)
        self.force_result_label.setGeometry(10, 245, 100, 25)
        self.force_result_label.setFont(font_0)
        self.force_result_label.setStyleSheet(f"color: {s.RESULT_FORCE_COLOR};")

        #Значеня зусилля
        self.force_result_value = QLineEdit('?', self)
        self.force_result_value.setGeometry(120, 245, 100, 25)
        self.force_result_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)    
        self.force_result_value.setFont(font_0)
        self.force_result_value.setStyleSheet(s.result_style)

        #Розмірність зусилля
        self.tonage_label_force = QLabel("тонн(и)", self)
        self.tonage_label_force.setGeometry(230, 245, 100, 20)
        self.tonage_label_force.setFont(font_0)
        self.tonage_label_force.setStyleSheet(f"color: {s.RESULT_FORCE_COLOR};")

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()

    def paintEvent(self, a0: gui.QPaintEvent) -> None:
        painter = gui.QPainter(self)
        pixmap = gui.QPixmap("img/main_12.jpg")
        #pixmap = gui.QPixmap("img/2.png")
        painter.drawPixmap(self.rect(), pixmap)

    #Розрахунок навантаження
    def calculate_tonage_new(self):
        coeff_material = self.coefficient_material()
        
        perimeter_list = self.check_number_new(self.perimeter_value.text())
        thickness_list = self.check_number_new(self.thickness_value.text()) 

        self.message_perimeter.setText(perimeter_list[1])
        self.message_thickness.setText(thickness_list[1])
        self.message_perimeter.setGeometry(230, 50, perimeter_list[2], 30)
        self.message_thickness.setGeometry(230, 85, thickness_list[2], 30)

        if perimeter_list[0] == 0 :
            self.message_perimeter.setStyleSheet(s.error_value_style)

        else:
            self.message_perimeter.setStyleSheet(s.valide_value_style)

        if thickness_list[0] == 0:
            self.message_thickness.setStyleSheet(s.error_value_style)
        else:
            self.message_thickness.setStyleSheet(s.valide_value_style)

        if perimeter_list[0] != 0 and thickness_list[0] != 0:
            result = 0.0352 * coeff_material
            result = result * perimeter_list[0]
            result = result * thickness_list[0]
            result = round(result * float(self.amount_holes.currentText()), 2)
            self.perimeter_value.setText(str(round(perimeter_list[0], 1)))
            self.thickness_value.setText(str(round(thickness_list[0], 2)))
            self.message_perimeter.setStyleSheet(s.valide_value_style)
            self.message_thickness.setStyleSheet(s.valide_value_style)
            self.force_result_value.setText(str(result))
        else:
            self.force_result_value.setText("?")

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
                    message = f'"{letter}" є некоректний символ'
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
            
            if float(item_string) < 0.01:
                result[0] = 0
                result[1] = "0.01 мінімальне значення"
                result[2] = 210
                return result
            
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
        elif shape == "Квадрат з радіусом":
            self.square_one_radius(shape)
        elif shape == "Квадрат з радіусами":
            self.square_four_radius(shape)
        elif shape == "Квадрат у колі":
            self.square_in_round(shape)
        elif shape == "Прямокутник":
            self.rectangle(shape)
        elif shape == "Прямокутник з радіусом":
            self.rectangle_one_round(shape)
        elif shape == "Прямокутник з радіусами":
            self.rectangle_four_round(shape)
        elif shape == "Шестигранник":
            self.hexagon(shape)
        elif shape == "Овал з паралельними сторонами":
            self.oblong(shape)
        elif shape == "Трикутник рівносторонній":
            self.equilateral_triangle(shape)
        elif shape == "Трикутник рівнобедрений":
            self.isosceles_triangle(shape)

    #Закриваємо вікно форми у разі якщо у списку форм головного вікна оберемо "Оберіть форму одного отвору"
    def close_shape_window(self):
        if self.shape.currentText() == "Оберіть форму одного отвору":
            self.window_shape.close()

    #КОЛО
    #Вікно для кола
    def round_handler(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.image_round = gui.QPixmap(f"{ROUND_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(40, 30, 290, 300)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        self.window_shape.setFixedSize(370, 500)

        #ДІАМЕТР
        #Заголовок диаметра
        self.diameter_label = QLabel("D", self.window_shape)
        self.diameter_label.setGeometry(15, 350, 15, 20)
        self.diameter_label.setStyleSheet(s.all_labels_style)
        self.diameter_label.setFont(font_1)

        #Значення диаметра
        self.diameter_value = QLineEdit("0.0", self.window_shape)
        self.diameter_value.setGeometry(35, 350, 80, 25)
        self.diameter_value.setFont(font_3)
        self.diameter_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.diameter_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність диаметра
        self.mm_label_d = QLabel("мм", self.window_shape)
        self.mm_label_d.setGeometry(120, 350, 70, 20)
        self.mm_label_d.setFont(font_1)
        self.mm_label_d.setStyleSheet(s.all_labels_style)


        #Статус діаметра         
        self.message_diameter = QLabel(None, self.window_shape)
        self.message_diameter.setGeometry(150, 350, 150, 20)

        if self.diameter_value.text() in zero:
            self.message_diameter.setText("Відсутнє значення")
            self.message_diameter.setFont(font_4)
            self.message_diameter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_diameter.setStyleSheet(s.error_value_style)

        #Кнопка розрахунку
        self.btn_d = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_d.setGeometry(10, 380, 350, 30)
        self.btn_d.clicked.connect(self.perim_round)
        self.btn_d.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_d_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_d_peremeter.setFont(font_1)

        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)
        self.window_shape.show()

    #Периметер кола  
    def perim_round(self):

        diameter_list_d = self.check_number_new(self.diameter_value.text())
        self.message_diameter.setText(diameter_list_d[1])

        if diameter_list_d[0] == 0:
            self.message_diameter.setGeometry(150, 350, diameter_list_d[2], 20)
            self.message_diameter.setStyleSheet(s.error_value_style)
            self.perimeter.setText("?")
        else:
            r = g.Round()
            self.perimeter.setText(str(r.perimeter_round(diameter = diameter_list_d[0])))
            del(r)
            self.diameter_value.setText(str(round(diameter_list_d[0], 2)))
            self.message_diameter.setGeometry(150, 350, diameter_list_d[2], 20)
            self.message_diameter.setStyleSheet(s.valide_value_style)
    #КІНЕЦЬ КОЛО

    #НАПІВКОЛО
    def half_round_heandler(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 490)
        self.window_shape.setFixedSize(370, 490)

        #ДІАМЕТР
        #Заголовок диаметра
        self.diameter_hr_label = QLabel("D", self.window_shape)
        self.diameter_hr_label.setGeometry(15, 290, 15, 20)
        self.diameter_hr_label.setStyleSheet(s.all_labels_style)
        
        self.diameter_hr_label.setFont(font_1)

        #Значення диаметра
        self.diameter_hr_value = QLineEdit("0.0", self.window_shape)
        self.diameter_hr_value.setGeometry(35, 290, 80, 25)
        self.diameter_hr_value.setFont(font_3)
        self.diameter_hr_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.diameter_hr_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність диаметра
        self.mm_label_d_hr = QLabel("мм", self.window_shape)
        self.mm_label_d_hr.setGeometry(120, 290, 70, 20)
        self.mm_label_d_hr.setStyleSheet(s.all_labels_style)
        self.mm_label_d_hr.setFont(font_1)

        #Статус діаметра         
        self.message_diameter_hr = QLabel(None, self.window_shape)
        self.message_diameter_hr.setGeometry(150, 290, 150, 20)
        if self.diameter_hr_value.text() in zero:
            self.message_diameter_hr.setText("Відсутнє значення")
            self.message_diameter_hr.setFont(font_4)
            self.message_diameter_hr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_diameter_hr.setStyleSheet(s.error_value_style)      

        #Висота
        #Заголовок висоти
        self.height_hr_label = QLabel("H", self.window_shape)
        self.height_hr_label.setGeometry(15, 320, 15, 20)
        self.height_hr_label.setStyleSheet(s.all_labels_style)
        self.height_hr_label.setFont(font_1)

        #Значення висоти
        self.height_hr_value = QLineEdit("0.0", self.window_shape)
        self.height_hr_value.setGeometry(35, 320, 80, 25)
        self.height_hr_value.setFont(font_3)
        self.height_hr_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.height_hr_value.setStyleSheet(s.q_line_edit_style)
        
        #Розмірність висоти
        self.mm_label_h_hr = QLabel("мм", self.window_shape)
        self.mm_label_h_hr.setGeometry(120, 320, 70, 20)
        self.mm_label_h_hr.setStyleSheet(s.all_labels_style)
        self.mm_label_h_hr.setFont(font_1)

        #Статус висоти         
        self.message_height_hr = QLabel(None, self.window_shape)
        self.message_height_hr.setGeometry(150, 320, 150, 20)

        if self.height_hr_value.text() in zero:
            self.message_height_hr.setText("Відсутнє значення")
            self.message_height_hr.setFont(font_4)
            self.message_height_hr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_height_hr.setStyleSheet(s.error_value_style)         

        self.image_half_round = gui.QPixmap(f"{HALFROUND_IMAGE_PATH}")
        self.image_label = QLabel(self.window_shape)
        self.image_label.setGeometry(12, 10, int(250 * 1.387 ), 250)
        self.image_label.setPixmap(self.image_half_round )
        self.image_label.setScaledContents(True)

        #Кнопка розрахунку
        self.btn_perim = QPushButton("Розрахувати периметр та довжину хорди", self.window_shape)
        self.btn_perim.clicked.connect(self.perim_half_round_height)
        self.btn_perim.setGeometry(10, 350, 350, 30)
        self.btn_perim.setStyleSheet(s.btn_perimeter_1)

        #ХОРДА
        #Заголовок хорди
        self.lenght_hr_label = QLabel("Хорда L", self.window_shape)
        self.lenght_hr_label.setGeometry(15, 390, 150, 20)
        self.lenght_hr_label.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.lenght_hr_label.setFont(font_1)

        #Значення хорди
        self.lenght_hr_value = QLabel("0.0", self.window_shape)
        self.lenght_hr_value.setGeometry(165, 390, 90, 20)
        self.lenght_hr_value.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.lenght_hr_value.setFont(font_1)

        #Розмірність хорди
        self.mm_label_length_hr = QLabel("мм", self.window_shape)
        self.mm_label_length_hr.setGeometry(255, 390, 50, 20)
        self.mm_label_length_hr.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_label_length_hr.setFont(font_1)

        #ПЕРИМЕТР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_d_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_d_peremeter.setFont(font_1)

        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність периметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()

    #Периметер напівкільця
    def perim_half_round_height(self):

        diameter_list = self.check_number_new(self.diameter_hr_value.text())
        height_list = self.check_number_new(self.height_hr_value.text())

        self.message_diameter_hr.setText(diameter_list[1])
        self.message_height_hr.setText(height_list[1])

        self.message_diameter_hr.setGeometry(150, 290, diameter_list[2], 20)
        self.message_diameter_hr.setStyleSheet(s.error_value_style)
        self.message_height_hr.setGeometry(150, 320, height_list[2], 20)
        self.message_height_hr.setStyleSheet(s.error_value_style)
        self.lenght_hr_value.setText("?")
        self.perimeter.setText("?")

        if diameter_list[0] != 0:
            self.message_diameter_hr.setGeometry(150, 290, diameter_list[2], 20)
            self.message_diameter_hr.setStyleSheet(s.valide_value_style)
            self.diameter_hr_value.setText(str(round(diameter_list[0], 2)))
        if height_list[0] != 0:
            self.message_height_hr.setGeometry(150, 320, height_list[2], 20)
            self.message_height_hr.setStyleSheet(s.valide_value_style)
            self.height_hr_value.setText(str(round(height_list[0], 2)))

        if diameter_list[0] != 0 and height_list[0] != 0:
            if diameter_list[0] <= height_list[0]:
                self.message_diameter_hr.setText("Замалий розмір D")
                self.message_diameter_hr.setGeometry(150, 290, 190, 20)
                self.message_diameter_hr.setStyleSheet(s.error_value_style)
                self.message_height_hr.setText("Завеликий розмір H")
                self.message_height_hr.setGeometry(150, 320, 190, 20)
                self.message_height_hr.setStyleSheet(s.error_value_style)
            else:
                incomplete_circle = g.Incomplete_circle()
                if height_list[0] > (diameter_list[0] / 2):
                    #Висота більша за радіус
                    self.perimeter.setText(str(incomplete_circle.perim_in_circle(diameter_list[0], height_list[0])))
                    l = round(incomplete_circle.lenght_chold(diameter_list[0], height_list[0]), 2)
                    self.lenght_hr_value.setText(str(l))
                    del(incomplete_circle)
                elif height_list[0] == (diameter_list[0] / 2):
                    #Висота дорівнює радіусу
                    self.perimeter.setText(str(incomplete_circle.perim_half_round(diameter_list[0], height_list[0])))
                    self.lenght_hr_value.setText(str(height_list[0] * 2))
                    del(incomplete_circle)
                elif height_list[0] < (diameter_list[0] / 2):
                    #Висота меньша за радіус
                    l = round(incomplete_circle.lenght_chold(diameter_list[0], height_list[0]), 2)
                    self.lenght_hr_value.setText(str(l))
                    p = round((incomplete_circle.perim_half_round_height_less_radius(diameter_list[0], height_list[0])), 2)
                    self.perimeter.setText(str(p))
                    del(incomplete_circle)
    #КІНЕЦЬ НАПІВКОЛО 

    #КВАДРАТ
    #Вікно квадрата
    def square(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.window_shape.setFixedSize(370, 500)

        self.image_round = gui.QPixmap(f"{SQUARE_IMAGE_PATH}")
        self.image_label = QLabel(self.window_shape)
        self.image_label.setGeometry(52, 30, int(260 / 1.023), 260)
        self.image_label.setPixmap(self.image_round)
        self.image_label.setScaledContents(True)
        
        #Сторона
        #Заголовок сторони
        self.side_label = QLabel("A", self.window_shape)
        self.side_label.setGeometry(15, 350, 15, 20)
        self.side_label.setStyleSheet(s.all_labels_style)
        self.side_label.setFont(font_1)

        #Значення диаметра
        self.side_value = QLineEdit("0.0", self.window_shape)
        self.side_value.setGeometry(35, 350, 80, 25)
        self.side_value.setFont(font_3)
        self.side_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_value.setStyleSheet(s.q_line_edit_style)
        
        #Розмірність диаметра
        self.mm_label_side = QLabel("мм", self.window_shape)
        self.mm_label_side.setGeometry(120, 350, 70, 20)
        self.mm_label_side.setStyleSheet(s.all_labels_style)
        self.mm_label_side.setFont(font_1)

        #Статус сторони       
        self.message_side = QLabel(None, self.window_shape)
        self.message_side.setGeometry(150, 350, 150, 20)
        if self.side_value.text() in zero:
            self.message_side.setText("Відсутнє значення")
            self.message_side.setFont(font_4)
            self.message_side.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side.setStyleSheet(s.error_value_style)         
     
        #Кнопка розрахунку
        self.btn_s = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_s.clicked.connect(self.perim_square)
        self.btn_s.setGeometry(10, 380, 350, 30)
        self.btn_s.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_s_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_s_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 25)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()

    #Периметр квадрата
    def perim_square(self) -> None:
        square_list = self.check_number_new(self.side_value.text())
        self.message_side.setText(square_list[1])

        self.message_side.setGeometry(150, 350, square_list[2], 20)

        if square_list[0] == 0:
            self.message_side.setStyleSheet(s.error_value_style)   
            self.perimeter.setText("?")
        else:
            square = g.Square()
            self.side_value.setText(str(round(square_list[0], 2)))
            self.message_side.setStyleSheet(s.valide_value_style)      
            self.perimeter.setText(str(square.perimeter_square(float(square_list[0]))))                         
    #КІНЕЦЬ КВАДРАТ

    #КВАДРАТ З ОДНАКОВИМИ РАДІУСАМИ
    #Вікно квадрата з однаковими радіусами
    def square_one_radius(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)

        self.image_round = gui.QPixmap(f"{SQUARE_ONE_RADIUS_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(34, 30, int(260 * 1.16), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        self.window_shape.setFixedSize(370, 500)

        #Сторона 
        #Заголовок сторони
        self.side_one_round_square_label = QLabel("A", self.window_shape)
        self.side_one_round_square_label.setGeometry(15, 320, 15, 20)
        self.side_one_round_square_label.setStyleSheet(s.all_labels_style)
        self.side_one_round_square_label.setFont(font_1)

        #Значення сторони
        self.side_one_round_square_value = QLineEdit("0.0", self.window_shape)
        self.side_one_round_square_value.setGeometry(35, 320, 80, 25)
        self.side_one_round_square_value.setFont(font_3)
        self.side_one_round_square_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_one_round_square_value.setStyleSheet(s.q_line_edit_style)
        
        #Розмірність сторони
        self.mm_label_side_one_round_square = QLabel("мм", self.window_shape)
        self.mm_label_side_one_round_square.setGeometry(120, 320, 70, 20)
        self.mm_label_side_one_round_square.setStyleSheet(s.all_labels_style)
        self.mm_label_side_one_round_square.setFont(font_1)

        #Статус сторони       
        self.message_side_one_round_square = QLabel(None, self.window_shape)
        self.message_side_one_round_square.setGeometry(150, 320, 150, 20)
        if self.side_one_round_square_value.text() in zero:
            self.message_side_one_round_square.setText("Відсутнє значення")
            self.message_side_one_round_square.setFont(font_4)
            self.message_side_one_round_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_one_round_square.setStyleSheet(s.error_value_style)  

        #Радіус
        #Заголовок радіуса
        self.radius_one_round_square_label = QLabel("R", self.window_shape)
        self.radius_one_round_square_label.setGeometry(15, 350, 15, 20)
        self.radius_one_round_square_label.setStyleSheet(s.all_labels_style)
        self.radius_one_round_square_label.setFont(font_1)

        #Значення радіуса
        self.radius_one_round_square_value = QLineEdit("0.0", self.window_shape)
        self.radius_one_round_square_value.setGeometry(35, 350, 80, 25)
        self.radius_one_round_square_value.setFont(font_3)
        self.radius_one_round_square_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.radius_one_round_square_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_radius_one_round_square = QLabel("мм", self.window_shape)
        self.mm_label_radius_one_round_square.setGeometry(120, 350, 70, 20)
        self.mm_label_radius_one_round_square.setStyleSheet(s.all_labels_style)
        self.mm_label_radius_one_round_square.setFont(font_1)

        #Статус радіуса       
        self.message_radius_one_round_square = QLabel(None, self.window_shape)
        self.message_radius_one_round_square.setGeometry(150, 350, 150, 20)
        if self.radius_one_round_square_value.text() in zero:
            self.message_radius_one_round_square.setText("Відсутнє значення")
            self.message_radius_one_round_square.setFont(font_4)
            self.message_radius_one_round_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_radius_one_round_square.setStyleSheet(s.error_value_style)    

        #Кнопка розрахунку
        self.btn_square_one_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_square_one_radius.clicked.connect(self.perim_square_one_radius)
        self.btn_square_one_radius.setGeometry(10, 380, 350, 30)
        self.btn_square_one_radius.setStyleSheet(s.btn_perimeter_1)
        
        #ПЕРИМЕТР
        #Заголовок периметра
        self.label_square_one_radius_peremeter = QLabel("Периметр", self.window_shape)
        self.label_square_one_radius_peremeter.setGeometry(15, 420, 150, 20)
        self.label_square_one_radius_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.label_square_one_radius_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність периметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)
        self.window_shape.show()
    
    #Периметер квадрата з однаковими радіусами
    def perim_square_one_radius(self):

        side_list_qor = self.check_number_new(self.side_one_round_square_value.text())
        radius_list_qor = self.check_number_new(self.radius_one_round_square_value.text())

        self.message_side_one_round_square.setText(side_list_qor[1])
        self.message_side_one_round_square.setGeometry(150, 320, side_list_qor[2], 20)
        self.message_radius_one_round_square.setText(radius_list_qor[1])        
        self.message_radius_one_round_square.setGeometry(150, 350, radius_list_qor[2], 20)

        if side_list_qor[0] == 0:
            self.message_side_one_round_square.setStyleSheet(s.error_value_style)
        
        if radius_list_qor[0] == 0:
            self.message_radius_one_round_square.setStyleSheet(s.error_value_style)
        else:
            self.message_radius_one_round_square.setStyleSheet(s.valide_value_style)

        if side_list_qor[0] != 0 and radius_list_qor[0] != 0:
            if side_list_qor[0] - (2 * radius_list_qor[0]) < 0:
                self.message_radius_one_round_square.setText("Завеликий радіус")
                self.message_side_one_round_square.setText("Замала сторона")
                self.message_radius_one_round_square.setStyleSheet(s.error_value_style)
                self.message_side_one_round_square.setStyleSheet(s.error_value_style)
                self.perimeter.setText("?")
            else:
                square_one_r = g.Square_One_Radius()
                self.perimeter.setText(str(square_one_r.perimeter_square_one_radius(side_list_qor[0], radius_list_qor[0])))
                self.message_side_one_round_square.setStyleSheet(s.valide_value_style)
                self.message_radius_one_round_square.setStyleSheet(s.valide_value_style)
                del(square_one_r)
        else:
            self.perimeter.setText("?")
    #КІНЕЦЬ КВАДРАТ З ОДНАКОВИМИ РАДІУСАМИ

    #КВАДРАТ З РІЗНИМИ РАДІУСАМИ
    #Вікно квадрата з різними радіусами
    def square_four_radius(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 390, 560)
        self.window_shape.setFixedSize(390, 560)


        self.image_round = gui.QPixmap(f"{SQUARE_FOUR_RADIUS_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(21, 30, int(260 * 1.336), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона 
        #Заголовок сторони
        self.side_four_radius_label = QLabel("A", self.window_shape)
        self.side_four_radius_label.setGeometry(15, 300, 30, 20)
        self.side_four_radius_label.setStyleSheet(s.all_labels_style)
        self.side_four_radius_label.setFont(font_1)

        #Значення сторони
        self.side_four_radius_value = QLineEdit("0.0", self.window_shape)
        self.side_four_radius_value.setGeometry(50, 300, 80, 25)
        self.side_four_radius_value.setFont(font_3)
        self.side_four_radius_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_four_radius_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_label_side_four_radius_label = QLabel("мм", self.window_shape)
        self.mm_label_side_four_radius_label.setGeometry(135, 300, 70, 20)
        self.mm_label_side_four_radius_label.setStyleSheet(s.all_labels_style)
        self.mm_label_side_four_radius_label.setFont(font_1)

        #Статус сторони       
        self.message_side_four_radius = QLabel(None, self.window_shape)
        self.message_side_four_radius.setGeometry(170, 300, 150, 20)
        if self.message_side_four_radius.text() in zero:
            self.message_side_four_radius.setText("Відсутнє значення")
            self.message_side_four_radius.setFont(font_4)
            self.message_side_four_radius.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_four_radius.setStyleSheet(s.error_value_style)

        #Радіус R1
        #Заголовок радіуса
        self.r1_square_label = QLabel("R1", self.window_shape)
        self.r1_square_label.setGeometry(15, 330, 30, 20)
        self.r1_square_label.setStyleSheet(s.all_labels_style)
        self.r1_square_label.setFont(font_1)

        #Значення радіуса
        self.r1_square_value = QLineEdit("0.0", self.window_shape)
        self.r1_square_value.setGeometry(50, 330, 80, 25)
        self.r1_square_value.setFont(font_3)
        self.r1_square_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r1_square_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r1 = QLabel("мм", self.window_shape)
        self.mm_label_r1.setGeometry(135, 330, 70, 20)
        self.mm_label_r1.setStyleSheet(s.all_labels_style)
        self.mm_label_r1.setFont(font_1)

        #Статус радіуса       
        self.message_r1_square = QLabel(None, self.window_shape)
        self.message_r1_square.setGeometry(170, 330, 150, 20)
        if self.r1_square_value.text() in zero:
            self.message_r1_square.setText("Відсутнє значення")
            self.message_r1_square.setFont(font_4)
            self.message_r1_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r1_square.setStyleSheet(s.error_value_style)

        #Радіус R2
        #Заголовок радіуса
        self.r2_square_label = QLabel("R2", self.window_shape)
        self.r2_square_label.setGeometry(15, 360, 30, 20)
        self.r2_square_label.setStyleSheet(s.all_labels_style)
        self.r2_square_label.setFont(font_1)

        #Значення радіуса
        self.r2_square_value = QLineEdit("0.0", self.window_shape)
        self.r2_square_value.setGeometry(50, 360, 80, 25)
        self.r2_square_value.setFont(font_3)
        self.r2_square_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r2_square_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r2 = QLabel("мм", self.window_shape)
        self.mm_label_r2.setGeometry(135, 360, 70, 20)
        self.mm_label_r2.setStyleSheet(s.all_labels_style)
        self.mm_label_r2.setFont(font_1)

        #Статус радіуса       
        self.message_r2_square = QLabel(None, self.window_shape)
        self.message_r2_square.setGeometry(170, 360, 150, 20)
        if self.r2_square_value.text() in zero:
            self.message_r2_square.setText("Відсутнє значення")
            self.message_r2_square.setFont(font_4)
            self.message_r2_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r2_square.setStyleSheet(s.error_value_style)

        #Радіус R3
        #Заголовок радіуса
        self.r3_square_label = QLabel("R3", self.window_shape)
        self.r3_square_label.setGeometry(15, 390, 30, 20)
        self.r3_square_label.setStyleSheet(s.all_labels_style)
        self.r3_square_label.setFont(font_1)

        #Значення радіуса
        self.r3_square_value = QLineEdit("0.0", self.window_shape)
        self.r3_square_value.setGeometry(50, 390, 80, 25)
        self.r3_square_value.setFont(font_3)
        self.r3_square_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r3_square_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r3 = QLabel("мм", self.window_shape)
        self.mm_label_r3.setGeometry(135, 390, 70, 20)
        self.mm_label_r3.setStyleSheet(s.all_labels_style)
        self.mm_label_r3.setFont(font_1)


        #Статус радіуса       
        self.message_r3_square = QLabel(None, self.window_shape)
        self.message_r3_square.setGeometry(170, 390, 150, 20)
        if self.r3_square_value.text() in zero:
            self.message_r3_square.setText("Відсутнє значення")
            self.message_r3_square.setFont(font_4)
            self.message_r3_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r3_square.setStyleSheet(s.error_value_style)  

        #Радіус R4
        #Заголовок радіуса
        self.r4_square_label = QLabel("R4", self.window_shape)
        self.r4_square_label.setGeometry(15, 420, 30, 20)
        self.r4_square_label.setStyleSheet(s.all_labels_style)
        self.r4_square_label.setFont(font_1)

        #Значення радіуса
        self.r4_square_value = QLineEdit("0.0", self.window_shape)
        self.r4_square_value.setGeometry(50, 420, 80, 25)
        self.r4_square_value.setFont(font_3)
        self.r4_square_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r4_square_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r4 = QLabel("мм", self.window_shape)
        self.mm_label_r4.setGeometry(135, 420, 70, 20)
        self.mm_label_r4.setStyleSheet(s.all_labels_style)
        self.mm_label_r4.setFont(font_1)

        #Статус радіуса       
        self.message_r4_square = QLabel(None, self.window_shape)
        self.message_r4_square.setGeometry(170, 420, 150, 20)
        if self.r4_square_value.text() in zero:
            self.message_r4_square.setText("Відсутнє значення")  
            self.message_r4_square.setFont(font_4)
            self.message_r4_square.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r4_square.setStyleSheet(s.error_value_style)           
        
        #Кнопка розрахунку
        self.btn_square_four_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_square_four_radius.clicked.connect(self.perim_square_four_radius)
        self.btn_square_four_radius.setGeometry(10, 450, 370, 30)
        self.btn_square_four_radius.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_sfr_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_sfr_peremeter.setGeometry(15, 490, 150, 20)
        self.Label_sfr_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_sfr_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 490, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)
        
        #Розмірність приметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 490, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 520, 370, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()

    #Периметер квадрата з різними радіусами
    def perim_square_four_radius(self) -> None:

        side_sfr_list = self.check_number_new(self.side_four_radius_value.text())
        r1_sfr_list = self.check_number_new(self.r1_square_value.text())
        r2_sfr_list = self.check_number_new(self.r2_square_value.text())
        r3_sfr_list = self.check_number_new(self.r3_square_value.text())
        r4_sfr_list = self.check_number_new(self.r4_square_value.text())

        self.message_side_four_radius.setText(side_sfr_list[1])
        self.message_side_four_radius.setGeometry(170, 300, side_sfr_list[2], 20) 
        self.message_r1_square.setText(r1_sfr_list[1])
        self.message_r1_square.setGeometry(170, 330, r1_sfr_list[2], 20) 
        self.message_r2_square.setText(r2_sfr_list[1])
        self.message_r2_square.setGeometry(170, 360, r2_sfr_list[2], 20)
        self.message_r3_square.setText(r3_sfr_list[1])
        self.message_r3_square.setGeometry(170, 390, r3_sfr_list[2], 20)
        self.message_r4_square.setText(r4_sfr_list[1])
        self.message_r4_square.setGeometry(170, 420, r4_sfr_list[2], 20)

        if side_sfr_list[0] == 0:
            self.perimeter.setText('?')
            self.message_side_four_radius.setStyleSheet(s.error_value_style)
        else:
            self.message_side_four_radius.setStyleSheet(s.valide_value_style)
        
        if r1_sfr_list[0] == 0:           
            self.message_r1_square.setStyleSheet(s.error_value_style)
        else:
            self.message_r1_square.setStyleSheet(s.valide_value_style)

        if r2_sfr_list[0] == 0:      
            self.message_r2_square.setStyleSheet(s.error_value_style)
        else:
            self.message_r2_square.setStyleSheet(s.valide_value_style)
    
        if r3_sfr_list[0] == 0:         
            self.message_r3_square.setStyleSheet(s.error_value_style)
        else:
            self.message_r3_square.setStyleSheet(s.valide_value_style)

        if r4_sfr_list[0] == 0:         
            self.message_r4_square.setStyleSheet(s.error_value_style)
        else:
            self.message_r4_square.setStyleSheet(s.valide_value_style)

        if side_sfr_list[0] != 0 and r1_sfr_list[0] != 0 and r2_sfr_list[0] != 0 and r3_sfr_list[0] != 0 and r4_sfr_list[0] != 0:
            s1 = side_sfr_list[0] - r1_sfr_list[0] - r2_sfr_list[0]
            s2 = side_sfr_list[0] - r2_sfr_list[0] - r3_sfr_list[0]
            s3 = side_sfr_list[0] - r3_sfr_list[0] - r4_sfr_list[0]
            s4 = side_sfr_list[0] - r4_sfr_list[0] - r1_sfr_list[0]
            if s1 < 0 or s2 < 0 or s3 < 0 or s4 < 0:
                self.message_side_four_radius.setText("Замала сторона")
                self.message_side_four_radius.setStyleSheet(s.error_value_style)
                if s1 < 0:
                    self.r3_square_value.setText(str(round(r3_sfr_list[0],2)))
                    self.r4_square_value.setText(str(round(r4_sfr_list[0],2)))
                    self.perimeter.setText('?')
                    self.message_r1_square.setText("Завеликий радіус")
                    self.message_r1_square.setStyleSheet(s.error_value_style)
                    self.message_r2_square.setText("Завеликий радіус")
                    self.message_r2_square.setStyleSheet(s.error_value_style)
                if s2 < 0:
                    self.r1_square_value.setText(str(round(r1_sfr_list[0],2)))
                    self.r4_square_value.setText(str(round(r4_sfr_list[0],2)))
                    self.perimeter.setText('?')
                    self.message_r2_square.setText("Завеликий радіус")
                    self.message_r2_square.setStyleSheet(s.error_value_style)
                    self.message_r3_square.setText("Завеликий радіус")
                    self.message_r3_square.setStyleSheet(s.error_value_style)
                if s3 < 0:
                    self.r1_square_value.setText(str(round(r1_sfr_list[0],2)))
                    self.r2_square_value.setText(str(round(r2_sfr_list[0],2)))
                    self.perimeter.setText('?')
                    self.message_r3_square.setText("Завеликий радіус")
                    self.message_r3_square.setStyleSheet(s.error_value_style)
                    self.message_r4_square.setText("Завеликий радіус")
                    self.message_r4_square.setStyleSheet(s.error_value_style)
                if s4 < 0:
                    self.r2_square_value.setText(str(round(r2_sfr_list[0],2)))
                    self.r3_square_value.setText(str(round(r3_sfr_list[0],2)))
                    self.perimeter.setText('?')
                    self.message_r4_square.setText("Завеликий радіус")
                    self.message_r4_square.setStyleSheet(s.error_value_style)
                    self.message_r1_square.setText("Завеликий радіус")
                    self.message_r1_square.setStyleSheet(s.error_value_style)
            else:
                square_four_r = g.Square_four_Radius()
                self.side_four_radius_value.setText(str(round(side_sfr_list[0], 2)))
                self.r1_square_value.setText(str(round(r1_sfr_list[0],2)))
                self.r2_square_value.setText(str(round(r2_sfr_list[0],2)))
                self.r3_square_value.setText(str(round(r3_sfr_list[0],2)))
                self.r4_square_value.setText(str(round(r4_sfr_list[0],2)))

                self.perimeter.setText(str(square_four_r.perimeter_square_four_radius(
                    side_sfr_list[0], 
                    r1_sfr_list[0],
                    r2_sfr_list[0],
                    r3_sfr_list[0],
                    r4_sfr_list[0]
                    )))
                del(square_four_r)
                # self.perimeter.setText(str(g.Square_four_Radius.perimeter_square_four_radius(
                #     side_sfr_list[0], 
                #     r1_sfr_list[0],
                #     r2_sfr_list[0],
                #     r3_sfr_list[0],
                #     r4_sfr_list[0]
                #     )))                           
        else:
            self.perimeter.setText('?')
    #КІНЕЦЬ КВАДРАТ З РІЗНИМИ РАДІУСАМИ
    
    #КВАДРАТ УКОЛІ
    #Вікно квадрата у колі
    def square_in_round(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.window_shape.setFixedSize(370, 500)

        self.image_round = gui.QPixmap(f"{SQUARE_IN_ROUND_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(49, 30, int(260 * 1.045), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона квадрата у колі
        #Заголовок сторони
        self.side_sir_label = QLabel("A", self.window_shape)
        self.side_sir_label.setGeometry(15, 320, 15, 20)
        self.side_sir_label.setStyleSheet(s.all_labels_style)
        self.side_sir_label.setFont(font_1)

        #Значення сторони
        self.side_sir_value = QLineEdit("0.0", self.window_shape)
        self.side_sir_value.setGeometry(35, 320, 80, 25)
        self.side_sir_value.setFont(font_3)
        self.side_sir_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_sir_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_label_sir = QLabel("мм", self.window_shape)
        self.mm_label_sir.setGeometry(120, 320, 70, 20)
        self.mm_label_sir.setStyleSheet(s.all_labels_style)
        self.mm_label_sir.setFont(font_1)

        #Статус сторони       
        self.message_side_sir = QLabel(None, self.window_shape)
        self.message_side_sir.setGeometry(150, 320, 150, 20)
        if self.side_sir_value.text() in zero:
            self.message_side_sir.setText("Відсутнє значення")
            self.message_side_sir.setFont(font_4)
            self.message_side_sir.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_sir.setStyleSheet(s.error_value_style)  

        #Діаметер
        #Заголовок 
        self.diameter_sir_label = QLabel("D", self.window_shape)
        self.diameter_sir_label.setGeometry(15, 350, 15, 20)
        self.diameter_sir_label.setStyleSheet(s.all_labels_style)
        self.diameter_sir_label.setFont(font_1)

        #Значення діаметра
        self.diameter_sir_value = QLineEdit("0.0", self.window_shape)
        self.diameter_sir_value.setGeometry(35, 350, 80, 25)
        self.diameter_sir_value.setFont(font_3)
        self.diameter_sir_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.diameter_sir_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність діаметра
        self.mm_label_diameter_sir = QLabel("мм", self.window_shape)
        self.mm_label_diameter_sir.setGeometry(120, 350, 70, 20)
        self.mm_label_diameter_sir.setStyleSheet(s.all_labels_style)
        self.mm_label_diameter_sir.setFont(font_1)

        #Статус діаметра    
        self.message_diameter_sir = QLabel(None, self.window_shape)
        self.message_diameter_sir.setGeometry(150, 350, 150, 20)
        if self.diameter_sir_value.text() in zero:
            self.message_diameter_sir.setText("Відсутнє значення")
            self.message_diameter_sir.setFont(font_4)
            self.message_diameter_sir.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_diameter_sir.setStyleSheet(s.error_value_style)   

        #Кнопка розрахунку
        self.btn_perimeter = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_perimeter.clicked.connect(self.perim_sir)
        self.btn_perimeter.setGeometry(10, 380, 350, 30)
        self.btn_perimeter.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТР
        #Заголовок периметра
        self.Label_sfr_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_sfr_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_sfr_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_sfr_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)
    
        #Розмірність приметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()
    
    #Периметер квадрата у колі
    def perim_sir(self) -> None:

        list_side_sir = self.check_number_new(self.side_sir_value.text())
        list_diameter = self.check_number_new(self.diameter_sir_value.text())

        self.message_side_sir.setText(list_side_sir[1])
        self.message_diameter_sir.setText(list_diameter[1])

        self.message_side_sir.setGeometry(150, 320, list_side_sir[2], 20)
        self.message_diameter_sir.setGeometry(150, 350, list_diameter[2], 20)
        
        if list_diameter[0] != 0:
            self.message_diameter_sir.setStyleSheet(s.valide_value_style)
        else:
            self.message_diameter_sir.setStyleSheet(s.error_value_style)                          

        if list_side_sir[0] != 0:
            self.message_side_sir.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_sir.setStyleSheet(s.error_value_style)                      

        if list_diameter[0] != 0 and list_side_sir[0] != 0:
            self.message_side_sir.setStyleSheet(s.error_value_style)
            self.message_diameter_sir.setStyleSheet(s.error_value_style)
            if (list_side_sir[0] / 0.707106) <= list_diameter[0]:
                self.message_side_sir.setText("Замала сторона")
                self.message_diameter_sir.setText("Завеликий діаметер")
                self.message_side_sir.setGeometry(150, 320, 150, 20)
                self.message_diameter_sir.setGeometry(150, 350, 150, 20)
                self.perimeter.setText("?")
                self.message_side_sir.setStyleSheet(s.error_value_style)
                self.message_diameter_sir.setStyleSheet(s.error_value_style)
            elif list_diameter[0] <= list_side_sir[0]:
                self.message_side_sir.setText("Завелика сторона")
                self.message_diameter_sir.setText("Замалий діаметер")
                self.perimeter.setText("?")
                self.message_side_sir.setStyleSheet(s.error_value_style)
                self.message_diameter_sir.setStyleSheet(s.error_value_style)
                self.message_side_sir.setGeometry(150, 320, 150, 20)
                self.message_diameter_sir.setGeometry(150, 350, 150, 20)            
            else:
                square_in_round = g.Square_in_round()
                self.side_sir_value.setText(str(round(list_side_sir[0], 2)))
                self.diameter_sir_value.setText(str(round(list_diameter[0], 2)))
                self.perimeter.setText(str(square_in_round.perimeter_square_in_round(list_side_sir[0], list_diameter[0])))
                self.message_side_sir.setStyleSheet(s.valide_value_style)
                self.message_diameter_sir.setStyleSheet(s.valide_value_style)
                del(square_in_round)
        else:
            self.perimeter.setText("?")
    #КІНЕЦЬ КВАДРАТ УКОЛІ

    #ПРЯМОКУТНИК
    #вікно прямокутника
    def rectangle(self, shape: str) -> None:        
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 500)
        self.window_shape.setFixedSize(370, 500)

        self.image_round = gui.QPixmap(f"{RECTANGE_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(78, 30, int(260 * 0.823), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона A
        #Заголовок сторони
        self.side_a_label = QLabel("A", self.window_shape)
        self.side_a_label.setGeometry(15, 320, 15, 20)
        self.side_a_label.setStyleSheet(s.all_labels_style)
        self.side_a_label.setFont(font_1)

        #Значення сторони
        self.side_a_value = QLineEdit("0.0", self.window_shape)
        self.side_a_value.setGeometry(35, 320, 80, 25)
        self.side_a_value.setFont(font_3)
        self.side_a_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_a_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_label_side_a = QLabel("мм", self.window_shape)
        self.mm_label_side_a.setGeometry(120, 320, 70, 20)
        self.mm_label_side_a.setStyleSheet(s.all_labels_style)
        self.mm_label_side_a.setFont(font_1)

        #Статус сторони       
        self.message_side_a = QLabel(None, self.window_shape)
        self.message_side_a.setGeometry(150, 320, 150, 20)
        if self.side_a_value.text() in zero:
            self.message_side_a.setText("Відсутнє значення")
            self.message_side_a.setFont(font_4)
            self.message_side_a.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_a.setStyleSheet(s.error_value_style)  
        
        #Сторона B
        #Заголовок сторони
        self.side_b_label = QLabel("B", self.window_shape)
        self.side_b_label.setGeometry(15, 350, 15, 20)
        self.side_b_label.setStyleSheet(s.all_labels_style)
        self.side_b_label.setFont(font_1)

        #Значення сторони
        self.side_b_value = QLineEdit("0.0", self.window_shape)
        self.side_b_value.setGeometry(35, 350, 80, 25)
        self.side_b_value.setFont(font_3)
        self.side_b_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_b_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_label_side_b = QLabel("мм", self.window_shape)
        self.mm_label_side_b.setGeometry(120, 350, 70, 20)
        self.mm_label_side_b.setStyleSheet(s.all_labels_style)
        self.mm_label_side_b.setFont(font_1)

        #Статус сторони       
        self.message_side_b = QLabel(None, self.window_shape)
        self.message_side_b.setGeometry(150, 350, 150, 20)
        if self.side_b_value.text() in zero:
            self.message_side_b.setText("Відсутнє значення")
            self.message_side_b.setFont(font_4)
            self.message_side_b.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_b.setStyleSheet(s.error_value_style)  

        #Кнопка розрахунку
        self.btn_rectangle = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_rectangle.clicked.connect(self.perim_rectangle)
        self.btn_rectangle.setGeometry(10, 380, 350, 30)
        self.btn_rectangle.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_rect_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_rect_peremeter.setGeometry(15, 420, 150, 20)
        self.Label_rect_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_rect_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 420, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 420, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 450, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show() 

    #Периметер прямокутника
    def perim_rectangle(self):

        side_a_list = self.check_number_new(self.side_a_value.text())
        side_b_list = self.check_number_new(self.side_b_value.text())

        self.message_side_a.setText(side_a_list[1])
        self.message_side_b.setText(side_b_list[1])

        self.message_side_a.setGeometry(150, 320, side_a_list[2], 20)
        self.message_side_b.setGeometry(150, 350, side_b_list[2], 20)

        if side_a_list[0] == 0:
            self.message_side_a.setStyleSheet(s.error_value_style)
        else:
            self.message_side_a.setStyleSheet(s.valide_value_style)                    

        if side_b_list[0] == 0:
            self.message_side_b.setStyleSheet(s.error_value_style)
        else:
            self.message_side_b.setStyleSheet(s.valide_value_style)  

        if side_a_list[0] != 0 and side_b_list[0] != 0:
            rectangle = g.Rectangle()
            self.side_a_value.setText(str(round(side_a_list[0], 2)))
            self.side_b_value.setText(str(round(side_b_list[0], 2)))
            p = rectangle.perimeter_rectangle(side_a_list[0], side_b_list[0])
            self.perimeter.setText(str(round(p, 2)))
            del(rectangle)
        else:
            self.perimeter.setText("?")                      
    #КІНЕЦЬ ПРЯМОКУТНИК

    #ПРЯМОКУТНИК З ОДНИМ РАДІУСОМ
    #Вікно прямокутника з одним радіусом
    def rectangle_one_round(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setGeometry(950, 200, 380, 510)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setFixedSize(370, 510)

        self.image_round = gui.QPixmap(f"{RECTANGLE_ONE_RADIUS_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(62, 30, int(260 * 0.948), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона A
        #Заголовок сторони а
        self.side_a_label_req = QLabel("A", self.window_shape)
        self.side_a_label_req.setGeometry(15, 310, 15, 20)
        self.side_a_label_req.setStyleSheet(s.all_labels_style)
        self.side_a_label_req.setFont(font_1)

        #Значення сторони а
        self.side_a_value_req = QLineEdit("0.0", self.window_shape)
        self.side_a_value_req.setGeometry(35, 310, 80, 25)
        self.side_a_value_req.setFont(font_3)
        self.side_a_value_req.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_a_value_req.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони а
        self.mm_label_side_a_req = QLabel("мм", self.window_shape)
        self.mm_label_side_a_req.setGeometry(120, 310, 70, 20)
        self.mm_label_side_a_req.setStyleSheet(s.all_labels_style)
        self.mm_label_side_a_req.setFont(font_1)

        #Статус сторони       
        self.message_side_a_req = QLabel(None, self.window_shape)
        self.message_side_a_req.setGeometry(150, 310, 150, 20)
        if self.side_a_value_req.text() in zero:
            self.message_side_a_req.setText("Відсутнє значення")
            self.message_side_a_req.setFont(font_4)
            self.message_side_a_req.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_a_req.setStyleSheet(s.error_value_style)  

        #Сторона B
        #Заголовок сторони
        self.side_b_label_req = QLabel("B", self.window_shape)
        self.side_b_label_req.setGeometry(15, 340, 15, 20)
        self.side_b_label_req.setStyleSheet(s.all_labels_style)
        self.side_b_label_req.setFont(font_1)

        #Значення сторони
        self.side_b_value_req = QLineEdit("0.0", self.window_shape)
        self.side_b_value_req.setGeometry(35, 340, 80, 25)
        self.side_b_value_req.setFont(font_3)
        self.side_b_value_req.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_b_value_req.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_label_side_b_req = QLabel("мм", self.window_shape)
        self.mm_label_side_b_req.setGeometry(120, 340, 70, 20)
        self.mm_label_side_b_req.setStyleSheet(s.all_labels_style)
        self.mm_label_side_b_req.setFont(font_1)

        #Статус сторони       
        self.message_side_b_req = QLabel(None, self.window_shape)
        self.message_side_b_req.setGeometry(150, 340, 150, 20)
        if self.side_b_value_req.text() in zero:
            self.message_side_b_req.setText("Відсутнє значення")
            self.message_side_b_req.setFont(font_4)
            self.message_side_b_req.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_b_req.setStyleSheet(s.error_value_style) 

        #РАДІУС
        #Заголовок радіуса
        self.r_label_req = QLabel("R", self.window_shape)
        self.r_label_req.setGeometry(15, 370, 15, 20)
        self.r_label_req.setStyleSheet(s.all_labels_style)
        self.r_label_req.setFont(font_1)

        #Значення радіуса
        self.r_value_req = QLineEdit("0.0", self.window_shape)
        self.r_value_req.setGeometry(35, 370, 80, 25)
        self.r_value_req.setFont(font_3)
        self.r_value_req.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r_value_req.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r = QLabel("мм", self.window_shape)
        self.mm_label_r.setGeometry(120, 370, 70, 20)
        self.mm_label_r.setStyleSheet(s.all_labels_style)
        self.mm_label_r.setFont(font_1)

        #Статус радіуса       
        self.message_side_r_req = QLabel(None, self.window_shape)
        self.message_side_r_req.setGeometry(150, 370, 150, 20)
        if self.r_value_req.text() in zero:
            self.message_side_r_req.setText("Відсутнє значення")
            self.message_side_r_req.setFont(font_4)
            self.message_side_r_req.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_r_req.setStyleSheet(s.error_value_style) 


        #Кнопка розрахунку
        self.btn_s_req = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_s_req.clicked.connect(self.req_one_radius)
        self.btn_s_req.setGeometry(10, 400, 350, 30)
        self.btn_s_req.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter_req = QLabel("Периметр", self.window_shape)
        self.Label_s_peremeter_req.setGeometry(15, 440, 150, 20)
        self.Label_s_peremeter_req.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_s_peremeter_req.setFont(font_1)

        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 440, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter_req = QLabel("мм", self.window_shape)
        self.mm_result_perimeter_req.setGeometry(255, 440, 50, 20)
        self.mm_result_perimeter_req.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter_req.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter_req = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter_req.clicked.connect(self.add_value)
        self.btn_add_perimeter_req.setGeometry(10, 470, 350, 30)      
        self.btn_add_perimeter_req.setStyleSheet(s.add_button_style)

        self.window_shape.show()
    
    #Периметр прямокутника с однаковими радіусами
    def req_one_radius(self):
        side_a_req_list = self.check_number_new(self.side_a_value_req.text()) 
        side_b_req_list = self.check_number_new(self.side_b_value_req.text())
        side_r_req_list = self.check_number_new(self.r_value_req.text())

        self.message_side_a_req.setText(side_a_req_list[1])
        self.message_side_b_req.setText(side_b_req_list[1])
        self.message_side_r_req.setText(side_r_req_list[1])

        self.message_side_a_req.setGeometry(150, 310, side_a_req_list[2], 20)
        self.message_side_b_req.setGeometry(150, 340, side_b_req_list[2], 20)
        self.message_side_r_req.setGeometry(150, 370, side_r_req_list[2], 20)

        if side_a_req_list[0] != 0:
            self.message_side_a_req.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_a_req.setStyleSheet(s.error_value_style)

        if side_b_req_list[0] != 0:
            self.message_side_b_req.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_b_req.setStyleSheet(s.error_value_style)            

        if side_r_req_list[0] != 0:
            self.message_side_r_req.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_r_req.setStyleSheet(s.error_value_style)           

        d = 2 * side_r_req_list[0]

        if side_a_req_list[0] != 0 and side_b_req_list[0] != 0 and side_r_req_list[0] != 0:
            if d > side_a_req_list[0] and d > side_b_req_list[0]:
                self.message_side_a_req.setText("Замала сторона")
                self.message_side_a_req.setStyleSheet(s.error_value_style)
                self.message_side_b_req.setText("Замала сторона")
                self.message_side_b_req.setStyleSheet(s.error_value_style) 
                self.message_side_r_req.setText("Завеликий радіус")
                self.message_side_r_req.setStyleSheet(s.error_value_style) 
                self.perimeter.setText("?")              
            elif side_r_req_list[0] > side_a_req_list[0] and side_r_req_list[0] > side_b_req_list[0]:
                self.message_side_r_req.setStyleSheet(s.error_value_style)
                self.message_side_r_req.setText("Завеликий радіус")
                self.perimeter.setText("?")
            elif side_a_req_list[0] <= side_b_req_list[0] and (side_a_req_list[0] - d) < 0:
                self.message_side_a_req.setText("Замала сторона")
                self.message_side_a_req.setStyleSheet(s.error_value_style) 
                self.message_side_r_req.setStyleSheet(s.error_value_style) 
                self.message_side_r_req.setText("Завеликий радіус")
                self.message_side_r_req.setStyleSheet(s.error_value_style) 
                self.perimeter.setText("?")
            elif side_b_req_list[0] <= side_a_req_list[0] and (side_b_req_list[0] - d) < 0:
                self.message_side_b_req.setText("Замала сторона")
                self.message_side_b_req.setStyleSheet(s.error_value_style) 
                self.message_side_r_req.setText("Завеликий радіус")
                self.message_side_r_req.setStyleSheet(s.error_value_style) 
                self.perimeter.setText("?")                
            else:
                rectangle_one_r = g.Rectangle_One_Radius()
                self.side_a_value_req.setText(str(round(side_a_req_list[0], 2)))
                self.side_b_value_req.setText(str(round(side_b_req_list[0], 2)))
                self.r_value_req.setText(str(round(side_r_req_list[0], 2)))
                self.perimeter.setText(str(rectangle_one_r.parimeter_rectangle_one_radius(
                    side_a_req_list[0], 
                    side_b_req_list[0], 
                    side_r_req_list[0]
                    )))
                del(rectangle_one_r)
        else:
            self.perimeter.setText("?")
    #КІНЕЦЬ ПРЯМОКУТНИК З ОДНИМ РАДІУСОМ

    #ПРЯМОКУТНИК З РІНИМИ РАДИУСАМИ
    #Вікно прямокутника з різними радіусами
    def rectangle_four_round(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setGeometry(950, 200, 390, 560)
        self.window_shape.setFixedSize(390, 560)
        self.window_shape.setWindowTitle(shape)
        self.image_round = gui.QPixmap(f"{RECTANGLE_FOUR_RADIUS_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(47, 10, int(250 * 1.131), 250)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона A
        #Заголовок сторони
        self.side_a_four_radius_label_rfr = QLabel("A", self.window_shape)
        self.side_a_four_radius_label_rfr.setGeometry(15, 270, 30, 20)
        self.side_a_four_radius_label_rfr.setStyleSheet(s.all_labels_style)
        self.side_a_four_radius_label_rfr.setFont(font_1)

        #Значення сторони
        self.side_a_four_radius_value = QLineEdit("0.0", self.window_shape)
        self.side_a_four_radius_value.setGeometry(50, 270, 80, 25)
        self.side_a_four_radius_value.setFont(font_3)
        self.side_a_four_radius_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_a_four_radius_value.setStyleSheet(s.q_line_edit_style)
        #Розмірність сторони
        self.mm_label_side_a_four_radius_label = QLabel("мм", self.window_shape)
        self.mm_label_side_a_four_radius_label.setGeometry(135, 270, 70, 20)
        self.mm_label_side_a_four_radius_label.setStyleSheet(s.all_labels_style)
        self.mm_label_side_a_four_radius_label.setFont(font_1)

        #Статус сторони       
        self.message_side_a_four_radius = QLabel(None, self.window_shape)
        self.message_side_a_four_radius.setGeometry(170, 270, 150, 20)
        if self.message_side_a_four_radius.text() in zero:
            self.message_side_a_four_radius.setText("Відсутнє значення")
            self.message_side_a_four_radius.setFont(font_4)
            self.message_side_a_four_radius.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_a_four_radius.setStyleSheet(s.error_value_style) 

        #Сторона B
        #Заголовок сторони
        self.side_b_four_radius_label_rfr = QLabel("B", self.window_shape)
        self.side_b_four_radius_label_rfr.setGeometry(15, 300, 30, 20)
        self.side_b_four_radius_label_rfr.setStyleSheet(s.all_labels_style)
        self.side_b_four_radius_label_rfr.setFont(font_1)

        #Значення сторони
        self.side_b_four_radius_value = QLineEdit("0.0", self.window_shape)
        self.side_b_four_radius_value.setGeometry(50, 300, 80, 25)
        self.side_b_four_radius_value.setFont(font_3)
        self.side_b_four_radius_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_b_four_radius_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_label_side_b_four_radius_label = QLabel("мм", self.window_shape)
        self.mm_label_side_b_four_radius_label.setGeometry(135, 300, 70, 20)
        self.mm_label_side_b_four_radius_label.setStyleSheet(s.all_labels_style)
        self.mm_label_side_b_four_radius_label.setFont(font_1)

        #Статус сторони       
        self.message_side_b_four_radius = QLabel(None, self.window_shape)
        self.message_side_b_four_radius.setGeometry(170, 300, 150, 20)
        if self.message_side_b_four_radius.text() in zero:
            self.message_side_b_four_radius.setText("Відсутнє значення")
            self.message_side_b_four_radius.setFont(font_4)
            self.message_side_b_four_radius.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_b_four_radius.setStyleSheet(s.error_value_style) 

        #Радіус R1
        #Заголовок радіуса
        self.r1_square_label_rfr = QLabel("R1", self.window_shape)
        self.r1_square_label_rfr.setGeometry(15, 330, 30, 20)
        self.r1_square_label_rfr.setStyleSheet(s.all_labels_style)
        self.r1_square_label_rfr.setFont(font_1)

        #Значення радіуса
        self.r1_square_value_rfr = QLineEdit("0.0", self.window_shape)
        self.r1_square_value_rfr.setGeometry(50, 330, 80, 25)
        self.r1_square_value_rfr.setFont(font_3)
        self.r1_square_value_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r1_square_value_rfr.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r1_rfr = QLabel("мм", self.window_shape)
        self.mm_label_r1_rfr.setGeometry(135, 330, 70, 20)
        self.mm_label_r1_rfr.setStyleSheet(s.all_labels_style)
        self.mm_label_r1_rfr.setFont(font_1)

        #Статус радіуса       
        self.message_r1_square_rfr = QLabel(None, self.window_shape)
        self.message_r1_square_rfr.setGeometry(170, 330, 150, 20)
        if self.r1_square_value_rfr.text() in zero:
            self.message_r1_square_rfr.setText("Відсутнє значення")
            self.message_r1_square_rfr.setFont(font_4)
            self.message_r1_square_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r1_square_rfr.setStyleSheet(s.error_value_style) 

        #Радіус R2
        #Заголовок радіуса
        self.r2_square_label_rfr = QLabel("R2", self.window_shape)
        self.r2_square_label_rfr.setGeometry(15, 360, 30, 20)
        self.r2_square_label_rfr.setStyleSheet(s.all_labels_style)
        self.r2_square_label_rfr.setFont(font_1)

        #Значення радіуса
        self.r2_square_value_rfr = QLineEdit("0.0", self.window_shape)
        self.r2_square_value_rfr.setGeometry(50, 360, 80, 25)
        self.r2_square_value_rfr.setFont(font_3)
        self.r2_square_value_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r2_square_value_rfr.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r2_rfr= QLabel("мм", self.window_shape)
        self.mm_label_r2_rfr.setGeometry(135, 360, 70, 20)
        self.mm_label_r2_rfr.setStyleSheet(s.all_labels_style)
        self.mm_label_r2_rfr.setFont(font_1)

        #Статус радіуса       
        self.message_r2_square_rfr = QLabel(None, self.window_shape)
        self.message_r2_square_rfr.setGeometry(170, 360, 150, 20)
        if self.r2_square_value_rfr.text() in zero:
            self.message_r2_square_rfr.setText("Відсутнє значення")
            self.message_r2_square_rfr.setFont(font_4)
            self.message_r2_square_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r2_square_rfr.setStyleSheet(s.error_value_style) 
        #Радіус R3
        #Заголовок радіуса
        self.r3_square_label_rfr = QLabel("R3", self.window_shape)
        self.r3_square_label_rfr.setGeometry(15, 390, 30, 20)
        self.r3_square_label_rfr.setStyleSheet(s.all_labels_style)
        self.r3_square_label_rfr.setFont(font_1)

        #Значення радіуса
        self.r3_square_value_rfr = QLineEdit("0.0", self.window_shape)
        self.r3_square_value_rfr.setGeometry(50, 390, 80, 25)
        self.r3_square_value_rfr.setFont(font_3)
        self.r3_square_value_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r3_square_value_rfr.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r3_rfr = QLabel("мм", self.window_shape)
        self.mm_label_r3_rfr.setGeometry(135, 390, 70, 20)
        self.mm_label_r3_rfr.setStyleSheet(s.all_labels_style)
        self.mm_label_r3_rfr.setFont(font_1)

        #Статус радіуса       
        self.message_r3_square_rfr = QLabel(None, self.window_shape)
        self.message_r3_square_rfr.setGeometry(170, 390, 150, 20)
        if self.r3_square_value_rfr.text() in zero:
            self.message_r3_square_rfr.setText("Відсутнє значення")
            self.message_r3_square_rfr.setFont(font_4)
            self.message_r3_square_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r3_square_rfr.setStyleSheet(s.error_value_style) 

        #Радіус R4
        #Заголовок радіуса
        self.r4_square_label_rfr = QLabel("R4", self.window_shape)
        self.r4_square_label_rfr.setGeometry(15, 420, 30, 20)
        self.r4_square_label_rfr.setStyleSheet(s.all_labels_style)
        self.r4_square_label_rfr.setFont(font_1)


        #Значення радіуса
        self.r4_square_value_rfr = QLineEdit("0.0", self.window_shape)
        self.r4_square_value_rfr.setGeometry(50, 420, 80, 25)
        self.r4_square_value_rfr.setFont(font_3)
        self.r4_square_value_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.r4_square_value_rfr.setStyleSheet(s.q_line_edit_style)

        #Розмірність радіуса
        self.mm_label_r4_rfr = QLabel("мм", self.window_shape)
        self.mm_label_r4_rfr.setGeometry(135, 420, 70, 20)
        self.mm_label_r4_rfr.setStyleSheet(s.all_labels_style)
        self.mm_label_r4_rfr.setFont(font_1)

        #Статус радіуса       
        self.message_r4_square_rfr = QLabel(None, self.window_shape)
        self.message_r4_square_rfr.setGeometry(170, 420, 150, 20)
        if self.r4_square_value_rfr.text() in zero:
            self.message_r4_square_rfr.setText("Відсутнє значення")
            self.message_r4_square_rfr.setFont(font_4)
            self.message_r4_square_rfr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_r4_square_rfr.setStyleSheet(s.error_value_style)            
        
        #Кнопка розрахунку
        self.btn_rectangle_four_radius = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_rectangle_four_radius.clicked.connect(self.perim_rectangle_four_radius)
        self.btn_rectangle_four_radius.setGeometry(10, 450, 370, 30)
        self.btn_rectangle_four_radius.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_rfr_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_rfr_peremeter.setGeometry(15, 490, 150, 20)
        self.Label_rfr_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_rfr_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 490, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)
        
        #Розмірність приметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 490, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 520, 370, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()             

    #Периметер прямокутника з різними радіусами
    def perim_rectangle_four_radius(self) -> None:
        list_s1 = self.check_number_new(self.side_a_four_radius_value.text())
        list_s2 = self.check_number_new(self.side_b_four_radius_value.text())
        list_r1 = self.check_number_new(self.r1_square_value_rfr.text())
        list_r2 = self.check_number_new(self.r2_square_value_rfr.text())
        list_r3 = self.check_number_new(self.r3_square_value_rfr.text())
        list_r4 = self.check_number_new(self.r4_square_value_rfr.text())

        self.message_side_a_four_radius.setText(list_s1[1])
        self.message_side_b_four_radius.setText(list_s2[1])
        self.message_r1_square_rfr.setText(list_r1[1])
        self.message_r2_square_rfr.setText(list_r2[1])
        self.message_r3_square_rfr.setText(list_r3[1])
        self.message_r4_square_rfr.setText(list_r4[1])

        self.message_side_a_four_radius.setGeometry(170, 270, list_s1[2], 20)
        self.message_side_b_four_radius.setGeometry(170, 300, list_s2[2], 20)
        self.message_r1_square_rfr.setGeometry(170, 330, list_r1[2], 20)
        self.message_r2_square_rfr.setGeometry(170, 360, list_r2[2], 20)
        self.message_r3_square_rfr.setGeometry(170, 390, list_r3[2], 20)
        self.message_r4_square_rfr.setGeometry(170, 420, list_r4[2], 20)

        if list_s1[0] != 0:
            self.message_side_a_four_radius.setStyleSheet(s.valide_value_style)
            self.side_a_four_radius_value.setText(str(float(round(list_s1[0], 2))))
        else:
            self.message_side_a_four_radius.setStyleSheet(s.error_value_style)

        if list_s2[0] != 0:
            self.message_side_b_four_radius.setStyleSheet(s.valide_value_style)
            self.side_b_four_radius_value.setText(str(float(round(list_s2[0], 2))))
        else:
            self.message_side_b_four_radius.setStyleSheet(s.error_value_style)

        if list_r1[0] != 0:
            self.message_r1_square_rfr.setStyleSheet(s.valide_value_style)
            self.r1_square_value_rfr.setText(str(float(round(list_r1[0], 2))))
        else:
            self.message_r1_square_rfr.setStyleSheet(s.error_value_style)

        if list_r2[0] != 0:
            self.message_r2_square_rfr.setStyleSheet(s.valide_value_style)
            self.r2_square_value_rfr.setText(str(float(round(list_r2[0], 2))))
        else:
            self.message_r2_square_rfr.setStyleSheet(s.error_value_style) 

        if list_r3[0] != 0:
            self.message_r3_square_rfr.setStyleSheet(s.valide_value_style)
            self.r3_square_value_rfr.setText(str(float(round(list_r3[0], 2))))
        else:
            self.message_r3_square_rfr.setStyleSheet(s.error_value_style) 

        if list_r4[0] != 0:
            self.message_r4_square_rfr.setStyleSheet(s.valide_value_style)
            self.r4_square_value_rfr.setText(str(float(round(list_r4[0], 2))))
        else:
            self.message_r4_square_rfr.setStyleSheet(s.error_value_style)

        if list_s1[0] != 0 and list_s2[0] != 0 and list_r1[0] != 0 and list_r2[0] != 0 and list_r3[0] != 0 and list_r4[0] != 0:

            s_1_rfr = list_s1[0] - list_r1[0] - list_r2[0]
            s_2_rfr = list_s2[0] - list_r2[0] - list_r3[0]
            s_3_rfr = list_s1[0] - list_r3[0] - list_r4[0]
            s_4_rfr = list_s2[0] - list_r4[0] - list_r1[0]    

            if s_1_rfr < 0 or s_2_rfr < 0 or s_3_rfr < 0 or s_4_rfr < 0:
                if s_1_rfr < 0:
                    self.perimeter.setText('?')

                    self.message_side_a_four_radius.setStyleSheet(s.error_value_style)
                    self.message_side_a_four_radius.setText("Замала сторона")
                    self.message_side_a_four_radius.setGeometry(170, 270, 150, 20)

                    self.message_r1_square_rfr.setText("Завеликий радіус")
                    self.message_r1_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r1_square_rfr.setGeometry(170, 330, 150, 20)

                    self.message_r2_square_rfr.setText("Завеликий радіус")
                    self.message_r2_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r2_square_rfr.setGeometry(170, 360, 150, 20)
                    
                if s_2_rfr < 0:
                    self.perimeter.setText('?')
                    self.message_side_b_four_radius.setText("Замала сторона")
                    self.message_side_b_four_radius.setGeometry(170, 300, 150, 20)
                    self.message_side_b_four_radius.setStyleSheet(s.error_value_style)

                    self.message_r2_square_rfr.setText("Завеликий радіус")
                    self.message_r2_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r2_square_rfr.setGeometry(170, 360, 150, 20)
                    
                    self.message_r3_square_rfr.setText("Завеликий радіус")
                    self.message_r3_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r3_square_rfr.setGeometry(170, 390, 150, 20)

                if s_3_rfr < 0:
                    self.perimeter.setText('?')

                    self.message_side_a_four_radius.setStyleSheet(s.error_value_style)
                    self.message_side_a_four_radius.setText("Замала сторона")
                    self.message_side_a_four_radius.setGeometry(170, 270, 150, 20)

                    self.message_r3_square_rfr.setText("Завеликий радіус")
                    self.message_r3_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r3_square_rfr.setGeometry(170, 390, 150, 20)

                    self.message_r4_square_rfr.setText("Завеликий радіус")
                    self.message_r4_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r4_square_rfr.setGeometry(170, 420, 150, 20)
                if s_4_rfr < 0:
                    self.perimeter.setText('?')

                    self.message_side_b_four_radius.setText("Замала сторона")
                    self.message_side_b_four_radius.setGeometry(170, 300, 150, 20)
                    self.message_side_b_four_radius.setStyleSheet(s.error_value_style)

                    self.message_r4_square_rfr.setText("Завеликий радіус")
                    self.message_r4_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r4_square_rfr.setGeometry(170, 420, 150, 20)

                    self.message_r1_square_rfr.setText("Завеликий радіус")
                    self.message_r1_square_rfr.setStyleSheet(s.error_value_style)
                    self.message_r1_square_rfr.setGeometry(170, 330, 150, 20)                                  
            else:
                rectangle_four_r = g.Rectangel_Four_Radius()
                self.perimeter.setText(str(rectangle_four_r.perimeter_rectangle_four_radius(
                    list_s1[0], 
                    list_s2[0], 
                    list_r1[0], 
                    list_r2[0], 
                    list_r3[0], 
                    list_r4[0]
                    )))
                del(rectangle_four_r) 
        else:
            self.perimeter.setText('?')
    #КІНЕЦЬ ПРЯМОКУТНИК З РІНИМИ РАДИУСАМИ

    #ШЕСТИГАРННИК
    #Вікно шестигранника
    def hexagon(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setGeometry(950, 200, 390, 600)
        self.window_shape.setWindowTitle(shape)
        self.image_round = gui.QPixmap(f"{HEXAGON_IMAGE_PATH}")

        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(72, 10, int(250 / 1.131), 250)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        self.window_shape.setFixedSize(390, 600)
        #Сторона 
        #Заголовок сторони
        self.hex_a_label = QLabel("A", self.window_shape)
        self.hex_a_label.setGeometry(15, 270, 30, 20)
        self.hex_a_label.setStyleSheet(s.all_labels_style)
        self.hex_a_label.setFont(font_1)        

        #Значення сторони
        self.hex_a_value = QLineEdit("0.0", self.window_shape)
        self.hex_a_value.setGeometry(50, 270, 80, 25)
        self.hex_a_value.setFont(font_3)
        self.hex_a_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hex_a_value.setStyleSheet(s.q_line_edit_style)        

        #Розмірність сторони
        self.mm_hex_a_label = QLabel("мм", self.window_shape)
        self.mm_hex_a_label.setGeometry(135, 270, 70, 20)
        self.mm_hex_a_label.setStyleSheet(s.all_labels_style)
        self.mm_hex_a_label.setFont(font_1)

        #Статус сторони       
        self.message_hex_a = QLabel(None, self.window_shape)
        self.message_hex_a.setGeometry(170, 270, 150, 20)
        if self.hex_a_value.text() in zero:
            self.message_hex_a.setText("Відсутнє значення")
            self.message_hex_a.setFont(font_4)
            self.message_hex_a.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_hex_a.setStyleSheet(s.error_value_style)

        #Кнопка розрахунку
        self.btn_hex_a = QPushButton("Розрахувати периметр по А", self.window_shape)
        self.btn_hex_a.setGeometry(10, 300, 370, 30)
        self.btn_hex_a.clicked.connect(self.perim_hex_a)
        self.btn_hex_a.setStyleSheet(s.btn_perimeter_1)

        #Висота
        #Заголовок висоти
        self.hex_h_label = QLabel("H", self.window_shape)
        self.hex_h_label.setGeometry(15, 360, 30, 20)
        self.hex_h_label.setStyleSheet(s.all_labels_style)
        self.hex_h_label.setFont(font_1)

        #Значення висоти
        self.hex_h_value = QLineEdit("0.0", self.window_shape)
        self.hex_h_value.setGeometry(50, 360, 80, 25)
        self.hex_h_value.setFont(font_3)
        self.hex_h_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hex_h_value.setStyleSheet(s.q_line_edit_style)        

        #Розмірність сторони
        self.mm_hex_h_label = QLabel("мм", self.window_shape)
        self.mm_hex_h_label.setGeometry(135, 360, 70, 20)
        self.mm_hex_h_label.setStyleSheet(s.all_labels_style)
        self.mm_hex_h_label.setFont(font_1)

        #Статус сторони       
        self.message_hex_h = QLabel(None, self.window_shape)
        self.message_hex_h.setGeometry(170, 360, 150, 20)
        if self.hex_h_value.text() in zero:
            self.message_hex_h.setText("Відсутнє значення")
            self.message_hex_h.setFont(font_4)
            self.message_hex_h.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_hex_h.setStyleSheet(s.error_value_style)
        
        #Кнопка розрахунку
        self.btn_hex_h = QPushButton("Розрахувати периметр по H", self.window_shape)
        self.btn_hex_h.clicked.connect(self.perim_hex_h)
        self.btn_hex_h.setGeometry(10, 390, 370, 30)  
        self.btn_hex_h.clicked.connect(self.perim_hex_h)
        self.btn_hex_h.setStyleSheet(s.btn_perimeter_1)

        #Діаметр
        #Заголовок діаметра
        self.hex_d_label = QLabel("D", self.window_shape)
        self.hex_d_label.setGeometry(15, 450, 30, 20)
        self.hex_d_label.setStyleSheet(s.all_labels_style)
        self.hex_d_label.setFont(font_1)

        #Значення висоти
        self.hex_d_value = QLineEdit("0.0", self.window_shape)
        self.hex_d_value.setGeometry(50, 450, 80, 25)
        self.hex_d_value.setFont(font_3)
        self.hex_d_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hex_d_value.setStyleSheet(s.q_line_edit_style)        

        #Розмірність сторони
        self.mm_hex_d_label = QLabel("мм", self.window_shape)
        self.mm_hex_d_label.setGeometry(135, 450, 70, 20)
        self.mm_hex_d_label.setStyleSheet(s.all_labels_style)
        self.mm_hex_d_label.setFont(font_1)

        #Статус сторони       
        self.message_hex_d = QLabel(None, self.window_shape)
        self.message_hex_d.setGeometry(170, 450, 150, 20)
        if self.hex_d_value.text() in zero:
            self.message_hex_d.setText("Відсутнє значення")
            self.message_hex_d.setFont(font_4)
            self.message_hex_d.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_hex_d.setStyleSheet(s.error_value_style)
  
        #Кнопка розрахунку
        self.btn_hex_d = QPushButton("Розрахувати периметр по D", self.window_shape)
        self.btn_hex_d.setGeometry(10, 480, 370, 30)  
        self.btn_hex_d.clicked.connect(self.perim_hex_d)
        self.btn_hex_d.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_d_peremeter.setGeometry(15, 530, 150, 20)
        self.Label_d_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_d_peremeter.setFont(font_1)


        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 530, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 530, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер кола до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 560, 370, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()
    
    #Периметр шестирганника по стороні А
    def perim_hex_a(self):
        hex_a_list = self.check_number_new(self.hex_a_value.text())
        self.message_hex_a.setText(hex_a_list[1])
        self.message_hex_a.setGeometry(170, 270, hex_a_list[2], 20)
        self.message_hex_h.setGeometry(170, 360, 150, 20)
        self.message_hex_d.setGeometry(170, 450, 150, 20)
        
        if hex_a_list[0] != 0:
            hex_a = g.Hexagon()
            self.message_hex_a.setText(hex_a_list[1])
            self.message_hex_a.setStyleSheet(s.valide_value_style)
            self.message_hex_h.setStyleSheet(s.valide_value_style)
            self.message_hex_h.setText("Валідне значення")
            self.message_hex_d.setText("Валідне значення")
            self.message_hex_d.setStyleSheet(s.valide_value_style)
            self.hex_a_value.setText(str(round(hex_a_list[0], 2)))
            self.hex_h_value.setText(str(hex_a.h_hexagon_a(hex_a_list[0])))
            self.hex_d_value.setText(str(hex_a.d_hexagon_a(hex_a_list[0])))
            self.perimeter.setText(str(hex_a.perimeter_hexagon_a(hex_a_list[0])))
            del(hex_a)
        else:
            self.message_hex_a.setStyleSheet(s.error_value_style)
            self.message_hex_d.setStyleSheet(s.error_value_style)
            self.message_hex_h.setStyleSheet(s.error_value_style)
            self.message_hex_h.setText("Відсутнє значення")
            self.message_hex_d.setText("Відсутнє значення")
            self.hex_h_value.setText("0.0")
            self.hex_d_value.setText("0.0")
            self.perimeter.setText("?")      

    #Периметр шестирганника по відстані проміж паралельними сторонами H
    def perim_hex_h(self):
        hex_h_list = self.check_number_new(self.hex_h_value.text())
        self.message_hex_h.setText(hex_h_list[1])
        self.message_hex_h.setGeometry(170, 360, hex_h_list[2], 20)
        self.message_hex_a.setGeometry(170, 270, 150, 20)
        self.message_hex_d.setGeometry(170, 450, 150, 20)
        if hex_h_list[0] != 0:
            hex_h = g.Hexagon()
            self.message_hex_h.setStyleSheet(s.valide_value_style)
            self.message_hex_a.setStyleSheet(s.valide_value_style)
            self.message_hex_d.setStyleSheet(s.valide_value_style)
            self.message_hex_a.setText("Валідне значення")
            self.message_hex_d.setText("Валідне значення")
            self.hex_h_value.setText(str(round(hex_h_list[0], 2)))
            self.hex_a_value.setText(str(hex_h.a_hexagon_h(hex_h_list[0])))
            self.hex_d_value.setText(str(hex_h.d_hexagon_h(hex_h_list[0])))
            self.perimeter.setText(str(hex_h.perimeter_hexagon_h(hex_h_list[0])))
            del(hex_h)
        else:
            self.message_hex_h.setStyleSheet(s.error_value_style)
            self.message_hex_d.setStyleSheet(s.error_value_style)
            self.message_hex_a.setStyleSheet(s.error_value_style)
            self.message_hex_a.setText("Відсутнє значення")
            self.message_hex_d.setText("Відсутнє значення")
            self.hex_a_value.setText("0.0")
            self.hex_d_value.setText("0.0")
            self.perimeter.setText("?") 

    #Периметр шестирганника по діаметру описаного кола
    def perim_hex_d(self):
        hex_d_list = self.check_number_new(self.hex_d_value.text())
        self.message_hex_d.setText(hex_d_list[1])
        self.message_hex_d.setGeometry(170, 450, hex_d_list[2], 20)
        self.message_hex_h.setGeometry(170, 360, 150, 20)
        self.message_hex_a.setGeometry(170, 270, 150, 20)
        if hex_d_list[0] != 0:
            hex_d = g.Hexagon()
            self.message_hex_d.setStyleSheet(s.valide_value_style)
            self.message_hex_a.setStyleSheet(s.valide_value_style)
            self.message_hex_h.setStyleSheet(s.valide_value_style)
            self.message_hex_a.setText("Валідне значення")
            self.message_hex_h.setText("Валідне значення")
            self.hex_d_value.setText(str(round(hex_d_list[0], 2)))
            self.hex_a_value.setText(str(hex_d.a_hexagon_d(hex_d_list[0])))
            self.hex_h_value.setText(str(hex_d.h_hexagon_d(hex_d_list[0])))
            self.perimeter.setText(str(hex_d.perimeter_hexagon_d(hex_d_list[0])))
            del(hex_d)               
        else:
            self.message_hex_d.setStyleSheet(s.error_value_style)
            self.message_hex_a.setStyleSheet(s.error_value_style)
            self.message_hex_h.setStyleSheet(s.error_value_style)
            self.message_hex_a.setText("Відсутнє значення")
            self.message_hex_h.setText("Відсутнє значення")
            self.hex_a_value.setText("0.0")
            self.hex_h_value.setText("0.0")
            self.perimeter.setText("?")   
    #КІНЕЦЬ ШЕСТИГАРННИК

    #ОВАЛ
    #Вікно овала
    def oblong(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 410)
        self.window_shape.setFixedSize(370, 410)

        self.image_round = gui.QPixmap(f"{OBLONG_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(12, 10, int(200 / 0.577), 200)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона A
        #Заголовок сторони а
        self.oblong_side_a_label = QLabel("A", self.window_shape)
        self.oblong_side_a_label.setGeometry(15, 240, 15, 20)
        self.oblong_side_a_label.setStyleSheet(s.all_labels_style)
        self.oblong_side_a_label.setFont(font_1)

        #Значення сторони а
        self.oblong_side_a_value = QLineEdit("0.0", self.window_shape)
        self.oblong_side_a_value.setGeometry(35, 240, 80, 25)
        self.oblong_side_a_value.setFont(font_3)
        self.oblong_side_a_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oblong_side_a_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони а
        self.mm_label_oblong_side_a = QLabel("мм", self.window_shape)
        self.mm_label_oblong_side_a.setGeometry(120, 240, 70, 20)
        self.mm_label_oblong_side_a.setStyleSheet(s.all_labels_style)
        self.mm_label_oblong_side_a.setFont(font_1)


        #Статус сторони       
        self.message_oblong_side_a = QLabel(None, self.window_shape)
        self.message_oblong_side_a.setGeometry(150, 240, 150, 20)
        if self.oblong_side_a_value.text() in zero:
            self.message_oblong_side_a.setText("Відсутнє значення")
            self.message_oblong_side_a.setFont(font_4)
            self.message_oblong_side_a.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_oblong_side_a.setStyleSheet(s.error_value_style)  

        #Сторона B
        #Заголовок сторони b
        self.oblong_side_b_label = QLabel("B", self.window_shape)
        self.oblong_side_b_label.setGeometry(15, 270, 15, 20)
        self.oblong_side_b_label.setStyleSheet(s.all_labels_style)
        self.oblong_side_b_label.setFont(font_1)

        #Значення сторони b
        self.oblong_side_b_value = QLineEdit("0.0", self.window_shape)
        self.oblong_side_b_value.setGeometry(35, 270, 80, 25)
        self.oblong_side_b_value.setFont(font_3)
        self.oblong_side_b_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.oblong_side_b_value.setStyleSheet(s.q_line_edit_style)


        #Розмірність сторони b
        self.mm_label_oblong_side_b = QLabel("мм", self.window_shape)
        self.mm_label_oblong_side_b.setGeometry(120, 270, 70, 20)
        self.mm_label_oblong_side_b.setStyleSheet(s.all_labels_style)
        self.mm_label_oblong_side_b.setFont(font_1)

        #Статус сторони       
        self.message_oblong_side_b = QLabel(None, self.window_shape)
        #self.message_oblong_side_b.setGeometry(100, 80, 150, 20)
        self.message_oblong_side_b.setGeometry(150, 270, 150, 20)
        if self.oblong_side_a_value.text() in zero:
            self.message_oblong_side_b.setText("Відсутнє значення")
            self.message_oblong_side_b.setFont(font_4)
            self.message_oblong_side_b.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_oblong_side_b.setStyleSheet(s.error_value_style) 

        #Кнопка розрахунку
        self.btn_oblong = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_oblong.clicked.connect(self.perim_oblong)
        self.btn_oblong.setGeometry(10, 300, 350, 30)
        self.btn_oblong.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 340, 150, 20)
        self.Label_s_peremeter.setStyleSheet("color: #8B00FF;")
        self.Label_s_peremeter.setFont(font_1)

        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 340, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 340, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 370, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)

        self.window_shape.show()

    #Периметер овала
    def perim_oblong(self) -> None:

        oblong_a_list = self.check_number_new(self.oblong_side_a_value.text())
        oblong_b_list = self.check_number_new(self.oblong_side_b_value.text())

        self.message_oblong_side_a.setText(oblong_a_list[1])
        self.message_oblong_side_b.setText(oblong_b_list[1])

        self.message_oblong_side_a.setGeometry(150, 240, oblong_a_list[2], 20)
        self.message_oblong_side_b.setGeometry(150, 270, oblong_b_list[2], 20)
        if oblong_a_list[0] != 0:
            self.message_oblong_side_a.setStyleSheet(s.valide_value_style)
        else:
            self.message_oblong_side_a.setStyleSheet(s.error_value_style)

        if oblong_b_list[0] != 0:
            self.message_oblong_side_b.setStyleSheet(s.valide_value_style)
        else:
            self.message_oblong_side_b.setStyleSheet(s.error_value_style)
                      
        if oblong_a_list[0] != 0 and oblong_b_list[0] != 0:
            if oblong_a_list[0] < oblong_b_list[0]:
                self.message_oblong_side_a.setStyleSheet(s.error_value_style)
                self.message_oblong_side_b.setStyleSheet(s.error_value_style)
                self.message_oblong_side_a.setGeometry(150, 240, 150, 20)
                self.message_oblong_side_b.setGeometry(150, 270, 150, 20)
                self.message_oblong_side_a.setText("Замале значення")
                self.message_oblong_side_b.setText("Завелике значення")
                self.perimeter.setText("?")
            else:
                oblong = g.Oblong()
                self.message_oblong_side_a.setStyleSheet(s.valide_value_style)
                self.message_oblong_side_b.setStyleSheet(s.valide_value_style)
                self.perimeter.setText(str(oblong.perimeter_oblong(oblong_a_list[0], oblong_b_list[0])))
                self.oblong_side_a_value.setText(str(round(oblong_a_list[0], 2)))
                self.oblong_side_b_value.setText(str(round(oblong_b_list[0], 2)))
                del(oblong)
        else:
            self.perimeter.setText("?")
    #КІНЕЦЬ ОВАЛ

    #ТРИКУТНИК РІВНОСТОРОННІЙ
    #Вікно трикутника рівносоторонній
    def equilateral_triangle(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.shape.currentTextChanged.connect(self.close_shape_window)
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 520)

        self.image_round = gui.QPixmap(f"{TRIANGLE_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(13, 10, int(260 * 1.325), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)
        self.window_shape.setFixedSize( 370, 520)

        #Сторона A
        #Заголовок сторони а
        self.eq_tr_side_label = QLabel("A", self.window_shape)
        self.eq_tr_side_label.setGeometry(15, 300, 15, 20)
        self.eq_tr_side_label.setStyleSheet(s.all_labels_style)
        self.eq_tr_side_label.setFont(font_1)
        
        #Значення сторони
        self.eq_tr_side_value = QLineEdit("0.0", self.window_shape)
        self.eq_tr_side_value.setGeometry(35, 300, 80, 25)
        self.eq_tr_side_value.setFont(font_3)
        self.eq_tr_side_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.eq_tr_side_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_eq_tr_side_label = QLabel("мм", self.window_shape)
        self.mm_eq_tr_side_label.setGeometry(120, 300, 70, 20)
        self.mm_eq_tr_side_label.setStyleSheet(s.all_labels_style)
        self.mm_eq_tr_side_label.setFont(font_1)

        #Статус сторони       
        self.message_eq_tr_side = QLabel(None, self.window_shape)
        self.message_eq_tr_side.setGeometry(150, 300, 150, 20)
        if self.eq_tr_side_value.text() in zero:
            self.message_eq_tr_side.setText("Відсутнє значення")
            self.message_eq_tr_side.setFont(font_4)
            self.message_eq_tr_side.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_eq_tr_side.setStyleSheet(s.error_value_style) 

        #Кнопка розрахунку через сторону А
        self.btn_eq_tr_a = QPushButton("Розрахувати периметр по A", self.window_shape)
        self.btn_eq_tr_a.clicked.connect(self.perim_eq_riangle_a)
        self.btn_eq_tr_a.setGeometry(10, 330, 350, 30)
        self.btn_eq_tr_a.setStyleSheet(s.btn_perimeter_1)

        #Сторона H
        #Заголовок висоти h
        self.eq_tr_height_label = QLabel("H", self.window_shape)
        self.eq_tr_height_label.setGeometry(15, 380, 15, 20)
        self.eq_tr_height_label.setStyleSheet(s.all_labels_style)
        self.eq_tr_height_label.setFont(font_1)

        #Значення висоти
        self.eq_tr_height_value = QLineEdit("0.0", self.window_shape)
        self.eq_tr_height_value.setGeometry(35, 380, 80, 25)
        self.eq_tr_height_value.setFont(font_3)
        self.eq_tr_height_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.eq_tr_height_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність висоти
        self.mm_eq_tr_height_label = QLabel("мм", self.window_shape)
        self.mm_eq_tr_height_label.setGeometry(120, 380, 70, 20)
        self.mm_eq_tr_height_label.setStyleSheet(s.all_labels_style)
        self.mm_eq_tr_height_label.setFont(font_1)
        #Статус сторони       
        self.message_eq_tr_height = QLabel(None, self.window_shape)
        self.message_eq_tr_height.setGeometry(150, 380, 150, 20)
        if self.eq_tr_height_value.text() in zero:
            self.message_eq_tr_height.setText("Відсутнє значення")
            self.message_eq_tr_height.setFont(font_4)
            self.message_eq_tr_height.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_eq_tr_height.setStyleSheet(s.error_value_style) 

        #Кнопка розрахунку через висоту H
        self.btn_eq_tr_h = QPushButton("Розрахувати периметр по H", self.window_shape)
        self.btn_eq_tr_h.clicked.connect(self.perim_eq_riangle_h)
        self.btn_eq_tr_h.setGeometry(10, 410, 350, 30)
        self.btn_eq_tr_h.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 450, 150, 20)
        self.Label_s_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_s_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 450, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 450, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 480, 350, 30)      
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)
        self.window_shape.show()

    #Периметер рівносторонього трикутника через сторону
    def perim_eq_riangle_a(self) -> None:
        side_a_list = self.check_number_new(self.eq_tr_side_value.text())
        self.message_eq_tr_side.setText(side_a_list[1])

        self.message_eq_tr_side.setGeometry(150, 300, side_a_list[2], 20)

        if side_a_list[0] != 0:
            triangle = g.Equilateral_triangle()
            self.message_eq_tr_side.setGeometry(150, 300, 150, 20)
            self.message_eq_tr_height.setGeometry(150, 380, 150, 20)
            self.message_eq_tr_side.setStyleSheet(s.valide_value_style)
            self.message_eq_tr_height.setStyleSheet(s.valide_value_style)
            self.message_eq_tr_height.setText("Валідне значення")      
            self.perimeter.setText(str(triangle.perim_eq_tr_side(side_a_list[0])))
            self.eq_tr_height_value.setText(str(triangle.height_eq_tr_side(side_a_list[0])))        
        else:
            self.message_eq_tr_side.setGeometry(150, 300, side_a_list[2], 20)
            self.message_eq_tr_height.setGeometry(150, 380, 150, 20)
            self.message_eq_tr_side.setStyleSheet(s.error_value_style)
            self.message_eq_tr_height.setStyleSheet(s.error_value_style)
            self.message_eq_tr_height.setText("Відсутнє значення")  
            self.eq_tr_height_value.setText("0.0")
            self.perimeter.setText("?")

    #Периметер рівносторонього трикутника через висоту
    def perim_eq_riangle_h(self) -> None:
        height_h_list = self.check_number_new(self.eq_tr_height_value.text())

        self.message_eq_tr_height.setText(height_h_list[1])
        self.message_eq_tr_height.setGeometry(150, 380, height_h_list[2], 20)

        if height_h_list[0] != 0:
            triangle = g.Equilateral_triangle()
            self.message_eq_tr_side.setGeometry(150, 300, 150, 20)
            self.message_eq_tr_height.setGeometry(150, 380, 150, 20)
            self.message_eq_tr_height.setStyleSheet(s.valide_value_style)
            self.message_eq_tr_side.setStyleSheet(s.valide_value_style)
            self.message_eq_tr_side.setText("Валідне значення")            
            self.perimeter.setText(str(triangle.perim_eq_tr_height(height_h_list[0])))
            self.eq_tr_side_value.setText(str(triangle.side_eq_tr_height(height_h_list[0])))
        else:
            self.message_eq_tr_side.setGeometry(150, 300, 150, 20)
            self.message_eq_tr_height.setGeometry(150, 380, height_h_list[2], 20)
            self.eq_tr_side_value.setText("0.0")
            self.message_eq_tr_height.setStyleSheet(s.error_value_style)
            self.message_eq_tr_side.setStyleSheet(s.error_value_style)
            self.message_eq_tr_side.setText("Відсутнє значення")
            self.eq_tr_side_value.setText(str(g.Equilateral_triangle.side_eq_tr_height(height_h_list[0])))
            self.perimeter.setText("?")
    #КІНЕЦЬ ТРИКУТНИК РІВНОСТОРОННІЙ

    #РІВНОБЕДРЕНИЙ ТРИКУТНИК
    #Вікно рівнобедреного трикутника
    def isosceles_triangle(self, shape: str) -> None:
        self.window_shape = ShapeWindow()
        self.window_shape.setWindowTitle(shape)
        self.window_shape.setGeometry(950, 200, 370, 600)

        self.image_round = gui.QPixmap(f"{ISOSCELES_TRIANGLE_IMAGE_PATH}")
        self.image_lable = QLabel(self.window_shape)
        self.image_lable.setGeometry(61, 30, int(260 * 0.955), 260)
        self.image_lable.setPixmap(self.image_round)
        self.image_lable.setScaledContents(True)

        #Сторона A
        #Заголовок сторони
        self.side_a_is_tr_label = QLabel("A", self.window_shape)
        self.side_a_is_tr_label.setGeometry(15, 320, 15, 20)
        self.side_a_is_tr_label.setStyleSheet(s.all_labels_style)
        self.side_a_is_tr_label.setFont(font_1)

        #Значення сторони
        self.side_a_is_tr_value = QLineEdit("0.0", self.window_shape)
        self.side_a_is_tr_value.setGeometry(35, 320, 80, 25)
        self.side_a_is_tr_value.setFont(font_3)
        self.side_a_is_tr_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_a_is_tr_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_side_a_is_tr_label = QLabel("мм", self.window_shape)
        self.mm_side_a_is_tr_label.setGeometry(120, 320, 70, 20)
        self.mm_side_a_is_tr_label.setStyleSheet(s.all_labels_style)
        self.mm_side_a_is_tr_label.setFont(font_1)

        #Статус сторони       
        self.message_side_a_is_tr = QLabel(None, self.window_shape)
        self.message_side_a_is_tr.setGeometry(150, 320, 150, 20)
        if self.side_a_is_tr_value.text() in zero:
            self.message_side_a_is_tr.setText("Відсутнє значення")
            self.message_side_a_is_tr.setFont(font_4)
            self.message_side_a_is_tr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_a_is_tr.setStyleSheet(s.error_value_style) 

        #Сторона B
        #Заголовок сторони
        self.side_b_is_tr_label = QLabel("B", self.window_shape)
        self.side_b_is_tr_label.setGeometry(15, 350, 15, 20)
        self.side_b_is_tr_label.setStyleSheet(s.all_labels_style)
        self.side_b_is_tr_label.setFont(font_1)

        #Значення сторони
        self.side_b_is_tr_value = QLineEdit("0.0", self.window_shape)
        self.side_b_is_tr_value.setGeometry(35, 350, 80, 25)
        self.side_b_is_tr_value.setFont(font_3)
        self.side_b_is_tr_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.side_b_is_tr_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_side_b_is_tr_label = QLabel("мм", self.window_shape)
        self.mm_side_b_is_tr_label.setGeometry(120, 350, 70, 20)
        self.mm_side_b_is_tr_label.setStyleSheet(s.all_labels_style)
        self.mm_side_b_is_tr_label.setFont(font_1)

        #Статус сторони       
        self.message_side_b_is_tr = QLabel(None, self.window_shape)
        self.message_side_b_is_tr.setGeometry(150, 350, 150, 20)
        if self.side_b_is_tr_value.text() in zero:
            self.message_side_b_is_tr.setText("Відсутнє значення")
            self.message_side_b_is_tr.setFont(font_4)
            self.message_side_b_is_tr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_side_b_is_tr.setStyleSheet(s.error_value_style) 

        #Висота H
        #Заголовок сторони
        self.height_is_tr_label = QLabel("H", self.window_shape)
        self.height_is_tr_label.setGeometry(15, 380, 15, 20)
        self.height_is_tr_label.setStyleSheet(s.all_labels_style)
        self.height_is_tr_label.setFont(font_1)

        #Значення сторони
        self.height_is_tr_value = QLineEdit("0.0", self.window_shape)
        self.height_is_tr_value.setGeometry(35, 380, 80, 25)
        self.height_is_tr_value.setFont(font_3)
        self.height_is_tr_value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.height_is_tr_value.setStyleSheet(s.q_line_edit_style)

        #Розмірність сторони
        self.mm_height_is_tr_label = QLabel("мм", self.window_shape)
        self.mm_height_is_tr_label.setGeometry(120, 380, 70, 20)
        self.mm_height_is_tr_label.setStyleSheet(s.all_labels_style)
        self.mm_height_is_tr_label.setFont(font_1)

        #Статус сторони       
        self.message_height_is_tr = QLabel(None, self.window_shape)
        self.message_height_is_tr.setGeometry(150, 380, 150, 20)
        if self.height_is_tr_value.text() in zero:
            self.message_height_is_tr.setText("Відсутнє значення")
            self.message_height_is_tr.setFont(font_4)
            self.message_height_is_tr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) 
            self.message_height_is_tr.setStyleSheet(s.error_value_style) 

        #Кнопка розрахунку через сторону А та сторону В
        self.btn_perim_is_tr_a_b = QPushButton("Розрахувати периметр по А та В", self.window_shape)
        self.btn_perim_is_tr_a_b.clicked.connect(self.perim_is_tr_a_b)
        self.btn_perim_is_tr_a_b.setGeometry(10, 410, 350, 30)      
        self.btn_perim_is_tr_a_b.setStyleSheet(s.btn_perimeter_1)

        #Кнопка розрахунку через сторону А та сторону H
        self.btn_perim_is_tr_a_h = QPushButton("Розрахувати периметр по А та Н", self.window_shape)
        self.btn_perim_is_tr_a_h.clicked.connect(self.perim_is_tr_a_h)
        self.btn_perim_is_tr_a_h.setGeometry(10, 450, 350, 30)      
        self.btn_perim_is_tr_a_h.setStyleSheet(s.btn_perimeter_1)

        #Кнопка розрахунку через сторону B та сторону H
        self.btn_perim_is_tr_b_h = QPushButton("Розрахувати периметр по B та Н", self.window_shape)
        self.btn_perim_is_tr_b_h.clicked.connect(self.perim_is_tr_b_h)
        self.btn_perim_is_tr_b_h.setGeometry(10, 490, 350, 30)      
        self.btn_perim_is_tr_b_h.setStyleSheet(s.btn_perimeter_1)

        #ПЕРИМЕТЕР
        #Заголовок периметра
        self.Label_s_peremeter = QLabel("Периметр", self.window_shape)
        self.Label_s_peremeter.setGeometry(15, 530, 150, 20)
        self.Label_s_peremeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.Label_s_peremeter.setFont(font_1)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(165, 530, 90, 20)
        self.perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.perimeter.setFont(font_1)

        #Розмірність диаметра
        self.mm_result_perimeter = QLabel("мм", self.window_shape)
        self.mm_result_perimeter.setGeometry(255, 530, 50, 20)
        self.mm_result_perimeter.setStyleSheet(f"color: {s.PERIMETER_COLOR};")
        self.mm_result_perimeter.setFont(font_1)

        #Кнопка периметер квадрата до загального розраунку
        self.btn_add_perimeter = QPushButton("Передати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.clicked.connect(self.add_value)
        self.btn_add_perimeter.setGeometry(10, 560, 350, 30)
        self.btn_add_perimeter.setStyleSheet(s.add_button_style)        
        self.window_shape.show()

    #Периметер рівнобедреного трикутника через дві сторони
    def perim_is_tr_a_b(self) -> None:
        
        side_a_list = self.check_number_new(self.side_a_is_tr_value.text())
        side_b_list = self.check_number_new(self.side_b_is_tr_value.text())
        
        self.message_side_a_is_tr.setText(side_a_list[1])
        self.message_side_b_is_tr.setText(side_b_list[1])

        self.message_side_a_is_tr.setGeometry(150, 320, side_a_list[2], 20)
        self.message_side_b_is_tr.setGeometry(150, 350, side_b_list[2], 20)

        if side_a_list[0] != 0:
            self.message_side_a_is_tr.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
            self.message_height_is_tr.setStyleSheet(s.error_value_style)
            self.height_is_tr_value.setText("0.0")
            self.message_height_is_tr.setText("Відсутнє значення")
            self.perimeter.setText("?")

        if side_b_list[0] != 0:
            self.message_side_b_is_tr.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_b_is_tr.setStyleSheet(s.error_value_style)
            self.message_height_is_tr.setStyleSheet(s.error_value_style)
            self.height_is_tr_value.setText("0.0")
            self.message_height_is_tr.setText("Відсутнє значення")
            self.perimeter.setText("?")

        if side_a_list[0] != 0 and side_b_list[0] != 0:
            if side_a_list[0] * 2 <= side_b_list[0]:
                self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
                self.message_side_b_is_tr.setStyleSheet(s.error_value_style)
                self.message_height_is_tr.setStyleSheet(s.error_value_style)
                self.message_side_a_is_tr.setText("Завелика сторона")
                self.message_side_b_is_tr.setText("Замала сторона")
                self.height_is_tr_value.setText("0.0")
                self.message_height_is_tr.setText("Відсутнє значення")
                self.perimeter.setText("?")
            else:
                isosceles_triangle = g.Isosceles_triangle()
                self.message_side_a_is_tr.setStyleSheet(s.valide_value_style)
                self.message_side_b_is_tr.setStyleSheet(s.valide_value_style)
                self.message_height_is_tr.setText("Валідне значення")
                self.message_height_is_tr.setStyleSheet(s.valide_value_style)
                self.side_a_is_tr_value.setText(str(round(side_a_list[0], 2)))
                self.side_b_is_tr_value.setText(str(round(side_b_list[0], 2)))
                self.perimeter.setText(str(isosceles_triangle.perim_is_tr_side_a_b(side_a_list[0], side_b_list[0])))
                self.height_is_tr_value.setText(str(isosceles_triangle.height_is_tr_side_a_b(side_a_list[0], side_b_list[0])))
                del(isosceles_triangle)
        else:
            self.perimeter.setText("?")
            self.height_is_tr_value.setText("0.0")
            self.message_height_is_tr.setStyleSheet(s.error_value_style)

    #Периметер рівнобедреного трикутника через довгу сторону та висоту
    def perim_is_tr_a_h(self) -> None:

        side_a_list = self.check_number_new(self.side_a_is_tr_value.text())
        height_list = self.check_number_new(self.height_is_tr_value.text())
        
        self.message_side_a_is_tr.setText(side_a_list[1]) 
        self.message_height_is_tr.setText(height_list[1])

        self.message_side_a_is_tr.setGeometry(150, 320, side_a_list[2], 20)
        self.message_height_is_tr.setGeometry(150, 380, height_list[2], 20)

        if side_a_list[0] != 0:
            self.message_side_a_is_tr.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_b_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_b_is_tr.setText("Відсутнє значення")
            self.side_b_is_tr_value.setText("0.0")
            self.perimeter.setText("?")

        if height_list[0] != 0:
            self.message_height_is_tr.setStyleSheet(s.valide_value_style)
        else:
            self.message_height_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_b_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_b_is_tr.setText("Відсутнє значення")
            self.side_b_is_tr_value.setText("0.0")
            self.perimeter.setText("?")            
        
        if side_a_list[0] != 0 and height_list[0] != 0:
            if side_a_list[0] <= height_list[0]:
                self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
                self.message_side_b_is_tr.setStyleSheet(s.error_value_style)
                self.message_height_is_tr.setStyleSheet(s.error_value_style)
                self.message_side_a_is_tr.setText("Замала сторона")
                self.message_side_b_is_tr.setText("Відсутнє значення")
                self.message_height_is_tr.setText("Завелика сторона")
                self.side_b_is_tr_value.setText("0.0")
                self.perimeter.setText("?")
            else:
                isosceles_triangle = g.Isosceles_triangle()
                self.message_side_a_is_tr.setStyleSheet(s.valide_value_style)
                self.message_side_b_is_tr.setStyleSheet(s.valide_value_style)
                self.message_height_is_tr.setStyleSheet(s.valide_value_style)
                self.perimeter.setText(str(isosceles_triangle.perim_is_tr_side_a_height(side_a_list[0], height_list[0])))
                self.side_b_is_tr_value.setText(str(isosceles_triangle.side_b_is_tr_side_a_height(side_a_list[0], height_list[0])))
                del(isosceles_triangle)      
        else:
            self.perimeter.setText("?")
            self.side_b_is_tr_value.setText("0.0")
            self.message_side_b_is_tr.setStyleSheet(s.error_value_style)

    #Периметер рівнобедреного трикутника через коротку сторону та висоту
    def perim_is_tr_b_h(self) -> None:
        side_b_list = self.check_number_new(self.side_b_is_tr_value.text())
        height_list = self.check_number_new(self.height_is_tr_value.text())

        self.message_side_b_is_tr.setText(side_b_list[1]) 
        self.message_height_is_tr.setText(height_list[1])

        self.message_side_b_is_tr.setGeometry(150, 350, side_b_list[2], 20)
        self.message_height_is_tr.setGeometry(150, 380, height_list[2], 20)

        if side_b_list[0] != 0:
            self.message_side_b_is_tr.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_b_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_a_is_tr.setText("Відсутнє значення")
            self.side_a_is_tr_value.setText("0.0")
            self.perimeter.setText("?")

        if height_list[0] != 0:
            self.message_height_is_tr.setStyleSheet(s.valide_value_style)
        else:
            self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
            self.message_height_is_tr.setStyleSheet(s.error_value_style)
            self.message_side_a_is_tr.setText("Відсутнє значення")
            self.side_a_is_tr_value.setText("0.0")
            self.perimeter.setText("?")           

        if side_b_list[0] != 0 and height_list[0] != 0:
            isosceles_triangle = g.Isosceles_triangle()
            self.message_side_a_is_tr.setStyleSheet(s.valide_value_style)
            self.message_side_b_is_tr.setStyleSheet(s.valide_value_style)
            self.message_height_is_tr.setStyleSheet(s.valide_value_style)
            self.perimeter.setText(str(isosceles_triangle.perim_is_tr_height_side_b(height_list[0], side_b_list[0])))
            self.side_a_is_tr_value.setText(str(isosceles_triangle.side_a_is_tr_side_b_height(side_b_list[0], height_list[0])))
            del(isosceles_triangle)
        else:
            self.perimeter.setText("?")
            self.side_a_is_tr_value.setText("0.0")
            self.message_side_a_is_tr.setStyleSheet(s.error_value_style)
    #КІНЕЦЬ РІВНОБЕДРЕНИЙ ТРИКУТНИК

    #Передаємо з вікна форми до головного вікна периметер
    def add_value(self):
        if self.perimeter.text() != "?":
            self.perimeter_value.setText(self.perimeter.text())
            self.message_perimeter.setStyleSheet(s.valide_value_style)
            self.message_perimeter.setText("Валідне значення")
            self.message_perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        if self.perimeter_value.text() in zero:
            self.message_perimeter.setText("Відсутнє значення")
            self.message_perimeter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.message_perimeter.setGeometry(230, 50, 150, 20)
            self.message_perimeter.setStyleSheet(s.error_value_style)

class ShapeWindow(QMdiSubWindow):
    def __init__(self):
        super(ShapeWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(gui.QIcon(f'{ICON}'))
           
if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    # gui.QFontDatabase.addApplicationFont("fonts/Kareliac bold.otf")
    # gui.QFontDatabase.addApplicationFont("fonts/v_CCYadaYadaYadaInt.ttf")
    # gui.QFontDatabase.addApplicationFont("fonts/Aver_Bold_Italic.ttf")
    # gui.QFontDatabase.addApplicationFont("fonts/v_WhizBang.ttf")
    #font_0 = gui.QFont("KareliaC", 16)
    font_0 = gui.QFont("Arial Narrow", 18)
    #font_1 = gui.QFont("v_CCYadaYadaYadaInt", 14)
    font_1 = gui.QFont("Arial Narrow", 16)

    #font_2 = gui.QFont("Aver", 11)
    font_2 = gui.QFont("Arial Narrow", 13)
    #font_3 = gui.QFont("v_CCYadaYadaYadaInt", 12)
    font_3 = gui.QFont("Arial Narrow", 14)

    #font_4 = gui.QFont("v_WhizBang", 10)
    font_4 = gui.QFont("Arial Narrow", 12)
    main_window = MainWindow()
    main_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    main_window.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    main_window.setFixedSize(450, 350)
    main_window.show()

    sys.exit(my_app.exec_())