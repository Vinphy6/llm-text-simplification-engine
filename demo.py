from src.inference import (
    simplify_zero_shot,
    simplify_fine_tuned
)
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

    
    finetuned = simplify_fine_tuned(
        text,
        "ft:gpt-4o-mini-2024-07-18:personal::Dn5uTSHC"
    )

    print("\nSimplified:")
    print(simplified)


    print("\nFinetuned:")
    print(finetuned)


    print("\nOriginal readability:")
    print(
        readability_score(text)
    )


    print("\nSimplified readability:")
    print(
        readability_score(simplified)
    )


    print("\nFinetuned readability:")
    print(
        readability_score(finetuned)
    )

    
if __name__ == "__main__":
    main()