#Кольри для усіх типов вікон
HOVER_COLOR: str = "#32CD32"
FOCUS_COLOR: str  = "#00FFFF" 
#00FA9A

#Стилі для головного вікна
FORM_LIST_COLOR: str  = "Cornsilk"
PERIMETER_MAIN_WINDOW_COLOR: str  = "lightgreen"
MATERIAL_THICKNESS_COLOR: str  = "coral"
HOLES_COLOR: str = "MediumAquaMarine"
RESULT_FORCE_COLOR: str  = "#F0F8FF"

#Стиль для QComgoBox з формами
form_style_shape = "" +\
    "QComboBox {" +\
        "color: Green;" +\
        f"background-color: {FORM_LIST_COLOR};" +\
        "border: 2px solid blue;" +\
    "}" +\
    "QComboBox:hover {" +\
        f"border: 3px solid {HOVER_COLOR}" +\
    "}" +\
    "QComboBox QAbstractItemView {" +\
        "color: Green;" +\
        f"background-color: {FORM_LIST_COLOR};" +\
        "border: 2px solid #00FF00;" +\
    "}"+\
    "QScrollBar {" +\
        f"background : {FORM_LIST_COLOR};" +\
    "}"+\
    "QScrollBar::handle::pressed {"+\
            "background : lightgreen;"+\
    "}"      

#Стиль для периметра головного вікна
perimeter_main_window_style: str = "" +\
    "QLineEdit{" +\
        f"background-color: {PERIMETER_MAIN_WINDOW_COLOR};" +\
        "color: #008CBA;"+\
        "border: 2px solid blue;" +\
        "border-radius: 10px; text-align: center;" +\
    "}" +\
    "QLineEdit:hover {" +\
        f"border: 3px solid {HOVER_COLOR};" +\
    "}" +\
    "QLineEdit:focus {" +\
        f"border: 2px solid {FOCUS_COLOR};" +\
    "}"

#Стиль для товщини матеріала
material_thickness_style: str =  "" +\
    "QLineEdit{" +\
        f"background-color: {MATERIAL_THICKNESS_COLOR};" +\
        "color: #008CBA;" +\
        "border: 2px solid blue;" +\
        "border-radius: 10px; text-align: center;" +\
    "}" +\
    "QLineEdit:hover {" +\
        f"border: 3px solid {HOVER_COLOR};" +\
    "}" +\
    "QLineEdit:focus {" +\
        f"border: 2px solid {FOCUS_COLOR};" +\
    "}"

#Стиль для QComgoBox з матеріалом
materials_style = "" +\
    "QComboBox {" +\
        "color: MediumAquaMarine;" +\
        "background-color: Yellow;" +\
        "border: 2px solid blue;" +\
    "}" +\
    "QComboBox:hover {" +\
        f"border: 3px solid {HOVER_COLOR};" +\
    "}" +\
    "QComboBox QAbstractItemView {" +\
        "color: Green;" +\
        "background-color: Yellow;" +\
        f"border: 2px solid {FOCUS_COLOR};" +\
    "}"

#Стиль для QComgoBox з отворів
holes_style = "" +\
    "QComboBox {" +\
        f"color: Olive; background-color: MediumAquaMarine; border: 2px solid blue;" +\
    "}" +\
    "QComboBox:hover {" +\
        f"border: 3px solid {HOVER_COLOR};" +\
    "}" +\
    "QComboBox QAbstractItemView {" +\
        "color: Olive;" +\
        "background-color: MediumAquaMarine;" +\
        f"border: 2px solid {FOCUS_COLOR};" +\
    "}"+\
    "QScrollBar {" +\
        f"background : {HOLES_COLOR};" +\
    "}"+\
    "QScrollBar::handle::pressed {"+\
        f"background : {HOVER_COLOR};"+\
    "}"

#Стиль для результата
result_style = "" +\
    "QLineEdit{" +\
        "border-radius: 10px;" +\
        "border: 2px solid rgb(0, 255, 255);" +\
        "color: #660099;" +\
    "}"

#Стилі відображення повідомлення про стан введеної інформації
error_value_style: str = "background-color: red; color: white; border-radius: 10px;"
valide_value_style: str = "background-color: green; color: white; border-radius: 10px;"

#Довжина фону повідомлення про стан введеної інформації
error_width_1: int = 150
error_width_2: int = 210
valid_width: int = 150
message_width: int = 150


#Стилі для вікна форм
#Кольори параметрів 
FIRST_PARAMETER_COLOR = "#7B68EE"

SECOND_PARAMETER_COLOR = "#00BFFF"  

THIRD_PARAMETER_COLOR = "#00CED1" 

FOURTH_PARAMETER_COLOR = "#20B2AA"  

FIFTH_PARAMETER_COLOR = "#3CB371" 

SIXTH_PARAMETER_COLOR = "#228B22"

SUBRESULT_COLOR = "#FFA500"

PERIMETER_COLOR = "#8B00FF"

#Стиль для кнопки розрахунку зусилля
force_button_style: str = ""+\
        "QPushButton {" +\
            "color: #FFEFD5;" +\
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(30, 144, 255), stop:1 rgb(100,149,237));" +\
            "border-radius: 10px;" +\
            "font-size: 16px;" +\
            "font-weight: bold;" +\
        "}" +\
        "QPushButton:hover {" +\
            f"background-color: {HOVER_COLOR};" +\
        "}"      
