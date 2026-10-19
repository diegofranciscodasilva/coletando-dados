# Coletor de citações

Projeto simples em Python para praticar coleta de dados da web. O programa acessa o site [Quotes to Scrape](https://quotes.toscrape.com/), extrai o texto e o autor das citações da primeira página e exibe os resultados no terminal.

## Requisitos

- Python 3.9 ou superior (o código usa anotações de tipo com tipos genéricos).
- Acesso à internet.

## Instalação

Abra um terminal na pasta do projeto e instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

Se `python` não apontar para o interpretador desejado no Windows, use o caminho completo dele:

```powershell
& "C:\Python314\python.exe" -m pip install -r requirements.txt
```

## Execução

Na pasta do projeto, execute:

```powershell
python main.py
```

Ou, no Windows, usando o caminho completo do interpretador:

```powershell
& "C:\Python314\python.exe" "C:\Users\diego\Desktop\coletando-dados\main.py"
```

O programa imprime a quantidade de citações encontradas e, em seguida, cada citação com seu autor.

## Como funciona

1. `requests` envia uma requisição HTTPS para o site, com timeout de 10 segundos.
2. A resposta HTTP é verificada; falhas de rede ou respostas de erro são reportadas.
3. `BeautifulSoup` analisa o HTML e localiza os blocos `div.quote`.
4. Para cada bloco, o programa extrai o texto (`span.text`) e o autor (`small.author`).
5. A função `raspar_dados_web()` retorna os registros como uma lista de dicionários; `main()` exibe os resultados.

## Dependências

As dependências do projeto estão registradas em [requirements.txt](requirements.txt):

- `beautifulsoup4`: análise do HTML.
- `requests`: requisições HTTP/HTTPS.

## Limitações e melhorias futuras

- A coleta cobre somente a primeira página. O próprio código contém um comentário indicando onde considerar o suporte à paginação.
- Os resultados são exibidos no terminal, mas ainda não são salvos em CSV ou JSON.
- A extração depende da estrutura HTML atual do site; alterações nela podem exigir ajustes nos seletores.

## 👨‍💻 Autor

### Diego Francisco da Silva

Desenvolvedor Front-End em formação e estudante de Engenharia de Software.

- **[Site Empresa](https://diegofranciscodasilva.github.io/dev-software-web/)**: dev.software.web Site Empresa
- **[LinkedIn](https://www.linkedin.com/in/diego-francisco-da-silva/)**: diego-francisco-da-silva
- **[GitHub](https://github.com/diegofranciscodasilva)**: diegofranciscodasilva
- **[Instagram](https://www.instagram.com/diego_francisco_da_silva/)**: @diego_francisco_da_silva
- **[Instagram](https://www.instagram.com/dev.software.web/)**: @dev.software.web

---

Feito com ❤️ por Diego.
