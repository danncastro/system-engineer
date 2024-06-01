# Análises de Código

***

## <mark style="color:red;">Overview</mark>

Quando um computador analisa o código-fonte de um programa, ele segue um processo geralmente conhecido como "compilação" ou "interpretação", dependendo da linguagem de programação e do ambiente de execução. Vou explicar cada processo:

***

### <mark style="color:red;">**Compilação**</mark>

No processo de compilação, o código-fonte é traduzido integralmente para uma linguagem de baixo nível, geralmente linguagem de máquina ou código intermediário.

<figure><img src="../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

O compilador analisa o código-fonte em etapas, como análise léxica (quebra o código em tokens), análise sintática (verifica a estrutura gramatical correta) e análise semântica (garante que as instruções tenham significado válido).

<figure><img src="../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

Após a análise, o compilador gera um arquivo executável ou código intermediário, que pode ser executado diretamente pela máquina ou por uma máquina virtual específica.

<figure><img src="../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

Exemplos de linguagens compiladas incluem C, C++, Java (compilada para bytecode) e Rust.

***

### <mark style="color:red;">**Interpretação**</mark>

No processo de interpretação, o código-fonte é lido e executado linha por linha por um programa chamado "interpretador".

O interpretador analisa cada linha do código-fonte, converte-a em instruções de baixo nível e executa essas instruções diretamente.

Como não há um passo de compilação completo, a interpretação pode ser mais lenta em comparação com a execução de código compilado, mas oferece vantagens em termos de portabilidade e facilidade de depuração.

Exemplos de linguagens interpretadas incluem Python, JavaScript e Ruby.

***

{% hint style="info" %}
Além desses métodos principais, há também abordagens híbridas, como a compilação just-in-time (JIT), onde o código é compilado durante a execução, proporcionando um equilíbrio entre desempenho e flexibilidade.
{% endhint %}

Independentemente do método utilizado, o objetivo final é transformar o código-fonte em instruções que o computador possa entender e executar para realizar as tarefas especificadas pelo programa.

***
