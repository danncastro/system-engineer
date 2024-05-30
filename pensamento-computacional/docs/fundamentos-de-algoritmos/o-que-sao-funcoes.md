# O que são funções

***

## <mark style="color:red;">Funções</mark>

Em programação, uma função é um bloco de código reutilizável que realiza uma tarefa específica. As funções são usadas para organizar o código, torná-lo mais modular e facilitar a reutilização de código. Elas ajudam a dividir um programa em partes menores e mais gerenciáveis.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

A ideia básica por trás de uma função é que você pode definir um conjunto de instruções que executa uma determinada tarefa e, em seguida, chamar essa função sempre que precisar executar essa tarefa. Isso evita a necessidade de repetir o mesmo código várias vezes em seu programa.

<figure><img src="../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

Uma função geralmente tem os seguintes componentes:

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Nome**</mark>

Um identificador que é usado para chamar a função.

#### <mark style="color:blue;">**Parâmetros**</mark>

Valores que podem ser passados para a função quando ela é chamada. Esses valores são usados dentro da função para realizar o trabalho necessário.

#### <mark style="color:blue;">**Corpo**</mark>

O conjunto de instruções que define o que a função faz. Este é o código que é executado quando a função é chamada.

#### <mark style="color:blue;">**Valor de retorno**</mark>

O valor que a função retorna após concluir sua execução. Nem todas as funções têm um valor de retorno, mas aquelas que o têm podem fornecer informações úteis de volta para o código que as chamou.

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

Por exemplo, considere uma função simples que adiciona dois números:

```python
def soma(a, b):
    return a + b

resultado = soma(3, 5)
print(resultado)  # Isso imprimirá 8

```

Neste exemplo, a função `soma` recebe dois parâmetros `a` e `b`, e retorna a soma desses dois valores. Quando chamamos a função com `soma(3, 5)`, ela retorna 8, que é então atribuído à variável `resultado`.

***
