from django.db import models

class PatternManager(models.Manager):
    def live(self):
        return super(PatternManager, self).get_query_set().filter(visible=True)

class PatternBase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    visible = models.BooleanField(default=True)
    order = models.IntegerField(default=100)

    objects = PatternManager()

    def __unicode__(self):
	return self.title

    class Meta:
	abstract = True


class PatternCategory(PatternBase):
    class Meta:
	verbose_name_plural = 'Pattern Categories'

    @models.permalink
    def get_absolute_url(self):
        return ('pattern:category', (), { 'category_slug': self.slug })


class Pattern(PatternBase):
    category = models.ForeignKey(PatternCategory, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    markup = models.TextField()
    css = models.TextField( blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        category = self.category.slug if self.category else 'uncategorized'
        return ('pattern:detail', (), {'slug': self.slug })

