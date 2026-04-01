import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Property, Inquiry, Showing


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['property_count'] = Property.objects.count()
    ctx['property_apartment'] = Property.objects.filter(property_type='apartment').count()
    ctx['property_villa'] = Property.objects.filter(property_type='villa').count()
    ctx['property_plot'] = Property.objects.filter(property_type='plot').count()
    ctx['property_total_price'] = Property.objects.aggregate(t=Sum('price'))['t'] or 0
    ctx['inquiry_count'] = Inquiry.objects.count()
    ctx['inquiry_buy'] = Inquiry.objects.filter(inquiry_type='buy').count()
    ctx['inquiry_rent'] = Inquiry.objects.filter(inquiry_type='rent').count()
    ctx['inquiry_invest'] = Inquiry.objects.filter(inquiry_type='invest').count()
    ctx['inquiry_total_budget'] = Inquiry.objects.aggregate(t=Sum('budget'))['t'] or 0
    ctx['showing_count'] = Showing.objects.count()
    ctx['showing_scheduled'] = Showing.objects.filter(status='scheduled').count()
    ctx['showing_completed'] = Showing.objects.filter(status='completed').count()
    ctx['showing_cancelled'] = Showing.objects.filter(status='cancelled').count()
    ctx['recent'] = Property.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def property_list(request):
    qs = Property.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(property_type=status_filter)
    return render(request, 'property_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def property_create(request):
    if request.method == 'POST':
        obj = Property()
        obj.title = request.POST.get('title', '')
        obj.property_type = request.POST.get('property_type', '')
        obj.location = request.POST.get('location', '')
        obj.area_sqft = request.POST.get('area_sqft') or 0
        obj.price = request.POST.get('price') or 0
        obj.status = request.POST.get('status', '')
        obj.bedrooms = request.POST.get('bedrooms') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/properties/')
    return render(request, 'property_form.html', {'editing': False})


@login_required
def property_edit(request, pk):
    obj = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.property_type = request.POST.get('property_type', '')
        obj.location = request.POST.get('location', '')
        obj.area_sqft = request.POST.get('area_sqft') or 0
        obj.price = request.POST.get('price') or 0
        obj.status = request.POST.get('status', '')
        obj.bedrooms = request.POST.get('bedrooms') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/properties/')
    return render(request, 'property_form.html', {'record': obj, 'editing': True})


@login_required
def property_delete(request, pk):
    obj = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/properties/')


@login_required
def inquiry_list(request):
    qs = Inquiry.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(client_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(inquiry_type=status_filter)
    return render(request, 'inquiry_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def inquiry_create(request):
    if request.method == 'POST':
        obj = Inquiry()
        obj.client_name = request.POST.get('client_name', '')
        obj.client_phone = request.POST.get('client_phone', '')
        obj.client_email = request.POST.get('client_email', '')
        obj.property_title = request.POST.get('property_title', '')
        obj.inquiry_type = request.POST.get('inquiry_type', '')
        obj.budget = request.POST.get('budget') or 0
        obj.status = request.POST.get('status', '')
        obj.source = request.POST.get('source', '')
        obj.save()
        return redirect('/inquiries/')
    return render(request, 'inquiry_form.html', {'editing': False})


@login_required
def inquiry_edit(request, pk):
    obj = get_object_or_404(Inquiry, pk=pk)
    if request.method == 'POST':
        obj.client_name = request.POST.get('client_name', '')
        obj.client_phone = request.POST.get('client_phone', '')
        obj.client_email = request.POST.get('client_email', '')
        obj.property_title = request.POST.get('property_title', '')
        obj.inquiry_type = request.POST.get('inquiry_type', '')
        obj.budget = request.POST.get('budget') or 0
        obj.status = request.POST.get('status', '')
        obj.source = request.POST.get('source', '')
        obj.save()
        return redirect('/inquiries/')
    return render(request, 'inquiry_form.html', {'record': obj, 'editing': True})


@login_required
def inquiry_delete(request, pk):
    obj = get_object_or_404(Inquiry, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/inquiries/')


@login_required
def showing_list(request):
    qs = Showing.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(property_title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'showing_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def showing_create(request):
    if request.method == 'POST':
        obj = Showing()
        obj.property_title = request.POST.get('property_title', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.agent = request.POST.get('agent', '')
        obj.date = request.POST.get('date') or None
        obj.time_slot = request.POST.get('time_slot', '')
        obj.status = request.POST.get('status', '')
        obj.feedback = request.POST.get('feedback', '')
        obj.save()
        return redirect('/showings/')
    return render(request, 'showing_form.html', {'editing': False})


@login_required
def showing_edit(request, pk):
    obj = get_object_or_404(Showing, pk=pk)
    if request.method == 'POST':
        obj.property_title = request.POST.get('property_title', '')
        obj.client_name = request.POST.get('client_name', '')
        obj.agent = request.POST.get('agent', '')
        obj.date = request.POST.get('date') or None
        obj.time_slot = request.POST.get('time_slot', '')
        obj.status = request.POST.get('status', '')
        obj.feedback = request.POST.get('feedback', '')
        obj.save()
        return redirect('/showings/')
    return render(request, 'showing_form.html', {'record': obj, 'editing': True})


@login_required
def showing_delete(request, pk):
    obj = get_object_or_404(Showing, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/showings/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['property_count'] = Property.objects.count()
    data['inquiry_count'] = Inquiry.objects.count()
    data['showing_count'] = Showing.objects.count()
    return JsonResponse(data)
