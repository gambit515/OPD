from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Tag, Record
from django.contrib import messages
from .forms import StudentRequestForm

def home(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'guidbook_app/index.html', {'categories': categories,'tags':tags})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    records = Record.objects.filter(category=category)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'guidbook_app/category_detail.html', {'category': category,'categories':categories,'tags':tags, 'records': records})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    records = Record.objects.filter(tags=tag)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'guidbook_app/category_detail.html', {'category': tag, 'records': records,'categories':categories,'tags':tags})

def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'guidbook_app/record_detail.html', {'record': record,'categories':categories,'tags':tags})


def student_request_view(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = StudentRequestForm(request.POST, request.FILES)  # Добавьте request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш запрос успешно отправлен!")
            return redirect('student_request')
    else:
        form = StudentRequestForm()

    return render(request, 'guidbook_app/student_request_form.html', {'form': form,'categories':categories,'tags':tags})