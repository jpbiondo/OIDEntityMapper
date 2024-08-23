from entities.entity import Entity

class EntityMapper:

    def map_text_to_entity(self, entityText):
        entityExpression = entityText.split('=')

        return Entity(
            entityExpression[0].strip(),
            list(map(lambda attr: attr.strip(), entityExpression[1].split('+')))
        )

    def map_entity_to_text(self, entity):
        return (
            '{entityName} = '.format(entityName = entity.name)) + " + ".join(entity.attributes)