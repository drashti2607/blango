from django.contrib import admin
from blog.models import Tag, Post, Comment, AuthorProfile


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')

class AuthorProfile(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
    related_name="profile"
  )
  bio = models.TextField()
  
  def __str__(self):
    return f"{self.__class__.__name__} object for {self.user}"

  
# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

admin.site.register(AuthorProfile)