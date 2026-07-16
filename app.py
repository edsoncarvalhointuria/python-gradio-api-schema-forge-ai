import gradio as gr
import os

def validar_api(json_entrada):
    return f"SUCESSO! ModelScope 2026 ativo. Enviado: {json_entrada}"

# Criamos o bloco (Padrão recomendado no Gradio 6)
with gr.Blocks() as demo:
    entrada = gr.Textbox(label="Input JSON/Texto")
    botao = gr.Button("Validar")
    saida = gr.Textbox(label="Resultado")
    
    botao.click(fn=validar_api, inputs=entrada, outputs=saida)

print('olá mundo')
demo.queue(default_concurrency_limit=None) 

if __name__ == "__main__":
    # O ModelScope exige escutar na interface aberta (0.0.0.0) 
    # e na porta 15181 capturada pelo proxy Quart no seu log
    demo.launch(
        server_name="0.0.0.0", 
        server_port=15181,
        allowed_paths=["*"]
    )