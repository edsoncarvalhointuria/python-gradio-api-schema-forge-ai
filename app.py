import gradio as gr

# Esta é a função que será acionada pela nossa API
def validar_api(json_entrada):
    return f"SUCESSO! A API do ModelScope está viva. Você enviou: {json_entrada}"

# Aqui configuramos a interface que gera a API invisível por trás
demo = gr.Interface(
    fn=validar_api, 
    inputs="text", 
    outputs="text"
)
print('olá mundo')
# O comando que levanta o servidor na porta correta
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=15181)