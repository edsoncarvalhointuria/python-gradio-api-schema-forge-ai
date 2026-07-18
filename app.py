import modal
from pydantic import BaseModel


def downloadModel():
    from transformers import AutoModelForCausalLM, AutoTokenizer

    model_name = "edsoncarvalhointuria/merged-schema-forg-ai"
    AutoModelForCausalLM.from_pretrained(model_name)
    AutoTokenizer.from_pretrained(model_name)


image = (
    modal.Image.debian_slim(python_version="3.13")
    .pip_install("torch", "transformers", "accelerate", "pydantic", "fastapi[standard]")
    .run_function(downloadModel)
)

app = modal.App("schema-forg-ai")


class RequestData(BaseModel):
    type: str
    message: str


@app.cls(image=image, gpu="T4", timeout=120)
class GeneratedSchema:
    system_messages = {
        "zod": "Você é um Engenheiro de Software Sênior especialista em TypeScript. Sua tarefa é receber um objeto JSON bruto e gerar o código TypeScript correspondente utilizando a biblioteca 'zod' e estendendo com '@asteasolutions/zod-to-openapi'. Crie schemas modulares, fortemente tipados e inclua descrições e exemplos OpenAPI detalhados baseados nos valores do JSON. Retorne APENAS o código TypeScript, sem formatação markdown (```typescript) e sem explicações textuais.",
        "yaml": "Converta o JSON de entrada em uma especificação OpenAPI 3.0 em YAML com a indentação correta. Aloque as entidades dentro de 'components:\n  schemas:\n    NomeDaEntidade:'. Quando precisar referenciar, use o padrão estrito: $ref: '#/components/schemas/NomeDaEntidade'. Retorne apenas o código YAML.",
        "json": "Você é um Arquiteto de Software especialista em documentação de APIs. Converta o JSON de entrada em uma especificação OpenAPI 3.0 em formato JSON estruturado. Inclua as raízes obrigatórias ('openapi', 'info', 'components' com os schemas, e 'paths'). Retorne APENAS o código JSON válido.",
    }

    @modal.enter()
    def load_models(self):
        from transformers import AutoModelForCausalLM, AutoTokenizer

        model_name = "edsoncarvalhointuria/merged-schema-forg-ai"
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    @modal.fastapi_endpoint(method="POST")
    def questionToModel(self, json: RequestData):
        messages = [
            {"role": "system", "content": self.system_messages[json.type]},
            {"role": "user", "content": json.message},
        ]
        inputs = self.tokenizer.apply_chat_template(
            messages, add_generation_prompt=True, tokenize=True, return_tensors="pt"
        ).to("cuda")
        output = self.model.generate(**inputs, max_new_tokens=2048)

        total_input = inputs["input_ids"].shape[1]
        model_reponse = output[0][total_input:]

        response = self.tokenizer.decode(model_reponse, skip_special_tokens=True)
        return {"response": response}
