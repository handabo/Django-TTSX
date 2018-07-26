from django.db import models


# 创建用户信息模型
class UserModel(models.Model):
    username = models.CharField(max_length=32, unique=True)      # 用户名
    password = models.CharField(max_length=256)                  # 密码
    password_c = models.CharField(max_length=256)                # 确认密码
    email = models.CharField(max_length=64, unique=True)         # 邮箱
    recipients = models.CharField(max_length=10, default='')     # 收件人姓名
    phone = models.CharField(max_length=11, default='')          # 收件人电话
    addressee_p = models.CharField(max_length=6, default='')     # 收件人邮编
    direction = models.CharField(max_length=100, default='')     # 收件人地址

    class Meta:
        db_table = 'sx_users'


# 创建用户Ticket模型
class UserTicketModel(models.Model):
    user = models.ForeignKey(UserModel)        # 关联用户模型
    ticket = models.CharField(max_length=256)  # 密码
    out_time = models.DateTimeField()          # 过期时间

    class Meta:
        db_table = 'sx_users_ticket'


