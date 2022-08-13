from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from rdkit import Chem
from rdkit.Chem import AllChem
from itertools import chain

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/", response_description="Reaction performed successfully")
async def root(reaction_smarts:str, reactants:str)->set():
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
    # return set of reactants smiles codes
    return product_smiles