from PyQt5 import uic, QtWidgets

def calculoSalario():

    salario = float(formulario.txtSalario.text())
    desconto = float(formulario.txtDescontos.text())

    percentualDesconto = desconto / 100
    salarioBruto = salario - (salario * percentualDesconto)
    FgtsMensal = salario / 100 * 8
    FgtsAnual = FgtsMensal * 12

    formulario.labelResultado.setText(str(f'R${salarioBruto:.2f}'))
    formulario.labelFgtsMensal.setText(str(f'R${FgtsMensal:.2f}'))
    formulario.labelFgtsAnual.setText(str(f'R${FgtsAnual:.2f}'))

app = QtWidgets.QApplication([])
formulario = uic.loadUi('telaSalario.ui')
formulario.buttonCalcular.clicked.connect(calculoSalario)

formulario.show()
app.exec()
