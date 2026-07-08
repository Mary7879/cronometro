 Cronômetro Python

Um cronômetro simples, leve e preciso desenvolvido em Python, utilizando `threading` para não bloquear o terminal.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green
Funcionalidades

- Iniciar, pausar e resetar o cronômetro
- Exibição em tempo real no terminal (`HH:MM:SS`)
- Não bloqueia a execução principal (thread separada)
- Método `obter_tempo()` para integração com outros programas
- Controle via comandos no terminal (exemplo interativo)

Instalação

```bash
git clone https://github.com/SEU_USUARIO/cronometro-python.git
cd cronometro-python

# Instalar como pacote (opcional)
pip install -e .
