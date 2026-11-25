import requests

GITHUB_ZEN_URL = "https://api.github.com/zen"


def fetch_github_zen() -> str:
    """يسحب حكمة عشوائية من واجهة GitHub Zen API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-zen-cli-python",
    }
    response = requests.get(GITHUB_ZEN_URL, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text.strip()


def main() -> None:
    try:
        quote = fetch_github_zen()
        border = "=" * (len(quote) + 6)
        print(f"\n{border}")
        print(f"  💡 {quote}")
        print(f"{border}\n")
    except requests.exceptions.RequestException as err:
        print(f"❌ تعذّر الاتصال بـ GitHub: {err}")


if __name__ == "__main__":
    main()