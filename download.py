
import requests
from bs4 import BeautifulSoup

def get_image_sources(url) -> str:
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all img tags and get their src attribute
        img_sources = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
        
        return img_sources[0]
    else:
        # If the request was unsuccessful, print an error message
        print(f"Failed to retrieve page: {url}")
        return "not_found"

# Example usage:
if __name__ == "__main__":
    gifs = []

    # URL of the webpage you want to extract image sources from
    webpage_urls = [
        "http://1x-upon.com/~despens/olia/summer/",
        "http://www.newrafael.com/olia/summer/",
        "http://www.entropy8.com/olia/summer/",
        "http://nikoprincen.com/olia/summer/",
        "http://saskia-aldinger.com/olia/summer/",
        "http://www.sebastianschmieg.com/olia/summer/",
        "http://www.constantdullaart.com/olia/summer/",
        "http://GLI.TC/H/olia/summer/",
        "http://jonaslund.biz/olia/summer/",
        "http://bukk.it/olia/summer/",
        "http://thxalot.org/olia/summer/",
        "http://www.raquelmeyers.com/olia/summer/",
        "http://www.anthonyantonellis.com/olia/summer/",
        "http://kevinbewersdorf.org/olia/summer/",
        "http://www.emiliegervais.com/olia/summer/",
        "http://kimasendorf.com/olia/summer/",
        "http://jamesbridle.com/olia/summer/",
        "http://www.bram.org/olia/summer",
        "http://todayandtomorrow.net/olia/summer/",
        "http://jaka.org/olia/summer/",
        "http://www.leegte.org/olia/summer/",
        #"http://fernandoalfonso.com/olia/summer/",
        "http://www.faithholland.com/olia/summer/",
        "http://www.evan-roth.com/olia/summer/",
        "http://k0a1a.net/olia/summer/",
        "http://reas.com/olia/summer/",
    ]
    
    # Call the function to get image sources
    for webpage_url in webpage_urls:
        image_sources = get_image_sources(webpage_url)
        gifs.append(webpage_url + image_sources)

    # Print the image sources
    for gif in gifs:
        print(gif)