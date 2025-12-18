from src.utils import initialise_portfolio


def main():
    portfolio = initialise_portfolio()

    print(portfolio.model_dump())


if __name__ == "__main__":
    main()
