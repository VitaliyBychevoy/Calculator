import sys

from PyQt5.QtWidgets import *
import PyQt5.QtGui as gui


material = {
    "Алюміній": 0.5,
    "Мідь": 0.57,
    "Сталь звичайна": 1,
    "Сталь нержавіюча": 1.5
 }
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(500, 200, 300, 600)
        self.setWindowTitle("Calculator")
        
        
        self.perimetr_lalel = QLabel("Периметр", self)
        self.perimetr_lalel.setGeometry(10, 20, 100, 20)
        self.perimetr_velue = QLineEdit("0.0", self)
        self.perimetr_velue.setGeometry(120, 20, 100, 20)

        self.thickness_label = QLabel("Товщина матеріала", self)
        self.thickness_label.setGeometry(10, 45, 100, 20)
        self.thickness_velue = QLineEdit("0.0", self)
        self.thickness_velue.setGeometry(120, 45, 100, 20)

        self.material_label = QLabel("Оберіть матеріал", self)
        self.material_label.setGeometry(10, 70, 100, 20)
        self.material_name = QLineEdit("Сталь звичайна", self)
        self.material_name.setGeometry(120, 70, 100, 20)

        self.amount_holes_label = QLabel("Кількість отворів", self)
        self.amount_holes_label.setGeometry(10, 95, 100, 20)
        self.amount_holes_value = QLineEdit("1", self)
        self.amount_holes_value.setGeometry(120, 95, 100, 20)


        self.btn = QPushButton("Розрахувати", self)
        self.btn.setGeometry(20, 120, 180, 20)
        self.btn.clicked.connect(self.calculate_tonage)



        self.force_result_label = QLabel("Небхідне зісилля", self)
        self.force_result_label.setGeometry(10, 145, 100, 20)
        self.force_result_value = QLineEdit('N', self)
        self.force_result_value.setGeometry(120, 145, 40, 20)

        self.manterial = QComboBox(self)
        self.manterial.addItem("Алюміній")
        self.manterial.addItem("Мідь")
        self.manterial.addItem("Сталь звичайна")
        self.manterial.addItem("Сталь нержавіюча")
        self.manterial.setGeometry(10, 200, 150, 20)

    def calculate_tonage(self):
        coeff_material = self.coefficient_material()
        result = 0.0352 * coeff_material * float(self.thickness_velue.text()) * float(self.perimetr_velue.text()) * float(self.amount_holes_value.text())
        print(float(self.amount_holes_value.text()))
        self.force_result_value.setText(str(result))


    def coefficient_material(self) -> float:
        coeff = 0.0
        coeff = material[self.material_name.text()]
        return coeff


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(my_app.exec_())