#Стиль кнопки для передачі периметра у розрахунок
add_button_style: str = ""+\
        "QPushButton {" +\
            "color: #FFEFD5;" +\
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(30, 144, 255), stop:1 rgb(128, 0, 128));" +\
            "border-radius: 10px;" +\
            "font-size: 16px;" +\
            "font-weight: bold;" +\
        "}" +\
        "QPushButton:hover {" +\
            f"background-color: {HOVER_COLOR};" +\
        "}"
        
#Стиль для першої кнопки розрахунку периметра
btn_perimeter_1: str = "" +\
        "QPushButton {" +\
            "color: #FFEFD5;" +\
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 100, 0), stop:1 rgb(60, 179, 113));" +\
            "border-radius: 10px;" +\
            "font-size: 14px;" +\
            "font-weight: bold;" +\
        "}" +\
        "QPushButton:hover {" +\
            f"background-color: {HOVER_COLOR};" +\
        "}"

#Стиль для другої кнопки розрахунку периметра
btn_perimeter_2: str = "" +\
        "QPushButton {" +\
            "color: #FFEFD5;" +\
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 69, 0), stop:1 rgb(255, 127, 80));" +\
            "border-radius: 10px;" +\
            "font-size: 14px;" +\
            "font-weight: bold;" +\
        "}" +\
        "QPushButton:hover {" +\
            f"background-color: {HOVER_COLOR};" +\
        "}"

#Стиль для третьої кнопки розрахунку периметра
btn_perimeter_3: str = "" +\
        "QPushButton {" +\
            "color: #FFEFD5;" +\
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(123, 104, 238), stop:1 rgb(70, 130, 180));" +\
            "border-radius: 10px;" +\
            "font-size: 14px;" +\
            "font-weight: bold;" +\
        "}" +\
        "QPushButton:hover {" +\
            f"background-color: {HOVER_COLOR};" +\
        "}"

#Стиль для першого параметра форми
q_line_edit_style_1: str = "" +\
        "QLineEdit {" +\
            f"background-color: {FIRST_PARAMETER_COLOR};" +\
            "color: #FFFFE0;" +\
            "border: 2px solid blue;" +\
            "border-radius: 10px; text-align: center;" +\
        "}" +\
        "QLineEdit:hover {" +\
            f"border: 3px solid {HOVER_COLOR};" +\
        "}" +\
        "QLineEdit:focus {" +\
            f"border: 3px solid {FOCUS_COLOR};" +\
        "}"

#Стиль для першого параметра форми
q_line_edit_style_2: str = "" +\
        "QLineEdit {" +\
            f"background-color: {SECOND_PARAMETER_COLOR};" +\
            "color: #FFFFE0;" +\
            "border: 2px solid blue;" +\
            "border-radius: 10px; text-align: center;" +\
        "}" +\
        "QLineEdit:hover {" +\
            f"border: 3px solid {HOVER_COLOR};" +\
        "}" +\
        "QLineEdit:focus {" +\
            f"border: 3px solid {FOCUS_COLOR};" +\
        "}"

#Стиль для третього параметра форми
q_line_edit_style_3: str = "" +\
        "QLineEdit {" +\
            f"background-color: {THIRD_PARAMETER_COLOR};" +\
            "color: #FFFFE0;" +\
            "border: 2px solid blue;" +\
            "border-radius: 10px; text-align: center;" +\
        "}" +\
        "QLineEdit:hover {" +\
            f"border: 3px solid {HOVER_COLOR};" +\
        "}" +\
        "QLineEdit:focus {" +\
            f"border: 3px solid {FOCUS_COLOR};" +\
        "}"

#Стиль для четвертого параметра форми
q_line_edit_style_4: str = "" +\
        "QLineEdit {" +\
            f"background-color: {FOURTH_PARAMETER_COLOR};" +\
            "color: #FFFFE0;" +\
            "border: 2px solid blue;" +\
            "border-radius: 10px; text-align: center;" +\
        "}" +\
        "QLineEdit:hover {" +\
           f"border: 3px solid {HOVER_COLOR};" +\
        "}" +\
        "QLineEdit:focus {" +\
            f"border: 3px solid {FOCUS_COLOR};" +\
        "}"

#Стиль для п'ятого параметра форми
q_line_edit_style_5: str = "" +\
        "QLineEdit {" +\
            f"background-color: {FIFTH_PARAMETER_COLOR};" +\
            "color: #FFFFE0;" +\
            "border: 2px solid blue;" +\
            "border-radius: 10px; text-align: center;" +\
        "}" +\
        "QLineEdit:hover {" +\
            f"border: 3px solid {HOVER_COLOR};" +\
        "}" +\
        "QLineEdit:focus {" +\
            f"border: 3px solid {FOCUS_COLOR};" +\
        "}"

#Стиль для шостого параметра форми
q_line_edit_style_6: str = "" +\
        "QLineEdit {" +\
            f"background-color: {SIXTH_PARAMETER_COLOR};" +\
            "color: #FFFFE0;" +\
            "border: 2px solid blue;" +\
            "border-radius: 10px; text-align: center;" +\
        "}" +\
        "QLineEdit:hover {" +\
            f"border: 3px solid {HOVER_COLOR};" +\
        "}" +\
        "QLineEdit:focus {" +\
            f"border: 3px solid {FOCUS_COLOR};" +\
        "}"