# **HTML5**

HTML5 é a mais recente versão da linguagem HTML. Trouxe novas funcionalidades e perspectivas em relação ao papel exercido pelo HTML na Web. HTML traz novas tags, como < header > para cabeçalhos, < nav > para menus, < video > e < audio > para respectivos elementos, além de apresentar uma sintaxe mais simples como por exemplo para declaração do DOCTYPE.

Uma página HTML é composta por alguns elementos básicos. São eles: (i) a declaração do tipo do documento; (ii) a tag HTML, que armazenará todo conteúdo da página; (iii) o cabeçalho, que armazena informações estruturais da página; e (iv) o corpo, que armazenará os conteúdos e formatações da página.

---

## **Introdução ao HTML**

* Hypertext Markup Language ou linguagem de marcação de hipertexto.
* Utilizada na descrição e produção de páginas WEB.
* Lembre - se: NÂO é uma lingaguem de programação, é linguagem de marcação!
* Composta por uma série de TAGs de marcação.

---

## **!DOCTYPE**

* O < DOCTYPE > não é um elemento HTML, mas sim uma instrução para que o navegador saiba a versão da linguagem de marcação que está sendo utilizada.
* A linguagem HTML5 requer um elemento < DOCTYPE > para garantir que a página seja renderizada pelo navegador de maneira correta, mas não se refere a nenhum arquivo externo (DTD)
* A declaração DOCTYPE no HTML5 é

        <!DOCTYPE html>

* Não é case sensitive

### **< html lang="pt-BR >"**

Além de definir a tabela de codificação de caracteres que o navegador deve usar para renderizar (processar e exibir) a página (por meio do atributo **charset** do elemento < meta >), é importante utilizar o atributo **lang** no elemento < html > para que os navegadores saibam qual é a linguagem (idioma) principal utilizado.

### **< meta charset="UTF-8" >**

Para estabelecer a codificação de caracteres no HTML5, podemos utilizar um elemento < meta > com um atributo charset que especifica a codificação.

* Por exemplo, < meta charset="ISO-8859-1" > pode ser usado para especificar a codificação ISO-8859-1. O valor UTF-8 também pode ser utilizado

---

## **Estrutura Básica de um Documento HTML**

Para que websites sejam bem desenvolvidos, existe um conjunto de tags que indicam onde cada conteúdo deve ser inserido. Em geral, essas tags são apenas estruturais, ou seja, ao serem inseridas, não trazem modificações a estrutura da página.

    <html>
        <head>
        </head>

        <body>
        </body>
    </html>

### **Interpretação do conteúdo**

* O texto entre < html > e </ html > descrevem a página WEB;
* O texto entre < body > e </ body > será o conteúdo visível da página;
* O texto entre < h1 > e </ h1 > é apresentado em destaque, como um título;
* O texto entre < p > e </ p > é apresentado em um parágrafo

---

## **Tags HTML**

* São palavras-chave, digitas entre '<'  '>' (Ex..: < b >.)
* Normalmente utilizadas em pares (Ex..: < b > Texto em negrito </ b >)
* As tags não distinguem esntre maiúsculas e minúsculas (HTML não é case sensitive).
* Espaços extras não são considerados.

> < b > - Tag de abertura
>> </ b > - Tag de fechamento

**[Tag Div](*)**  
Essa tag permite a inserção de divisórias nas páginas, ou seja, são tags estruturais que permitirão que você organize seu código.

        <div>
        <p>Conteúdo de uma div</p>
        </div>

**[Tag de Hiperlink](*)**  
A tag de Hiperlink é a tag ***< a >*** e é preciso definir o link para a página dentro do atributo **href**, definida pelas tags.

    <a href="conteudo"> Texto </a>

**[Tag de Imagem](*)**  
É preciso usar o atributo **src** para especificar o nome do arquivo. Pode ser um arquivo na Web Também.

* É possível também a utilização dos atributos **width** e **height** para definição de largura(width) e altura (height).

