from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from sx_user.models import UserTicketModel


class UserMiddle(MiddlewareMixin):
    def process_request(self, request):
        # 需要登录验证的页面
        need_login = ['/store/index/',
                      '/store/list/',
                      '/user/user_center_info/',
                      '/user/user_center_order/',
                      '/user/user_center_site/',
                      '/shopping/detail/',
                      '/shopping/addgoods/',
                      '/shopping/subgoods/',
                      '/shopping/goodsnum/',

                      '/shopping/tatalprice/',
                      '/shopping/buycart/',
                      '/shopping/addcart/',
                      '/order/place_order/',


                      ]
        # 判断页面是否需要登录
        if request.path in need_login:
            # 如果需要验证登录,则获取cookies中的ticket值
            ticket = request.COOKIES.get('ticket')
            # 如果cookies中没有ticket值, 则跳转到登录页面
            if not ticket:
                return HttpResponseRedirect(reverse('user:login'))
            # 将获取的ticket值保存在变量user_ticket中
            user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()

            if user_ticket:
                # 判断ticket值是否过期，如果没过期
                if datetime.now() > user_ticket.out_time.replace(tzinfo=None):
                    # 过期处理
                    UserTicketModel.objects.filter(user=user_ticket.user).delete()
                    return HttpResponseRedirect(reverse('user:login'))
                else:
                    # 没过期处理
                    request.user = user_ticket.user
                    # ttsx_users_ticket表中查询当前的user, 且ticket值不等于cookie中的ticket值
                    UserTicketModel.objects.filter(Q(user=user_ticket.user) & Q(ticket=ticket))
                    return None
            else:
                return HttpResponseRedirect(reverse('user:login'))
        else:
            return None

