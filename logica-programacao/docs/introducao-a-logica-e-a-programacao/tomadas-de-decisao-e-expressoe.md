# Tomadas de Decisão e Expressõe

***

## <mark style="color:red;">Expressões Aritméticas</mark>

Em programação, expressões aritméticas são combinações de valores numéricos, operadores aritméticos e, opcionalmente, outras expressões, que são utilizadas para realizar cálculos matemáticos. Essas expressões são fundamentais para realizar operações como adição, subtração, multiplicação e divisão dentro de um programa.

> _São expressões que utilizam operadores aritméticos e funções aritméticas envolvendo constantes e variáveis_

#### <mark style="color:blue;">Exemplo:</mark>

```python
50+50
total+50
```

As expressões aritméticas são compostas por:

1. **Operandos**: são os valores numéricos que participam da operação. Por exemplo, em uma expressão como `3 + 5`, os operandos são os números 3 e 5.
2.  **Operadores**: são os símbolos que indicam a operação a ser realizada entre os operandos. Os operadores aritméticos básicos incluem:

    <figure><img src="../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

Além desses operadores básicos, linguagens de programação geralmente suportam outros operadores aritméticos, como o operador de resto (%), que retorna o resto da divisão entre dois números inteiros.

Por exemplo, considere a seguinte expressão em uma linguagem de programação como Python:

```python
resultado = 10 * (5 + 3) / 2
```

Nesta expressão, os operandos são os números 10, 5, 3 e 2, e os operadores são a multiplicação (\*), a adição (+) e a divisão (/). A ordem de avaliação das operações segue as regras convencionais da matemática, conhecidas como PEMDAS (Parênteses, Expoentes, Multiplicação e Divisão - da esquerda para a direita, e Adição e Subtração - da esquerda para a direita).

Expressões aritméticas podem ser simples, envolvendo apenas dois operandos e um operador, ou mais complexas, com múltiplos operandos e operadores combinados. Elas são amplamente utilizadas em programação para realizar cálculos matemáticos em algoritmos e aplicações de software.

Em resumo, as expressões aritméticas são uma parte essencial da linguagem de programação, permitindo que os programadores realizem uma ampla gama de cálculos matemáticos dentro de seus programas de forma eficiente e precisa.

***

## <mark style="color:red;">Expressões Literais</mark>

Expressões literais são sequências de caracteres que representam valores de dados fixos, como \[_`números, strings, caracteres ou valores booleanos`_]. Em essência, uma expressão literal é uma forma direta e explícita de representar um valor específico dentro de um programa.

> _São expressões com constantes e/ou variáveis que tem como resultado valores literais. Utilizaremos expressões literais na atribuição de valor para uma variável ou constante._

#### <mark style="color:blue;">Exemplos:</mark>

```python
nome="Danniel Gutierres de Castro"
nome <--- "Danniel Gutierres de Castro"
media=(nota1+nota2+nota3+nota4)/4
```

Existem diferentes tipos de expressões literais, cada uma representando um tipo de dado distinto. Aqui estão alguns exemplos comuns:

#### <mark style="color:blue;">**Literais Numéricos**</mark><mark style="color:blue;">:</mark>&#x20;

São expressões que representam números. Por exemplo:

* `10` (um número inteiro)
* `3.14` (um número de ponto flutuante)
* `-5` (um número inteiro negativo)
* `1e3` (notação científica para 1000)

#### <mark style="color:blue;">**Literais de Strings**</mark><mark style="color:blue;">:</mark>&#x20;

Representam sequências de caracteres. As strings são geralmente delimitadas por aspas simples (' ') ou duplas (" ").

* `"Olá, mundo!"`
* `'Python é incrível'`
* `"12345"` (uma string contendo caracteres numéricos)

#### <mark style="color:blue;">**Literais de Caracteres**</mark><mark style="color:blue;">:</mark>&#x20;

Representam caracteres individuais e são geralmente delimitados por aspas simples.

* `'a'`
* `'X'`
* `'5'` (um caractere, não um número)

#### <mark style="color:blue;">**Literais Booleanos**</mark><mark style="color:blue;">:</mark>

Representam os valores verdadeiro ou falso.

* `True`
* `False`

Expressões literais são importantes porque fornecem uma maneira direta de especificar valores de dados dentro de um programa. Elas são usadas em várias partes do código, como atribuições de variáveis, definições de constantes, parâmetros de função e muito mais.

Por exemplo, em Python, podemos atribuir um valor literal a uma variável da seguinte maneira:

```python
numero = 42
mensagem = "Olá, mundo!"
ativo = True
```

Neste exemplo, `42` é um literal numérico, `"Olá, mundo!"` é um literal de string e `True` é um literal booleano.

Em resumo, expressões literais são representações diretas de valores de dados dentro de um programa. Elas desempenham um papel fundamental na programação, tornando mais fácil e legível para os desenvolvedores especificarem valores fixos em seus códigos.

***

### <mark style="color:red;">Exemplos de Expressões Aritméticas e Literais</mark>

| Variáveis | Comando de atribuição | Procedimento                                                |
| --------- | --------------------- | ----------------------------------------------------------- |
| A         | A = 2                 | Armazenar o valor 2 na variável A                           |
| B         | B = A + 3             | Somar o valor de A(2) com 3 e armazenar em B(5)             |
| C         | C = A + B             | Somar o valor de A(2) e o valor de B(5) e armazenar em C(7) |

<figure><img src="../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">Operadores Relacionais</mark>

Operadores relacionais são símbolos utilizados em programação para comparar dois valores e determinar a relação entre eles. Esses operadores são comumente usados para criar expressões lógicas que ajudam a controlar o fluxo de execução de um programa. Eles retornam um valor booleano (verdadeiro ou falso) que indica se a relação entre os operandos é verdadeira ou falsa.

> _Os operadores relacionais são um grupo de operadores que tem como função comparar dados. São explessões compostas por outras expressões ou variáveis numéricas com operadores relacionais. Expressões relacionais retornam valores lógicos (**verdadeiro / falso**)._

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">Exercitanto os Operadores Relacionais</mark>

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">Tomadas de decisão</mark>

Tomadas de decisão são uma parte essencial da programação, permitindo que os programas executem diferentes ações com base em condições específicas. Essas estruturas de controle de fluxo permitem que os desenvolvedores criem algoritmos flexíveis e adaptáveis, capazes de responder dinamicamente a diferentes situações.

> _Quando o programa e escrito, geralmente ocorre a necessidade de decidir o que fazer dependendo de alguma condição encontrada durante a execução._

#### <mark style="color:blue;">Exemplos de tomada de decisão</mark>

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

***

### <mark style="color:red;">Exercitanto a Tomada de Decisão</mark>

Defina 4 variaveis \[Janeiro, Fevereiro, Março e Abril] que receberá valores de vendas de um funcionario, defina uma variavel vendas que receberá a soma de venda dessas 4 variaveis e caso o valor seja acima ou igual a 5000Mil, exiba uma mensagem parabenizando-o por receber um abono de 10%, caso seja menor que 5000mil, exiba uma mensagem dizendo que ele receberá um abono de 3%.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

***
