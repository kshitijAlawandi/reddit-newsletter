import praw
import config

try:
    reddit = praw.Reddit(
        client_id = config.REDDIT_CLIENT_ID,
        client_secret = config.REDDIT_CLIENT_SECRET,
        user_agent = config.REDDIT_USER_AGENT
    )
    print(f"Reddit Authentication with client secret successful")
except:
    print(f"Reddit Authentication failed")

def fetch_top_posts(subreddits: list, limit: int = 5, time_filter: str = 'week'):
    all_posts = []
    if reddit:
        for sub_reddit in subreddits:
            sub_reddit_name = reddit.subreddit(sub_reddit)

            top_posts = sub_reddit_name.top(time_filter=time_filter, limit=limit)

            for post in top_posts:
                # We only want to summarize text posts, not just links or images
                if post.selftext:
                    post_data = {
                        'id': post.id,
                        'title': post.title,
                        'selftext': post.selftext,
                        'url': post.url,
                        'score': post.score,
                        'subreddit': sub_reddit_name,
                    }
                    all_posts.append(post_data)

            print(f"Successfully fetched {len(all_posts)} text-based posts.")
            return all_posts
    return None