from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)


urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre"),
    path("actors/", ActorList.as_view(), name="actors"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor"),
    path("cinema-halls/", cinema_hall_list, name="cinema-halls"),
    path("cinema-halls/<int:pk>/", cinema_hall_detail, name="cinema-hall"),
    path("", include(router.urls)),
]

app_name = "cinema"
