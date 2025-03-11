from flask import Flask  # Aqui estamos importando a classe Flask do módulo flask para criar nossa aplicação

# Criamos uma instância do Flask e armazenamos na variável "app"
# O parâmetro __name__ indica que este arquivo será reconhecido como o principal da aplicação
app = Flask(__name__)

# Aqui estamos criando uma rota para o endpoint "/"
# Ou seja, quando acessarmos http://127.0.0.1:5000/, a função abaixo será executada
@app.route("/")
def pagar_pessoas():
    # Retorna uma mensagem formatada em HTML para ser exibida na página principal
    return "<h1>Começar a semana, pagando suas dívidas, é bom demais</h1>"

# Criamos uma rota para o endpoint "/pix"
# Quando acessarmos http://127.0.0.1:5000/pix, a função será chamada automaticamente
@app.route("/pix")
def mande_o_pix():
    # Retorna uma mensagem formatada em HTML para ser exibida na rota "/pix"
    return "<h3>Pagar as pessoas faz bem pras pessoas!!! =D</h3>"

# Criamos uma rota para o endpoint "/comidas"
# Quando acessarmos http://127.0.0.1:5000/comidas, essa função será executada
@app.route("/comidas")
def prato_do_dia():
    # Retorna uma mensagem formatada em HTML descrevendo o prato do dia
    return "<h1>O prato do dia é feijoada com farofinha com bacon e de sobremesa brownie com sorvete!!!</h1>"

# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração (nesse modo nossa API responde automaticamente a qualquer atualização que fizermos no código)
    app.run(debug=True)
