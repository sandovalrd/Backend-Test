from django.urls import path
from .views import menu_create, MenuUpdate, MenuList, MenuDelete, FoodCreate, FoodUpdate, FoodList, FoodDelete, AdditionalCreate, AdditionalUpdate, AdditionalDelete, AdditionalList, menu_today
from django.contrib.auth.decorators import permission_required
urlpatterns = [

    # url for Menu

    path('add/', menu_create, name='menu-add'),
    path('menu/<int:pk>/', permission_required('menu.change_menu')(MenuUpdate.as_view()), name='menu-update'),
    path('menu/<int:pk>/delete/', permission_required('menu.delete_menu')(MenuDelete.as_view()), name='menu-delete'),
    path('list/', permission_required('menu.change_menu')(MenuList.as_view()), name='menu-list'),
    path('today/', menu_today, name='menu-today'),
    
    # url for food

    path('food/add/', permission_required('menu.add_food')(FoodCreate.as_view()), name='food-add'),
    path('food/<int:pk>/', permission_required('menu.change_food')(FoodUpdate.as_view()), name='food-update'),
    path('food/<int:pk>/delete/', permission_required('menu.delete_food')(FoodDelete.as_view()), name='food-delete'),
    path('food/list/', FoodList.as_view(), name='food-list'),

	# url for Additional food

    path('food/additional/add/', permission_required('menu.add_additionalfood')(AdditionalCreate.as_view()), name='additional-add'),
    path('food/additional/<int:pk>/', permission_required('menu.change_additionalfood')(AdditionalUpdate.as_view()), name='additional-update'),
    path('food/additional/<int:pk>/delete/', permission_required('menu.delete_additionalfood')(AdditionalDelete.as_view()), name='additional-delete'),
    path('food/additional/list/', permission_required('menu.change_additionalfood')(AdditionalList.as_view()), name='additional-list'),

]