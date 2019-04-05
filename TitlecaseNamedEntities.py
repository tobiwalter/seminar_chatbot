from rasa_nlu.components import Component
# from rasa_nlu import utils
# from rasa_nlu.model import Metadata


class TitlecaseNamedEntities(Component):
    name = "titlecase_named_entities"
    requires = ["entities"]
    provides = ["entities"]
    defaults = {'entities' : ['given-name', 'last-name']}
    language_list = None
    entities_to_convert = []

    def __init__(self, component_config=None):
        super(TitlecaseNamedEntities, self).__init__(component_config)
        self.entities_to_convert = component_config['entities']

        if (len(self.entities_to_convert) == 0):
            self.entities_to_convert = ['given-name','last-name']

    def process(self, message, **kwargs):
        ents = message.get("entities", [])
        if (len(ents)):
            for ent in ents:
                if ent['entity'] in self.entities_to_convert:
                    source_txt = message.text[ent['start']:ent['end']]
                    replacement = source_txt.title()
                    original = ent['value']
                    ent['value'] = replacement
                    ent['modifiers'] = [self.name]