from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    ModelViewSet,
    CinemaHallViewSet
)

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={
        "get": "list",
        "post": "create"
    }
)

cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }
)

router = routers.DefaultRouter()

router.register("movies", ModelViewSet, basename="movies")


urlpatterns = [
    path("genre/", GenreList.as_view(), name="genre_list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre_detail"),

    path("actor/", ActorList.as_view(), name="actore_list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),

    path("cinemahall/", cinema_hall_list, name="cinema_hall_list"),
    path(
        "cinemahall/<int:pk>/",
        cinema_hall_detail,
        name="cinema_hall_detail"
    ),

    path("", include(router.urls)),

]

app_name = "cinema"
