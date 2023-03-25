# FLarm

from decimal import Decimal

from ... import nmea

class FLA(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        name = manufacturer + data[0]
        cls = _cls.sentence_types.get(name, _cls)
        return super(FLA, cls).__new__(cls)

    def __init__(self, manufacturer, data):
        self.sentence_type = manufacturer + data[0]
        super(FLA, self).__init__(manufacturer, data)


class FLAU(FLA):
    """ # PFLAU,<RX>,<TX>,<GPS>,<Power>,<AlarmLevel>,<RelativeBearing>,<AlarmType>,
    <RelativeVertical>,<RelativeDistance>,<ID>
    """
    fields = (
        ("Subtype", "type"),
        ("Number of aircrafts received", "rx", int),
        ("Transmission status", "tx", int),
        ("GPS status", "gps", int),
        ("Power status", "power", int),
        ("Alarm Level", "alarm_level", int),
        ("Relative Bearing", "bearing", int),
        ("Alarm Type", "alarm_type", int),
        ("Relative Vertical", "vertical", int),
        ("Relative Distance", "distance", int),
        ("Hex Identifier", "id"),
    )

class FLAA(FLA):
    """ PFLAA,<AlarmLevel>,<RelativeNorth>,<RelativeEast>, <RelativeVertical>,
    <IDType>,<ID>,<Track>,<TurnRate>,<GroundSpeed>, <ClimbRate>,<AcftType>

    $PFLAA,0,-4679,-7787,7097,1,4B0295!ADS_4B0295,284,,183,9.1,9*4E
    """
    fields = (
        ("Subtype", "type"),
        ("Alarm Level", "alarm_level", int),
        ("Relative North", "north", int),
        ("Relative East", "east", int),
        ("Relative Vertical", "vertical", int),
        ("ID Type", "id_type", int),
        ("Identifier", "id"),
        ("Track", "track", int),
        ("Turn Rate", "turn_rate"),
        ("Ground Speed", "gs", int),
        ("Climb Rate", "climb_rate", Decimal),
        ("Aircraft Type (Hex)", "type"),
      
    )

