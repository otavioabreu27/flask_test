# Imports das bibliotecas Flask e mysqldb
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração inicial do banco de dados
# *IMPORTANTE*
# As credenciais de banco podem precisar ser alteradas
# de computador em computador
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = 'fatec' 
app.config['MYSQL_DB'] = 'Flask'

# Instanciando um objeto que herda a classe my sql do mysqldb
mysql = MySQL(app)

# Este comando executa uma ação no banco usando linguagem dml ou ddl
#   cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')

# Para salvar as alterações feitas no banco
#   mysql.connection.commit()

# Fechando o cursor
#   cursor.close()

# Ouando a rota da requisiçao for localhost:5000/ que é a pardrão
# é chamado o método render_template que carrega uma página html
# que no flask é chamada de template
@app.route('/')
def home():
    # Instanciando o cursor mysql
    cur = mysql.connection.cursor()
    cur.close()
    return render_template('home.html')

# O __name__ por padrão é main, portanto quando satisfazer essa função
# a aplicação é rodada
if __name__ == "__main__":
    app.run()
