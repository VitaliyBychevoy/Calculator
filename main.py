import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as gui


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

        self.setGeometry(500, 200, 600, 300)
        self.setWindowTitle("Calculator")
        
        
        self.perimeter_lalel = QLabel("Периметр", self)
        self.perimeter_lalel.setGeometry(10, 20, 100, 20)
        self.perimeter_velue = QLineEdit("0.0", self)
        self.perimeter_velue.setGeometry(120, 20, 40, 20)


        self.mm_label_perimeter = QLabel("мм", self)
        self.mm_label_perimeter.setGeometry(165, 20, 40, 20)

        self.message_perimeter = QLabel(None, self)
        self.message_perimeter.setGeometry(190, 20, 150, 20)

        if self.perimeter_velue.text() in zero:
            self.message_perimeter.setText("Відсутнє значення")


        self.thickness_label = QLabel("Товщина матеріала", self)
        self.thickness_label.setGeometry(10, 45, 100, 20)
        self.thickness_velue = QLineEdit("0.0", self)



        self.thickness_velue.setGeometry(120, 45, 40, 20)

        self.mm_label_thickness = QLabel("мм", self)
        self.mm_label_thickness.setGeometry(165, 45, 40, 20)

        self.message_thickness = QLabel(None, self)
        self.message_thickness.setGeometry(190, 45, 150, 20)

        if self.thickness_velue.text() in zero:
            self.message_thickness.setText("Відсутнє значення")


        self.material_label = QLabel("Оберіть матеріал", self)
        self.material_label.setGeometry(10, 70, 100, 20)
        self.material = QComboBox(self)
        self.material.addItem("Сталь звичайна")
        self.material.addItem("Сталь нержавіюча")
        self.material.addItem("Алюміній")
        self.material.addItem("Мідь")

        self.material.setGeometry(120, 70, 200, 20)

        self.amount_holes_label = QLabel("Кількість отворів", self)
        self.amount_holes_label.setGeometry(10, 95, 100, 20)


        self.amount_holes = QComboBox(self)
        for i in range(1, 21):
            self.amount_holes.addItem(str(i))
        self.amount_holes.setGeometry(120, 95, 40, 20)


        self.btn = QPushButton("Розрахувати", self)
        self.btn.setGeometry(120, 120, 200, 20)
        self.btn.clicked.connect(self.calculate_tonage_new)



        self.force_result_label = QLabel("Небхідне зусилля", self)
        self.force_result_label.setGeometry(10, 145, 100, 20)
        self.force_result_value = QLineEdit('?', self)
        self.force_result_value.setGeometry(120, 145, 40, 20)

        self.tonage_label_force = QLabel("тонн(и)", self)
        self.tonage_label_force.setGeometry(165, 145, 40, 20)


        self.force_result_label = QLabel("Форма", self)
        self.force_result_label.setGeometry(330, 20, 40, 20)
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
        self.shape.setGeometry(380, 20, 210, 25)

        self.btn_perimeter = QPushButton("Розрахувати периметер", self)
        self.btn_perimeter.setGeometry(330, 55, 260, 25)


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
        

    def coefficient_material(self) -> float:
        coeff = 0.0
        coeff = material[self.material.currentText()]
        return coeff

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
    
if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(my_app.exec_())
