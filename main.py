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

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 600, 500)
        self.setWindowTitle("Calculator")
        
        
        self.perimeter_lalel = QLabel("Периметр", self)
        self.perimeter_lalel.setGeometry(10, 20, 100, 20)
        self.perimeter_velue = QLineEdit("0.0", self)
        self.perimeter_velue.setGeometry(120, 20, 40, 20)


        self.mm_label_perimeter = QLabel("мм", self)
        self.mm_label_perimeter.setGeometry(165, 20, 40, 20)

        self.message_perimeter = QLabel(None, self)
        self.message_perimeter.setGeometry(210,20, 150, 20)
        if self.perimeter_velue.text() == "0.0" or self.perimeter_velue.text() == "0,0":
            self.message_perimeter.setText("Периметр відсутній")
            print("Периметр відсутній")

        self.thickness_label = QLabel("Товщина матеріала", self)
        self.thickness_label.setGeometry(10, 45, 100, 20)
        self.thickness_velue = QLineEdit("0.0", self)



        self.thickness_velue.setGeometry(120, 45, 40, 20)

        self.mm_label_thickness = QLabel("мм", self)
        self.mm_label_thickness.setGeometry(165, 45, 40, 20)

        self.message_thickness = QLabel(None, self)
        self.message_thickness.setGeometry(210,45, 150, 20)

        if self.thickness_velue.text() == "0.0" or self.thickness_velue.text() == "0,0":
            self.message_thickness.setText("Товщина відсутня")
            print("Товщина відсутня")        

        self.material_label = QLabel("Оберіть матеріал", self)
        self.material_label.setGeometry(10, 70, 100, 20)
        self.material = QComboBox(self)
        self.material.addItem("Сталь звичайна")
        self.material.addItem("Сталь нержавіюча")
        self.material.addItem("Алюміній")
        self.material.addItem("Мідь")

        self.material.setGeometry(120, 70, 150, 20)

        self.amount_holes_label = QLabel("Кількість отворів", self)
        self.amount_holes_label.setGeometry(10, 95, 100, 20)
        # self.amount_holes_value = QLineEdit("1", self)
        # self.amount_holes_value.setGeometry(120, 95, 100, 20)

        self.amount_holes = QComboBox(self)
        for i in range(1, 21):
            self.amount_holes.addItem(str(i))
        self.amount_holes.setGeometry(120, 95, 40, 20)


        self.btn = QPushButton("Розрахувати", self)
        self.btn.setGeometry(20, 120, 180, 20)
        self.btn.clicked.connect(self.calculate_tonage)



        self.force_result_label = QLabel("Небхідне зісилля", self)
        self.force_result_label.setGeometry(10, 145, 100, 20)
        self.force_result_value = QLineEdit('N', self)
        self.force_result_value.setGeometry(120, 145, 40, 20)




    def calculate_tonage(self):
        coeff_material = self.coefficient_material()
        print(self.thickness_velue.text())

        if self.perimeter_velue.text() == "0.0" or self.perimeter_velue.text() == "0,0" or self.perimeter_velue.text() is None:
            self.message_perimeter.setText("Периметр відсутній")
            print("Периметр відсутній")
            self.force_result_value.setText("0.0")
        elif self.thickness_velue.text() == "0.0" or self.thickness_velue.text() == "0,0" or self.thickness_velue.text() is None:
            self.message_thickness.setText("Товщина відсутня")
            print("Товщина відсутня")
            self.force_result_value.setText("0.0")
        elif not self.check_perimeter():
            print("Периметр повинен мати числа 0-9 або кому чи крапку")
            self.message_perimeter.setText("Периметр повинен мати числа 0-9 або кому чи крапку")

            self.force_result_value.setText("0.0")
        elif not self.check_thickness():
            print("Товщина повинна мати числа 0-9 або кому чи крапку")
            self.message_thickness.setText("Товщина повинна мати числа 0-9 або кому чи крапку")
            self.force_result_value.setText("0.0")
        else:
            self.message_perimeter.setText("Периметр валідний")
            self.message_thickness.setText("Товщина валідна")
            result = 0.0352 * coeff_material
            result = result * float(self.thickness_velue.text())
            result = result * float(self.perimeter_velue.text())
            result = round(result * float(self.amount_holes.currentText()), 2)
            print(self.amount_holes.currentText())
            self.force_result_value.setText(str(result))


    def calculate_tonage_new(self):
        coeff_material = self.coefficient_material()

        perimeter_list = self.check_number_new(self.perimeter_velue.text())

        thickness_list = self.check_number_new(self.thickness_velue.text())

        if perimeter_list[0] == 0:
            self.message_perimeter.setText(perimeter_list[1])
            self.force_result_value.setText("0.0")
        elif thickness_list[0] == 0:
            self.message_thickness.setText(thickness_list[1])
            self.force_result_value.setText("0.0")
        else:
            result = 0.0352 * coeff_material
            result = result * perimeter_list[1]
            result = result * thickness_list[1]
            result = round(result * float(self.amount_holes.currentText()), 2)
            self.force_result_value.setText(str(result))
        

    def coefficient_material(self) -> float:
        coeff = 0.0
        coeff = material[self.material.currentText()]
        return coeff

    def check_number_new(item_string: str) -> list:
        result = [0, 'Статус']
        item_string = item_string.strip()
        if item_string == "0.0":
            result[0] = 0
            result[1] = "Відсутніє значення"
            
        for letter in item_string:
            if letter not in exceptable_number:
                result[0] = 0
                message = f"{letter} не корректний символ. (Можливі символи 0-9 , .)"
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
    
    def check_number(test_number: str) -> float:
        for letter in test_number:
            if letter not in exceptable_number:
                return 0.0
        if "," in test_number:
            test_number = test_number.replace(",", ".", -1)
        return float(test_number)

    def check_thickness(self) -> bool:
        thickness = str(self.thickness_velue.text())
        exceptable_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
        for letter in thickness:
            if letter not in exceptable_number:
                self.force_result_value.setGeometry(120, 145, 400, 20)
                self.force_result_value.setText("Товщина повинна мати числа 0-9 або кому чи крапку")
                return False
        
        return True
    
    def check_perimeter(self) -> bool:
        perimeter = str(self.perimeter_velue.text())
        exceptable_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
        for letter in perimeter:
            if letter not in exceptable_number:
                self.force_result_value.setGeometry(120, 145, 400, 20)
                self.force_result_value.setText("Периметер повинен мати числа 0-9 або кому чи крапку")
                return False
        
        return True
if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(my_app.exec_())
