# SQLAchemy_DB

Utilizando a linguagem Python. O objetivo é desenvolver uma aplicação na qual podemos Criar, Pesquisar e Excluir usuários de um banco
de dados. Na qual a o banco de dados MySQL é composto por:

	id_usuario int unsigned zerofill auto_increment not null,
	nome varchar(255) not null,
	email varchar(255) not null UNIQUE,

Para facilitar o processo, utilizei a biblioteca Flask do Python.
