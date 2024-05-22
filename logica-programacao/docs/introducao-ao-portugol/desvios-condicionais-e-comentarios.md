# Desvios Condicionais e Comentários

***

## <mark style="color:red;">Utilização SE</mark>

Em Portugol, o desvio condicional "se" é utilizado para tomar decisões com base em condições específicas. Ele permite que o programa execute diferentes conjuntos de instruções dependendo se uma determinada condição é verdadeira ou falsa.

> É utilizada a palavra reservada "se", a condição a ser testada entre parenteses e as instruções que devem ser executadas entre chaves caso o desvio seja "Verdadeiro"

```
se (condição) então
    // conjunto de instruções a serem executadas se a condição for verdadeira
fimse
```

Aqui está uma breve explicação de como ele é utilizado:

#### <mark style="color:blue;">**Definição da Condição**</mark><mark style="color:blue;">:</mark>&#x20;

A condição é uma expressão lógica que avalia se algo é verdadeiro ou falso. Por exemplo, pode ser uma comparação entre variáveis, como "idade > 18", ou uma combinação de condições usando operadores lógicos, como "idade > 18 E sexo = 'Feminino'".

#### <mark style="color:blue;">**Execução Condicional**</mark><mark style="color:blue;">:</mark>&#x20;

Se a condição definida dentro do "se" for avaliada como verdadeira, o conjunto de instruções dentro do bloco "então" será executado. Caso contrário, o programa simplesmente ignora esse bloco e continua sua execução.

#### <mark style="color:blue;">**Fim do Desvio Condicional**</mark><mark style="color:blue;">:</mark>&#x20;

O comando "fimse" marca o final do bloco de código que está condicionalmente executando. É importante delimitar corretamente onde o desvio condicional termina para evitar erros de sintaxe.

### <mark style="color:red;">Exercitando o desvio condicional SE</mark>

```java
programa
{
	funcao inicio()
	{
		real nota1,nota2,nota3,nota4,media
		cadeia aluno

		escreva("Digite o nome do aluno: ")
		leia(aluno)
		escreva("Digite a nota 1: ")
		leia(nota1)
		escreva("Digite a nota 2: ")
		leia(nota2)
		escreva("Digite a nota 3: ")
		leia(nota3)
		escreva("Digite a nota 4: ")
		leia(nota4)

		media = (nota1+nota2+nota3+nota4)/4
		escreva("Sua média é: " + media)

		se(media>=7){
			escreva("\n" + "Parabéns!! Você foi aprovado")
		}
	}
}
```

<figure><img src="../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">Utilização SEnao</mark>

O "senão" é uma parte importante de estruturas de desvio condicional em linguagens de programação, incluindo o Portugol. Ele oferece uma alternativa a ser executada caso a condição especificada no "se" não seja verdadeira.&#x20;

> Imaginando o cenario em que a condição seja "falsa" um outro conjunto de comandos deve ser executado.

Aqui está uma explicação simples sobre como o "senão" é utilizado:

#### <mark style="color:blue;">**Execução Alternativa**</mark><mark style="color:blue;">:</mark>&#x20;

Quando uma condição dentro de um bloco "se" não é satisfeita (ou seja, é avaliada como falsa), o programa pode executar um conjunto alternativo de instruções especificado após o "senão".

#### <mark style="color:blue;">**Estrutura Básica**</mark><mark style="color:blue;">:</mark>

```plaintext
se (condição) então
    // conjunto de instruções a serem executadas se a condição for verdadeira
senão
    // conjunto de instruções a serem executadas se a condição não for verdadeira
fimse
```

#### <mark style="color:blue;">**Uso Prático**</mark><mark style="color:blue;">:</mark>

O "senão" é útil para lidar com casos em que há mais de uma possibilidade de resultado. Por exemplo, em um programa que verifica se um número é par, o "senão" pode lidar com o caso em que o número é ímpar.

Ele também pode ser aninhado dentro de outros desvios condicionais, permitindo múltiplas alternativas.

***

### <mark style="color:red;">Exercitando o desvio condicional SEnao</mark>

```java
programa
{
	funcao inicio()
	{
		real nota1,nota2,nota3,nota4,media
		cadeia aluno

		escreva("Digite o nome do aluno: ")
		leia(aluno)
		escreva("Digite a nota 1: ")
		leia(nota1)
		escreva("Digite a nota 2: ")
		leia(nota2)
		escreva("Digite a nota 3: ")
		leia(nota3)
		escreva("Digite a nota 4: ")
		leia(nota4)

		media = (nota1+nota2+nota3+nota4)/4
		escreva("Sua média é: " + media)

		se(media>=7){
			escreva("\n" + "Parabéns!! Você foi aprovado")
		}

		senao{
			escreva("\n" + "Infelizmente você foi reprovado")
		}
	}
}
```

<figure><img src="../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">Comentários</mark>

Comentários são trechos de texto que são ignorados pelo compilador e servem apenas para facilitar a compreensão do código pelos programadores. Eles são úteis para adicionar explicações, notas ou lembretes dentro do código-fonte.&#x20;

Aqui está uma explicação básica sobre como usar comentários em Portugol:

#### <mark style="color:blue;">**Comentários de Linha Única**</mark><mark style="color:blue;">:</mark>