* Caso a especificação seja de tamanho diferente da figura original, irá deformar a figura.

        <img src="conteudo.jpg"/>
        <img src="https://conteudo_web.jpg"/>

**[Linhas HTML](*)**  
A tag < hr /> cria uma linha horizontal em uma página HTML, podendo ser usada para separar conteúdo.

    Parágrafo
    <hr/>

**[Quebra de Linhas HTML](*)**  

    Parágrafo
    <br/>
    Parágrafo

**[Tag de Formatação](*)**
Para se declarar parágrafos em páginas pode-se utilizar a tag < p >. Entretanto, é possível aplicar diversos tipos de formatações a parágrafos. Veja o exemplo a seguir:

        <p>
            <b>Texto em negrito</b>
            <i>Texto em itálico</i>
            <u>Texto sublinhado</u>
            <sub>Texto subscrito</sub>
            <sup>Texto sobrescrito</sup>
            <big>Texto com fonte maior do que o padrão</big>
            <small>Texto com fonte menor do que o padrão</small>
            <em>Texto em itálico</em>
            <strong>Texto em negrito</strong>
        </p>  

Podemos ainda alterar a fonte usando o atributo style:

        <!-- Declarando uma única fonte -->
        <p style="font-family: 'Times New Roman'">Olá, mundo!</p>
        
        <!-- Declarando duas possíveis fontes -->
        <p style="font-family: 'Helvetica, Arial'">Olá, mundo novamente!</p>

        <!-- Declarando o tamanho das fontes -->
        <p style="font-size: '5'">Olá, mundo novamente!</p>

**[Estilo](*)**  
A tag < style > deve ser declarada dentro da tag < head >. Estilos permitem que sua página tenha diversos tipos de formatações. Eles podem ser declarados com o atributo style (como mostrado anteriormente) ou com a tag < style >.

        <style>
        p { color: red; }
        </>

Podemos ainda aplicar cores ao fundo. Observe o exemplo a seguir:

        <style>
        body { background-color: red; }
        </style>

---

## **Atributos HTML**

* Atributos fornecem informações adicionais aos elementos HTML.
* Elementos HTML podem ou não ter atributos.
* Atributos são sempre especificados nas tags de abertura
* Valores de atributos sempre devem estar delimitados por aspas duplas ou simples (Em alguns momentos pode até omitir as aspas).

### **Sintaxe**

    <uma_tag nome_do_atributo = "valor_do_atributo">

---

## **Elementos HTML**

Vários elementos HTML não tem conteúdo (como a tag de imagem).
Elementos sem sem conteúdo são fechados na própria tag de abertura ( como na tag de imagem ou na de pular linha) **Exemplo:**

    <br/>

Um elemento HTML é o conjunto formado por:

1. Uma tag de abertura.
2. Uma tag de fechamento
3. Conteúdo (O que estiver entre as tags);

Alguns elementos HTML podem ser aninhados, isto é, podemos inserir elementos HTML como conteúdo de outros elementos.

    <html>
        <body>
            <p>Coffe</p>
            <p><img src="imagem.jpg" width="25%" height="30%"/></p>
            <p><b>Texto</b></p>
        </body>
    </html>

### **Elemento Canvas**

O elemento HTML < canvas > pode ser usado para desenhar via código (normalmente JavaScript).

* Por exemplo,  ele pode ser usado para desenhar **gráficos**, fazer **composição de fotos**, **criar animações** ou até mesmo fazer processamento ou renderização de vídeos em tempo real.

### **Elemento video**

Subistituição do Adobe Flash

### **Elemento Audio**

Para tocar um arquivo de áudio num documento HTML, juntamente com o atributo **controls** que adiciona os botões de **play, pause e volume**

### **SVG**

O Formato SVG(Scalable Vectorial Graphics) é uma especificação de linguagem baseada em XML para representar arquivos vetoriais bidimensionais, estáticos ou animados.

