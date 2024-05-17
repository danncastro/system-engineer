---
description: >-
  Para que o endpoint seja mostrado no Swagger UI, pelo menos uma operação deve
  ser definida, usando algum verbo (ou método) HTTP, como [get, put, delete,
  post, patch]...etc.
---

# Mapeando os endpoints da aplicação

Para identificarmos o corpo de uma requisição, não usamos **`[parameters]`**. Os valores possíveis para **\[in]** de cada um dos parameters são: **`[query, header, path ou cookie]`**`.`

Cada chave do mapa é um tipo de mídia que será enviado como o cabeçalho **\[Content-Type]**. Em nosso exemplo, como a API só suporta JSON, informamos apenas **`[application/json].`**
