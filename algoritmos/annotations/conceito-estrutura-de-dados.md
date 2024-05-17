## Estrutura de dados
- É uma estrutura organizada de dados na memória de um computador ou em qualquer dispositivo de armazenamento, de forma que os dados possam ser utilizados de forma correta.
- Essas estruturas encontram muitas aplicações no desenvolvimento de sistemas, sendo que algumas são altamente especializadas e utilizadas em tarefas específicas.
- Usando as estruturas adequadas através de algoritmos, podemos trabalhar com uma grande quantidade de dados, como aplicações em bancos de dados ou serviços de busca.

---
#### Algoritmo
- Um algoritmo é um conjunto de instruções estruturadas e ordenadas, seu objetivo é realizar uma tarefa ou operações específicas.
- Os algoritmos são utilizados para manipular dados nas estruturas de várias formas como por exemplo:
***[inserir], [excluir], [procurar], [ordenar_dados]***
- Em uma estrutura de dados devemos saber como realizar um determinado conjunto de operações básicas, como por exemplo:
    - ##### Iserir dados
    - ##### Excluir dados
    - ##### Localizar um elemento
    - ##### Percorrer todos os itens constituintes da estrutura para visualização
    - ##### Classificar, que se resume em colocar os itens de dados em uma determinada ordem *  (numérica, alfabética, etc...)*

---
#### Principais estruturas de dados
- ###### Vetores e Matrizes [Arrays]
    - Vetores e Matrizes ou Arrays são estruturas de dados simples que podem auxiliar quando há muitas variáveis do mesmo tipo em um algoritmo.
    - ***Vetor ou Array uni-dimensional*** é uma variável que armazena várias variáveis do mesmo tipo.
        - O vetor é uma estrutura de dados indexada, que pode armazenar uma determinada quantidade de valores do mesmo tipo.
    - ***Matriz ou Array multi-dimensional*** é um vetor de vetores.
        - Uma matriz é um vetor que possui duas ou mais dimensões.

- ###### Registros
    - É uma estrutura que fornece um formato especializado para armazenar informações em memória.
    - Enquanto ***Arrays*** nos permite armazenar vários dados de um único tipo de dados, o recurso ***Registro*** nos permite armazenar mais de um tipo de dado.
        - Exemplos que constituem o registro de um cliente:
        
            |               |  |
            | ------------- | -|
            | CPF           |  |
            | Nome          |  |
            | Endereço      |  |
            | Contato       |  |
    - Toda  estrutura de registro tem um nome (ex: livro), e seus campos podem ser acessados por meio do uso do operador ponto **(.)**. Por exemplo, para acessar o preço de um livro, poderíamos utilizar a seguinte declaração:
        ~~~
        livro.preço
        ~~~
    - Exemplo de um programa que declara e armazenai informações de três livros:
        ~~~
        ALGORITMO
        //declaração do tipo de dado
        tipo
            estrutura_livro = registro
                nome = caracter
                preco = real
                pagina = inteiro
            fimregistro

        //declaração de variáveis
            i inteiro
            livro array [1..3] de estrutura_livro

            escreva("Entre com os nomes, preços e números de páginas de três livros")
            para i de 1 ate 3 faca //leitura dos dados
                leia(livro[i].nome, livro.[i].preco, livro.[i].paginas)
            fimpara
        FIMALGORITMO

- ###### Lista
    - Estrutura de dados que armazena os dados de determinado tipo em uma ordem específica.
    - A diferença entre listas e arrays é a de que as listars possuem tamanho ajustável, enquanto arrays possuem tamanho fixo
    - Existem dois tipos de listas:
        - ***Ligadas*** - Nesse tipo de lista, existem os nós onde cada um dos nós conhecem o valor que está sendo armazenado em seu interior além de conhecer o elemento posterior a ele: Por isso ela é chamada de "*lista ligada*", pois os nós são amarrados com essa indicação de qual é o próximo nó.
        - ***Duplamente ligadas*** - Constituem uma variação das listas ligadas, a grande diferença das listas duplamente ligada para as listas ligadas é que elas são bidirecionais. Naturalmente, não conseguimos "*andar para trás*" em listas ligadas, pois os nós de uma lista ligada somente quem é o próximo elemento. Nas listas duplamente ligadas, os nós sabem quem é o próximo elemento e também quem é o elemento anterior, o que permite a navegação reversa.

- ###### Pilha
    -  Estrutura de dados que serve como uma coleção de elementos, e permite o acesso a somente um item de dados armazenado.
    - O acesso aos itens de uma pilha é restrito - somente um item pode ser lido ou removido por vez.
    - Tipos de pilhas:
        - **LIFO ou UEPS** - A estrutura do tipo PILHA LIFO *(Last In First Out)* ou UEPS *(Último que Entra Primeiro que Sai)*, apresenta o seguinte critério: *O primeiro elemento a ser retirado é o último que tiver sido inserido*.
        - **FIFO ou PEPS** - A estrutura do tipo PILHA FIFO *(First In First Out)* ou PEPS (Primeiro que Entra Primeiro que Sai), apresenta o seguinte critério: *O primeiro elemento a ser retirado é o primeiro que tiver sido inserido.*

- ###### Fila
    - Admite remoção de elementos e inserção de novos sujeita a seguinte regra de operação:
        - O elemento removido é o que está na estrutura ha mais tempo ou seja, o primeiro objeto inserido na fila é também o primeiro a ser removido seguindo o conceito *FIFO*.

- ###### Árvore
    - É uma estrutura de dados que organiza seus elementos de forma hierárquica, onde existe um elemento que fica no topo da árvore, chamado de *raiz* e existem os elementos subordinados a ele, que são chamados de nós ou folhas.

- ###### Tabela Hash
    - Uma tabela hash, de dispersão ou espalhamento é uma estrutura de dados especial, que associa chaves de pesquisa a valores.
    - ***Hashing***: Uma tabela hash é uma generalização da idéia de array, porém utiliza uma função denominada *Hashing* para espelhar os elementos, fazendo com que os mesmos fiquem de forma não ordenada dentro do "*array*" que define a tabela.
    - ***Porque espelhar ?***
    A tabela hash permite a associação de "*valores*" a "*chaves*"
        - **Valores :** É a posição ou índice onde o elemento se encontra.
        - **Chaves :** Parte da informação que compõe o elemento a ser manipulado.
        - Espalhar facilita a busca na estrutura de dados, pois a partir de uma chave podemos acessar de forma rápida uma posição do "*array*".

- ###### Grafos
- São estruturas que permitem programar a relação entre objetos.
    - Os objetos são vértices ou "*nós*" do grafo
    - Os  relacionamentos são arestas