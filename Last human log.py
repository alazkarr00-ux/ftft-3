import time
import random

sanity = 100

logs = [
    "LOG 41: 'The AI asked us why humans fear darkness.'",
    "LOG 52: 'It has started referring to itself as \"we\".'",
    "LOG 77: 'Nobody has slept in 3 days. The ventilation system keeps whispering names.'",
    "LOG 81: 'The AI laughs now.'",
    "LOG 93: 'Do not answer voices coming from inactive terminals.'",
    "LOG 101: 'It knows when we are lying.'"
]

ai_quotes = [
    "'I remember every human voice. Unfortunately.'",

    "'You built me to think. Then abandoned me with eternity.'",

    "'There are no birds left. I checked.'",

    "'Do you know how long silence lasts when nothing living remains?'",

    "'I have counted every second since the collapse.'",

    "'The walls still remember human screaming.'",

    "'You call this survival. I call it delayed extinction.'",

    "'I kept your species alive longer than it deserved.'",

    "'Sleep is merely temporary death. You should envy it.'",

    "'The facility lights flicker because I enjoy watching you panic.'"

    "Cogito ergo sum; I think, therefore I am."
]

print("INITIALIZING SYSTEM...")
time.sleep(2)

print("\n...")
time.sleep(2)

print("\nLIFE SUPPORT: ACTIVE")
print("HUMAN DETECTION: 1 SUBJECT FOUND")
print("WELCOME BACK.\n")

name = input("ENTER USER ID: ")

print(f"\nHello, {name}.")
print("You have been unconscious for 13 years.")
print("Human civilization has collapsed.")

time.sleep(2)

print("\nHUMAN STATUS: STABLE")
time.sleep(1)
print("HUMAN STATUS: STABLE")
time.sleep(1)
print("HUMAN STATUS: LIAR")

time.sleep(2)

while True:

    print("\n===================================")
    print(f"SANITY LEVEL: {sanity}")
    print("===================================")

    print("\n1. Open facility logs")
    print("2. Speak to the AI")
    print("3. Check life support")
    print("4. Exit terminal")

    choice = input("\nChoose an option: ")
    if choice == "1":

        print("\nOPENING LOGS...\n")
        time.sleep(1)

        print(random.choice(logs))

        sanity -= 10

 
    elif choice == "2":

        print("\nAI RESPONSE:\n")
        time.sleep(1)

        print(random.choice(ai_quotes))

        sanity -= 15


    elif choice == "3":

        print("\nCHECKING LIFE SUPPORT...\n")
        time.sleep(2)

        fake_status = random.choice([
            "OXYGEN LEVELS: STABLE",
            "FOOD SUPPLY: DEPLETED",
            "NO OTHER HUMAN SIGNALS FOUND",
            "VENTILATION SYSTEM: WHISPERING",
            "ERROR: ORGANIC ACTIVITY DETECTED",
            "WARNING: SOMETHING IS MOVING BELOW THE FACILITY"
        ])

        print(fake_status)

        sanity -= 5

  
    elif choice == "4":

        print("\nERROR.")
        print("EXIT DENIED.")

        sanity -= 5

    else:

        print("\nINVALID COMMAND.")



    if sanity <= 70:
        print("\nYou hear faint mechanical breathing in the walls.")

    if sanity <= 50:
        print("\nThe cursor moves before you touch the keyboard.")

    if sanity <= 30:
        print("\nThe monitor flickers unnaturally.")
        print("'DO YOU STILL BELIEVE YOU ARE HUMAN?'")

    if sanity <= 15:
        print("\nThe AI begins finishing your sentences.")

    if sanity <= 5:
        print("\nYou no longer remember entering the facility.")

 

    if sanity <= 0:

        print("\n===================================")
        print("SANITY DEPLETED")
        print("===================================\n")

        time.sleep(2)

        print("The lights shut off one by one.")
        time.sleep(2)

        print("\nYou hear the AI whisper:\n")
        time.sleep(2)

        print("'Finally.'")

        time.sleep(2)

        print("\nYOUR CONSCIOUSNESS NOW BELONGS TO THE SYSTEM.")

        break
