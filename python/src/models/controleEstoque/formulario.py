from PyQt5 import uic, QtWidgets
import mysql.connector

from relatorio import relatorio
from alteracaoCadastral import alteracaoCadastral

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'pmysql',
    password = 'Senha@123',
    database = 'CONTROLE_DE_ESTOQUE'
)

numeroID = 0

def removerCadastro():
    removerDados = listarCadastro.tableWidget.currentRow()
    listarCadastro.tableWidget.removeRow(removerDados)
    
    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM cadastro_de_produtos')
    leituraBanco = cursor.fetchall()

    valorID = leituraBanco [removerDados][0]
    cursor.execute(f'DELETE FROM cadastro_de_produtos WHERE id = {str(valorID)}')
    conexao.commit()

def alterarCadastro():
    alterarCadastro.show()
    global numeroID

    dados = listarCadastro.tableWidget.currentRow()
    cursor = conexao.cursor()
    cursor.execute('SELECT id FROM cadastro_de_produtos')
    leituraBanco = cursor.fetchall()

    valorId = leituraBanco [dados][0]
    cursor.execute(f'SELECT * FROM cadastro_de_produtos WHERE id = {str(valorId)}')
    leituraBanco = cursor.fetchall()
    
    numeroID = valorId
    
    alterarCadastro.txtAlteracaCadastralId.setText(str(leituraBanco [0][0]))
    alterarCadastro.txtAlteracaoCadastralProduto.setText(str(leituraBanco [0][1]))
    alterarCadastro.txtAlteracaoCadastralPreco.setText(str(leituraBanco [0][2]))
    alterarCadastro.txtAlteracaoCadastralQuantidade.setText(str(leituraBanco [0][3]))

def salvarAlteracoes():
    global numeroID

    id = alterarCadastro.txtAlteracaCadastralId.text()
    produto = alterarCadastro.txtAlteracaoCadastralProduto.text()
    preco = alterarCadastro.txtAlteracaoCadastralPreco.text()
    quantidade = alterarCadastro.txtAlteracaoCadastralQuantidade.text()
    
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE cadastro_de_produtos SET id='{id}', produto='{produto}', preco='{preco}', quantidade='{quantidade}' WHERE id='{numeroID}'")
    
    alterarCadastro.close()
    listarCadastro.close()
    conexao.commit()

def listarCadastro():
    listarCadastro.show()

    cursor = conexao.cursor()
    comandoSqlListar = 'SELECT * FROM cadastro_de_produtos'
    cursor.execute(comandoSqlListar)
    leituraBanco = cursor.fetchall()
    
    listarCadastro.tableWidget.setRowCount(len(leituraBanco))
    listarCadastro.tableWidget.setColumnCount(4)
    
    for linhas in range(0, len(leituraBanco)):
        for colunas in range(0, 4):
            listarCadastro.tableWidget.setItem(linhas, colunas, QtWidgets.QTableWidgetItem(str(leituraBanco[linhas][colunas])))

def cadastroProduto():
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text()
    quantidade = formulario.txtQuantidade.text()

    cursor = conexao.cursor()
    comandoSqlCadastro = 'INSERT INTO cadastro_de_produtos (produto, preco, quantidade) VALUES (%s, %s, %s)'
    dados = (str(produto), str(preco), str(quantidade))

    cursor.execute(comandoSqlCadastro, dados)
    conexao.commit()
    
    formulario.txtProduto.setText('')
    formulario.txtPreco.setText('')
    formulario.txtQuantidade.setText('')
    formulario.labelConfirmacaoInTela.setText('PRODUTO CADASTRADO COM SUCESSO')

app = QtWidgets.QApplication([])
formulario = uic.loadUi('telaFormulario.ui')
formulario.buttonCadastrar.clicked.connect(cadastroProduto)

formulario.buttonRelatorio.clicked.connect(listarCadastro)
listarCadastro = relatorio

listarCadastro.buttonAlterarRegistro.clicked.connect(alterarCadastro)
listarCadastro.buttonApagarRegistro.clicked.connect(removerCadastro)
alterarCadastro = alteracaoCadastral

alterarCadastro.buttonConfirmarAlteracoes.clicked.connect(salvarAlteracoes)

formulario.show()
app.exec()