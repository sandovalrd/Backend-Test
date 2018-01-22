from django.urls import path
from .views import menu_create, MenuUpdate, MenuList, MenuDelete, FoodCreate, FoodUpdate, FoodList, FoodDelete, AdditionalCreate, AdditionalUpdate, AdditionalDelete, AdditionalList

urlpatterns = [

    # url for Menu

    path('add/', menu_create, name='menu-add'),
    path('menu/<int:pk>/', MenuUpdate.as_view(), name='menu-update'),
    path('menu/<int:pk>/delete/', MenuDelete.as_view(), name='menu-delete'),
    path('list/', MenuList.as_view(), name='menu-list'),

	# url for food

    path('food/add/', FoodCreate.as_view(), name='food-add'),
    path('food/<int:pk>/', FoodUpdate.as_view(), name='food-update'),
    path('food/<int:pk>/delete/', FoodDelete.as_view(), name='food-delete'),
    path('food/list/', FoodList.as_view(), name='food-list'),

	# url for Additional food

    path('food/additional/add/', AdditionalCreate.as_view(), name='additional-add'),
    path('food/additional/<int:pk>/', AdditionalUpdate.as_view(), name='additional-update'),
    path('food/additional/<int:pk>/delete/', AdditionalDelete.as_view(), name='additional-delete'),
    path('food/additional/list/', AdditionalList.as_view(), name='additional-list'),

]