import random

openings = [
    "...You underestimated me.",
    "...They called me insane.",
    "...You laughed at my ideas.",
    "...Society rejected my genius.",
    "...Nobody listened to me."
]

actions = [
    "Now I shall destroy the internet.",
    "The pigeons will rise tonight.",
    "I will rewrite reality itself.",
    "Your WiFi privileges are gone forever.",
    "The moon shall evaporate."
]

reasons = [
    "because I was denied chocolate cake.",
    "all because of one bad group project.",
    "because humanity has disappointed me.",
    "after my calculator stopped working during exams.",
    "because no one appreciated my PowerPoint presentations."
]

plot_twists = [
    "Even the raccoons support my cause...",
    "This was all part of my master plan...",
    "You were doomed from the beginning...",
    "History will remember my name...",
    "The pigeons warned you..."
]

print("▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷")
print(" VILLAIN MONOLOGUE GENERATOR")
print("▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷▶▷\n")

input("Press Enter to generate a villain speech...\n")

speech = (
    random.choice(openings) + "\n" +
    random.choice(actions) + "\n" +
    random.choice(reasons) + "\n" +
    random.choice(plot_twists)
)

print("YOUR MONOLOGUE:\n")
print(speech)
