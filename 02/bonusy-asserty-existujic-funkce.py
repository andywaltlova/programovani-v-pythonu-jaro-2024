################################################################################
# -- Cilem je napsat asserty ktere overi ze funkce dela to co predpokladame -- #
################################################################################


# Function: find_pet(housing_type, activity_level)
# Definition: Define a function that suggests a pet based on a user's lifestyle.
# Parameters:
# housing_type (string): Type of housing the user lives in (e.g., "apartment", "house with yard", "small apartment").
# activity_level (string): User's activity level (e.g., "busy", "active", "calm").

def find_pet(housing_type, activity_level):
    if housing_type == "apartment":
        if activity_level == "busy":
            return "Cat"
        elif activity_level == "calm":
            return "Fish"
    elif housing_type == "house with yard":
        return "Dog"
    elif housing_type == "small apartment":
        return "Hamster"

# TODO: asserty

# Function: plan_vacation(destination_type, preference)
# Definition: Define a function that plans a vacation destination based on the user's preferences.
# Parameters:
# destination_type (string): Type of destination preferred by the user (e.g., "beach", "mountains", "city").
# preference (string): User's preference for the vacation (e.g., "relaxation", "adventure", "culture").

def plan_vacation(destination_type, preference):
    if destination_type == "beach":
        return "Maldives" if preference == "relaxation" else "Phuket"
    elif destination_type == "mountains":
        return "Swiss Alps" if preference == "adventure" else "Aspen"
    elif destination_type == "city":
        return "Tokyo" if preference == "culture" else "New York City"

# TODO: asserty

# Function: guess_celebrity(field, descriptor, fact)
# Definition: Define a function that gives clues for guessing a celebrity based on the user's interest.
# Parameters:
# field (string): Field of fame the celebrity is known for (e.g., "actor", "musician", "scientist").
# descriptor (string): Descriptor of the celebrity's achievement or fame (e.g., "Oscar winner", "pop star", "theory of relativity").

def guess_celebrity(field, descriptor, fact):
    if field == "actor":
        return "Johnny Depp" if "Oscar winner" in descriptor else "Leonardo DiCaprio"
    elif field == "musician":
        return "Michael Jackson" if "pop star" in descriptor else "Elvis Presley"
    elif field == "scientist":
        return "Albert Einstein" if "theory of relativity" in descriptor else "Isaac Newton"

# TODO: asserty
