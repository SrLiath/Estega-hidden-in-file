# Estega - hidden in file
 
 Este é um aplicativo simples de esteganografia desenvolvido com PyQt6.
 Ele permite esconder e extrair arquivos dentro de um arquivo portador
 (como uma imagem ou outro arquivo binário) utilizando a técnica de esteganografia,
 em que os dados ocultos são anexados ao final do arquivo portador.

 ## Funcionalidades

 - **Selecionar arquivo portador**: Permite selecionar um arquivo no qual outro arquivo será escondido.
 - **Selecionar arquivo a esconder**: Permite selecionar o arquivo que será ocultado.
 - **Esconder arquivo**: Esconde o arquivo selecionado dentro do arquivo portador.
 - **Extrair arquivos escondidos**: Extrai os arquivos escondidos dentro do arquivo portador.

 ## Pré-requisitos

 - Python 3.x
 - PyQt6

 ## Instalação

 1. Clone este repositório ou baixe o arquivo.
 2. Instale os pré-requisitos executando:

 ```bash
 pip install pyqt6
 ```

 ## Uso

 1. Execute o script com o seguinte comando:

 ```bash
 python estega.py
 ```

 2. A interface gráfica será aberta com as seguintes opções:
    - Selecionar o arquivo portador.
    - Selecionar o arquivo a esconder.
    - Esconder o arquivo no portador.
    - Extrair arquivos escondidos.

 ## Como funciona?

 - **Esconder arquivo**: O arquivo a ser escondido será anexado ao final do arquivo portador,
 e uma marcação especial (`---FIM_ARQUIVO---`) será escrita para indicar o fim do arquivo oculto.
 
 - **Extrair arquivos escondidos**: O programa tenta localizar essa marcação dentro do arquivo portador
 e extrai todos os dados antes da marcação, salvando-os como arquivos binários.

 ## Exemplo

 1. Selecione um arquivo de imagem ou outro tipo de arquivo como o arquivo portador.
 2. Selecione um arquivo (ex.: um arquivo de texto ou qualquer outro tipo de arquivo) como o arquivo a esconder.
 3. Clique em "Esconder arquivo". O arquivo a esconder será anexado ao arquivo portador.
 4. Clique em "Extrair arquivos escondidos" para salvar o arquivo extraído.

 ## Contribuições

 Se desejar contribuir, sinta-se à vontade para fazer um fork deste repositório,
 adicionar melhorias e enviar pull requests.

 ## Licença

 Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
       
