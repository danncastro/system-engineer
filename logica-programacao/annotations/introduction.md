# **Lógica de Programação**

Significa apenas contextualizar a lógica na programação de computadores, buscando a melhor sequência de ações para solucionar um problema.

---

## **Algoritmo em Programação**

Sequência de passos lógicos para execução de uma tarefa comunicadas em alguma linguagem **Alto nível (Humano)**, **Baixo nível (Máquina)**, podendo ser simplificados ou com tomadas de decições entre sim e não, etc...

* Exemplo: ***Receita de bolo***

---

## **Formas de representar um Algoritmo**

**[Linguagem natual](*)**  
Solução usando passos descritivos;

**[Fluxograma](*)**  
Ferramenta utilizada para representar graficamente o algoritmo, isto é, a sequência lógica e coerente do fluxo de dados. Um tipo de diagrama e pode ser entendido como uma representação esquemática de um processo. Podemos entendê-lo, na prática, como a documentação dos passos necessários para a execução de um processo qualquer.

    Início -> Entrada -> Processamento -> Saída -> Fim

**[Pseudocódigo](*)**  
É uma forma genérica e mais próxima das linguagens de programaçao de escrever um algoritmo, utilizando uma linguagem simples (nativa, ou seja, em português a quem o escreve, de forma a ser entendida por qualquer pessoa).

---

## Inferência Lógica

Conclusão baseada em determinados dados, ou seja, é a consequência com base em premissas.

* Exemplo de Inferência:

    > Todos os homens são mortais
    >> Sócrates é um homem
    >>> Portanto, Sócrates é mortal.

---

## **Princípio da dedução, indução, metacognição e abstração**

**[Dedução](*)**  
Baseado em uma inferência, a comparação de premissas nos ajuda a **DEDUZIR** e afirmar uma lógica como correta ou errada.

**[Indução](*)**  
Baseado em uma inferência e na observação de um passado (histórico), somos **INDUZIDOS** a acreditar que a lógica está correta ou errada.

**[Metacognição](*)**  
Pensar como você pensa

**[Abstração](*)**  
Habilidade de concentrar aspectos essenciais de um contexto qualquer, ignorando características menos importantes ou acidentais

---

## **Linguagem de progamação**

É uma linguagem escrita e formal que especifica um conjunto de instruções e regras usadas para gerar programas (software).

* Um Software pode ser desenvolvido para rodar em um computador, dispositivo móvel ou em qualquer equipamento que permita sua execução. O que é obvio para nós, certamente não é obvio para uma máquina, se queremos que ela faça algo devemos falar com ela, ***essa é a função da linguagem de programação, servir de meio para comunicação entre computadores e humanos.***

### **Tipos de linguagem**

**[Alto nível](*)**  
São aquelas cuja sintaxe se aproxima mais da nossa linguagem e se distanciam mais da linguagem de máquina
> C\
PHP\
Javascript\
C#\
C++\
Python

**[Baixo nível](*)**  
São aquelas que se aproximam mais da linguagem de máquina. Essas linguagens são as que temos que ter conhecimento direto da arquitetura do computador para que possamos fazer algo.
> Asemble

**[Compiladas](*)**  
É uma linguagem de programação em que o código fonte, é executado diretamente pelo sistema operacional ou pelo processador, após ser traduzido por meio de um processo chamado ***compilação***.
> C#\
VisualBasic\
Delphi\
C++

**[Interpretadas](*)**  
É uma linguagem de programaçãoem que o código fonte é executado por um programa de computador chmado **interpretador**, que em seguida é executado pelo sistema operacional ou processador.
>JavaScript\
PHP\
Python

**[Portugol](*)**  
É uma pseudolinguagem que permite ao leitor desenvolver algoritmos estruturados em português de forma simples e intuitiva, independentemente de linguagem de programação.

* Pseudolinguagem que permite ao programador pensar no problema em si e não no equipamento que irá executar o algoritmo.

---

## **Variáveis**

São objetos que armazenarão os dados, esses devem ter um tipo definido. Na programação, uma variável é um objeto (uma posição, frequentemente localizada na memória) capaz de reter e representar um valor ou expressão. Espaço em  memória do computador destinado a um dado que é alterado durante a execução do algoritmo.

