from django.shortcuts import render
from .forms import OrderForm

def mainview(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            
            return render(request, 'done.html')
    else:
        form = OrderForm()
        return render(request, 'index.html', {'form':form})
