from django.db.models import *
# from adaptor.model import CsvDbModel


class Player(Model):
    Name = CharField(max_length=50)
    Age = IntegerField()
    Photo = CharField(max_length=100)
    Nationality = CharField(max_length=50)
    Flag = CharField(max_length=100)
    Overall = IntegerField()
    Potential = IntegerField()
    Club = CharField(max_length=50)
    ClubLogo = CharField(max_length=100)
    Value = CharField(max_length=10)
    Wage = CharField(max_length=10)
    PreferredFoot = CharField(max_length=10)
    Position = CharField(max_length=10)
    Height = CharField(max_length=10)
    Weight = CharField(max_length=10)
    Finishing = IntegerField()
    HeadingAccuracy = IntegerField()
    ShortPassing = IntegerField()
    Volleys = IntegerField()
    Dribbling = IntegerField()
    Curve = IntegerField()
    FKAccuracy = IntegerField()
    LongPassing = IntegerField()
    BallControl = IntegerField()
    Acceleration = IntegerField()
    SprintSpeed = IntegerField()
    Agility = IntegerField()
    Reactions = IntegerField()
    Balance = IntegerField()
    ShotPower = IntegerField()
    Jumping = IntegerField()
    Stamina = IntegerField()
    Strength = IntegerField()
    LongShots = IntegerField()
    Aggression = IntegerField()
    Interceptions = IntegerField()
    Positioning = IntegerField()
    Vision = IntegerField()
    Penalties = IntegerField()
    Marking = IntegerField()

    def __str__(self):
        return self.Name


# class MyCsvModel(CsvDbModel):
#     class Meta:
#         dbModel = Player
#         delimiter = ","
#         has_header = True
