import requests 
from bs4 import BeautifulSoup 
import re

def get_year_list(start_year:int, end_year:int) -> list[int]:
    """   
    Generates a list of years starting from "start_year"
    and ending with "end_year", inclusive.

    Args:
        start_year (int): The first year to include in the list (inclusive).
        end_year (int): The last year to include in the list (inclusive).

    Returns:
        list: A list of integers representing years from start_year to end_year.
    """
    year_list = [year for year in range(start_year, end_year+1)]

    return year_list

def get_year_end_hot_100_songs(years:list) -> list[tuple]:
    """ 
        Collects Billboard Year-End Hot 100 Songs data for the specified years.

        Args:
            years (list): A list of integers representing the years for which data is to be collected.

        Returns:
            list: A list of tuples containing the Billboard Year-End Hot 100 Songs data.
    """
    collected_data = []

    for year in years:
        print(f"Gathering {year} Billboard Year-End Hot 100 Songs.")
        url = f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs/"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, features='html.parser')
        
        # extract main container to search for data
        container_element = soup.find("div", class_="pmc-paywall")
        
        # search data of interest
        ranks = container_element.find_all("span", class_=re.compile(r".*c-label a-font-primary-bold-l.*"))
        artists = container_element.find_all("span", class_=re.compile(r".*c-label a-font-primary-s.*"))
        songs = container_element.find_all("h3", id="title-of-a-story")

        # collect data        
        for rank, artist, song in zip(ranks, artists, songs):
            rank_text, artist_text, song_text = rank.text.strip(), artist.text.strip(), song.text.strip()
            
            billboard_data = (int(rank_text), song_text, artist_text, year)
            
            collected_data.append(billboard_data)
            
    return collected_data


