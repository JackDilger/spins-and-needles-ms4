from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    content = models.TextField()
    event_date = models.DateTimeField(max_length=254, null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    event_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    location = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-event_date']

    def __str__(self):
        return self.title
