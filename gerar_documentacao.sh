#!/bin/bash

# Script para gerar a documentação em PDF

# Criar diretório para os PDFs se não existir
mkdir -p docs/pdf

# Converter os arquivos Markdown para PDF
echo "Convertendo guia de implantação para PDF..."
manus-md-to-pdf docs/guia_implantacao.md docs/pdf/guia_implantacao.pdf

echo "Convertendo guia do usuário para PDF..."
manus-md-to-pdf docs/guia_usuario.md docs/pdf/guia_usuario.pdf

echo "Convertendo demonstração para PDF..."
manus-md-to-pdf docs/demonstracao.md docs/pdf/demonstracao.pdf

echo "Convertendo README para PDF..."
manus-md-to-pdf README.md docs/pdf/readme.pdf

echo "Documentação gerada com sucesso!"
echo "Os arquivos PDF estão disponíveis no diretório docs/pdf/"

