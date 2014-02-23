from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=50)
    desc = models.TextField()
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    blog = models.ForeignKey(Blog)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
