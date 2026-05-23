import random

quotes = [
    {
        "quote": "I am the greatest artist that God has ever created.",
        "answer": "kanye"
    },
    {
        "quote": "The broad masses are more easily fooled than inspired.",
        "answer": "hitler"
    },
    {
        "quote": "I still think I am the best.",
        "answer": "kanye"
    },
    {
        "quote": "Strength lies not in defense but in attack.",
        "answer": "hitler"
    },
    {
        "quote": "I refuse to accept other people's ideas of happiness for me.",
        "answer": "kanye"
    },
    {
    
        "quote": "I am Warhol. I am the number one most impactful artist of our generation.",
        "answer": "kanye"
    },
    {
        "quote": "If you tell a big enough lie and repeat it frequently enough, it will be believed.",
        "answer": "hitler"
    },
    {
        "quote": "My greatest pain in life is that I will never be able to see myself perform live.",
        "answer": "kanye"
    },
    {
        "quote": "The victor will never be asked if he told the truth.",
        "answer": "hitler"
    },
    {
        "quote": "For me giving up is way harder than trying.",
        "answer": "kanye"
    },
    {
        "quote": "He alone, who owns the youth, gains the future.",
        "answer": "hitler"
    },
    {
        "quote": "I feel like I'm too busy writing history to read it.",
        "answer": "kanye"
    },
    {
        "quote": "Words build bridges into unexplored regions.",
        "answer": "hitler"
    },
    {
        "quote": "I am unquestionably, undoubtedly, the greatest human artist of all time.",
        "answer": "kanye"
    },
    {
        "quote": "Great strength lies in detail.",
        "answer": "hitler"
    }
]

score = 0

print("Welcome to 'Kanye or Hitler?'")
print("▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷")

random.shuffle(quotes)

for q in quotes:
    print("\nQuote:")
    print(f'"{q["quote"]}"')

    guess = input("Who said it? (kanye/hitler): ").lower()

    if guess == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! It was {q['answer']}")

print("\nGame Over!")
print(f"Your final score: {score}/{len(quotes)}")
