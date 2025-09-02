# Tetris Demo

Um jogo de Tetris simples, baseado na web, construído com Python e Flask.

## Funcionalidades

*   Jogabilidade clássica de Tetris
*   Contagem de pontuação
*   Detecção de fim de jogo
*   Interface web simples e limpa

## Começando

Estas instruções permitirão que você obtenha uma cópia do projeto em execução em sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

*   Python 3
*   pip (instalador de pacotes Python)

### Instalação

1.  Clone o repositório
    ```sh
    git clone https://github.com/gbassan-br/tetris-demo.git
    ```
2.  Crie e ative um ambiente virtual
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  Instale os pacotes Python
    ```sh
    pip install Flask
    ```

## Uso

Execute a aplicação Flask:
```sh
python app.py
```
Abra seu navegador e navegue para `http://localhost:8080`.

## Executando os testes

Este projeto não inclui uma suíte de testes automatizada. O teste manual pode ser realizado executando a aplicação e jogando o jogo.

## Construído com

*   [Flask](https://flask.palletsprojects.com/) - O framework web utilizado
*   HTML, CSS, JavaScript - Frontend
