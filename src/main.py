from reddit_client import stream_comments
from prompt_filter import extract_food_prompt


def handle_comment(comment):
    text = comment.body
    prompt = extract_food_prompt(text)

    if prompt:
        print("\n==============================")
        print("NEW FOOD PROMPT DETECTED:")
        print(prompt)
        print("==============================\n")
        # to do: connect image model (not yet)


def main():
    for comment in stream_comments():
        try:
            handle_comment(comment)
        except Exception as e:
            print("Error processing a comeent:", e)


if __name__ == "__main__":
    main()
