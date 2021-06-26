from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=100)

class Point(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    fill_type = models.CharField(max_length=100)
    color = models.CharField(max_length=100, default="FFF")
    angle = models.IntegerField(null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='points')

    def to_json(self):
        return {

            'id': self.id,
            'name': self.name,
            'description': self.description,
            'points': [self.longitude, self.latitude],
            'fill type': self.fill_type,
            'color': self.color,
            'angle': self.angle

        }
