from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView


def home(request):
    return render(request, 'index.html')

# class field1CreateView(CreateView):
#     model = field1
#     template_name = 'your_app/create.html'
#     fields = '__all__'
# class field1CreateView(CreateView):
#     model = YourModel
#     template_name = 'your_app/create.html'
#     fields = '__all__'
# class field1DetailView(DetailView):
#     model = field1
#     template_name = 'conf_app/detail.html'
#     class field1UpdateView(UpdateView):
#     model = field1
#     template_name = 'conf_app/update.html'
#     fields = '__all__'
# class field1DeleteView(DeleteView):
#     model = field1
#     template_name = 'conf_app/delete.html'
#     success_url = '/conf_app/list/'


