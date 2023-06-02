import json
import pytest
from app import app, colleagues

client = app.test_client()

def test_user_adds_colleague_with_valid_city_to_dataset():
    data = {"name": "Martin", "city": "Berlin"}
    response = client.post("/add_colleague", json=data)

    assert len(colleagues) == 1
    assert response.status_code == 200


def test_user_gets_map_with_pins():
    response = client.get("/map")

    assert response.status_code == 200
    assert b"<html>" in response.data


# User can add colleague to dataset
# takes name and city as input
# adds colleague to dataset
# Visualize html map with pins with name and city
#
#