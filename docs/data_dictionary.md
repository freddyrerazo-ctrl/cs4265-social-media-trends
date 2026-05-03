# Data Dictionary

## Input Schema (raw_tweets.csv)
| Field | Type | Description |
|-------|------|-------------|
| platform | String | Social media platform |
| post_id | String | Unique post identifier |
| user_id | String | Unique user identifier |
| username | String | Username |
| user_verified | Boolean | Verified account flag |
| user_followers_count | Integer | Follower count |
| user_location | String | User location |
| post_text | String | Post content |
| language | String | Language of post |
| hashtags | String | Hashtags used |
| mentions | String | User mentions |
| post_length | Integer | Character count |
| like_count | Integer | Number of likes |
| comment_count | Integer | Number of comments |
| share_count | Integer | Number of shares |
| engagement_score | Float | Engagement metric |
| posted_datetime | String | Post timestamp |
| day_of_week | String | Day posted |
| is_trending_topic | Boolean | Trending flag |
| topic_category | String | Topic classification |
| sentiment_label | String | Sentiment category |
| sentiment_score | Float | Sentiment value |
| emotion_label | String | Emotion category |
| toxicity_score | Float | Toxicity value |
| sarcasm_detected | Boolean | Sarcasm flag |
| spam_flag | Boolean | Spam flag |
| data_source_url | String | Source URL |

## Output Schema
| Field | Type | Description |
|-------|------|-------------|
| platform | String | Social media platform |
| post_id | String | Post identifier |
| username | String | Username |
| topic_category | String | Topic classification |
| sentiment_score | Float | Sentiment value |
| viral_impact | Float | engagement_score * like_count |
| prediction | Integer | KMeans cluster (0-4) |
