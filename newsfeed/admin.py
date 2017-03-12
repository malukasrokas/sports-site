from django.contrib import admin
from .models import *

# Register models
admin.site.register(Post)
admin.site.register(ForumPost)
admin.site.register(Chat)
admin.site.register(Comment)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Stats)
