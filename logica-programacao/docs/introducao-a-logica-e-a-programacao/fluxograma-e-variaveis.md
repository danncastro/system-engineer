---
description: >-
  Ferramenta utilizada para representar graficamente o algoritmo, isto é, a
  sequência lógica e coerente do fluxo de dados.
---

# Fluxograma e Variáveis

***

## <mark style="color:red;">O que é um Fluxograma?</mark>

Um fluxograma é uma representação visual de um processo ou algoritmo. Na lógica de programação, é uma ferramenta útil para planejar e entender a sequência de ações necessárias para resolver um problema ou realizar uma tarefa.

```bash
Início -> Entrada -> Processamento -> Saída -> Fim
```

Imagine que você está planejando uma viagem de carro de uma cidade para outra. Antes de sair, você geralmente planeja sua rota, certo? Você olha o mapa, identifica as estradas que vai seguir, onde fazer paradas, e assim por diante. Um fluxograma em programação é como esse mapa, mas para o seu código. Ele mostra o caminho que seu programa vai seguir, as decisões que ele vai tomar ao longo do caminho, e como todas as partes se conectam. É uma ferramenta útil para visualizar e planejar o funcionamento do seu programa antes de começar a escrever o código.

<figure><img src="../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

***

### <mark style="color:red;">Diagrama de Blocos</mark>

Um diagrama de blocos em um fluxograma de programação é uma representação visual das diferentes partes ou componentes de um algoritmo ou programa. Cada bloco no diagrama representa uma função, operação ou etapa específica do processo. Esses blocos são conectados por linhas que mostram a ordem em que as etapas devem ser executadas.

> _São tipos de blocos diferentes para representar cada tipo de ação ou método de um fluxograma, não é um padrão definitivo, mas abaixo temos um exemplo:_

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">Exemplo de diagrama de blocos  escritos de duas formas.</mark>

<figure><img src="../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">O que são variáveis?</mark>

São Espaço em memória do computador destinado a um dado que é alterado durante a execução do algoritmo.

> _Na programação, uma variável é um objeto (uma posição, frequentemente localizada na memória) capaz de reter e representar um valor ou expressão._

Variáveis são como "caixas" ou "contêineres" que armazenam dados em um programa de computador. Elas têm um nome único e um tipo de dados associado, como números, texto, booleanos (verdadeiro/falso), entre outros. As variáveis permitem que você armazene e manipule valores durante a execução de um programa.

Por exemplo, se você estiver escrevendo um programa para calcular a média de três números, você pode usar variáveis para armazenar esses números temporariamente:

```warpscript
Algoritmo calcularMedia
    // Definindo as variáveis
    numero1: inteiro
    numero2: inteiro
    numero3: inteiro
    media: real

    // Atribuindo valores às variáveis
    numero1 <- 10
    numero2 <- 15
    numero3 <- 20

    // Calculando a média
    media <- (numero1 + numero2 + numero3) / 3

    // Exibindo o resultado
    Escrever("A média dos números é:", media)
Fim Algoritmo
```

Neste pseudocódigo, as variáveis `numero1`, `numero2`, `numero3` e `media` são declaradas com seus tipos de dados correspondentes (inteiro para os números e real para a média). Em seguida, valores são atribuídos a essas variáveis e a média é calculada subtraindo pela quantidade de variaveis.

Variáveis são fundamentais na programação, pois permitem que você armazene dados dinâmicos e os manipule de acordo com a lógica do seu programa.

***

### <mark style="color:red;">Tipos de variáveis</mark>

Variáveis e constantes podem ser classificadas basicamente de quatro tipos:

<mark style="color:blue;">**Numéricas**</mark><mark style="color:blue;">:</mark>&#x20;

Variáveis que armazenam valores numéricos, como inteiros (números inteiros), reais (números com parte decimal) e até mesmo complexos (números complexos, geralmente encontrados em linguagens de programação mais avançadas).

```bash
Números inteiros:
0, 1, 5, 60, 800, … -58, -50, -49, 32, -10, -5
```

```bash
Números fracionários
5.95, 9.54, -8.8, -0.555 … 0, 1, 5, 50, 60,  800, -58, -50, -49, 32, -10, -5
```

<mark style="color:blue;">**Caracteres**</mark><mark style="color:blue;">:</mark>

Variáveis que armazenam caracteres individuais, como letras, números e símbolos. Por exemplo, 'a', '5', '?'.&#x20;

```bash
'Programação' 
'PROGRAMAÇÃO'
'KU*&NH53g'
'Fone: (xx)xxxx-xxxx'
'Rua lailaila, n°7'
```

<mark style="color:blue;">**Alfanuméricas**</mark><mark style="color:blue;">:</mark>&#x20;

Variáveis que podem armazenar tanto caracteres quanto números. Elas são usadas para representar palavras, frases ou combinações de letras e números. Por exemplo, "Olá mundo!", "123abc".

<mark style="color:blue;">**Lógicas**</mark><mark style="color:blue;">:</mark>&#x20;

Variáveis que armazenam valores lógicos, ou seja, verdadeiro (true) ou falso (false). Elas são usadas para controle de fluxo em expressões condicionais e estruturas de controle de decisão.

```bash
Verdadeiro ou Falso
True or False
```

***

### <mark style="color:red;">O que é uma constante?</mark>

Em programação, uma constante é um valor que não pode ser alterado durante a execução de um programa. Ao contrário das variáveis, cujos valores podem ser modificados ao longo do tempo, as constantes mantêm o mesmo valor durante toda a execução do programa.

> _São valores imutáveis e não são alterados durante a vida útil do programa._

As constantes são frequentemente usadas para representar valores fixos que são conhecidos antes da execução do programa e que não devem ser alterados. Por exemplo, em um programa de cálculo de área de um círculo, o valor de π (pi) pode ser representado como uma constante, pois é um valor fixo que não muda.

As constantes podem ser de diferentes tipos de dados, como numéricas, de texto ou lógicas, dependendo do contexto em que são usadas. Elas são úteis para tornar o código mais legível e manter a consistência dos valores ao longo do programa.

Em muitas linguagens de programação, as constantes são declaradas usando uma palavra-chave específica, como const ou final, seguida pelo nome da constante e seu valor. Por exemplo, em algumas linguagens de programação como em Python, podemos declarar uma constante para representar o valor de π da seguinte maneira:

```python
# Definindo uma constante para representar o valor de pi
PI = 3.14159

# Usando a constante para calcular a área de um círculo
raio = 5
area = PI * (raio ** 2)

# Exibindo o resultado
exiba ("A área do círculo é:", area)
```

Ao usar constantes em um programa, você pode evitar erros causados por tentativas de modificar valores que não devem ser alterados e tornar seu código mais fácil de entender e manter.

***

## <mark style="color:red;">Exercitando Fluxosgramas e Variáveis</mark>

{% embed url="http://flowgorithm.org/" %}

1. Vamos baixar o Flowgorithm e efetuar a criação do fluxograma para exibir a média de um aluno.

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

2. Além do valor de média, faça a soma de todas as notas e exiba na execução do programa.

<figure><img src="../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

***
