import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    'platform': ['Twitter', 'Instagram', 'LinkedIn', 'Twitter', 'Instagram'],
    'text': [
        'Basketball has changes a lot since michael jordan',
        'the Customer Service was very unresponsive and bad',
        'Great work environment and helpful colleagues.',
        'Elon Musk is doing really great things on this app(Sarcasm)',
        'The algorithm for the ads are very smartly installed'
    ],
    'trending_topic': [
        '#Basketball',   
        '#CustomerService',
        '#Workplace',
        '#AppFeedback',
        '#Marketing'
    ]
}

df = pd.DataFrame(data)

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'[^A-Za-z\s]', '', text)  
    text = text.lower().strip()  
    return text

df['cleaned_text'] = df['text'].apply(clean_text)

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['cleaned_text'].apply(get_sentiment)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 8))
topics = df['trending_topic'].unique()
fig, axes = plt.subplots(len(topics), 1, figsize=(10, len(topics) * 3), sharex=True)
for i, topic in enumerate(topics):
    topic_data = df[df['trending_topic'] == topic]
    sns.countplot(x='sentiment', data=topic_data, order=['Positive', 'Neutral', 'Negative'], ax=axes[i])
    axes[i].set_title(f'Sentiment for: {topic}')
    axes[i].set_xlabel('')  
    axes[i].set_ylabel('Count')

plt.tight_layout()
plt.show()

output_file = 'manual_sentiment_analysis_with_trending_topics.xlsx'
df.to_excel(output_file, index=False)

print(f"Analysis complete! Results saved to {output_file}")







