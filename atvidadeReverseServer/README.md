Relatório - Ataque com Threads e Paralelismo

Este repositório contém um exemplo de código em Python que demonstra um ataque utilizando threads e paralelismo. O objetivo do ataque é estressar um servidor simulado enviando múltiplas requisições simultaneamente.
Funcionamento do Ataque

O ataque consiste em enviar uma lista de mensagens para o servidor em paralelo, utilizando threads para executar o envio de requisições de forma concorrente. Cada thread é responsável por enviar uma mensagem para o servidor.

O código do cliente (client.py) é responsável por estabelecer uma conexão com o servidor e enviar as requisições. Ele cria um número configurável de threads, onde cada uma delas envia uma mensagem para o servidor. O servidor, por sua vez, recebe as requisições em threads separadas, tratando cada uma delas independentemente.
Threads e Paralelismo

As threads são unidades de execução independentes que podem ser executadas em paralelo. No contexto do ataque, as threads são utilizadas para enviar requisições ao servidor de forma concorrente. Cada thread é responsável por uma requisição e executa em paralelo com as demais.

O paralelismo é alcançado através do uso das threads. Ao criar múltiplas threads para enviar requisições simultaneamente, podemos explorar o poder de processamento paralelo da CPU, maximizando a utilização dos recursos disponíveis.
Como Executar

Para executar o ataque, siga as etapas abaixo:

    Certifique-se de ter o Python instalado em sua máquina.

    Clone este repositório para o seu ambiente local.

    Navegue até o diretório do projeto no terminal.

    Execute o servidor primeiro, utilizando o seguinte comando:

    bash

    python3 server.py

Em seguida, execute o cliente para iniciar o ataque:

bash

    python3 client.py

O cliente enviará um número configurável de requisições simultâneas para o servidor.

Observe a saída no terminal do servidor, que exibirá as mensagens recebidas e processadas.

![Print do monitor de sistemas](caminho/para/a/imagem.jpg)


-------------------------------------
Funcionamento da Reversão da String
-------------------------------------

Além de realizar o ataque simulado com threads e paralelismo, o código também demonstra a funcionalidade de reversão da string. Após receber uma requisição do cliente, o servidor realiza a reversão da string antes de enviá-la de volta como resposta.

Após receber a mensagem do cliente, o servidor executa as seguintes etapas:

    Recebe a mensagem do cliente.

    Inicia um loop para simular um processamento intensivo na CPU por 10 segundos. Essa etapa foi adicionada para simular uma carga de trabalho significativa no servidor.

    Inverte a ordem dos caracteres da mensagem recebida, criando uma nova string que contém a mensagem revertida.

    Envia a string revertida de volta ao cliente como resposta.

Dessa forma, ao receber a resposta do servidor, o cliente imprime a string revertida na saída.
