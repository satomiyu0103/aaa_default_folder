import requests


def main():
    res = requests.get("https://example.com")
    print(res.status_code)


if __name__ == "__main__":
    main()
