# 🧠 Redução de Dimensionalidade em Imagens - Colorida, Cinza e Binária

Este projeto faz parte do desafio proposto no bootcamp de Machine Learning da DIO.  
Exploramos a **redução de dimensionalidade** aplicando transformações de imagens coloridas (RGB) para **escala de cinza** e posteriormente para **binária (preto e branco)**.

## 🖼️ Objetivo

Demonstrar como converter imagens para representações mais simples e com menos informações (dimensões reduzidas), que podem ser utilizadas como entrada em modelos de **visão computacional** com menor custo computacional.

## 🎯 Etapas do projeto

O notebook realiza as seguintes etapas:

- Upload da imagem pelo usuário
- Conversão da imagem colorida (RGB) para:
  - Escala de cinza (1 canal, valores de 0 a 255)
  - Binária (valores 0 ou 255, com threshold)
- Visualização lado a lado das três versões da imagem:
  - **Colorida**
  - **Cinza**
  - **Binária**

## 🔍 Benefícios da Redução

- **Imagem em tons de cinza**: Reduz de 3 canais (RGB) para 1 canal, mantendo formas e contraste.
- **Imagem binária**: Redução extrema de dimensionalidade, útil para tarefas simples de detecção de bordas, OCR, etc.

## 📈 Visualizações

O notebook exibe as três imagens com seus respectivos títulos usando `matplotlib` para facilitar a comparação entre os formatos.

## 🚀 Execução

O notebook foi desenvolvido no Google Colab.  
Acesse diretamente aqui:

👉 [`img_dim_reduct.ipynb`](img_dim_reduct.ipynb)

________

Ou se preferir código em Python para teste local.  
Acesse diretamente aqui:

🐍 [`img_dim_reduc.py`](img_dim_reduc.py)

⚠️ Instale as dependências
```bash
pip install -r requirements.txt
``` 
ou 

```bash
pip install Pillow matplotlib numpy
``` 
Exemplo de saída:
![alt text](image_example.png)


## 🧑‍💻 Tecnologias

- Python
- PIL (Pillow)
- Matplotlib
- Google Colab

---

> Projeto criado para fins educacionais como parte do bootcamp de Machine Learning da **DIO**.
