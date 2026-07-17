<<<<<<< HEAD
# 🚀 Schema Forge AI - Motor de Inferência / Inference Engine

[![🇧🇷 Português]](#-português) | [![🇺🇸 English]](#-english)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-Float16-EE4C2C.svg)
![Gradio](https://img.shields.io/badge/Gradio-6.0-orange.svg)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-yellow.svg)

---

## 🇧🇷 Português

Este repositório contém o Motor de Inferência (Back-end/API) do **Schema Forge AI**. Ele hospeda um modelo de linguagem especializado (LLM) baseado no Microsoft Phi-3, refinado via QLoRA, para gerar código fortemente tipado, especificações e schemas a partir de objetos JSON brutos.

A infraestrutura foi projetada para rodar em contêineres e é exposta assincronamente através de uma API Gradio (Job Queues / SSE), pronta para ser consumida por aplicações Front-end (Next.js).

### 🧠 Arquitetura do Modelo

*   **Modelo Base:** `microsoft/Phi-3-mini-4k-instruct`
*   **Técnica de Fine-Tuning:** QLoRA (Parameter-Efficient Fine-Tuning)
*   **Especialidades:**
    *   `zod`: Geração de código TypeScript tipado com `@asteasolutions/zod-to-openapi`.
    *   `yaml`: Especificação OpenAPI 3.0 estruturada.
    *   `json`: JSON Schema (Draft 2020-12) com validações robustas.
*   **Gerenciamento de Memória:** Carregamento em escopo global (Singleton) utilizando precisão de 16-bits (`torch.float16`) para evitar gargalos de OOM (Out of Memory).

### 🔌 Contrato da API (Integração Front-end)

A aplicação utiliza o Gradio como interface para gerar automaticamente uma rota de API REST/SSE assíncrona. Para consumir este serviço utilizando a biblioteca `@gradio/client` no Next.js, utilize o seguinte contrato:

#### Parâmetros de Entrada (Inputs)
A função de inferência exige dois parâmetros obrigatórios na ordem exata:
1.  **`user_text`** *(string)*: O objeto JSON bruto ou a instrução fornecida pelo usuário.
2.  **`type`** *(string)*: O formato de saída desejado. Valores aceitos: `"zod"`, `"yaml"`, `"json"`.

#### Formato de Saída (Output)
A API retorna um Dicionário Python nativo que é serializado automaticamente pelo Gradio como um objeto JSON estruturado:

```json
{
  "response": "// Seu código Typescript/Zod, YAML ou JSON Schema gerado aqui..."
}
```

### 🛠️ Como Rodar Localmente

**1. Clone o repositório:**
```bash
git clone https://github.com/edsoncarvalhointuria/python-gradio-api-schema-forge-ai.git
cd schema-forge-ai-api
```
**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```
**3. Inicie o servidor Gradio:**
```bash
python app.py
```
*O servidor estará disponível por padrão em `[http://0.0.0.0:7860](http://0.0.0.0:7860)`.*

### ☁️ Deploy (ModelScope / Alibaba Cloud)
Este projeto foi otimizado para deploy direto no ModelScope. A plataforma detectará automaticamente o arquivo `app.py` na raiz do projeto e construirá o contêiner Docker injetando as dependências do `requirements.txt`. Nenhuma configuração extra de hardware virtual é necessária.

---

## 🇺🇸 English

This repository contains the Inference Engine (Back-end/API) for **Schema Forge AI**. It hosts a specialized Large Language Model (LLM) based on Microsoft Phi-3, fine-tuned via QLoRA, to generate strongly typed code, specifications, and schemas from raw JSON objects.

The infrastructure is designed to run in containers and is exposed asynchronously via a Gradio API (Job Queues / SSE), ready to be consumed by Front-end applications (Next.js).

### 🧠 Model Architecture

*   **Base Model:** `microsoft/Phi-3-mini-4k-instruct`
*   **Fine-Tuning Technique:** QLoRA (Parameter-Efficient Fine-Tuning)
*   **Specialties:**
    *   `zod`: Generation of typed TypeScript code with `@asteasolutions/zod-to-openapi`.
    *   `yaml`: Structured OpenAPI 3.0 specification.
    *   `json`: JSON Schema (Draft 2020-12) with robust validations.
*   **Memory Management:** Global scope loading (Singleton pattern) using 16-bit precision (`torch.float16`) to prevent Out of Memory (OOM) bottlenecks.

### 🔌 API Contract (Front-end Integration)

The application uses Gradio as an interface to automatically generate an asynchronous REST/SSE API route. To consume this service using the `@gradio/client` library in Next.js, use the following contract:

#### Input Parameters
The inference function requires two mandatory parameters in the exact following order:
1.  **`user_text`** *(string)*: The raw JSON object or the instruction provided by the user.
2.  **`type`** *(string)*: The desired output format. Accepted values: `"zod"`, `"yaml"`, `"json"`.

#### Output Format
The API returns a native Python Dictionary that is automatically serialized by Gradio as a structured JSON object:

```json
{
  "response": "// Your generated Typescript/Zod, YAML, or JSON Schema code here..."
}
```

### 🛠️ Local Setup

**1. Clone the repository:**
```bash
git clone https://github.com/edsoncarvalhointuria/python-gradio-api-schema-forge-ai.git
cd schema-forge-ai-api
```
**2. Install dependencies:**
```bash
pip install -r requirements.txt
```
**3. Start the Gradio server:**
```bash
python app.py
```
*The server will be available by default at `[http://0.0.0.0:7860](http://0.0.0.0:7860)`.*

### ☁️ Deployment (ModelScope / Alibaba Cloud)
This project has been optimized for direct deployment on ModelScope. The platform will automatically detect the `app.py` file in the project's root and build the Docker container, injecting the dependencies from `requirements.txt`. No extra virtual hardware configuration is required.
=======
---
# 详细文档见https://modelscope.cn/docs/%E5%88%9B%E7%A9%BA%E9%97%B4%E5%8D%A1%E7%89%87




## 启动文件(若SDK为Gradio/Streamlit，默认为app.py, 若为Static HTML, 默认为index.html)
deployspec:
   entry_file: app.py
license: Apache License 2.0
---
#### Clone with HTTP
```bash
 git clone https://www.modelscope.ai/studios/edsoncarvalhointuria/schema-forg-ai.git
 
```
>>>>>>> alibaba/master
