from bs4 import BeautifulSoup


def extract_info(house):
    """
    Function to extract the information from the HTML content
    @param house: HTML content of the house
    @return: List with the information of the house
    """

    valor = house.get("data-price")
    barrio = house.get("data-location")
    num_habitaciones = house.get("data-rooms")
    mts2 = house.get("data-floorarea")
    num_banos = 0
    banos_tag = house.find("p", {"data-test": "bathrooms"})
    if banos_tag:
        num_banos = banos_tag.text.strip().split()[0]  # Extrae solo el número

    return [barrio, valor, num_habitaciones, num_banos, mts2]


def extract_and_parse_info(html_content, curr_date):
    """
    Function to extract and parse the information from the HTML content
    @param html_content: HTML content of the houses
    @param curr_date: Current date
    @return: List with the information of the houses
    """

    soup = BeautifulSoup(html_content, "html.parser")

    houses_data = []

    for house in soup.find_all("a", class_="listing listing-card"):
        houses_data.append([curr_date] + extract_info(house))

    return houses_data
