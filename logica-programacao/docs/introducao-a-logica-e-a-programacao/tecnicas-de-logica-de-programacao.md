# Técnicas de Lógica de Programação

***

## <mark style="color:red;">**Técnica Linear**</mark>

A técnica linear é uma abordagem direta para resolver problemas, onde as instruções são executadas sequencialmente, uma após a outra, sem desvios ou ramificações. É como seguir uma linha reta de execução, onde cada etapa depende da anterior e leva à próxima.

***

### <mark style="color:red;">**Características da Técnica Linear:**</mark>

#### <mark style="color:blue;">**Sequencialidade**</mark>

As instruções são executadas em uma ordem específica, uma após a outra, sem saltos ou desvios para outras partes do código.

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Processamento Direto**</mark>

Cada instrução é processada conforme é encontrada no código, sem a necessidade de decisões complexas ou iterações.

#### <mark style="color:blue;">**Facilidade de Compreensão**</mark>

A técnica linear é fácil de entender e seguir, pois segue uma progressão lógica e direta de instruções.

#### <mark style="color:blue;">**Limitações em Complexidade**</mark>

Embora seja eficaz para resolver problemas simples e diretos, a técnica linear pode tornar-se complicada e ineficiente para problemas mais complexos que exigem decisões condicionais ou iterações.

***

## <mark style="color:red;">Técnica Estruturada</mark>

A técnica estruturada em lógica, também conhecida como programação estruturada, é um paradigma de programação que visa criar algoritmos de forma clara, organizada e eficiente. Em vez de escrever um programa como uma sequência linear de instruções, na programação estruturada, o programa é dividido em estruturas lógicas bem definidas, como sequência, seleção e iteração.

#### <mark style="color:blue;">**Sequência**</mark>

As instruções são executadas em uma ordem específica, uma após a outra. Isso é semelhante à forma como as tarefas são realizadas na vida cotidiana. Por exemplo, para fazer uma omelete, primeiro quebramos os ovos, os batemos, os fritamos e depois os servimos.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Seleção**</mark>

Também conhecida como estrutura de decisão, permite que o programa tome diferentes caminhos dependendo de uma condição específica. Por exemplo, em um programa de controle de acesso, se a senha inserida estiver correta, o usuário terá acesso; caso contrário, será negado o acesso.

#### <mark style="color:blue;">**Iteração**</mark>

Também chamada de loops, permite que um conjunto de instruções seja repetido várias vezes até que uma condição seja atendida. Por exemplo, um loop pode ser usado para imprimir os números de 1 a 10, executando a instrução de impressão repetidamente até que o número 10 seja atingido.

> _A programação estruturada promove o uso de três tipos principais de estruturas de controle de fluxo: sequencial, seleção e iteração, e desencoraja o uso de estruturas de controle de fluxo complexas, como o desvio incondicional (goto), que podem tornar o código difícil de entender e dar manutenção._

Um dos princípios fundamentais da programação estruturada é o "princípio da única entrada, única saída" (Single Entry, Single Exit - SESE), que significa que cada bloco de código deve ter apenas um ponto de entrada e um ponto de saída. Isso torna o código mais fácil de entender e depurar.

Ao adotar a programação estruturada, os programadores podem escrever código mais legível, fácil de entender, testar e manter. Isso resulta em programas mais robustos e menos propensos a erros, facilitando a colaboração entre diferentes desenvolvedores em um projeto de software.

***

## <mark style="color:red;">Técnica Modular</mark>&#x20;

A técnica modular é uma abordagem de design de software que envolve dividir um programa em partes menores e mais gerenciáveis, chamadas de módulos ou funções. Cada módulo é responsável por realizar uma tarefa específica e pode ser desenvolvido e testado independentemente dos outros módulos do programa. Essa abordagem facilita o desenvolvimento, manutenção e depuração de software, tornando-o mais organizado, flexível e reutilizável.

Existem várias vantagens em utilizar a técnica modular:

#### <mark style="color:blue;">**Divisão de tarefas**</mark>

Ao dividir o programa em módulos, cada módulo é responsável por uma única tarefa. Isso torna o programa mais fácil de entender, pois cada parte concentra-se em uma funcionalidade específica.

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

#### <mark style="color:blue;">**Reutilização de código**</mark>

Os módulos podem ser reutilizados em diferentes partes do programa ou até mesmo em projetos diferentes, economizando tempo e esforço de desenvolvimento.

#### <mark style="color:blue;">**Facilidade de manutenção**</mark>

Com a técnica modular, é mais fácil localizar e corrigir bugs, pois as partes do programa são menores e mais isoladas. Além disso, ao fazer uma alteração em um módulo, geralmente é necessário alterar apenas esse módulo, sem afetar o restante do programa.

#### <mark style="color:blue;">**Desenvolvimento colaborativo**</mark>

Vários desenvolvedores podem trabalhar em diferentes módulos simultaneamente, facilitando o desenvolvimento colaborativo de software.

#### <mark style="color:blue;">**Testabilidade**</mark>

Os módulos podem ser testados individualmente, o que simplifica o processo de teste e garante que cada parte do programa funcione conforme o esperado.

> _Para implementar a técnica modular, os programadores geralmente utilizam conceitos como funções, classes e métodos, dependendo da linguagem de programação. Por exemplo, em linguagens como Python, C++ ou Java, as funções são usadas para encapsular blocos de código que realizam uma tarefa específica. Em linguagens orientadas a objetos, como Java e C++, as classes são utilizadas para agrupar dados e métodos relacionados em um único objeto, facilitando a modularidade e a reutilização de código._

***
