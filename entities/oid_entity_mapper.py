from entities.entity import Entity

import re


FK_CHAR = '*'
PK_CHAR = '#'

class OIDEntityMapper:
    def entity_to_OIDEntity(self, entity):

        oid_attributes_list = []

        for attr in entity.attributes:

            if FK_CHAR in attr and PK_CHAR not in attr:
                self.__map_fk_attribute(attr, oid_attributes_list)

            elif PK_CHAR in attr:
                self.__map_pk_attribute(attr, oid_attributes_list)

            else:
                oid_attributes_list.append(attr)

        oid_attributes_list.append('#OID' + entity.name.capitalize())
        oid_attributes_list.sort()

        return Entity(entity.name, oid_attributes_list)


    def __map_fk_attribute(self, attr, attributes_list):
        new_attr = attr.replace(FK_CHAR, '')
        foreign_entity_name = self.__get_entity_name(new_attr).capitalize()
        attributes_list.append(f'*OID{foreign_entity_name}')


    def __map_pk_attribute(self, attr, attributes_list):
        if FK_CHAR in attr:
            new_attr = attr.replace(FK_CHAR, '').replace(PK_CHAR, '')
            foreign_entity_name = self.__get_entity_name(new_attr).capitalize()
            attributes_list.append(f'*OID{foreign_entity_name}')
        else:
            new_attr = attr.replace(PK_CHAR, '')
            attributes_list.append(new_attr)

    def __get_entity_name(self, attribute):
        match = re.match(r'[a-z]+',attribute)
        return match.group(0) if match else attribute

