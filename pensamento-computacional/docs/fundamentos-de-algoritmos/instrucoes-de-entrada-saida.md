# Instruções de Entrada/Saída

***

A entrada de dados refere-se à maneira como um algoritmo recebe informações do usuário ou de algum dispositivo externo, como um arquivo. A saída de dados, por outro lado, é a maneira como o algoritmo apresenta ou armazena os resultados após processar essas informações.

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

Existem várias maneiras de realizar entrada e saída de dados em algoritmos, dependendo do contexto em que o algoritmo está sendo executado. Aqui estão algumas das principais:

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Entrada via teclado (input)**</mark>

Nesse método, o usuário fornece dados diretamente ao programa através do teclado. Em muitas linguagens de programação, como Python, C++, Java, entre outras, você pode usar funções específicas para receber entradas do teclado. Por exemplo, em Python, a função `input()` é usada para receber entrada do usuário.

#### <mark style="color:blue;">**Entrada de arquivo**</mark>

Às vezes, os dados podem ser lidos de um arquivo em vez de serem digitados manualmente pelo usuário. Isso é comum quando você tem uma grande quantidade de dados ou quando os dados são gerados por outra fonte. As linguagens de programação geralmente têm funções para abrir, ler e fechar arquivos.

#### <mark style="color:blue;">**Saída para o console (output)**</mark>

A saída padrão para muitos algoritmos é o console ou a tela do computador. As informações processadas são exibidas para o usuário neste formato. Por exemplo, em muitas linguagens de programação, você usa a função `print()` para exibir resultados na tela.

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Saída para arquivo**</mark>

Assim como os dados podem ser lidos de um arquivo, os resultados também podem ser escritos em um arquivo. Isso é útil quando você deseja armazenar os resultados para uso futuro ou compartilhamento com outros programas.

Aqui está um exemplo simples em Python que recebe dois números do usuário, os soma e exibe o resultado:

```python
# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Processamento
soma = num1 + num2

# Saída de dados
print("A soma dos números é:", soma)

```

Neste exemplo, `input()` é usado para receber entrada do usuário, `+` é usado para somar os números e `print()` é usado para exibir o resultado na tela.

Essas são as noções básicas das instruções de entrada e saída de dados em algoritmos. Dependendo da linguagem de programação que você está usando, os detalhes exatos podem variar um pouco, mas o conceito geral é o mesmo.

***
