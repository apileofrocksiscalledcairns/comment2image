import praw

def create_reddit_client():
    return praw.Reddit(
        client_id="TO BE DETERMINED, SENT REQUEST 12/3/25",
        client_secret="TO BE DETERMINED, SENT REQUEST 12/3/25",
        user_agent="food_prompt_extractor:1.0"
    )


def stream_comments(subreddit_name="comment2img"):
    reddit = create_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    print(f"lisstening to r/{subreddit_name}…")

    for comment in subreddit.stream.comments(skip_existing=True):
        yield comment
