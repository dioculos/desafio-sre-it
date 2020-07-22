# desafio-sre-it
Desafio de SRE.

# Descrição

Esta aplicação é uma API REST construída em Python, utilizando o framework FastAPI para a API, a livraria tinydb para persistência de dados, Docker para conter a aplicação em containers, Git para versionamento de arquivos.

# Requerimentos

Para rodar este sistema é necessário ter os seguintes componentes:

    Docker Container Engine v19.03 ou superior;

# Instruções

Para subir esta aplicação, você pode baixar a imagem contida em Docker e rodá-la localmente. A imagem se encontra no seguinte link: https://hub.docker.com/r/oculosdeoculos/desafio-sre

Utilizando o console de comando do seu sistema operacional de preferência, você pode enviar o comando:

docker pull oculosdeoculos/desafio-sre:final

Após coletar a imagem do container, você pode rodá-la utilizando o seguinte comando:

docker pull oculosdeoculos/desafio-sre:final

Isso irá baixar o container para sua máquina.

docker run --name desafio_app -p 5057:5057 --rm desafio_app:final

Este comando irá montar corretamente o ambiente e redirecionar as portas necessárias. A partir deste comando, o container estará rodando e pronto para receber chamadas, feitas através do link: http://localhost:5057. 

Para fazer o setup do banco de dados e coletar as informações necessárias, você deve acessar o caminho http://localhost:5057/start, que irá preencher o banco de dados.

Alternativamente, é oferecida na imagem o banco de dados preenchido (arquivo hts.json).

Para acessar o Kibana e poder visualizar os logs gerados pela aplicação, é necessário primeiramente montar e iniciar o container com o sistema de monitoramento. Isso pode ser feito usando os seguintes comandos:

cd elastdocker

make setup & make all

Para acessar o Elastic, acesse o caminho: https://localhost:5601/, com as seguintes credenciais:

username: elastic
password: changeme

# API

A API REST contida neste sistema possui uma série de funções, que estão documentadas neste link: https://documenter.getpostman.com/view/7498137/T17J7mda?version=latest

A coleção assume que o container esteja rodando localmente com as informações oferecidas neste documento.

Para obter uma coleção Postman desta API, use este link: https://www.getpostman.com/collections/bfce78333f28831c409f
