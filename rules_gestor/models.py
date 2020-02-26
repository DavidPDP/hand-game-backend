# For more information consult the data model documentation. 
# The model creation is isolated from the framework, this allows 
# decoupling the cohesion between the persistence layer and the business layer.
from django.db import models

class Modes(models.Model):
    name = models.CharField(unique=True, max_length=45)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'it001_modes'

    def __str__(self):
        return self.name


class Moves(models.Model):
    name = models.CharField(unique=True, max_length=45)
    description = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'it001_moves'
    
    def __str__(self):
        return self.name


class Rules(models.Model):
    winner = models.OneToOneField(Moves, models.DO_NOTHING, db_column='winner', primary_key=True)
    loser = models.ForeignKey(Moves, models.DO_NOTHING, db_column='loser', related_name='+')
    mode = models.ForeignKey(Modes, models.DO_NOTHING, db_column='mode')
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'it001_rules'
        unique_together = (('winner', 'loser', 'mode'),)
    
    def __str__(self):
        return self.description
    
    def getWinnerMove(self):
        return self.winner.name
    
    def getLoserMove(self):
        return self.loser.name
