from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, DetailView
from .models import Rating
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .filters import RatingFilter


class RatingFormView(CreateView):
    model = Rating
    template_name = 'reports/rating_form.html'
    fields = '__all__'
    success_url = reverse_lazy('end_form')


def end_form(request):
    return render(request, 'reports/endform.html')


class DetailRatingView(LoginRequiredMixin, DetailView):
    model = Rating
    template_name = 'reports/rate_detail.html'
    context_object_name = 'rate'
    login_url = 'login'


@login_required(login_url='login')
def get_Details(request):
    total = Rating.objects.all().count()
    rate_by_one = Rating.objects.filter(rating='1').count()
    rate_by_two = Rating.objects.filter(rating='2').count()
    rate_by_three = Rating.objects.filter(rating='3').count()
    rate_by_four = Rating.objects.filter(rating='4').count()
    rate_by_five = Rating.objects.filter(rating='5').count()
    context = {"total": total, "one": rate_by_one, "two": rate_by_two, "three": rate_by_three,
               "four": rate_by_four, "five": rate_by_five}
    return render(request, 'reports/main.html', context=context)


@login_required(login_url='login')
def rate1_list(request):
    model = Rating.objects.filter(rating='1')
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'reports/rate1_list.html', {"rates": model})


@login_required(login_url='login')
def rate2_list(request):
    model = Rating.objects.filter(rating='2')
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'reports/rate2_list.html', {"rates": model})


@login_required(login_url='login')
def rate3_list(request):
    model = Rating.objects.filter(rating='3')
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'reports/rate3_list.html', {"rates": model})


@login_required(login_url='login')
def rate4_list(request):
    model = Rating.objects.filter(rating='4')
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'reports/rate4_list.html', {"rates": model})


@login_required(login_url='login')
def rate5_list(request):
    model = Rating.objects.filter(rating='5')
    page = request.GET.get('page', 1)
    paginator = Paginator(model, 8)
    try:
        model = paginator.page(page)
    except PageNotAnInteger:
        model = paginator.page(1)
    except EmptyPage:
        model = paginator.page(paginator.num_pages)
    return render(request, 'reports/rate5_list.html', {"rates": model})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'reports/login.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'reports/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def search(request):
    rates = Rating.objects.all()
    rate_filter = RatingFilter(request.GET, queryset=rates)
    rates = rate_filter.qs
    context = {"rates": rates, "myfilter": rate_filter}
    return render(request, 'reports/search.html', context)
