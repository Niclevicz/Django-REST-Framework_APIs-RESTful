from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewsSet, CursoViewsSet, MatriculaViewsSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register("estudantes", EstudanteViewsSet, basename="Estudantes")
router.register("cursos", CursoViewsSet, basename="Cursos")
router.register("matriculas", MatriculaViewsSet, basename="Matricula")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]