**[Regras sobre variáveis](*)**
> Nome da variável

* Primeira letra - **Não numérica**
* Não pode inicializar com caracteres e números
* Não pode conter espaços em branco
* Não é possivel a utilização de palavras reservadas

Uma boa pratica na declação de variaveis é utilizar **comelCase** onde a primeira letra se inicia com minúsculos e a segunda palavra com maiúsculo.

    primeiroNome, segundoNome

### **Tipos de Variáveis e Constantes**

Variáveis e constantes podem ser classificadas basicamente de quatro tipos:

> Constantes

* São valores imutáveis e não são alterados durante a vida útil do programa.

***Declação de constante***

    const pi=3,14
    const raio = número

**[Inteiros](*)**  
Números inteiros:
> 0, 1, 5, 60, 800, … -58, -50, -49, 32, -10, -5

**[Reais](*)**  
Números fracionários
> 5.95, 9.54, -8.8, -0.555 … 0, 1, 5, 50, 60,  800, -58, -50, -49, 32, -10, -5

**[Caracteres](*)**  
Letras não representadas por números

Exemplo:

    'Programação' 
    'PROGRAMAÇÃO'
    'KU*&NH53g'
    'Fone: (xx)xxxx-xxxx'
    'Rua lailaila, n°7'

**[Lógicos](*)**  
Valores boleanos
> Verdadeiro ou Falso
>> True or False

**[Alfanuméricos](*)**  
> Letras e numeros

---

## **Entrada e saída de dados**

**[Imput (Entrada de dados)](*)**  
No processo de execução do algoritmo, muitas das vezes os dados utilizados são inseridos em tempo de execução, não estáticos, e essa inserção é o imput para que o algoritmo funcione conforme o desejado.

**[Output (Saída de dados)](*)**  
Uma vez que processamos os dados dentro do algoritmo, precisamos mostrar o resultado para o usuário.

---

## **Tipos de estruturas de controle**

**[Sequencial](*)**  
Representam a execução das ações de um algoritmo de forma encadeada.

**[Tomada de Decisão](*)**  
Quando o programa e escrito, geralmente ocorre a necessidade de decidir o que fazer dependendo de alguma condição encontrada durante a execução.

**[Condicional](*)**  
Comandos de decisão, em portugol utilizada a palavra reservada ***se***, a condição a ser testada entre parenteses e as instruções que devem ser executadas entre chaves, sejam ***verdadeiras***

    se (media >= 7){
        escreva("Parabéns!! Você foi aprovado!!")
    }

Se a condição for ***falsa*** um outro conjunto de comandos de ser executado, esse é o ***se-senao***
    se (media >=7){
        escreva("Parabéns!! Você foi aprovado!!")
    }
    senao {
        escreva("Infelizmente você foi reprovado!!")
    }

O comando **caso** é similar aos comandos ***se*** e ***senao***, e reduz a complexidade na escolha de diversas opções. Apesar de suas similaridades com o ***se***, ele possui algumas diferenças.

* Neste comando não é possível o uso de operadores lógicos, ele apenas trabalha com valores definidos.

