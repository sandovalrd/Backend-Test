from django.urls import path
from .views import menu_create, MenuUpdate, MenuList, FoodCreate, FoodUpdate, FoodList, AdditionalCreate, AdditionalUpdate, AdditionalList, menu_today, send_mail, MunuDetail, slack_message
from django.contrib.auth.decorators import permission_required
urlpatterns = [

    # url for Menu

    path('add/', menu_create, name='menu-add'),
    path('update/<uuid:pk>/', permission_required('menu.change_menu')(MenuUpdate.as_view()), name='menu-update'),
    path('list/', permission_required('menu.change_menu')(MenuList.as_view()), name='menu-list'),
    path('today/', menu_today, name='menu-today'),
    path('<uuid:pk>', MunuDetail.as_view()),
    path('email/', send_mail, name='email'),
    path('slack/', slack_message, name='slack-message'),
   
    # url for food

    path('food/add/', permission_required('menu.add_food')(FoodCreate.as_view()), name='food-add'),
    path('food/update/<int:pk>/', permission_required('menu.change_food')(FoodUpdate.as_view()), name='food-update'),
    path('food/list/', FoodList.as_view(), name='food-list'),

	# url for Additional food

    path('food/additional/add/', permission_required('menu.add_additionalfood')(AdditionalCreate.as_view()), name='additional-add'),
    path('food/additional/update/<int:pk>/', permission_required('menu.change_additionalfood')(AdditionalUpdate.as_view()), name='additional-update'),
    path('food/additional/list/', permission_required('menu.change_additionalfood')(AdditionalList.as_view()), name='additional-list'),

]
