import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import Literal

system_messages = {
    "zod": "Você é um Engenheiro de Software Sênior especialista em TypeScript. Sua tarefa é receber um objeto JSON bruto e gerar o código TypeScript correspondente utilizando a biblioteca 'zod' e estendendo com '@asteasolutions/zod-to-openapi'. Crie schemas modulares, fortemente tipados e inclua descrições e exemplos OpenAPI detalhados baseados nos valores do JSON. Retorne APENAS o código TypeScript, sem formatação markdown (```typescript) e sem explicações textuais.",
    "yaml": "Você é um Arquiteto de Software especialista em documentação de APIs. Converta o JSON de entrada em uma especificação OpenAPI 3.0 em formato YAML. Estruture corretamente os componentes (schemas) e garanta a tipagem rigorosa. Retorne APENAS o código YAML válido, sem comentários adicionais.",
    "json": "Você é um Arquiteto de Dados especialista em modelagem JSON. Sua tarefa é analisar os dados brutos de entrada e gerar um JSON Schema (Draft 2020-12) robusto e perfeitamente validado. Defina rigorosamente os tipos (string, number, boolean, array, object), especifique quais propriedades são obrigatórias e mapeie estruturas aninhadas com precisão. Retorne APENAS o JSON Schema cru, sem formatação markdown (```json) e sem conversas textuais.",
}


model_path = "edsoncarvalhointuria/merged-schema-forg-ai"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path, dtype=torch.float16, device_map="auto"
)


def askToModel(user: str, type: Literal["zod", "yaml", "json"]):
    messages = [
        {"role": "system", "content": system_messages[type]},
        {"role": "user", "content": user},
    ]
    inputs = tokenizer.apply_chat_template(
        messages, add_generation_prompt=True, tokenize=True, return_tensors="pt"
    ).to(model.device)
    print("iniciando", inputs)

    output = model.generate(**inputs, max_new_tokens=2048)

    size_messages = inputs["input_ids"].shape[1]
    model_response = output[0][size_messages:]

    response = tokenizer.decode(model_response, skip_special_tokens=True)
    print(response)

    return {"response": response}


window = gr.Interface(fn=askToModel, inputs=["text", "text"], outputs="json")

if __name__ == "__main__":
    window.launch()
