import pytest

import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../extract_info')))

from proyecto import extract_info


def test_extract_empty_info():

    html_content = ""

    curr_date = "2025-03-10"

    result = extract_info(html_content, curr_date)

    assert len(result) == 0


def test_extract_info_content():

    html_content = """
    <html>
        <body>
            <a class="listing listing-card" data-price="200000" data-location="Bogotá" 
            data-rooms="2" data-floorarea="50">
                <p data-test="bathrooms">1 baño</p>
            </a>
        </body>
    </html>
    """

    curr_date = "2025-03-10"

    expected_result = [["2025-03-10", "Bogotá", "200000", "2", "1", "50"]]

    result = extract_info(html_content, curr_date)

    # Compare both results
    assert result == expected_result

def test_extract_info_no_bathrooms():
    
    html_content = """
    <html>
        <body>
            <a class="listing listing-card" data-price="200000" data-location="Bogotá" 
            data-rooms="2" data-floorarea="50">
            </a>
        </body>
    </html>
    """

    curr_date = "2025-03-10"

    expected_result = [["2025-03-10", "Bogotá", "200000", "2", 0, "50"]]

    result = extract_info(html_content, curr_date)

    assert result == expected_result

def test_extract_info():

    html_content = """
    <html>
        <body>
            <a class="listing listing-card" data-price="200000" data-location="Bogotá" 
            data-rooms="2" data-floorarea="50">
                <p data-test="bathrooms">1 baño</p>
            </a>
            <a class="listing listing-card" data-price="300000" data-location="Bogotá" 
            data-rooms="3" data-floorarea="70">
                <p data-test="bathrooms">2 baños</p>
            </a>
        </body>
    </html>
    """

    curr_date = "2025-03-10"

    result = extract_info(html_content, curr_date)

    assert len(result) == 2
    assert result[0] == ["2025-03-10", "Bogotá", "200000", "2", "1", "50"]
    assert result[1] == ["2025-03-10", "Bogotá", "300000", "3", "2", "70"]