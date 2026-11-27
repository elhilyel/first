from urllib.error import URLError
from urllib.request import Request, urlopen

GITHUB_ZEN_URL = "https://api.github.com/zen"


def fetch_github_zen() -> str:
    """يسحب حكمة عشوائية من واجهة GitHub Zen API."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-zen-cli-python",
    }
    request = Request(GITHUB_ZEN_URL, headers=headers)
    with urlopen(request, timeout=10) as response:
        return response.read().decode("utf-8").strip()


def main() -> None:
    try:
        quote = fetch_github_zen()
        border = "=" * (len(quote) + 6)
        print(f"\n{border}")
        print(f"  💡 {quote}")
        print(f"{border}\n")
    except URLError as err:
        print(f"❌ تعذّر الاتصال بـ GitHub: {err}")


if __name__ == "__main__":
    main()