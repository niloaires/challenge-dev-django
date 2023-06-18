# Devolutiva do desafio técnico da DigitalSys

Este é um desafio técnico para criar um sistema de gestão de propostas de empréstimo pessoal utilizando a seguinte stack:

- Django
- Django Rest Framework
- Django Celery


#### Considerações iniciais
Prezado avaliador, a princípio, quero agradecer a oportunidade dada pela DigitalSys
no que diz respeito a este desafio técnico. Foi uma experiência muito enriquecedora e
desafiadora. 

Informo que fiz questão de manter ao máximo a semântica do código, bem como a
consonância com o PEP8.

No que diz respeito a execução das tasks no Celery, setei o tempo de repetição para 5 minutos,
no entanto, caso seja interessante, poderá reduzir esse tempo, através da linha 37 do arquivo
tasks.py, que se encontra no diretório: /apps/cadastros/tasks.py

### Cumprimento do requisito de orientação para execução do projeto:
1.1 - Clone o repositório e execute o comando abaixo alterar para acessar branch adequada:

```bash
git checkout main
```

1.2 - Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambientes:

```
DEBUG=True
```
1.3 - Instale em seu ambiente o docker e o docker-compose

Essa etapa pode ser feita através do link: https://docs.docker.com/engine/install/

1.4 - Execute o comando abaixo para subir o projeto (Verifique se as portas 8000, 3000, 5672 e 15672 estão disponíveis. Verifique ainda se está no diretório raiz do projeto):


```bash 
docker-compose -f docker-compose.yml up --build
```

1.5 - Criação de um usuário / senha padrão para o admin do sistema

1.5.1 - Execute o comando abaixo para criar um super usuário:

```bash
docker exec -it api_container python manage.py runscript criar_superusuario
``` 
Informe um nome de usuário da sua preferência e o Script deverá criar uma senha e informar ao final.


### Backend


O link para acesso ao admin é: http://localhost:8000/admin e deverá estar disponível ao final do script

2.1 - Cadastro de campos

No ambiente de admin, acesse o menu "Campos" e cadastre os campos que deverão constar na proposta.

Optei por criar um modelo de campos dinâmicos, onde o 
administrador do sistema poderá cadastrar os campos que 
devem constar na proposta através do django-admin. Como é mencionado nos requisitos, porém,  adicionei atributos de obrigatoriedade e campo único, para melhor a experiência no frontend.


### Frontend

Muito embora tenha sido informado que não seria avaliado o frontend, optei por criar 
um frontend em ReactJS para melhorar a experiência do usuário.
Uma vez que o passo de cadastro dos campos tenha sido cumprido, o usuário poderá acessar o formulóario através do link:

http://localhost:3000/nova-proposta

Após conclusão e validação do campo, em 3 segundos o usuário é direcionando para um lista de Propostas


### Task de avaliação da proposta (Celery)
O algorithmo de avaliação da proposta foi criado no arquivo tasks.py, 
onde com base no id do objeto (ímpar ou par) A avaliação da proposta é aprovada ou negada, assim
garantindo que 50% das proopostas sejam aprovadas. 

A execução da taks tem frequência de 5 minutos, 
para simular uma avaliação assíncrona.



#### Bibliotecas utilizadas
```
O projeto executa o a versão 3.8 do Python

amqp==5.1.1
asgiref==3.7.2
async-timeout==4.0.2
backports.zoneinfo==0.2.1
billiard==4.1.0
celery==5.3.0
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
cron-descriptor==1.4.0
Django==4.2.2
django-celery-beat==2.5.0
django-cors-headers==3.7.0
django-extensions==3.2.3
django-timezone-field==5.0
djangorestframework==3.14.0
kombu==5.3.0
pika==1.3.2
prompt-toolkit==3.0.38
python-crontab==2.7.1
python-dateutil==2.8.2
python-decouple==3.8
pytz==2023.3
redis==4.5.5
six==1.16.0
sqlparse==0.4.4
typing_extensions==4.6.3
tzdata==2023.3

```
