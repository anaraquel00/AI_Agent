# AI Project - Assistente de Composição Musical 🎸🤖

## 📖 Visão Geral
O **AI Project** é uma aplicação Python que utiliza inteligência artificial para gerar músicas baseadas em diferentes gêneros musicais. Ele combina progressões de acordes, letras poéticas e referências estilísticas para criar composições únicas. Além disso, a aplicação integra a API do Genius para buscar letras de músicas de bandas icônicas.

## 🏗️ Estrutura do Projeto
```
ai-project/
├── src/
│   ├── app.py                # Arquivo principal da aplicação
│   ├── dicionario_rimas.py   # Dicionário de rimas para geração de letras
│   ├── temas_detalhados.py   # Temas detalhados para cada gênero musical
│   ├── instrucoes_estilisticas.py # Instruções estilísticas para cada gênero
│   └── teste.py              # Script de teste para verificar dependências
├── requirements.txt          # Lista de dependências do projeto
├── .gitignore                # Arquivos e pastas ignorados pelo Git
├── README.md                 # Documentação do projeto
└── LICENSE                   # Licença do projeto
```

## 🚀 Funcionalidades
- **Geração de músicas personalizadas**:
  - Letras baseadas em temas específicos de cada gênero musical.
  - Progressões de acordes estilisticamente adequadas.
- **Integração com a API do Genius**:
  - Busca letras de músicas de bandas icônicas relacionadas ao gênero selecionado.
- **Interface Gradio**:
  - Interface gráfica para facilitar a interação com o usuário.

## 🛠️ Instalação
Siga os passos abaixo para configurar o projeto:

1. Clone o repositório:
   ```bash
   git clone <repository-url>
   cd ai-project
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure a API Key do Genius:
   - Obtenha um **Client Access Token** no [Genius API](https://genius.com/api-clients).
   - Substitua o valor da variável `GENIUS_API_KEY` no arquivo `app.py` pela sua chave.

## 🖥️ Uso
Para executar a aplicação, use o seguinte comando:

```bash
python3 src/app.py
```

A interface Gradio será aberta no navegador. Siga os passos abaixo:
1. Insira seu nome.
2. Escolha um subgênero musical.
3. Clique no botão "Criar Música".
4. Visualize a banda referência, progressão de acordes, letra gerada e letra de uma música da banda.

## 🎵 Exemplos de Saída
### Entrada:
- Nome: `Seu_Nome`
- Subgênero: `Alternative Rock`

### Saída:
- **Banda Referência**: Radiohead
- **Progressão de Acordes**: I-IV-V | I-vi-IV-V | IV-I-V-vi
- **Letra Gerada**:
  ```
  INTRO:
  [Riffs marcantes, refrões]
  Rebelião urbana rompe as barreiras opressão social
  Gritos abafados constroem um novo amanhã corrupção governamental
  ...
  ```
- **Letra da Banda**:
  ```
  Creep

  When you were here before
  Couldn't look you in the eye
  You're just like an angel
  Your skin makes me cry
  ...
  ```

## 🧪 Testes
Para verificar se todas as dependências estão instaladas corretamente, execute o script de teste:

```bash
python3 src/teste.py
```

Se o módulo `lyricsgenius` for importado com sucesso, a mensagem `lyricsgenius importado com sucesso!` será exibida.

## 📂 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou correções de bugs.

## 📜 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## 📧 Contato
Se tiver dúvidas ou sugestões, entre em contato pelo e-mail: `anaraquel00@gmail.com`.

---
**Divirta-se criando músicas incríveis com o AI Project! 🎶**