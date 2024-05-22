# Matrizes e Vetores

***

## <mark style="color:red;">**Matriz**</mark>

É uma coleção de variáveis de mesmo tipo, acessíveis com um único nome e armazenados contiguamente na memória.

Uma matriz é uma coleção de elementos dispostos em linhas e colunas. É basicamente uma tabela de valores. Os elementos de uma matriz são acessados através de suas coordenadas de linha e coluna. Matrizes podem ter várias dimensões, mas a mais comum é a bidimensional, que possui linhas e colunas.

Por exemplo, uma matriz $$2×32×3$$2 × 3 (2 linhas e 3 colunas) de números inteiros pode ser representada assim:

```
matriz=[123]
       [456]
```

***

## <mark style="color:red;">**Vetores**</mark>

São matrizes de uma só dimensão. A individualização de cada variável de um vetor é feita através do uso de \[_índices_].

Um vetor é uma coleção ordenada de elementos. Em termos simples, é uma lista de valores que são armazenados consecutivamente na memória. Cada elemento em um vetor é identificado por um índice que indica sua posição na sequência. Os vetores podem ser unidimensionais, ou seja, possuem apenas uma linha ou uma coluna.

Por exemplo, um vetor de números inteiros pode ser representado assim:&#x20;

```
vetor = [1,2,3,4,5]
```

***

### <mark style="color:red;">**Uso Prático:**</mark>

Os vetores são frequentemente utilizados para armazenar uma lista de elementos do mesmo tipo, como números, nomes ou qualquer outra informação.

As matrizes são utilizadas para representar dados tabulares, como planilhas ou imagens, onde os elementos estão organizados em linhas e colunas.

```java
programa
{	
	funcao inicio()
	{
		cadeia frutas[4]
		inteiro contador =  0

		frutas[0]="Maçã"
		frutas[1]="Pera"
		frutas[2]="Uva"
		frutas[3]="Java"

		faca{
			escreva(frutas[contador] + "\n")
			contador++

		}enquanto (contador <=3)
	}
}
```

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">Exercitando Matrizes e Vetores</mark>

```java
programa
{
	funcao inicio()
	{
		inteiro contador =  0
		cadeia cesta[][]={{"Pera","100"},{"Java","200"},{"Maça","900"}, {"Uva","89"}}

		faca{
			
			escreva("Produto: " + cesta[contador][0] + " Quantidade: " + cesta[contador][1] + "\n")
			contador++

		}enquanto(contador<=3)

	}
}
```

<figure><img src="../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

***

## <mark style="color:red;">Exercício Final</mark>

Crie uma matriz para armazenar e exibir as seguintes informações

| Nome     | Cidade         | Telefone      |
| -------- | -------------- | ------------- |
| Danniel  | Rio de Janeiro | (11)9999-8888 |
| Isabella | São Paulo      | (21)8888-9999 |
| Isinha   | Santos         | (13)9898-8989 |

```java
programa
{
	funcao inicio()
	{
		inteiro contador =  0
		cadeia cadastro[][]={{"Danniel","Rio de Janeiro", "(11)9999-8888"},{"Isabella","São Paulo", "(21)8888-9999"},{"Isinha","Santos","(13)9898-8989"}}

		faca{		
			escreva("Nome: " + cadastro[contador][0] + "\n" + " Cidade: " + cadastro[contador][1] + "\n" + "Telefone: " + cadastro[contador][2] + "\n")
			contador++
		}enquanto(contador<=2)
	}
}
```

<figure><img src="../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

***
