# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projeto

`pyascii` é uma pequena CLI que converte imagens em ASCII art. Recebendo
apenas um caminho de arquivo, imprime o ASCII no stdout. Recebendo um GIF
animado e um argumento de pasta, grava um arquivo de texto ASCII por frame
(`0001.txt`, `0002.txt`, ...) dentro dessa pasta.

## Ambiente & comandos

- Python 3.14 é fixado via `.python-version` / `.mise.toml`; as dependências
  são gerenciadas com **uv** (`pyproject.toml` + `uv.lock`). Não existe
  `requirements.txt`.
- Instalar / sincronizar dependências: `uv sync`
- Rodar a CLI: `uv run python ascii.py FILEPATH [FOLDER] [--low N] [--high N] [--columns N] [--inverse]`
- Não há suíte de testes, linter ou passo de build configurados. Não invente
  nenhum sem que seja pedido.

## Arquitetura

Tudo vive em `ascii.py` (um arquivo, ~80 linhas). Pipeline:

1. `_frame_to_ascii(im, ...)` é o núcleo: recebe um `PIL.Image`, converte
   para RGB se necessário, redimensiona para `columns` colunas de largura
   (altura escalada por `columns/2/width` para compensar a proporção do
   caractere), lê o brilho de cada pixel como `sum(rgb)//3` e mapeia o brilho
   em `DENSITY` (ampliada com `high` caracteres `¶` no início e `low`
   espaços no fim; invertida se `--inverse`).
2. `to_ascii(filepath, ...)` abre o arquivo e delega para `_frame_to_ascii`
   — é a API pública para imagem única.
3. `gif_to_ascii_folder(filepath, folder, ...)` itera `im.n_frames` via
   `im.seek(i)` e escreve cada frame usando `_frame_to_ascii`.
4. `to_ascii_cmd` é o entrypoint do Click. Escolhe o caminho de GIF apenas
   quando o argumento `folder` foi passado **e** a imagem reporta
   `is_animated`; caso contrário, cai no comportamento original de imagem
   única.

### Coisas que vale saber antes de editar

- O brilho do pixel é limitado com `min(..., 254)` porque a fórmula de índice
  `-1 - p * len(density_map) // 255` sairia do range em `p == 255` (branco
  puro). Mantenha o clamp se mexer nessa linha.
- O comportamento da CLI com um único argumento é um contrato de
  compatibilidade — mudanças em `to_ascii` / `_frame_to_ascii` não devem
  alterar a saída para entradas já existentes.
- Frames de GIF podem chegar em modo paleta (`P`); `_frame_to_ascii`
  converte para RGB para que `sum(i)//3` sempre receba uma tupla de 3
  elementos.

### Mantendo atualizado

Este projeto usa Pillow e outras bibliotecas. Elas são atualizadas com o tempo.
Quando o usuário pedir, atualize as bibliotecas para as versões mais novas, em
seguida SEMPRE execute um teste para ver se nada quebrou. Olhe a saída do teste
e resolva se tiver também algum deprecation warning.

