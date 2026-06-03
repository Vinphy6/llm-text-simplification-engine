from src.inference import simplify_zero_shot
from src.evaluation import readability_score


def main():

    text = input(
        "Enter text to simplify:\n"
    )


    print("\nOriginal:")
    print(text)


    simplified = simplify_zero_shot(
        text
    )


    print("\nSimplified:")
    print(simplified)


    print("\nOriginal readability:")
    print(
        readability_score(text)
    )


    print("\nSimplified readability:")
    print(
        readability_score(simplified)
    )


if __name__ == "__main__":
    main()