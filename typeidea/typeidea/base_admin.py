from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):

    """
    1.用来补充文章，分类，标签，侧边栏，友链这些model的owner字段
    2. 用来过滤当前用户创建的数据
    """
    exclude = ('owner',)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin,self).save_model(request,obj,form,change)

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner = request.user)