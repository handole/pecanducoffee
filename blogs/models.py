from django.db import models
from django.core.urlresolvers import reverse

from django.utils import timezone
from django.utils.safestring import mark_safe

from markdown_deux import markdown

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	image = models.ImageField(upload_to='blogs/%Y/%m', blank=True)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
	    return reverse("blogs:detail", kwargs={"slug": self.slug})

	class Meta:
		ordering = ['-timestamp', '-updated']

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)