* Ou seja, o SVG é uma linguagem para marcaçao que permite a construçao de gráficos vetoriais

---

## **Tabelas**

Podemos criar tabelas usando a tag < table >. As tabelas permitem organizar os dados possibilitando uma melhor visualização dos elementos numa página HTML. Podemos ter tabelas para apresentar:

* Orçamentos
* Folhas de pagamento
* Notas de alunos.

Cada linha deve ser declarada com a tag < tr > e cada célula com a tag < td >. Opcionalmente podemos usar a tag < th > para declarar células que representem a linha de cabeçalho.

Tabelas em HTML

* Definidas a partir da tag < table >
* Uma tabela é dividida em linhas com as ***table row*** (TAG < tr >)
* Cada linha é dividida em células com ***table data*** (TAG < td >)
* E podemos declarar células qie presentam as linhas  do cabeçalho ***table header*** (TAG < th >)

        <body>
            <table>
                 </tr> Linha1 <th> Cabeçalho 1 </th> <th> Cabeçalho 2 </th> <th> Cabeçalho 3 </th></tr>
                 </tr> Linha2 <td> Celula 1    </td> <td> Celula 2    </td> <td> Celula 3    </td></tr>
                 </tr> Linha3 <td> Celula 1    </td> <td> Celula 2    </td> <td> Celula 3    </td></tr>
            </table>
        </body>

### **Table - Atributo Border**

É preciso adicionar o atributo **border** com valor 1 para mostrar a linha da tabela. Quanto maior o valor do atributo, maior será a grossura da borda

* O estilo da tabela deve ser modificado no CSS no entando, o HTML tem algumas propriedades que podem modificar o estilo da tabela.

### **Outros atributos**

**[< td align="center" >](*)** - Alinha o conteúdo da célula. Valores: **left, center, right**\
**[< table bgcolor="blue" >](*)** - Muda a cor de fundo da tabela usando cores em inglês ou valores hexadecimais.\
**[< table bordercolor="red"](*)** - Muda a cor da borda externa.

## **Mesclar colunas de uma tabela**

Usando o atributo **colspan** em < td >;

* A célula irá ocupar o espaço de **n** colunas.
* O valor de **n** corresponde ao número de colunas que a célula irá expandir.
* Sintaxe

        <td colspan="n">
        <td colspan="2"></td>

## **Mesclar linhas de uma tabela**

Usando o atributo **rowspan** em < td >;

* A célula irá ocupar o espaço de **n** linhas.
* O valor de **n** corresponde ao número de linhas que a célula irá expandir.
* Sintaxe

        <td rowspan="n">
        <td rowspan="2"></td>

**Observação:** Quando o valor de **n** é 2, deve-se reduzir uma célula na linha abaixo (< td > e </ td >)

---

## **Listas**

Listas podem ser criadas usando a tag < ul > (listas não ordenadas) ou < ol > (listas ordenadas) e cada elemento pode ser inserido com a tag < li >.

### **Listas não ordenas em HTML**

* São definidas a partir da tag < ul > - unordered list
* Cada elemento da lista é definido a partir da tag < li > - list item

        <body>
            <ul>
                <li>Primeiro elemento</li>
                <li>Segundo elemento</li>
                <li>Terceiro elemento</li>
            </ul>
        </body>

### **Listas ordenas em HTML**

* São definidas a partir da tag < ol > - ordered list
* Cada elemento da lista é definido a partir da tag < li > - list item

        <body>
            <ol>
                <li>Primeiro elemento</li>
                <li>Segundo elemento</li>
                <li>Terceiro elemento</li>
            </ol>
        </body>

---

## **Formularios HTML**

Formulários permitem que o usuário envie dados para um sistema web. Devem ser declarados com a tag < form >. O atributo action indica a página que será carregada. O método de envio pode ser "post" (mais recomendado) ou "get" (envio pela url).

        <body>
            <form action="recebe.php" method="post" name="form"></form>
        </body>

### **Campos de texto**