programa //Programa de seleção de stream

        {
        
            funcao inicio()
            {
                escreva("Esolha uma das opções: [1-Netflix] [2-Amazon Prime] [3-HBO GO] [4-Sair do menu]\n")
                inteiro menu=0
                escreva ("Digite uma das opções: ")leia (menu)

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

E por ultimo temos a opção **escolha**.

**[Repetição](*)**  
Repetem uma ou mais ações caso uma condição estiver sendo satisfeita. Dentro da lógica de programação é uma estrutura que permite executar mais de uma vez o mesmo comando ou conjunto de comandos, de acordo com uma condição ou com um ***contador***.
> Para...Faça, Enquanto...Faça, Repita...até.

programa //Tabuada do 9

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

---

## **Operações Lógicas**

As operações lógicas são os fluxos que definimos caso um evento ocorra. Os fluxos ocorrem nas nossas proposiões. Preposições são um conjunto de palavras ou símbolos que exprimem um pensamento de sentido completo, ou seja, afirmam fatos. Exemplo: Brasília é capital do Brasil.

### **Tipos de Operações lógicas**

**[Negação](*)**  
Na lógica usamos o símbolo negação (~) pra negar uma preposição.

**[Conjunção](*)**  
O símbolo circunflexo (&&) é o símbolo da conjunção, que somente temos uma verdade quando ambos os valores são verdadeiros.

**[Disjunção](*)**
O Símbolo (v) é o quem reprenta a disjunção, onde se apenas um dos operadores for verdadeiro o resultado é verdadeiro.

**[Disjunção exclusiva](*)**  
O (||) é o símbolo que represeta a disjunção excluisva. Apenas uma preposição pode ser verdadeira.

**[Condicional](*)**  
O símbolo (->) condicional, diz que se uma preposição ocorre então temos um resultado.

**[Bicondicional](*)**  
O Símbolo ([<->]) bicondicional, uma preposição é dependente de outra.

### **Operadores aritméticos**

Nós temos operações básicas da matemática para nos ajudar a manipular os nossos dados contidos em nossas variáveis. São expressões que utilizam operadores aritméticos e funções aritméticas envolvendo constantes e variáveis.

|     Valor       |  Representação  |
| --------------- | :-------------: |
| Soma            |        +        |
| Subtração       |        -        |
| Multiplicação   |        *        |
| Divisão normal  |        /        |
| Divisão inteira |        \        |
| Exponenciação   |        ^        |
| Potenciação     |        ^^       |
| Porcentagem     |        %        |
| Modulo ou resto |      x % y      |

### **Expressões literais**

São expressões com constantes e/ou variáveis que tem como resultado valores literais. Utilizaremos expressões literais na atribuição de valor para uma variável ou constante.

    nome="José da Silva"
    nome <- "José da Silva"
    media=(nota1+nota2+nota3+nota4)/4

|Variável | atribuição   |    Procedimento  |
|-------- | :----------: | :--------------- |
|  A B C  |  A = 2       |  Armazena 2 em A |
|         |  B = A + 3   |    Soma A + 3    |
|         |  C = A + B   |    Soma A + B    |

### **Operadores relacionais**

Os operadores relacionais são um grupo de operadores que tem como função comparar dados. São explessões compostas por outras expressões ou variáveis numéricas com operadores relacionais. Expressões relacionais retornam valores lógicos (***verdadeiro / falso***).

| Símbolo |     Operador     |
| ------- | :--------------: |
|    >    |     Maior que    |
|    >=   |  Maior ou igual  |
|    <    |     Menor que    |
|    <=   |  Menor ou igual  |
|    ==   |     Igualdade    |
|    !=   |    Diferente de  |

### **Operadores de concatenação**

Operador de concatenação é bastante utilizado quando queremos mostrar um resultado/informação na tela para o usuário acompanhado de um texto explicativo.

* Termo utilizado em computação para designar a operação de unir o conteúdo de duas strings Strings é uma sequência de caracteres.

* Agrupamento de duas ou mais células que, incluindo fórmulas, textos ou outras informações contidas no seu interior, dá origem a um ***único resultado.***.

        escreval(nome, " : ", numero)

---

## Matrizes & Vetores

**[Matriz](*)**  
É uma coleção de variáveis de mesmo tipo, acessíveis com um único nome e armazenados contiguamente na memória.

**[Vetores](*)**  
São matrizes de uma só dimensão. A individualização de cada variável de um vetor é feita através do uso de [*índices*].

    cadeia Vetor[5]; //declara um vetor de 5 posições
    cadeia Matriz[5][3]; //declara uma matriz de 5 linhas 3 colunas

    cadeia frutas[4];
    frutas[0]="Maçã"
    frutas[1]="Pera"
    frutas[2]="Uva"
    frutas[3]="Melão"
    escreva(frutas[2])

    cadeia cesta[][] = {{"Maçã","100"},{"Pera","200"},{"Melão","300"}}
    escreva ("Fruta: " + cesta [0][0] + "Quantidade: " + cesta [0][1])
