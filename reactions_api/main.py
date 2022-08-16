from itertools import chain

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from rdkit import Chem
from rdkit.Chem import AllChem

output_limit = 20 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/", response_description="Reaction performed successfully")
async def root(reaction_smarts: str, reactants: str) -> dict():
    """
    Run the reaction SMARTS on reactants supplied in SMILES

    Example input:

    {"reaction_smarts": "[c:8]-[c:6]>>[c:8][I:55].[B:99][c:6]", "reactants": "CC1=CC=C(C=C1)C1=CC(=CC=C1C)C1=CC(C)=CC(C)=C1"}

    - **reaction_smarts**: valid SMARTS code for reaction
    - **reactants**: valid SMILES code for reactants

    Example output:

    List of SMILES codes (reaction products)

    {"products":["Cc1ccc(I)cc1", "Bc1ccc(C)c(-c2ccc(C)cc2)c1","Cc1ccc(-c2cc(I)ccc2C)cc1"]}
    """
    # validate reaction smarts and create reaction object from smarts
    try:
        # create rdkit reaction object from smarts
        reaction = AllChem.ReactionFromSmarts(reaction_smarts)
    except ValueError:
        # raise an exception if reaction is invalid
        raise HTTPException(status_code=400, detail="Reaction SMARTS code is invalid")
    # create rdkti molecule object from smiles
    molecule = Chem.MolFromSmiles(reactants)
    # raise an error if smiles is invalid
    if not molecule:
        raise HTTPException(status_code=400, detail="Reactants SMILES code is invalid")
    # run reaction on molecule to get reactants
    reactants = reaction.RunReactants((molecule,))
    # transform reactants tuples to plain list
    reactants_list = list(chain.from_iterable(reactants))
    # create empty to return unique reactants
    product_smiles = set()
    # iterate over reactants to get run clining and get unique values
    # collect molecules smiles codes in set
    for mol in reactants_list:
        if mol:
            # try to clean molecule structure
            try:
                Chem.SanitizeMol(mol)
            except ValueError:
                print("Sanitization failed.")
            # get SMILES code from molecule
            smi = Chem.MolToSmiles(mol)
            # check if code is unique and add to set
            if smi not in product_smiles:
                product_smiles.add(smi)
    # limit output to defined number
    products_smiles_list = list(product_smiles)[0:20]
    # return set of reactants smiles codes
    return {"products":products_smiles_list}
