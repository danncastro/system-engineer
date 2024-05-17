# JavaScript

## **W3S**

[**JavaScript Tutorial**](https://www.w3schools.com/js/default.asp)

***

## Instalando requisitos

[**nodejs**](https://nodejs.org/en)

```bash
sudo apt install node js
```

***

## Variaveis

Sempre que declaramos uma variável estamos reservando um espaço de memória no computador, uma variável serve como um nome, um endereço, para esse espaço de memória no computador.

Outra forma de chamar as variáveis textuais é chamá-las de strings.

Sobrescrever uma variável significa mudar o conteúdo dela e para isso precisamos atribuir com o = o novo valor que desejamos, mas só podemos fazer isso em variáveis declaradas sem o const

### Tipos de declação

*   **const**

    **constant** é um tipo de variável que não pode ser modificada uma vez que sua atribuição original foi feita.
*   **let**

    Permite mudança, existem variáveis que devem ter um estado inconstante, e neste caso usamos o **let** para defini-las, como por exemplo um contador que varia de números.

**REPL**

### Descrições de erros

* **ReferenceError**
* **TypeError**
* **SyntaxError**

Podemos salvar valores dentro de variáveis. Esses valores ficam salvos dentro da memória do computador e podem ser acessados em outros lugares do nosso código.

Quando colocamos algo entre aspas o interpretador do JS entende aquilo como sendo um texto literal.

```bash
const nome = "Lais";
console.log("nome");
```

```bash
nome
```

JS é case sensitive

***

## Operações aritmeticas

Conversão de tipos

**parceInt**\
**parseFloat**

Falha na identificação do tipo de variavel

**Not a Number**

Precedencia de operações

## Operadores lógicos

Os operadores lógicos devem ter no lado esquerdo e direito uma expressão booleana.

```javascript
if (idade > 18 && idade < 65)
{

}
```

**OR = ||**\
**AND = &&**

***

## Elementos

Na contagem de indices de uma lista se considera a posição **"0"** de maneira implícita.

**new Array**\
Cria uma nova lista

**.push**\
Cria um novo item dentro de uma lista

**.splice**\
Deleta um item da lista

**indices**\
Possibilita imprimir apenas um item especifico de uma lista, pra acessar um elemento especifico podemos chamar o nome dessa lista seguido de colchetes com o index desse elemento. ex: lista\[2], lembrando que listas sempre começam a contagem de elementos a partir do 0 então o index 2 mostra o terceiro elemento da lista.

```javascript
console.log(lista[2]);
```

***

## Condicionais

**if (condição) {ação}**\
**else if {true or false}**\
**else {false}**

*   Exemplo\
    João está criando uma aplicação para calcular o IR a partir do salário. Ele olhou na tabela de IRPF e implementou as regras para 15% e 22.5%:

    ```bash
    if(salario < 2600.0) {
      console.log("A sua aliquota é de 15%");
      console.log("Você pode deduzir até R$ 350");
    }         
    else if(salario < 3750.0) {
      console.log("A sua aliquota é de 22,5%");
      console.log("Você pode deduzir até R$ 636");
    }
    ```

***

## Loops

O while sempre precisará de uma expressão condicional que definirá quando o laço deve ser interrompido, lembre-se, essa expressão condicional precisará ser informada dentro dos parênteses do while e pode ainda utilizar qualquer um dos operadores de comparação e operadores lógicos.

Na expressão condicional do while é possível utilizar qualquer operador de comparação (< \[menor], > \[maior], <= \[menor ou igual], >= \[maior ou igual], == \[igual a] e != \[diferente de]) e qualquer operador lógico (&& \[and], || \[ou]). Todos os operadores de comparação e lógicos são válidos na expressão condicional do while

Ao trabalharmos com laços de repetição é comum iterarmos dentro desse laço até que a condição de saída seja atingida

**while**

```javascript
while(contador<3){
    if(listaDeDestinos[contador] == destino){
        destinoExiste = true;
        break;
    }
    contador += 1;
}
```

**for**\
Para o caso do for, a contagem deverá ser dividida em três partes: precisaremos inicializar o contador , colocar sua condição ( no casao, < 3 ) e por fim o comando que deverá ser executado ao final do loop, neste caso para evitar o loop infinito, somaremos + 1 np contador. Poderriamos escrever cont += 1, mas a forma mais comum de se encontrar no for é cont++.

```javascript
for(let cont = 0 ; cont <3 ; cont++){
    if(listaDeDestinos[contador] == destino){
        destinoExiste = true;
        }
}
```

**break**\
O comando break interrompe o fluxo de execução do laço de maneira forçada, sem precisarmos atingir a condição de saída. ao colocarmos um break dentro do laço estamos falando para o interpretador que quando ele chegar nessa linha ele deve sair do laço independentemente de outras condições.

```javascript
let contador = 0;
let destinoExiste = false
while(contador<3){

    if(listaDeDestinos[contador] == destino){
        console.log("Destino existe");
        destinoExiste = true;
        break;
    }
    contador += 1;
}
```

***

**debbuger**\
**IIFE**\
**Namespace**\
**Módulos**\
**setTimeout()**\
**setInterval**\
**requestAnimationFrame**
