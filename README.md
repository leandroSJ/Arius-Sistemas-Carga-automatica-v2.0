# Arius-Sistemas-Carga-automatica-v2.0
Automação de sistemas - Arius Sistemas | Carga e importação de tabelas para o PDV

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

> Execute cargas com apenas 1 clique, escolha um horário para executar as cargas diarias dê preferência aos horários em que sua loja esteja fechada

### O que o Arius-Sistemas-Carga-automatica-v2.0 faz?

- [x] Ele faz todo processo de uma carga completa que você fazeria manualmente
- [x] Loga no erp com usuario e senha fornecido no arquivo config.yaml
- [x] Clica em `Cadastro de produtos(PDV)`
- [x] Clica em SIM nas próximas janelas que aparecer e aguarda 120s para executar a próxima ação
- [x] Fecha o erp `alt+f4`
- [x] Abri o KW
- [x] Loga no kw com usuario e senha fornecido no arquivo config.yaml
- [x] Após realizar os passos para concluir a carga no KW ele fecha o kw emite um aviso `CARGA EFETUADA`



## 💻 Pré-instalação
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Se for compilar novamente faça isso:

* mova a pasta `arius_carga` para a o disco C:\\
* Instale a versão mais recente do `Python` se você não tem instalado em https://www.python.org/
* Pressione Win+R vai abrir uma caixinha com nome de Executar digite `cmd`e presione enter para abrir o cmd
* Ou se preferir abra o menu de aplicativos do windowns e digiete cmd e abra o programa
* Agora volte para o disco digite `cd c:\` e presione enter
* Entre na pasta arius_carga `cd arius_carga`
* Atualize o pip `python -m pip install --upgrade pip`
* Baixe o virtualenv com o `pip install virtualenv`
* Crie um ambiente virtual `python -m venv `amb_virtual`
* Ative seu ambiente virtual `amb_virtual\Scripts\activate.bat`
* Se ficou assim tudo certo `(amb_virtual) c:\arius_carga>`
* Agora basta navegar até a pasta `cd loja\src`
> Agora você está dentro da pasta onde estao os arquivos `carga_loja.py | log.txt | requirements.txt`
lembre-se de alerar o usuário e a senha no arquivo de configuração `config.yaml` após fazer a alteração salve o arquivo


## 🚀 Instalando Arius-Sistemas-Carga-automatica-v2.0

Para instalar o <Arius-Sistemas-Carga-automatica-v2.0>, siga estas etapas:
  
 Suponho que já estar com seu ambiente todo preparado para instalar novos Pacotes

 Vamos instalar todas as pendências:

 pip install -r requirements.txt
 Confira se esta tudo ok com o pip `python -m pip install --upgrade pip`
 
 * Gerando o arquivo .exe `pyinstaller --noconsole --onefile --icon=C:\arius_carga\icon\kw.ico C:\arius_carga\loja\src\carga_loja.py`
 * Va até o disco C:\ e procure a pasta `arius_carga\loja\src`
 * Dentro da pasta `dist`você encontrara o arquivo `carga_loja.exe`
 * Por fim crie um  atalho na área de trabalho para acessar esse arquivo `clique com o botao direito do mouse enviar para area de trabalho`


## 📫 Contribuindo para <Arius-Sistemas-Backup-NFCE-v3.0>
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os 
contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado---> Para contribuir com
<nome_do_projeto>, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.
6. Qualquer dúvida entra em conta via e-mail: leandro.dejesus@outlook.com.br coloca no assunto arius_backup_nfce_v3.0

Como alternativa, consulte a documentação do GitHub em 
[como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.
Desenvolvido com Python3, faça uma versão deste programa em sua linguagem de programação.
