from django.db import models


# 创建商品种类模型
class ArticleCategory(models.Model):
    kind = models.CharField(max_length=30)            # 分类
    isDelete = models.BooleanField(default=False)     # 是否删除

    class Meta:
        db_table = "sx_kind"


# 创建商品属性模型
class GoodsValue(models.Model):
    g_name = models.CharField(max_length=20)                  # 商品名称
    g_img = models.ImageField(upload_to='shop')               # 商品图片
    g_num = models.CharField(max_length=100)                  # 商品货号
    g_price = models.FloatField(default=0)                    # 商品价格
    g_unit = models.CharField(max_length=20, default='500g')  # 商品单位
    g_repertory = models.IntegerField()                       # 商品库存
    isDelete = models.BooleanField(default=False)             # 是否删除
    # 关联商品种类
    gtype = models.ForeignKey(ArticleCategory)

    class Meta:
        db_table = "sx_goods"

