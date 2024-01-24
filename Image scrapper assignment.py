#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape video data
def scrape_video_data():
    url = "https://www.youtube.com/@PW-Foundation/videos"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        videos = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-grid-video-renderer')

        data = []
        for video in videos[:5]:
            video_url = "https://www.youtube.com" + video['href']
            thumbnail_url = video.find('img')['src']
            title = video.find('span', {'class': 'style-scope ytd-grid-video-renderer'}).text
            views = video.find('span', {'class': 'style-scope ytd-grid-video-renderer'}).text
            post_time = video.find('span', {'class': 'style-scope ytd-grid-video-renderer'}).text

            data.append([video_url, thumbnail_url, title, views, post_time])

        return data
    else:
        print("Error accessing the website.")
        return None

# Function to save data to CSV file
def save_to_csv(data, filename='video_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Video URL', 'Thumbnail URL', 'Title', 'Views', 'Post Time'])
        writer.writerows(data)

# Main function
if __name__ == "__main__":
    video_data = scrape_video_data()

    if video_data:
        save_to_csv(video_data)
        print("Data scraped and saved to 'video_data.csv'")
    else:
        print("Unable to scrape data.")


# In[ ]:




