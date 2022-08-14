import json

from fastapi.testclient import TestClient

from reactions_api.main import app

# definie clinet
client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_post_valid_data():
    # define valid smiles code
    isopropanol_smiles = "CC(C)O"
    # define valid reaction SMARTS
    reaction_smarts = "[#6:1][O:2]>>[#6:1]=[O:2]"
    # define valid response
    acetone = "CC(C)=O"
    # define data
    data = {"reaction_smarts": reaction_smarts, "reactants": isopropanol_smiles}
    # send response
    response = client.post("/", params=data)
    # test status and data
    assert response.status_code == 200
    assert response.json() == [acetone]


def test_post_invalid_smiles():
    # define invalid smiles code
    isopropanol_smiles = "CC(C)O_BAD_404"
    # define valid reaction SMARTS
    reaction_smarts = "[#6:1][O:2]>>[#6:1]=[O:2]"
    # define valid response
    valid_response = {"detail": "Reactants SMILES code is invalid"}
    # define data
    data = {"reaction_smarts": reaction_smarts, "reactants": isopropanol_smiles}
    # send response
    response = client.post("/", params=data)
    # test status and data
    assert response.status_code == 400
    assert response.json() == valid_response


def test_post_invalid_smarts():
    # define valid smiles code
    isopropanol_smiles = "CC(C)O"
    # define invalid reaction SMARTS
    reaction_smarts = "[#6:1][O:2]>>[#6:1]=[O:2]_BAD_404"
    # define valid response
    valid_response = {"detail": "Reaction SMARTS code is invalid"}
    # define data
    data = {"reaction_smarts": reaction_smarts, "reactants": isopropanol_smiles}
    # send response
    response = client.post("/", params=data)
    # test status and data
    assert response.status_code == 400
    assert response.json() == valid_response
