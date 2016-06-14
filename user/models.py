from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)

class Entry(models.Model):
    user = models.ForeignKey(User,related_name='entries')
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    body = models.TextField()


    def __str__(self):
    	return self.user.username

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)

