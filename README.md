# Automatizador de Cliques para League of Legends

Este projeto é um automatizador de cliques desenvolvido para aceitar automaticamente as partidas do League of Legends (LOL). Ele localiza a imagem de confirmação de partida na tela e simula um clique quando a imagem é detectada, facilitando a aceitação das partidas de forma automática.

# Funcionalidades:
Detecta automaticamente a imagem do botão de "Aceitar" ou "Confirmar" e simula o clique para aceitar a partida.
Funciona com base em uma imagem de template, que pode ser personalizada de acordo com a sua necessidade.
O programa continua em execução até que a tecla Q seja pressionada.

# Pré-requisitos
Antes de rodar o programa, você precisa garantir que tem o Python instalado em sua máquina.

Além disso, será necessário instalar as dependências do projeto. Você pode fazer isso utilizando o pip, o gerenciador de pacotes do Python.

# Como rodar o programa
1. Baixe o repositório
Primeiro, baixe ou clone este repositório para sua máquina local. Se você usar o Git, pode rodar o seguinte comando no terminal:

bash
Copiar código
git clone https://github.com/paulinbacana77/ACL-Automa-o-de-Clique-lol-.git
2. Instale as dependências
Dentro da pasta do repositório, crie um ambiente virtual (opcional, mas recomendado) e instale as dependências necessárias utilizando o pip.

No terminal, execute os seguintes comandos:

bash
Copiar código
# Criar um ambiente virtual (opcional)
python -m venv venv

# Ativar o ambiente virtual
## No Windows:
venv\Scripts\activate
## No Linux/MacOS:
source venv/bin/activate

# Instalar as dependências
pip install -r requirements.txt
3. Alterar o caminho da imagem
O código utiliza uma imagem de template chamada 1.jpg para localizar o botão de aceitação da partida. Essa imagem deve ser colocada no mesmo diretório que o script.

Se você deseja usar uma imagem com outro nome ou local, altere o caminho da variável template_path no código. O caminho atual está configurado para um arquivo de imagem com o nome 1.jpg:

python
Copiar código
template_path = r"caminho\do\arquivo\aqui"
4. Rodando o programa
Com as dependências instaladas e o caminho da imagem configurado, basta rodar o script:

bash
Copiar código
python nome_do_script.py
O programa começará a monitorar a tela e aceitar as partidas automaticamente assim que detectar a imagem. Para parar o programa, pressione a tecla Q no seu teclado.

# Como transformar o programa em um executável
Se você deseja transformar este script Python em um executável para rodar sem a necessidade de ter o Python instalado, pode usar o PyInstaller.

Passo 1: Instalar o PyInstaller
Dentro do ambiente virtual (se você estiver usando um), instale o PyInstaller com o seguinte comando:

bash
Copiar código
pip install pyinstaller
Passo 2: Gerar o executável
Para criar o executável, execute o seguinte comando no terminal dentro da pasta do projeto:

bash
Copiar código
pyinstaller --onefile nome_do_script.py
Isso criará um executável no diretório dist dentro da sua pasta de projeto. O comando --onefile indica que o PyInstaller deve gerar um único arquivo executável.

Passo 3: Usando o executável
Após a execução do PyInstaller, o arquivo .exe estará disponível na pasta dist. Agora, você pode simplesmente executar o arquivo gerado para rodar o programa sem precisar instalar o Python.

# Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

# Observações Finais
Alterações na imagem: Se você precisar alterar a imagem usada para localizar o botão de aceitação, basta atualizar o arquivo 1.jpg com uma nova imagem e modificar o caminho no código se necessário.
Uso responsável: Lembre-se de que a automação de tarefas em jogos pode violar os termos de serviço de alguns jogos. Utilize o programa de maneira responsável e por sua conta e risco.