São utilizados para adicionar comentários em apenas uma linha.

São iniciados pelo caractere de barra dupla "//".

Qualquer texto após "//" na mesma linha é considerado um comentário e será ignorado pelo compilador.

Exemplo:

```portugol
// Este é um comentário de linha única
```

#### <mark style="color:blue;">**Comentários de Múltiplas Linhas**</mark><mark style="color:blue;">:</mark>

São utilizados para adicionar comentários que abrangem várias linhas.

São iniciados pelo caractere de barra asterisco "/_" e terminados por asterisco barra "_/".

Todo o texto entre "/_" e "_/" será considerado um comentário e ignorado pelo compilador.

Exemplo:

```portugol
/*
Este é um exemplo de
comentário de várias linhas
*/
```

#### <mark style="color:blue;">**Propósito dos Comentários**</mark><mark style="color:blue;">:</mark>

Os comentários ajudam a explicar o que o código está fazendo, tornando-o mais compreensível para outros programadores e até para o próprio autor do código no futuro.

Eles podem fornecer informações sobre a lógica por trás de determinadas partes do código, suas finalidades e possíveis limitações.

***

### <mark style="color:red;">Exercitando os comentários</mark>

```java
//Função do algoritmo: Calcular a média aritmética
//Autor: Danniel Gutierres

programa
{	
	funcao inicio()
	{
		real nota1,nota2,nota3,nota4,media
		cadeia aluno

		escreva("Digite o nome do aluno: ")
		leia(aluno)
		escreva("Digite a nota 1: ")
		leia(nota1)
		escreva("Digite a nota 2: ")
		leia(nota2)
		escreva("Digite a nota 3: ")
		leia(nota3)
		escreva("Digite a nota 4: ")
		leia(nota4)

		media = (nota1+nota2+nota3+nota4)/4
		escreva("Sua média é: " + media)

		//Verifica se a média é maior ou igual a 7
		se(media>=7){
			escreva("\n" + "Parabéns!! Você foi aprovado")
		}

		//Caso a média seja menor que 7
		senao{
			escreva("\n" + "Infelizmente você foi reprovado")
		}
	}
}
```

***

## <mark style="color:red;">Utilização do Caso</mark>

O desvio condicional "caso" é uma estrutura em Portugol (e em outras linguagens de programação) que permite executar diferentes blocos de código com base no valor de uma expressão. Ele é semelhante ao "se-senão", mas é mais adequado quando há várias possibilidades distintas a serem consideradas.&#x20;

> O comando **caso** é similar aos comandos _**se**_ e _**senao**_, e reduz a complexidade na escolha de diversas opções. Apesar de suas similaridades com o _**se**_, ele possui algumas diferenças. Neste comando não é possível o uso de operadores lógicos, ele apenas trabalha com valores definidos.

Aqui está uma explicação simples sobre como usar o desvio condicional "caso" em Portugol:

#### <mark style="color:blue;">**Estrutura Básica**</mark><mark style="color:blue;">:</mark>

```portugol
caso (expressão)
    opção 1: // caso o valor da expressão seja igual a opção 1
        // conjunto de instruções
    opção 2: // caso o valor da expressão seja igual a opção 2
        // conjunto de instruções
    ... // mais opções podem ser adicionadas conforme necessário
    senão: // caso nenhuma das opções anteriores seja verdadeira
        // conjunto de instruções
fimcaso
```

#### <mark style="color:blue;">**Funcionamento**</mark><mark style="color:blue;">:</mark>

A expressão é avaliada e comparada com os valores de cada opção.

Se o valor da expressão corresponder a uma das opções, o bloco de instruções correspondente é executado.

Se nenhum dos valores de opção corresponder ao valor da expressão, o bloco de instruções dentro do "senão" é executado.

#### <mark style="color:blue;">**Uso Prático**</mark><mark style="color:blue;">:</mark>

O desvio condicional "caso" é útil quando há várias alternativas possíveis para o valor de uma expressão.

Ele torna o código mais legível e organizado, especialmente em situações em que há muitas condições para serem consideradas.

***

### <mark style="color:red;">Exercitando o desvio condicional caso</mark>

```java
//Programa de seleção de stream

programa 

        {
            funcao inicio()
            {
                escreva("Esolha uma das opções: [1-Netflix] [2-Amazon Prime] [3-HBO GO] [4-Sair do menu]\n")
                inteiro menu=0
                escreva ("\n" + "Digite uma das opções: ")
                leia (menu)

                escolha(menu)
                {
                    caso 1:
                    escreva ("OK! abrindo Netflix")
                    pare
                
                    caso 2:
                    escreva ("OK! abrindo Amazon Prime")
                    pare

                    caso 3:
                    escreva ("OK! abrindo HBO GO")
                    pare

                    caso 4:
                    escreva ("Saindo do menu ...")
                    pare

                    caso contrario:
                    escreva ("Nenhuma das opções escolhidas")
                    pare
                }
            }
        }
```

<figure><img src="../.gitbook/assets/image (30).png" alt=""><figcaption><p>Opção 1 selecionada</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption><p>Opção 3 selecionada</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (32).png" alt=""><figcaption><p>Opção 4 selecionada</p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (33).png" alt=""><figcaption><p>Opção invalida selecionada</p></figcaption></figure>

***
