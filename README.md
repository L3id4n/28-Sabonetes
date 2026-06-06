# Agro Decide

Agro Decide é um sistema web desenvolvido em Python com Flask para auxiliar na tomada de decisão agrícola.

O sistema analisa características de uma propriedade rural, como temperatura média, índice de chuvas, pH do solo, fertilidade, drenagem, nível de nutrientes e clima da região, e compara esses dados com os requisitos de diferentes culturas.

Atualmente, o sistema realiza análises para:

*  Soja
*  Milho
*  Trigo

## Funcionalidades

* Interface web desenvolvida com Flask
* Análise automática de compatibilidade agrícola
* Ranking das culturas mais adequadas
* Recomendação das melhores opções de cultivo
* Sistema de pontuação baseado em critérios agronômicos

## Tecnologias Utilizadas

* Python
* Flask
* HTML
* CSS

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/L3id4n/28-Sabonetes.git
```

2. Instale as dependências:

```bash
pip install flask
```

3. Execute o projeto:

```bash
python app.py
```

4. Abra o navegador em:

```text
http://127.0.0.1:5000
```

## Como Funciona

O usuário informa dados da propriedade rural:

* Temperatura média
* Previsão de chuva
* pH do solo
* Fertilidade
* Drenagem
* Nível de nutrientes
* Clima da região

Com base nessas informações, o sistema calcula uma porcentagem de compatibilidade para cada cultura e apresenta um ranking com as melhores opções para cultivo.

## Objetivo

O projeto foi desenvolvido com fins educacionais para demonstrar a aplicação da programação na área do agronegócio, auxiliando produtores na análise inicial de culturas adequadas para determinadas condições ambientais.

## Equipe

Projeto desenvolvido por:

* Daniel Andrighetto (@L3id4n)
* Bernardo Reis Polo
* Brenda Buss Grohe
* Kemily Vitória Rodrigues Lima
* Vitória Lorenzão Barros
