# Estrutura de Repetição

***

## <mark style="color:red;">Definição</mark>

As estruturas de repetição são fundamentais na programação, permitindo que um conjunto de instruções seja executado repetidamente com base em uma condição específica. Essa capacidade é essencial para automatizar tarefas repetitivas e lidar com conjuntos de dados de maneira eficiente.

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

Existem geralmente três tipos principais de estruturas de repetição:

***

### <mark style="color:red;">**While**</mark>

O loop "while" repete um bloco de código enquanto uma condição especificada for verdadeira. Isso significa que o bloco de código dentro do loop é executado repetidamente até que a condição se torne falsa.

Exemplo em Python:

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

Neste exemplo, o código imprimirá os números de 0 a 4.

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

***

### <mark style="color:red;">**For**</mark>

O loop "for" é usado para iterar sobre uma sequência (como uma lista, tupla, conjunto ou string) e executa um bloco de código uma vez para cada item na sequência.

Exemplo em Python:

```python
for i in range(5):
    print(i)
```

Este código também imprimirá os números de 0 a 4.

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

***

### <mark style="color:red;">**Do-While**</mark> <mark style="color:red;"></mark><mark style="color:red;">(em algumas linguagens)</mark>

Este é um loop menos comum, onde o bloco de código é executado pelo menos uma vez, e então a condição é verificada. Se a condição for verdadeira, o bloco de código é repetido. Se for falsa, o loop é encerrado.

Exemplo em C:

```c
int contador = 0;
do {
    printf("%d\n", contador);
    contador++;
} while (contador < 5);
```

Neste exemplo, mesmo que a condição seja falsa, o bloco de código será executado pelo menos uma vez.

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Ao usar essas estruturas de repetição, é importante garantir que a condição de parada seja definida corretamente para evitar loops infinitos. Além disso, é possível interromper a execução de um loop antes da conclusão normal usando declarações como "break" (para sair do loop completamente) ou "continue" (para pular a iteração atual e ir para a próxima).
{% endhint %}

***
