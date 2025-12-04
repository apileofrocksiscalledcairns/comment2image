import re

# List of keywords that define “food-related”
FOOD_KEYWORDS = [
    "food", "meal", "dish", "snack", "dessert", "fruit", "vegetable",
    "drink", "beverage", "cuisine", "recipe", "candy", "bread", "pasta",
    "pizza", "burger", "cake", "cookie", "soup", "sandwich", "salad",
]

# Hard block: ban anything that is clearly out-of-scope
BANNED_TOPICS = [
    "weapon", "gun", "violence", "blood", "nsfw", "adult", "politics",
    "war", "explosion", "injury", "trump", "girl", "boy", "fat"
]


def extract_food_prompt(text: str) -> str | None:
    """
    pulls food-related description(s) and ensures the final prompt
    is !ONLY! about food
    """

    lower = text.lower()

    # reject if banned topics appear anywhere
    for banned in BANNED_TOPICS:
        if banned in lower:
            return None

    # detects if any of the food item "keywords" appear
    has_food_keyword = any(word in lower for word in FOOD_KEYWORDS)
    if not has_food_keyword:
        return None

    # clean up text: remove URLs, Reddit formatting, and emojis
    text = re.sub(r"http\S+", "", text)                        # remove URLs
    text = re.sub(r"[\[\]\(\)]", "", text)                     # remove brackets
    text = text.encode("ascii", "ignore").decode()             # remove emojis
    text = re.sub(r"\s+", " ", text).strip()                   # "normalize" whitespace

    # basic length and s check
    if 5 < len(text) < 300:
        return text
    
    return None
