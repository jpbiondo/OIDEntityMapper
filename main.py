from entities.entity_mapper import EntityMapper
from entities.oid_entity_mapper import OIDEntityMapper

INPUT_FILE = 'data/input_entities_list.txt'
OUTPUT_FILE = 'data/output_oid_entities_list.txt'

def map_entities_file_to_oid(input_file, output_file):
    entityMapper = EntityMapper()
    oidEntityMapper = OIDEntityMapper()

    with open(input_file, 'r') as infile:
        entities_lines = infile.readlines()

    entities_oids_list= [ oidEntityMapper.entity_to_OIDEntity(entityMapper.map_text_to_entity(entity_line)) for entity_line in entities_lines ]

    with open(output_file, 'w') as outfile:
        for entity in entities_oids_list:
            outfile.write(entityMapper.map_entity_to_text(entity) + '\n')


map_entities_file_to_oid(INPUT_FILE, OUTPUT_FILE)