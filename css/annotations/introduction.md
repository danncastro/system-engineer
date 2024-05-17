# **CSS - Cascading Style Sheet**

Folhas de estilos em cascaca (CSS) são um conjunto de regras de formatação que controlam a **aparência** de uma página da Web.

## **Por que estilo em cascata?**

* Há várias formas de inserir modificações no estilo CSS
* Ordem de prioridade
* Efeito cascata

    1. Folha de estilo padrão do navegador; ***Menor prioridade***
    2. Folha de estilo do usuário (se existir);
    3. Folha de estilo do desenvolvedor;

        * Estilo externo (importado);
        * Estilo incorporado (definido no head);
        * Estilo inline (Dentro de um elemento).

    4. Marcação *!important*; ***Maior prioridade***

---

## **Declaração de códigos CSS**

Há três formas:

**[Inline* (style="")](*)** - Feita diretamente na tag

        <div style="height:100px"></div>
        <p style="color: red">Texto</p>

**[Tag < style >](*)** - Código são declarados diretamente no código HTML através de *tag* < style >

        <head>
            <style>
                p{
                    color: red;
                }
            </style>
        </head>
        <body>
            <p>Texto</p>
        </body>

**[Importação / Link](*)** - Estilo importado de um arquivo ".css" separado

        <head>
            <link rel="stylesheet" type="text/css" href="style.css" />
        </head>

### **Sintaxe**

        seletor{
            declarações: valor;
        }

### **Seletores**

* Classes
* IDs
* Tags

### **Diferenças Classes vs IDs**

**[IDs](*)**  

* Identificadores **únicos**
* Declarados com **#**
* URLs

    > **[ www.site.com/#id ]**

**[Classes](*)**  

* Apresenta um estilo a um grupo de elementos
* Declarado com **. (Ponto)**

### **Plano de fundo**

Aplicado a *body* ou qualquer outra *tag (div)*

* Dica: Nunca use cores muito escuras ou saturadas!

        <!-- Inserindo uma cor -->
        background-color: #F4F4F4

        <!-- Inserindo uma imagem -->
        background-image: url(app/img/bg.jpg)

### **Posição (Position)**

Define a posição de um elemento em uma página, essas coordenadas são definidas atráves das propriedades

**[top](*)**\
**[bottom](*)**\
**[Position: fixed](*)**  

* Elementos fixos na mesma posição
* Ex: Menus

**[Position: relative](*)**  
Posiciona o elemento com base no canto superior esquerdo

* Uma div relative não sobrepõe outra
* Float: left ou right

**[Position: absolute](*)**  

* Utiliza o canto superior esquerdo do elemento pai* para se posicionar
* Se não estiver dentro de outro elemento, utiliza o *body* para se referenciar
* Uma dive pode sobrepor outra

### **Text**

**[Fonte](*)**

        font-family: helvetica, arial;

**[Cor](*)**

        color: #000;

**[Tamanho](*)**

        font-size: 100px;

**[Negrito](*)**

        font-weight: bold;

**[Espaçamento entre linhas](*)**

        line-height: 1.5;

### **Tamanho e espaçamento**

**[Largura](*)**

        width: 300px;

**[Altura](*)**

        height: 200px;

### **Box model**

        div{
            <!-- Margem externa -->
            margin: 10px; 

            <!-- Margem interna -->
            padding: 10px;

            <!-- Borda -->
            border: 10px solid #000;
        }

        margin: 20px 10px;

### **1º Superior e inferior 20px**

**[Left](*)**\
**[Bottom](*)**

### **2º Direita e esquerda 10px**

**[Right](*)**\
**[Left](*)**

* Declaração sentido horario

### Eliminando configurações do *browser*

        *{
            margin: 0;
            padding: 0;
        }
