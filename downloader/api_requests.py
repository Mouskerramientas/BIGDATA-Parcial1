import requests

from config import API_HEADERS, API_URL
from utils import NotFoundException


def fetch_page(page_index: int):
    """
    Function that downloads a page from the Mitula URL
    with the index of the page to download
    @param page_index: Index of the page to download
    @return: Request response (HTML code)
    """

    query_params = {
        "page": str(page_index),
        "operationType": "sell",
        "propertyType": "mitula_studio_apartment",
        "geoId": "mitula-CO-poblacion-0000014156",
        "text": "Bogot%C3%A1%2C++%28Cundinamarca%29",
    }

    response = requests.get(
        API_URL, params=query_params, headers=API_HEADERS
    )

    if response.status_code == 404:
        raise NotFoundException("❌ Error 404: Página no encontrada")

    if response.status_code != 200:
        raise Exception(f"❌ Error al descargar la página {page_index}: {response.status_code}")

    return response.text
