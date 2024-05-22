---
description: >-
  É uma linguagem escrita e formal que especifica um conjunto de instruções e
  regras usadas para gerar programas (software).
---

# Linguagens de Programação

Um Software pode ser desenvolvido para rodar em um computador, dispositivo móvel ou em qualquer equipamento que permita sua execução.&#x20;

{% hint style="success" %}
O que é obvio para nós, certamente não é obvio para uma máquina, se queremos que ela faça algo devemos falar com ela, _**essa é a função da linguagem de programação, servir de meio para comunicação entre computadores e humanos.**_
{% endhint %}

***

## <mark style="color:red;">O que são Linguagens de programação</mark>

Linguagens de programação são conjuntos de regras e símbolos que os programadores usam para escrever instruções que um computador pode entender e executar. Imagine-as como idiomas que permitem que humanos e computadores se comuniquem. Essas linguagens são usadas para criar programas de software, que são conjuntos de instruções que dizem ao computador o que fazer.

Existem muitas linguagens de programação diferentes, cada uma com suas próprias regras e propósitos. Algumas são mais adequadas para certas tarefas do que outras. Por exemplo, linguagens como Python e JavaScript são frequentemente usadas para desenvolvimento web, enquanto linguagens como C++ e Java são populares para desenvolvimento de software de sistemas.

As linguagens de programação podem variar em complexidade, desde aquelas que são fáceis de aprender e entender, até as mais avançadas que exigem um conhecimento mais profundo de computação e lógica. No entanto, todas elas têm o mesmo objetivo: permitir que os programadores instruam os computadores a realizar tarefas específicas de maneira eficiente e precisa.

{% hint style="info" %}
As linguagens de programação são frequentemente divididas em dois tipos principais: alto nível e baixo nível.
{% endhint %}

***

### <mark style="color:red;">**Linguagens de Alto Nível**</mark>

As linguagens de alto nível são projetadas para serem mais próximas da linguagem humana, o que as torna mais fáceis de entender e usar.

Elas permitem que os programadores escrevam código de forma mais abstrata, focando nos objetivos da programação em vez de se preocupar com detalhes específicos da máquina.

Exemplos de linguagens de alto nível incluem:

> &#x20;_Python, Java, JavaScript e C#_

Essas linguagens geralmente oferecem recursos poderosos e uma ampla gama de bibliotecas que simplificam o desenvolvimento de software.

***

### <mark style="color:red;">**Linguagens de Baixo Nível**</mark><mark style="color:red;">:</mark>

As linguagens de baixo nível são mais próximas da linguagem de máquina e são mais difíceis de entender para os humanos.

Elas fornecem um maior nível de controle sobre o hardware do computador e geralmente são usadas para tarefas que exigem alta eficiência e desempenho.

Exemplos de linguagens de baixo nível incluem:

> _Assembly e linguagem de máquina._

Programar em linguagens de baixo nível requer um conhecimento mais profundo do funcionamento interno do computador e pode ser mais propenso a erros se não for feito com cuidado.

{% hint style="info" %}
As linguagens de programação podem ser divididas em duas categorias principais: compiladas e interpretadas. Essas categorias descrevem como o código fonte é processado e executado pelo computador.
{% endhint %}

***

### <mark style="color:red;">**Linguagens Compiladas**</mark><mark style="color:red;">:</mark>

É uma linguagem de programação em que o código fonte, é executado diretamente pelo sistema operacional ou pelo processador, após ser traduzido por meio de um processo chamado _**compilação**_.

Nas linguagens compiladas, o código fonte é traduzido integralmente para linguagem de máquina (código executável) antes da execução do programa.

Um programa chamado compilador é usado para traduzir o código fonte em linguagem de máquina.

Uma vez compilado, o programa pode ser executado repetidamente sem a necessidade de recompilação, a menos que haja alterações no código fonte.

Exemplos de linguagens compiladas incluem

> &#x20;_C, C++,_ VisualBasic, Delphi, C# _e Rust._

Linguagens compiladas tendem a ser mais eficientes em termos de desempenho, pois o código é otimizado antes da execução.

***

### <mark style="color:red;">**Linguagens Interpretadas**</mark><mark style="color:red;">:</mark>

É uma linguagem de programação em que o código fonte é executado por um programa de computador chamado **interpretador**, que em seguida é executado pelo sistema operacional ou processador.

Nas linguagens interpretadas, o código fonte é traduzido e executado linha por linha em tempo real por um programa chamado interpretador.

O interpretador lê cada linha do código fonte, traduz para instruções de linguagem de máquina e executa imediatamente.

Exemplos de linguagens interpretadas incluem&#x20;

> Python, JavaScript, PHP e Ruby.

Como o código é traduzido e executado sob demanda, as linguagens interpretadas geralmente são mais lentas que as compiladas, mas oferecem maior flexibilidade e facilidade de depuração.

***

## <mark style="color:red;">O que é o Portugol?</mark>

O Portugol é uma linguagem de programação simples e didática, criada para ensinar conceitos básicos de programação de forma mais acessível aos iniciantes. Ela é frequentemente utilizada em cursos introdutórios de programação, especialmente em contextos educacionais.

> É uma pseudolinguagem que permite ao leitor desenvolver algoritmos estruturados em português de forma simples e intuitiva, independentemente de linguagem de programação.Permite ao programador pensar no problema em si e não no equipamento que irá executar o algoritmo.

O principal objetivo do Portugol é ensinar os fundamentos da lógica de programação e algoritmos de uma maneira mais fácil de entender. Ela usa uma sintaxe próxima à linguagem humana, o que a torna mais amigável para quem está começando a aprender a programar.

Uma das características do Portugol é sua capacidade de representar algoritmos de forma visual, através de fluxogramas, o que ajuda os iniciantes a compreenderem melhor o funcionamento dos programas.

{% embed url="https://portugol.dev/" %}

#### <mark style="color:blue;">Exercitanto o Pseudocodigo em Portugol</mark>

```java
programa
{
	funcao inicio()
	{
		escreva("Olá Danniel Gutierres")
	}
}
```

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

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
		
		escreva("O aluno: " + aluno + " Obteve a média: " + media)
	}
}
```

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

***

### <mark style="color:red;">Exercicio de Pseudocodigo com Portugol</mark>

Defina 4 variaveis \[Janeiro, Fevereiro, Março e Abril] que receberá valores de vendas de um funcionario, defina uma variavel vendasTotais que receberá a soma de venda dessas 4 variaveis e exiba na tela a soma total de vendas e o valor da variavel vendas.

```java
programa
{
	
	funcao inicio()
	{
		real janeiro,fevereiro,marco,abril,vendas,vendasTotal
		cadeia nome

		escreva("Digite o nome do vendedor: ")
		leia(nome)	
		escreva("Digite a venda de Janeiro: ")
		leia(janeiro)
		escreva("Digite a venda de Fevereiro: ")
		leia(fevereiro)
		escreva("Digite a venda de Março: ")
		leia(marco)
		escreva("Digite a venda de Abril: ")
		leia(abril)

		vendasTotal = (janeiro+fevereiro+marco+abril)
		vendas = vendasTotal/4
		
		escreva("O vendedor: " + nome + " vendeu um total de: " + vendasTotal)
		escreva(". Sua média de venda é de: " + vendas)
	}
}
```

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

***
