# OID Entity Mapper

## Overview

The **OID Entity Mapper** is a Python project designed to take text-format entities from an input file and map them to generate **unique identifiers** using** OID pattern**. This pattern is useful when persisting in relational databases as it creates identifiers which decouples tables from business attributes, allowing them to be uniquely identified in a database with that new identifier as a primary key.
## Motivation
I did the program as a way to get insights on how OID works and help me to do a college work.

## Input Format

The input file (`data/input_entities_list.txt`) should contain a list entities in different lines in the following format:
```
EntityDefinition := EntityName '=' AttributeList
EntityName := identifier
AttributeList := Attribute ( '+' Attribute )*
Attribute := PrimaryKeyAttribute | ForeignKeyAttribute | RegularAttribute
PrimaryKeyAttribute := '#' identifier | (*# | *#) identifier
ForeignKeyAttribute := '*' ForeignEntityName identifier
RegularAttribute := identifier
ForeignEntityName := identifier
identifier := [a-zA-Z_][a-zA-Z0-9_]*
```
### Example of valid inputs
```
User = #userId + name + *#addressId
Address = #addressId + street + city
```
### Output format
The output file (`data/output_oid_entities_list`) will contain the mapped entities with their unique identifiers (OIDPatterns).
### Example of expected output
Given the next input in `data/input_entities_list.txt`:
```
User = #userId + name + *#addressId
Address = #addressId + street + city
```
The expected output in `data/output_oid_entities_list` file would be:
```
User = #OIDUser + name + *OIDAddress
Address = #OIDAddress + street + city + *OIDUser
```
## Installation
1. Clone the repository:
```sh
git clone https://github.com/yourusername/oid-entity-mapper.git
cd oid-entity-mapper
```
2. Create a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Usage
1. Place your inputs in the `input_entities_list.txt` file in the data directory.
2. Run the script:
```sh
python main.py
```
3. The output will be saved in the data directory as `output_oid_entities_lis`.

##Contributing
Contributions and suggestions are welcome!  If you want to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
```sh
git checkout -b feature/your-feature-name
```
3.  Make your changes and commit them:
```sh
git commit -m "Add your feature or fix"
```
4. Push your changes to your fork:
```sh
git push origin feature/your-feature-name
```
5.  Open a pull request on the main repository.
