# The DTO pattern doesn't have much utility and meaning 
# in not distributed applications. In this particular case, 
# this pattern is used to meet with open-close principle. 
# Therefore, encapsulating the necessary information for 
# transmission between subsystems is key to cohesion and 
# elasticity of the system.
from marshmallow import Schema, fields

class OutputMovesMultimediaDTO(Schema):
    """
    Represents a DTO with well enough data for the user
    """
    move = fields.Str(attribute='winner__name')
    url = fields.Str(attribute='winner__image_url')

class OutputGameMultimediaDTO(Schema):
    """
    Represents a DTO with well enough data for the user
    """
    url = fields.Str(attribute='url')
    moves = fields.Nested(OutputMovesMultimediaDTO(),many=True)