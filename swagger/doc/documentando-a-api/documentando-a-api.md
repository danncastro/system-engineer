---
description: Documentando a API
---

# Documentando a API

```yaml
openapi: 3.0.1
info:
  title: API de consultório
  description: API para controlar médicos e suas especialidades dentro do consultório.
  version: 0.0.1
  termsOfService: https://mockapi.io
  contact:
    name: Suporte a Devs
    email: contato@example.com
    url: https://mockapi.io
  license:
    name: "Lincença: GPLv3"
    url: https://www.gnu.org/licenses/gpl-3.0.html
externalDocs:
  description: Documentação burocrática
  url: https://mockapi.io
servers:
- url: https://6096015d116f3f00174b29ba.mockapi.io/
  description: API de Teste
paths:
  /especialidades:
    get:
      summary: Recupera todas as especialidades
      responses:
        200:
          description: Sucesso
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Especialidades"
    post:
      summary: Cria nova especialidade
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                descricao:
                  type: string
      responses:
        201:
          description: "Sucesso"
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Especialidade"
  /especialidades/{id}:
    parameters:
    - name: id
      in: path
      schema:
        type: integer
      required: true
    get:
      summary: Recupera uma entidade pelo ID
      responses:
        200:
          description: Sucesso
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Especialidade"
        404:
          description: Especialidade não encontrada
          content:
            application/json:
              example: "Not Found"
security: 
- auth: []
components:
  schemas:
    Especialidade:
      type: object
      properties:
        id:
          type: integer
        descricao:
          type: string
    Especialidades:
      type: array
      items:
        $ref: "#/components/schemas/Especialidade"
  securitySchemes:
    auth:
      type: http
      scheme: bearer
      bearerFormat: JWT
```
