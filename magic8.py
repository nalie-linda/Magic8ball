import random
import sys

def magic8():
    responses = [
        "IT IS CERTAIN", "YOU MAY RELY ON IT", "AS I SEE IT, YES", "OUTLOOK LOOKS GOOD",
        "MOST LIKELY", "IT IS DECIDELY SO", "WITHOUT A DOUBT", "YES, DEFINETLY"]

    while True:
        prompt = input("Ask a magic8 ball question:")
        random_response = random.choice(responses)

        if prompt == "":
            sys.exit()
        else:
            print(random_response)


magic8()
