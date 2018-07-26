from django.db import models


# 创建后台管理员信息模型
class AdminUserModel(models.Model):
    username = models.CharField(u'用户名', max_length=32, unique=True)      # 用户名
    password = models.CharField(u'密码', max_length=256)                    # 密码

    class Meta:
        db_table = 'admin_users'


# 创建后台管理员Ticket模型
class UserTicketModel(models.Model):
    user = models.ForeignKey(AdminUserModel)   # 关联用户模型
    ticket = models.CharField(max_length=256)  # 密码
    out_time = models.DateTimeField()          # 过期时间

    class Meta:
        db_table = 'admin_users_ticket'
