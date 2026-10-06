# Avaliação Prática de QA - Testes Automatizados

## Objetivo

Esta avaliação consiste em testar e corrigir a função `calcular_desconto`, responsável por calcular o desconto de compras de um sistema de e-commerce.

Foram utilizados Python e Pytest para criação e execução dos testes automatizados.

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

Porém, de acordo com o requisito, compras de R$ 100,00 ou mais devem receber 10% de desconto.

A condição foi corrigida para:

if valor_compra >= 100

2. Cliente VIP em letras minúsculas

O código original reconhecia somente:

tipo_cliente == "VIP"

Dessa forma, valores como vip não eram reconhecidos como clientes VIP.

A validação foi corrigida utilizando:

tipo_cliente.upper() == "VIP"

Assim, valores como VIP, vip, Vip e vIp são reconhecidos corretamente.

Resultado dos testes
Execução inicial

Os testes identificaram os dois bugs presentes no código original:

2 failed, 9 passed
Após as correções

Após corrigir os problemas encontrados:

11 passed

Todos os testes automatizados foram executados com sucesso.

Tecnologias utilizadas
Python 3.14.2
Pytest 9.1.1
Git
GitHub
Estrutura do projeto
avaliacao-qa/
├── calculadora.py
├── test_calculadora.py
├── README.md
├── .gitignore
└── evidencias/
    ├── PRINT1.png
    └── PRINT2.png
Evidências

As evidências da execução dos testes estão disponíveis na pasta evidencias/.

PRINT1: execução inicial, demonstrando os testes que encontraram os bugs.
PRINT2: execução após as correções, demonstrando que todos os testes passaram.
