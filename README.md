# Reddit Insight Engine 🚀

An automated Python script that fetches top posts from specific subreddits, summarizes them using an AI, and distributes the insights as an email newsletter and social media posts.

## ✨ Features

-   **Multi-Subreddit Fetching**: Pulls the top posts from a predefined list of subreddits (e.g., r/SaaS, r/Entrepreneur).
-   **AI-Powered Summaries**: Leverages a Large Language Model (LLM) like Google's Gemini to generate concise, insightful summaries.
-   **Dual-Format Output**: Creates a short summary for email newsletters and a more detailed version for blog/social media posts.
-   **Automated Distribution**:
    -   Sends formatted emails to a subscriber list via an email service provider.
    -   (Optional) Posts detailed summaries directly to platforms like LinkedIn or Medium.
-   **Scheduled Execution**: Designed to be run automatically on a daily, weekly, or monthly schedule using a cron job or other schedulers.

## ⚙️ How It Works

The script follows a simple, linear flow:

1.  **Fetch**: Connects to the Reddit API to retrieve the top posts from the target subreddits for a given period.
2.  **Summarize**: Sends the collected post titles, content, and top comments to an AI API for summarization.
3.  **Publish**: Uses the generated summaries to format and send content through various publisher APIs (e.g., SendGrid for email, LinkedIn API for posts).

## 🛠️ Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

### 1. Clone the Repository

```bash
git clone [https://github.com/kshitijAlawandi/reddit-newsletter.git]
cd reddit-newsletter