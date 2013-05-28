from django.db import models

class System(models.Model):
    ARMED_AWAY = 1
    ARMED_HOME = 2
    DISARMED = 0
    SYSTEM_STATUS_CHOICES = (
        (ARMED_AWAY, 'Armed Away'), 
        (ARMED_HOME, 'Armed Home'), 
        (DISARMED, 'Disarmed'),
    )

    ALARM_ON = 1
    ALARM_OFF = 0
    ALARM_STATUS_CHOICES = (
        (ALARM_ON, 'Alarm On'),
        (ALARM_OFF, 'Alarm Off'),
    )

    passcode = models.SmallIntegerField(max_length=4)
    status = models.SmallIntegerField(choices=SYSTEM_STATUS_CHOICES, default=DISARMED)
    alarm_status = models.SmallIntegerField(choices=ALARM_STATUS_CHOICES, default=ALARM_OFF)


class Sensor(models.Model):
    name = models.TextField()
    location = models.TextField()
    system = models.ForeignKey('System')

    def __unicode__(self):
        return self.name