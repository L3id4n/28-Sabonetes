# Agro Decide

Agro Decide é um sistema web desenvolvido em Python com Flask para auxiliar na tomada de decisão agrícola.

O sistema analisa características de uma propriedade rural, como temperatura média, índice de chuvas, pH do solo, fertilidade, drenagem, nível de nutrientes e clima da região, comparando essas informações com os requisitos de diferentes culturas agrícolas.

Atualmente, o sistema realiza análises para as seguintes culturas:

* Soja
* Milho
* Trigo

---

## Equipe

| Integrante                    | Função                                                            |
| ----------------------------- | ----------------------------------------------------------------- |
| Daniel Andrighetto (@L3id4n)  | Desenvolvimento da aplicação, arquitetura do sistema e integração |
| Bernardo Reis Polo            | Concepção da ideia e definição dos requisitos                     |
| Brenda Buss Grohe             | Produção do vídeo Pitch e apresentação do projeto                 |
| Kemily Vitória Rodrigues Lima | Pesquisa do problema e análise do público-alvo                    |
| Vitória Lorenzão Barros       | Documentação e validação da solução                               |

---

## Escopo do Projeto

O Agro Decide tem como objetivo auxiliar produtores rurais na escolha da cultura mais adequada para plantio com base nas condições ambientais e características do solo.

A solução busca fornecer uma análise inicial rápida e acessível, auxiliando na tomada de decisão e reduzindo erros durante o planejamento agrícola.

---

## Funcionalidades

* Interface web desenvolvida com Flask
* Análise automática de compatibilidade agrícola
* Ranking das culturas mais adequadas
* Recomendação das melhores opções de cultivo
* Sistema de pontuação baseado em critérios agronômicos

---

## Tecnologias Utilizadas

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS

---

## Arquitetura

Fluxo geral da aplicação:

```text
Usuário
   ↓
Formulário Web
   ↓
Backend Flask
   ↓
Motor de Análise
   ↓
Ranking das Culturas
   ↓
Resultado Final
```

---

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

---

## Situação do Projeto

### Requisitos Planejados

* Cadastro das características da propriedade
* Sistema de análise agrícola
* Ranking de culturas
* Interface web intuitiva

### Implementado

✅ Cadastro das características da propriedade

✅ Sistema de análise de compatibilidade

✅ Ranking automático das culturas

✅ Interface web funcional

### Melhorias Futuras

* Inclusão de novas culturas agrícolas
* Integração com APIs meteorológicas
* Histórico de análises
* Recomendações mais detalhadas

---

## Como Executar

### 1. Instale o Python

É recomendado utilizar Python 3.10 ou superior.

Verifique sua versão instalada:

```bash
python --version
```

Caso não tenha o Python instalado, faça o download pelo site oficial:

https://www.python.org/downloads/

---

### 2. Clone o repositório

Certifique-se de ter o Git instalado em seu computador.

No terminal, execute:

```bash
git clone https://github.com/L3id4n/28-Sabonetes.git
```

---

### 3. Acesse a pasta do projeto

```bash
cd 28-Sabonetes
```

---

### 4. Instale as dependências

Ainda no terminal, execute:

```bash
pip install flask
```

---

### 5. Execute o projeto

```bash
python app.py
```

---

### 6. Abra no navegador

Acesse:

```text
http://127.0.0.1:5000
```

---

## Objetivo

O projeto foi desenvolvido com fins educacionais para demonstrar a aplicação da programação no agronegócio, auxiliando produtores na análise inicial de culturas adequadas para determinadas condições ambientais.

Além disso, busca incentivar o uso da tecnologia como ferramenta de apoio à tomada de decisão no setor agrícola.

---

## Licença

Projeto desenvolvido para fins educacionais e acadêmicos.
