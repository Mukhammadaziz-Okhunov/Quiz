from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *


savolqosh = Savol.objects.all()
def Home(request):
    quiz = Quizs.objects.all()
    return render(request, 'index.html', {'quiz': quiz})

def QuizSon(request, son):
    quiz = Quizs.objects.get(id=son)
    return render(request, 'quiz.html', {'quiz': quiz})


class QuizView(View):
    def get(self, request):
        return render(request, 'quiz.html')

class QuizDataView(View):
    def get(self, request, pk):
        quizi = Quizs.objects.get(id=pk)
        savollar = Savol.objects.filter(quiz=quizi)
        questions = []
        for s in savollar:
            answers = []
            javoblar = Javob.objects.filter(savol=s)
            for j in javoblar:
                answers.append(j.matn)
            questions.append({str(s): answers})
        return JsonResponse({
            'data': questions,
            'time': quizi.davomiyligi,
        })



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        l = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=l, password=p)
        if user is None:
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/home')

class RoyxatView(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password1']
        )
        login(request,user)
        return redirect('/home')

def LogoutView(request):
    logout(request)
    return redirect('/login')


class AddQuestionView(View):
    def get(self, request):
        return render(request, 'add_question.html', {'questions':savolqosh})


def AddOptionView(request, son):
    javobi = Savol.objects.filter(id=son)
    return render(request, 'add_options.html', {'questions':javobi})

def DelQuestionView(request, son):
    Savol.objects.filter(id=son).delete()
    return redirect('/add_question')