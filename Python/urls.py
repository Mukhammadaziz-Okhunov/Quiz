from django.contrib import admin
from django.urls import path
from quiz.views import *
from natija.views import *

from natija.views import *
from quiz.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home),
    path('logout/', LogoutView),
    path('<int:son>/', QuizSon),
    path('<int:pk>/data/', QuizDataView.as_view()),
    path('<int:pk>/save/', QuizSaveView.as_view()),


    path('quiz/', QuizView.as_view(), name='quiz'),
    path('results/', NatijaView.as_view(), name='natija'),
    path('result/<int:son>/', NatijaDelView),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RoyxatView.as_view(), name='royxat'),
    path('add_question/', AddQuestionView.as_view(), name='addQuestion'),
    path('add_options/<int:son>/', AddOptionView),
    path('delete_question/<int:son>/', DelQuestionView),
]