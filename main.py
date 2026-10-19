import sys

from bs4 import BeautifulSoup
import requests


def raspar_dados_web() -> list[dict[str, str]]:
    url = "https://quotes.toscrape.com/"
    print(f"Acessando o site: {url}...")

    headers = {"User-Agent": "Mozilla/5.0 (compatible; ColetorDeCitacoes/1.0)"}
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        resposta.raise_for_status()
    except requests.RequestException as erro:
        raise RuntimeError(f"Não foi possível acessar {url}: {erro}") from erro

    soup = BeautifulSoup(resposta.text, "html.parser")
    elementos = soup.select("div.quote")
    if not elementos:
        raise ValueError("Nenhuma citação foi encontrada; a estrutura da página pode ter mudado.")

    citacoes = []
    for indice, elemento in enumerate(elementos, 1):
        texto = elemento.select_one("span.text")
        autor = elemento.select_one("small.author")
        if texto is None or autor is None:
            raise ValueError(f"A citação {indice} não contém texto ou autor no formato esperado.")

        citacoes.append({"texto": texto.get_text(strip=True), "autor": autor.get_text(strip=True)})

    return citacoes


def main() -> int:
    try:
        citacoes = raspar_dados_web()
    except (RuntimeError, ValueError) as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 1

    print(f"\n--- ENCONTRADAS {len(citacoes)} CITAÇÕES ---")
    for indice, citacao in enumerate(citacoes, 1):
        print(f"{indice}. {citacao['texto']} — [{citacao['autor']}]")

    # Melhoria futura: seguir o link "Próxima" para coletar todas as páginas.
    # Melhoria futura: salvar os registros em CSV ou JSON para reutilizá-los.
    return 0


if __name__ == "__main__":
    sys.exit(main())
