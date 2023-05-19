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
        self.shape.addItem("Напівколо")
        self.shape.addItem("Квадрат")
        self.shape.addItem("Квадрат з однаковими радіусами")
        self.shape.addItem("Квадрат з різними радіусами")
        self.shape.addItem("Квадрат у колі")
        self.shape.addItem("Прямокутник")
        self.shape.addItem("Прямокутник з однаковими радіусами")
        self.shape.addItem("Прямокутник з різними радіусами")
        self.shape.addItem("Шестикутник")
        self.shape.addItem("Овал з паралельними сторонами")
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
        elif shape == "Шестикутник":
            self.hexagon(shape)
        elif shape == "Овал з паралельними сторонами":
            self.oblong(shape)
    
    #КОЛО
    #Вікно для кола
    def round_handler(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)

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
        self.message_diameter.setGeometry(120, 50, 150, 20)
        if self.diameter_velue.text() in zero:
            self.message_diameter.setText("Відсутнє значення")
        


        #Кнопка розрахунку
        self.btn_d = QPushButton("Розрахувати периметр", self.window_shape)
        self.btn_d.setGeometry(10, 80, 200, 20)
        self.btn_d.clicked.connect(self.perim_round)

        #ПЕРИМЕТР
        #Заголовок периметра
        self.Label_d_peremeter = QLabel("Периметер кола", self.window_shape)
        self.Label_d_peremeter.setGeometry(10, 100, 90, 20)
        
        #Значення периметра
        self.perimeter= QLabel("0.0", self.window_shape)
        self.perimeter.setGeometry(100, 100, 40, 20)

        #Розмірність диаметра
        self.mm_result_perimeret = QLabel("мм", self.window_shape)
        self.mm_result_perimeret.setGeometry(145, 100, 20, 20)

        #Кнопка периметер діаметра до загального розраунку
        self.btn_add_perimeter = QPushButton("Додати периметр у розрахунок", self.window_shape)
        self.btn_add_perimeter.setGeometry(10, 140, 200, 20)
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

    
    def half_round_heandler(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    def square(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    def square_one_radius(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    def square_four_radius(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    def square_in_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    def rectangle(self, shape: str) -> None:        
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show() 

    def rectangle_one_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    def rectangle_four_round(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()             

    def hexagon(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()
        
    def oblong(self, shape: str) -> None:
        self.window_shape = QMdiSubWindow()

        self.label_text = QLabel(shape, self.window_shape)
        self.window_shape.setGeometry(830, 200, 300, 300)
        self.label_text.setGeometry(10, 10, 200, 20)
        self.window_shape.show()

    #Передаэмо з вікна форми до головного вікна периметер
    def add_value(self):
        self.perimeter_velue.setText(self.perimeter.text())


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(my_app.exec_())
