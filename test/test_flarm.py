import pynmea2

"""
FLARM is working properly and currently receives 3 other aircraft. The most
dangerous of these aircraft is at 11 o’clock, position 32m below and 755m away.
It is a level 2 alarm.
"""
data_flarm1 = "$PFLAU,3,1,2,1,2,-30,2,-32,755*"

"""FLARM is working properly and receives two other aircraft. They are both out of
range."""
data_flarm2 = "$PFLAU,2,1,1,1,0,,0,,,*"

"""
There is a glider in the south-east direction, 1.7km away (1.2km south, 1.2km
east), 220m higher flying on south track with a ground speed of 30m/s in a slight
left turn with 4.5°/s turning rate, sinking with 1.4m/s. Its ID is a static FLARM-ID
“DD8F12”. There is no danger.
"""
data_flarm3 = "$PFLAA,0,-1234,1234,220,2,DD8F12,180,,30,-1.4,1*"


def test_flarm1():
    msg = pynmea2.parse(data_flarm1)
    assert msg.manufacturer == 'FLA'
    assert type(msg) == pynmea2.fla.FLAU
    assert msg.rx == 3
    assert msg.alarm_level == 2
    assert msg.alarm_type == 2
    assert msg.bearing == -30
    assert msg.vertical == -32
    assert msg.distance == 755

def test_flarm2():
    msg = pynmea2.parse(data_flarm2)
    assert msg.manufacturer == 'FLA'
    assert type(msg) == pynmea2.fla.FLAU
    assert msg.rx == 2
    assert msg.alarm_level == 0

def test_flarm3():
    msg = pynmea2.parse(data_flarm3)
    assert msg.manufacturer == 'FLA'
    assert type(msg) == pynmea2.fla.FLAA
    # TODO extend FLAA tests
