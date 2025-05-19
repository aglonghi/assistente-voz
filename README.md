# Assistente de Voz Offline com Raspberry Pi 3 + AIY Voice Kit v1

Este projeto usa Vosk para reconhecimento de fala em português, espeak-ng para síntese de voz e os componentes do AIY Voice Kit para um assistente local, sem internet.

## Comandos reconhecidos
- "que horas são"
- "ligue a luz"
- "desligue a luz"
- "me diga uma curiosidade"

## Requisitos
- Raspberry Pi OS Buster (ou superior)
- Python 3
- Instalar dependências via requisitos.txt

## Instalação
1. Clone este repositório:
   ```
   git clone <URL_DO_SEU_REPOSITÓRIO> assistente-voz
   ```
2. Entre no diretório:
   ```
   cd assistente-voz
   ```
3. Instale as dependências:
   ```
   pip3 install -r requisitos.txt
   ```
4. Baixe o modelo Vosk em português:
   - Acesse https://alphacephei.com/vosk/models
   - Faça download do "vosk-model-small-pt-0.3"
   - Descompacte na pasta `modelos/vosk-model-small-pt-0.3`

5. Execute o assistente:
   ```
   python3 assistente.py
   ```

## Uso
- Pressione o botão para iniciar a escuta.
- Fale o comando desejado.
- Aguarde a resposta por voz.
