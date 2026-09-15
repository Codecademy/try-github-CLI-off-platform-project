import random

ANSWERS = (
    "Yes - definitely",
    "It is decidedly so",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
)

def ask_magic_8_ball(name: str, question: str) -> None:
    """Print a random answer to a question."""
    random_number = random.randint(1, len(ANSWERS))

    match random_number:
        case 1:
            answer = "Yes - definitely"
        case 2:
            answer = "It is decidedly so"
        case 3:
            answer = "Without a doubt"
        case 4:
            answer = "Reply hazy, try again"
        case 5:
            answer = "Ask again later"
        case 6:
            answer = "Better not tell you now"
        case 7:
            answer = "My sources say no"
        case 8:
            answer = "Outlook not so good"
        case 9:
            answer = "Very doubtful"
        case _:
            answer = "Error"

    print(f"{name} asks: {question}")
    print(f"Magic 8 Ball's answer: {answer}")

if __name__ == "__main__":
    ask_magic_8_ball("Joe", "Will I win the lottery?")
