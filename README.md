# Digital Innovation One

Código criado para utilização junto a plataforma da Digital Innovation One

<p align="center"><img src="./Logo.png" width="500"></p>

# Darknet Project

Este projeto é baseado no Darknet, uma estrutura de código aberto escrita em C e CUDA para treinamento e inferência de redes neurais convolucionais, com foco em detecção de objetos usando o algoritmo YOLO (You Only Look Once).

## Requisitos

- Linux
- CUDA
- OpenCV

Certifique-se de ter instalado todas as dependências necessárias antes de prosseguir.

## Configuração

# Clone o repositório Darknet
git clone https://github.com/AlexeyAB/darknet.git

# Compile o Darknet
cd darknet
make


realiza várias tarefas relacionadas ao processamento de áudio, reconhecimento de fala e tradução. Aqui está um resumo das funcionalidades do código:

Instalar pacotes necessários: O notebook instala vários pacotes Python, como gTTS (Google Text-to-Speech), pydub (processamento de áudio), SpeechRecognition (reconhecimento de fala), ffmpeg-python (conversão de áudio), pyaudio (entrada e saída de áudio) e nltk (Natural Language Toolkit).

Gravar áudio: O notebook define uma função record que permite gravar áudio do usuário por um determinado número de segundos.

Adicionar pontuação correta ao texto traduzido: O código inclui uma função chamada add_punctuation, que analisa as palavras traduzidas e adiciona pontuação apropriada para melhorar a compreensão do texto.

Transcrever e traduzir áudio: O código inclui uma função chamada transcrever_e_traduzir, que utiliza o reconhecimento de fala para transcrever o áudio gravado em português e, em seguida, traduz o texto transcrito para o inglês usando a biblioteca Googletrans.

Solicitar entrada do usuário: O código apresenta um menu para o usuário escolher uma opção entre digitar uma frase, selecionar uma das cinco frases pré-definidas em português ou gravar uma frase usando o microfone.

Sintetizar áudio em português: Com base na escolha do usuário, o código usa a biblioteca gTTS para sintetizar o texto em português e reproduzir o áudio correspondente.

Conversão de formato de áudio: Se o usuário gravar uma frase usando o microfone, o áudio gravado em formato MP3 é convertido para o formato WAV.

Transcrição e tradução de áudio gravado: Após a conversão do formato do áudio gravado, a função transcrever_e_traduzir é chamada para transcrever o áudio em português e traduzi-lo para o inglês.

Note que, para obter a funcionalidade completa do código, é necessário executar o notebook Atvd1.ipynb no ambiente Colaboratory (Colab) ou em outro ambiente Python com os pacotes necessários instalados.
