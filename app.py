from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Carregando as configurações do banco de dados a partir do arquivo de configuração
db_config = yaml.safe_load(open('db_config.yaml'))
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'brainstorm'

# Configurando a conexão com o banco de dados
mysql = MySQL(app)

@app.route('/', methods=['GET'])
def Inicio():
    return """
<!DOCTYPE html>
<html>
<head>
	<title>Tudo bem</title>
	<style>
		body {
			background-color: #f2f2f2;
			font-family: Arial, sans-serif;
			color: #333;
			text-align: center;
			padding: 50px;
		}
		h1 {
			font-size: 36px;
			margin-bottom: 20px;
		}
		p {
			font-size: 24px;
			margin-bottom: 40px;
		}
	</style>
</head>
<body>
	<h1>Tudo bem?</h1>
	<p>O Banco de dados está conectado</p>
</body>
</html>
    """ 


@app.route('/create_user/<string:name>/<string:email>', methods=['GET'])
def create_user(name, email):
    
    # Inserindo o novo usuário no banco de dados
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuario (nome, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()

    return 'Usuário criado com sucesso'


@app.route('/users/', methods=['GET'])
def get_users():
    # Obtendo a lista de usuários do banco de dados
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    usuarios = cur.fetchall()
    cur.close()

    # Convertendo a lista de usuários para um formato JSON
    usuario_json = []
    for usuario in usuarios:
        usuario_dict = {'id': usuario[0], 'name': usuario[1], 'email': usuario[2]}
        usuario_json.append(usuario_dict)

    return {'Usuarios': usuario_json}

@app.route('/get_user/<int:id>', methods=['GET'])
def buscar_usuario(id):
    # Conecta ao banco de dados
    cur = mysql.connection.cursor()

    # Busca o usuário pelo id
    cur.execute("SELECT * FROM usuario WHERE id_usuario=%s", (id,))
    usuario = cur.fetchone()

    if usuario:
        return jsonify({'id': usuario[0], 'nome': usuario[1], 'email': usuario[2]})
    else:
        return jsonify({'mensagem': 'Usuário não encontrado!'})


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Deletando o usuário do banco de dados
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    mysql.connection.commit()
    cur.close()

    return 'Usuário deletado com sucesso'


if __name__ == '__main__':
    app.run(debug=True)
