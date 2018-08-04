from django.db import models

from sx_store.models import GoodsValue
from sx_user.models import UserModel


# 创建购物车模型
class CartInfo(models.Model):
    # 关联用户
    user = models.ForeignKey(UserModel)
    # 关联商品
    goods = models.ForeignKey(GoodsValue)
    # 购买的数量
    count = models.IntegerField(default=1)

    class Meta:
        db_table = "sx_cart"

