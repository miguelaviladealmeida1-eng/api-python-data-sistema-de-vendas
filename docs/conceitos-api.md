# Conceitos de API

## O que e uma API?

API significa Application Programming Interface. Ela permite que um sistema converse com outro sistema seguindo regras definidas.

Neste projeto, o Python conversa com uma API REST publica de produtos.

## Endpoint

Um endpoint e um endereco especifico usado para acessar um recurso.

Exemplo:

`GET /products`

## GET

O metodo HTTP GET e usado para buscar dados.

Exemplos usados no projeto:

- `GET /products`
- `GET /products/1`
- `GET /products/search?q=phone`
- `GET /products/categories`

## JSON

A API retorna os dados em JSON. No Python, a biblioteca Requests transforma a resposta em estruturas que podem ser trabalhadas pelo programa.

## Status HTTP

- 200: requisicao realizada com sucesso
- 400: requisicao invalida
- 404: recurso nao encontrado
- 500: erro no servidor

## Fluxo do projeto

API externa -> Python -> tratamento dos dados -> exibicao ou JSON

No futuro:

API externa -> Python -> MySQL -> FastAPI -> Front-end
