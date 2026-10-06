# Avaliação Prática de QA - Testes Automatizados

## Objetivo

Esta avaliação consiste em testar e corrigir a função `calcular_desconto`, responsável por calcular o desconto de compras de um sistema de e-commerce.

Foram utilizados **Python** e **Pytest** para criação e execução dos testes automatizados.

## Regras de negócio

A função deve seguir as seguintes regras:

- Compras abaixo de R$ 100,00 não recebem desconto base.
- Compras entre R$ 100,00 e R$ 499,99 recebem 10% de desconto.
- Compras a partir de R$ 500,00 recebem 20% de desconto.
- Clientes VIP recebem mais 5% de desconto sobre a porcentagem base.
- O cliente VIP deve ser reconhecido independentemente de letras maiúsculas ou minúsculas.
- O desconto máximo permitido é de R$ 200,00.

## Cenários de teste

Foram criados testes automatizados para verificar:

| Cenário | Valor da compra | Cliente | Desconto esperado |
|---|---:|---|---:|
| Compra abaixo de R$ 100 | R$ 50 | COMUM | R$ 0 |
| Compra exatamente R$ 100 | R$ 100 | COMUM | R$ 10 |
| Compra entre R$ 100 e R$ 500 | R$ 300 | COMUM | R$ 30 |
| Compra exatamente R$ 500 | R$ 500 | COMUM | R$ 100 |
| Compra acima de R$ 500 | R$ 600 | COMUM | R$ 120 |
| VIP abaixo de R$ 100 | R$ 50 | VIP | R$ 2,50 |
| VIP entre R$ 100 e R$ 500 | R$ 300 | VIP | R$ 45 |
| VIP em letras minúsculas | R$ 300 | vip | R$ 45 |
| VIP exatamente R$ 500 | R$ 500 | VIP | R$ 125 |
| Teto do desconto | R$ 2000 | COMUM | R$ 200 |
| Teto do desconto para VIP | R$ 2000 | VIP | R$ 200 |

## Bugs encontrados

Durante a execução dos testes no código original, foram encontrados dois problemas.

### 1. Compra de exatamente R$ 100,00

O código original utilizava:

```python
if valor_compra > 100
