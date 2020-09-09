from django.test import TestCase
from django.contrib.admin.models import LogEntry,CHANGE
from django.contrib.admin.options import get_content_type_for_model
from .models import Post
# Create your tests here.

#查询某个对象的变更
post = Post.objects.get(id = 1)
log_entries = LogEntry.objects.filter(
    content_type_id = get_content_type_for_model(post).pk,
    object_id = post.id,
)
for log in log_entries:
    print(log.object_id)