A tag < input type="text" /> é utilizada para criação de um campo de texto com uma linha.

        <body>
            <form>
                Nome: <input type="text" name="nome" />
                <br/>
                Sobrenome: <input type="text" name="sobrenome" />
            </form>
        </body>

### **Campos de Senha**

A tag < input type="password" /> é utilizada para criação de um campo de senha.

        <body>
            <form>
                Senha: <input type="password" name="senha" />
            </form>
        </body>

### **Area de texto**

A tag < textarea > é utilizada para criação de uma área de texto(com mais de uma linha);

        <body>
            <textarea name="texto" rows="5 cols="60">
                Digite aqui o texto
            </textarea>
        </body>

### **Radio buttons**

A tag < input type="radio" /> é utilizada na definição de um radio button.

* Eles permitem selecionar apenas uma opção de uma lista

        <body>
            <form>
                <input type="radio" name="bebida" value="exp" />Expresso
                <br/>
                <input type="radio" name="bebida" value="cap" />Capuccino
            </form>
        </body>

### **Checkboxes**

A tag < input type="checkbox" /> é utilizada na definição checkbox.

* Checkbox permitem aos usuários selecionarem uma ou mais opções de uma lista

        <body>
            <form>
                <input type="Checkboxes" name="carro" value="Ferrari" />Ferrari
                <br/>
                <input type="Checkboxes" name="carro" value="Fusca" />Fusca
            </form>
        </body>

### **Select**

A tag < select > é utilizada na criação de listas ***drop-down (comboboxes)***. Cada opção da lista é definida pela tag < option >

        <body>
            <form>
                <selec name="Cidades">
                    <option value="JP">João Pessoa</option>
                    <option value="Rec">Recife</option>
                    <option value="NT">Natal</option>
                </selec>
            </form>
        </body>

### **Submit buttons**

A tag < input type="submit" /> é utilizada na crição de um botão de submissão para o formulário.

* Um botão de submissão é usado para enviar os dados do formulário para um servidor
* Os dados são enviados para uma página específica, indicada no atributo **action** da tag < form >.
* O arquivo indicado no atributo **action** normalmente executa algum processamento nos dados enviados pelo formulário.

        <body>
            <form action="recebe.php" method="GET">
                Nome: <input type="text" name="nome" />
                <input type="submit" value="Enviar" />
            </form>
        </body>

### **Hidden: campo oculto**

        <input type="hidden>

### **Placeholder**

Exibe mensagens em campos de entrada de texto

---

## **Método GET e POST**

Dois atributos são de extrema importância para a tag < form >: **action** e **method**

* O atributo **action** irá executar a ação descrita quando o usuário clicar no botão de **submit**
* O atributo **method** especifica a forma que os dados digitados pelo usuário no formulário serão enviados.
* Caso seja especificado o tipo **GET**, os dados serão enviados pela **url** do navegador, **sem criptografia**.
* Caso seja especificado com **POST** os dados **serão criptografados** e enviados para o destino do **action** do formulário.

---

## **Fazer com que um site fique disponível na internet**

1. Comprar um domínio

    registro.br(para sites .com.br)

2. Dominio: Endereço a qual o site pode ser acessado, para que os roteadores possam encontrar um site nos data centers mundiais é necessario saber o endereço IP

        www.site.com.br -> 192.168.0.1
        Servidor DNS

3. Servidor de hospedagem: Computador que armazenará os dados do seu site e permitirá que qualquer pessoa o acesse, deve-se alugar um servidor web para manter o site no ar.

4. Publicar o site: Vincule o domínio ao servidor de hospedagem -> Enviar os arquivos do site para o servidor (FTP).

---

## **Hospedagem de Sites Gratuitos**

**[Netlify](*)**\
**[GitHubPages](*)**\
**[Zait](*)**\
**[Surge](*)**\
**[Google Drive](*)**

---

## **W3S**

**[HTML Introduction](https://www.w3schools.com/html/html_intro.asp)**
