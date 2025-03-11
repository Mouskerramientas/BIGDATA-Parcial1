import os
import sys
import pytest
import requests
from unittest.mock import patch, MagicMock



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../downloader')))

from api_requests import fetch_page
from config import API_URL, API_HEADERS
from utils import NotFoundException

"""
Test Fetch Page (casas.mitula.com)
"""
def test_fetch_page():
    page_index = 1
    fake_html = "<html><body><h1>Test Page</h1></body></html>"

    # Simulamos requests.get() usando patch
    with patch("requests.get") as mock_get:
        # Creamos un mock de la respuesta de requests.get()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = fake_html
        mock_get.return_value = mock_response  # Hacemos que requests.get() devuelva este mock

        # Llamamos a la función que queremos probar
        response = fetch_page(page_index)

        # Verificamos que se llame correctamente requests.get()
        mock_get.assert_called_once_with(
            API_URL,
            params={
                "page": str(page_index),
                "operationType": "sell",
                "propertyType": "mitula_studio_apartment",
                "geoId": "mitula-CO-poblacion-0000014156",
                "text": "Bogot%C3%A1%2C++%28Cundinamarca%29",
            },
            headers=API_HEADERS
        )

        # Verificamos que la respuesta no sea None y tenga el HTML simulado
        assert response is not None
        assert response == fake_html


def test_fetch_not_found_page():
    page_index = 1

    # Simulamos requests.get() usando patch
    with patch("requests.get") as mock_get:
        try:
            # Creamos un mock de la respuesta de requests.get()
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response  # Hacemos que requests.get() devuelva este mock

            # Llamamos a la función que queremos probar
            response = fetch_page(page_index)

            # Verificamos que se llame correctamente requests.get()
            mock_get.assert_called_once_with(
                API_URL,
                params={
                    "page": str(page_index),
                    "operationType": "sell",
                    "propertyType": "mitula_studio_apartment",
                    "geoId": "mitula-CO-poblacion-0000014156",
                    "text": "Bogot%C3%A1%2C++%28Cundinamarca%29",
                },
                headers=API_HEADERS
            )

            # Exception not catched
            assert False

        except NotFoundException:
            # Exception catched correctly
            assert True
