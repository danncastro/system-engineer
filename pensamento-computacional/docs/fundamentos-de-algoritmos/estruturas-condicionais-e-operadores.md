# Estruturas Condicionais e Operadores

***

## <mark style="color:red;">Estruturas Condicionais</mark>

As estruturas condicionais são blocos fundamentais em algoritmos e programação, permitindo que o código tome decisões com base em condições específicas. Elas são essenciais para a lógica de controle de fluxo, permitindo que um programa execute diferentes partes do código dependendo de certas circunstâncias.

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>



***

### <mark style="color:red;">If-else</mark>

O bloco "if-else" permite que você execute um bloco de código se uma condição for verdadeira e outro bloco de código se a condição for falsa. A estrutura básica é:

```plaintext
Se (condição):
    // código a ser executado se a condição for verdadeira
Senão:
    // código a ser executado se a condição for falsa
```

Por exemplo, em Python:

```python
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

***

### <mark style="color:red;">If-elif-else</mark>

Às vezes, você precisa avaliar várias condições. Nesse caso, você pode usar a estrutura "if-elif-else". Aqui está como funciona:

```plaintext
Se (condição1):
    // código a ser executado se a condição1 for verdadeira
Senão, se (condição2):
    // código a ser executado se a condição2 for verdadeira
...
Senão:
    // código a ser executado se nenhuma das condições anteriores for verdadeira
```

Por exemplo:

```python
nota = 75

if nota >= 90:
    print("Você tirou uma nota A.")
elif nota >= 80:
    print("Você tirou uma nota B.")
elif nota >= 70:
    print("Você tirou uma nota C.")
else:
    print("Você precisa melhorar sua nota.")
```

***

## <mark style="color:red;">Operadores</mark>

Os operadores são símbolos ou palavras reservadas que representam ações específicas a serem executadas em operandos (valores ou variáveis). Eles são usados para realizar operações matemáticas, comparações lógicas, atribuições de valores, entre outras tarefas em programação. Aqui estão alguns tipos comuns de operadores:

***

### <mark style="color:red;">Operadores Aritméticos</mark>

Esses operadores são usados para realizar operações matemáticas básicas, como adição, subtração, multiplicação, divisão, etc.

* **Adição (+)**: Soma dois operandos.
* **Subtração (-)**: Subtrai o segundo operando do primeiro.
* **Multiplicação (\*)**: Multiplica dois operandos.
* **Divisão (/)**: Divide o primeiro operando pelo segundo.
* **Módulo (%)**: Retorna o resto da divisão inteira do primeiro operando pelo segundo.
* **Potenciação (**)\*\*: Eleva o primeiro operando à potência do segundo.

***

### <mark style="color:red;">Operadores de Comparação</mark>

Esses operadores são usados para comparar valores. Eles retornam verdadeiro (True) ou falso (False) como resultado.

* **Igual a (==)**: Verifica se dois operandos são iguais.
* **Diferente de (!=)**: Verifica se dois operandos são diferentes.
* **Maior que (>)**: Verifica se o primeiro operando é maior que o segundo.
* **Menor que (<)**: Verifica se o primeiro operando é menor que o segundo.
* **Maior ou igual a (>=)**: Verifica se o primeiro operando é maior ou igual ao segundo.
* **Menor ou igual a (<=)**: Verifica se o primeiro operando é menor ou igual ao segundo.

***

### <mark style="color:red;">Operadores Lógicos</mark>

Esses operadores são usados para combinar expressões condicionais e retornar verdadeiro ou falso.

* **E (and)**: Retorna verdadeiro se ambas as expressões forem verdadeiras.
* **OU (or)**: Retorna verdadeiro se pelo menos uma das expressões for verdadeira.
* **NÃO (not)**: Inverte o valor de verdade de uma expressão.

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

***

### <mark style="color:red;">Operadores de Atribuição</mark>

Esses operadores são usados para atribuir valores a variáveis.

* **Atribuição (=)**: Atribui o valor do lado direito ao operando do lado esquerdo.
* **Atribuição com Adição (+=)**: Adiciona o valor do lado direito ao valor do operando do lado esquerdo e atribui o resultado ao operando do lado esquerdo.
* **Atribuição com Subtração (-=)**: Subtrai o valor do lado direito do valor do operando do lado esquerdo e atribui o resultado ao operando do lado esquerdo.
* **Atribuição com Multiplicação (\*=)**: Multiplica o valor do lado direito pelo valor do operando do lado esquerdo e atribui o resultado ao operando do lado esquerdo.
* **Atribuição com Divisão (/=)**: Divide o valor do operando do lado esquerdo pelo valor do lado direito e atribui o resultado ao operando do lado esquerdo.
* **Atribuição com Módulo (%=)**: Calcula o módulo do valor do operando do lado esquerdo pelo valor do lado direito e atribui o resultado ao operando do lado esquerdo.

***
