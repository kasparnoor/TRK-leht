from django.db import models

CLASSMODEL_CHOICES = (
    ('5a','5A'),
    ('5b', '5B'),
    ('6a','6B'),
    ('6b','6B'),
    ('7a','7A'),
    ('7b','7B'),
    ('7c','7C'),
    ('8a','8A'),
    ('8b','8B'),
    ('8c','8C'),
    ('9a','9A'),
    ('9b','9B'),
    ('9c','9C'),
    ('10a','10A'),
    ('10b','10B'),
    ('10c','10C'),
    ('11a','11A'),
    ('11b','11B'),
    ('11c','11C'),
    ('12a','12A'),
    ('12b','12B'),
    ('12c','12C'),
)

class ClassModel(models.Model):
    name            = models.CharField(max_length=3, choices=CLASSMODEL_CHOICES, default='8c')
    head_teacher           = models.CharField(max_length=40)
    def __str__(self):
        return self.name