from django.contrib import admin

# Register your models here.
from jobs.models import Job


class JobAdmin(admin.ModelAdmin):
    # 将默认字段隐藏掉
    exclude = ('creator', 'created_date', 'modified_date')
    # 修改列表中展示哪些字段
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    # 重写父类的方法，将创建者定义为登录的用户
    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Job, JobAdmin)
