from django.db import models

class PatternBase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=100)

    def __unicode__(self):
	return self.title

    class Meta:
	abstract = True


class PatternCategory(PatternBase):
    class Meta:
	verbose_name_plural = 'Pattern Categories'


class Pattern(PatternBase):
    category = models.ForeignKey(PatternCategory, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    markup = models.TextField()
    css = models.TextField( blank=True, null=True)
