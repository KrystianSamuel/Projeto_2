from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria =""


    if formulario.radioButton.isChecked(): 
        print("Categoria Fruta foi selecionado")
        categoria = "Fruta"
    elif formulario.radioButton_2.isChecked(): 
        print("Categoria Bebidas foi selecionado")
        categoria = "Bebidas"
    else :
        print("Categoria Lanches foi selecionado")
        categoria = "Lanche"
        
    print("Codigo",linha1) 
    print("Descricao",linha2)
    print("Preco",linha3)

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

def chama_segunda_tela():
    segunda_tela.show()

def chama_login_tela():
    login_tela.show()

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar.ui")
login_tela=uic.loadUi("login_adm.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
formulario.pushButton_3.clicked.connect(chama_login_tela)

formulario.show()
app.exec()


