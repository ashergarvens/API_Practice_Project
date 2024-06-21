from googleapiclient.discovery import build
import json
import sqlalchemy as db
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyBTPjZm-mB9TXuje8Gc1u8ofqR-Jbx990I'
youtube = build('youtube', 'v3', developerKey=api_key)


def fetch_videos(query, max_results=5):
    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=max_results
    )
    response = request.execute()
    return response['items']


# Fetch video data
videos = fetch_videos('Python programming')
print(json.dumps(videos, indent=4))

# Extract relevant fields and create a DataFrame
data = []
for video in videos:
    video_data = {
        'videoId': video['id'].get('videoId', ''),
        'title': video['snippet']['title'],
        'description': video['snippet']['description'],
        'channelTitle': video['snippet']['channelTitle'],
        'publishedAt': video['snippet']['publishedAt']
    }
    data.append(video_data)

df = pd.DataFrame(data)
print(df)

# Create an SQLite engine
engine = db.create_engine('sqlite:///youtube_videos.db')

# Insert DataFrame into the SQLite database
df.to_sql('videos', con=engine, if_exists='replace', index=False)

# Verify the data insertion by querying the database
with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM videos;")).fetchall()
    print(pd.DataFrame(query_result))
