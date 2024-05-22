---
description: >-
  Dentro da lógica de programação é uma estrutura que permite executar mais de
  uma vez o mesmo comando ou conjunto de comandos, de acordo com uma condição ou
  com um contador.
---

# Laços de repetição

***

## <mark style="color:red;">Definição</mark>

Um laço de repetição, também conhecido como **loop**, é uma estrutura de controle em programação que permite executar repetidamente um bloco de código até que uma condição especificada seja atendida. Ele é utilizado quando você precisa executar uma determinada tarefa várias vezes de forma automática, sem precisar repetir o mesmo código manualmente.&#x20;

Aqui está uma explicação simples sobre o conceito de laço de repetição:

#### <mark style="color:blue;">**Estrutura Básica**</mark><mark style="color:blue;">:</mark>

Um laço de repetição consiste em três partes principais: inicialização, condição e atualização.

O bloco de código dentro do laço é repetido enquanto a condição especificada for verdadeira.

Quando a condição se torna falsa, o laço é encerrado e a execução continua após o bloco do loop.

#### <mark style="color:blue;">**Tipos Comuns de Laços**</mark><mark style="color:blue;">:</mark>

**Laço "para"**: Executa um bloco de código um número específico de vezes.

**Laço "enquanto"**: Executa um bloco de código enquanto uma condição específica é verdadeira.

**Laço "faça enquanto"**: Similar ao "enquanto", mas garante que o bloco de código é executado pelo menos uma vez, mesmo que a condição seja falsa desde o início.

#### <mark style="color:blue;">**Uso Prático**</mark><mark style="color:blue;">:</mark>

Os loops são úteis para automatizar tarefas repetitivas, como processamento de listas de dados, cálculos iterativos e interação com o usuário.

Eles ajudam a tornar o código mais eficiente e legível, evitando a repetição desnecessária de instruções.

***

## <mark style="color:red;">Exercitando o Laço de Repetição</mark>

```java
//Tabuada do 9

programa 

        {
            funcao inicio()
            {
                inteiro contador, limite, resultado
                contador = 0
                limite = 10
                faca
                {
                    resultado = 9 * contador
                    escreva ("9 X " + contador + " = " + resultado + "\n")
                    contador ++ //contador = contador +1
                }enquanto (contador <= limite)
            }
        }
```

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

1. Faça um codigo que solicite ao usuário qual a tabuada que deseja ser exibida.

```java
//Tabuada do X

programa 
        {
            funcao inicio()
            {
                inteiro contador, limite, resultado, tabuada
                contador = 0
                limite = 10

                escreva("Qual tabuada deseja resolver?: ")
                leia(tabuada)
               
                faca
                {
                    resultado = 9 * contador
                    escreva (tabuada + " X " + contador + " = " + resultado + "\n")
                    contador ++ //contador = contador +1
                }enquanto (contador <= limite)
            }
        }
```

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

***
