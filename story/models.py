from django.db import models
from operator import itemgetter
import wikipedia

# Create your models here.

class Events(models.Model):
    date = models.IntegerField()
    PERIOD = (
    (1, 'Préhistoire'), (2, 'Première antiquité'), (3, 'VIème siècle av-jc'),
    (4, 'Vème siècle av-jc'),(5, 'IVème siècle av-jc'),(6, 'IIIème siècle av-jc'),
    (7, 'IIème siècle av-jc'),(8, 'Ier siècle av-jc'), (9, 'Ier siècle'),
    (10, 'IIème siècle'),(11, 'IIIème siècle'),(12, 'IVème siècle'),
    (13, 'Vème siècle'),(14, 'VIème siècle'), (15, 'VIIème siècle'),
    (16, 'VIIIème siècle'),(17, 'IXème siècle'),(18,'Xème siècle'),
    (19, 'XIème siècle'),(20, 'XIIème siècle'),(21, 'XIIIème siècle'),
    (22, 'XIVème siècle'),(23, 'XVème siècle'), (24, 'XVIème siècle'),
    (25, 'XVIIème siècle'),(26, 'XVIIIème siècle'),(27,'XIXème siècle'),
    (28, 'XXème siècle'),(29, 'XXIème siècle'),
    )
    period = models.IntegerField(choices = PERIOD)
    name = models.CharField(max_length=200, unique=True)
    autor = models.CharField(max_length=200)
    comment = models.TextField()
    HISTOIRE = 'HI'
    SCIENCE = 'SC'
    RELIGION = 'RE'
    SPORT = 'SP'
    ART = 'LI'
    PHILOSOPHIE = 'PH'
    CATEGORY = (
        (HISTOIRE, 'Histoire'),
        (SCIENCE, 'Science'),
        (RELIGION, 'Religion'),
        (SPORT, 'Sport'),
        (ART, 'art'),
        (PHILOSOPHIE, 'Philosophie'),
    )
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
        default=HISTOIRE,
    )
    theme = models.CharField(max_length=200)
    wiki = models.URLField()
