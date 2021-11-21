import PyQt5.QtWidgets as qtw
import sys


class Janela(qtw.QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('Calculadora')

        self.setGeometry(0, 0, 300, 400)
        self.setFixedSize(300, 400)

        btn1 = qtw.QPushButton('1', self, clicked=lambda: label_in.setText(label_in.text() + '1'))
        btn1.move(20, 50)
        btn1.resize(50, 50)
        btn1.setShortcut("1")

        btn2 = qtw.QPushButton('2', self, clicked=lambda: label_in.setText(label_in.text() + '2'))
        btn2.move(80, 50)
        btn2.resize(50, 50)
        btn2.setShortcut("2")

        btn3 = qtw.QPushButton('3', self, clicked=lambda: label_in.setText(label_in.text() + '3'))
        btn3.move(140, 50)
        btn3.resize(50, 50)
        btn3.setShortcut("3")

        btndiv = qtw.QPushButton(':', self, clicked=lambda: label_in.setText(label_in.text() + '/'))
        btndiv.move(200, 50)
        btndiv.resize(50, 50)
        btndiv.setShortcut("/")

        btn4 = qtw.QPushButton('4', self, clicked=lambda: label_in.setText(label_in.text() + '4'))
        btn4.move(20, 125)
        btn4.resize(50, 50)
        btn4.setShortcut("4")

        btn5 = qtw.QPushButton('5', self, clicked=lambda: label_in.setText(label_in.text() + '5'))
        btn5.move(80, 125)
        btn5.resize(50, 50)
        btn5.setShortcut("5")

        btn6 = qtw.QPushButton('6', self, clicked=lambda: label_in.setText(label_in.text() + '6'))
        btn6.move(140, 125)
        btn6.resize(50, 50)
        btn6.setShortcut("6")

        btntimes = qtw.QPushButton('X', self, clicked=lambda: label_in.setText(label_in.text() + '*'))
        btntimes.move(200, 125)
        btntimes.resize(50, 50)
        btntimes.setShortcut("*")

        btn7 = qtw.QPushButton('7', self, clicked=lambda: label_in.setText(label_in.text() + '7'))
        btn7.move(20, 200)
        btn7.resize(50, 50)
        btn7.setShortcut("7")

        btn8 = qtw.QPushButton('8', self, clicked=lambda: label_in.setText(label_in.text() + '8'))
        btn8.move(80, 200)
        btn8.resize(50, 50)
        btn8.setShortcut("8")

        btn9 = qtw.QPushButton('9', self, clicked=lambda: label_in.setText(label_in.text() + '9'))
        btn9.move(140, 200)
        btn9.resize(50, 50)
        btn9.setShortcut("9")

        btnmenos = qtw.QPushButton('-', self, clicked=lambda: label_in.setText(label_in.text() + '-'))
        btnmenos.move(200, 200)
        btnmenos.resize(50, 50)
        btnmenos.setShortcut("-")

        btn0 = qtw.QPushButton('0', self, clicked=lambda: label_in.setText(label_in.text() + '0'))
        btn0.move(20, 275)
        btn0.resize(50, 50)
        btn0.setShortcut("0")

        btncomma = qtw.QPushButton('.', self, clicked=lambda: label_in.setText(label_in.text() + '.'))
        btncomma.move(80, 275)
        btncomma.resize(50, 50)
        btncomma.setShortcut(".")

        btnmais = qtw.QPushButton('+', self, clicked=lambda: label_in.setText(label_in.text() + '+'))
        btnmais.move(140, 275)
        btnmais.resize(50, 50)
        btnmais.setShortcut("+")

        btnigual = qtw.QPushButton('=', self, clicked=lambda: press_ig())
        btnigual.move(200, 275)
        btnigual.resize(50, 50)
        btnigual.setShortcut("Return")

        btnc = qtw.QPushButton('C', self, clicked=lambda: press_c())
        btnc.move(20, 340)
        btnc.resize(110, 50)
        btnc.setShortcut("c")

        btnre = qtw.QPushButton('<--',self, clicked=lambda: press_())
        btnre.move(140,340)
        btnre.resize(110,50)
        btnre.setShortcut("Backspace")

        label_in = qtw.QLabel('input: ', self)
        label_in.move(10, 1)

        label_out = qtw.QLabel('result: ', self)
        label_out.move(10, 20)

        self.show()

        def press_():
            eq2 = label_in.text()
            if eq2[len(eq2) - 1] == ' ':
                return
            label_in.setText(eq2[:-1])

        def press_ig():
            eq = label_in.text()
            label_out.setText("result: " + str(eval(eq.replace("input: ", ""), {}, {})))

        def press_c():
            label_in.clear()
            label_in.setText('input: ')
            label_out.clear()
            label_out.setText('result: ')


app = qtw.QApplication([])
janela = Janela()
sys.exit(app.exec_())
