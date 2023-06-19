from django.shortcuts import render
from django.views import generic
from .forms import GoodsCreateForm, GoodsUpdateForm
from .models import Goods
from django.urls import reverse_lazy
from django.shortcuts import redirect

class GoodsCreate(generic.CreateView):
    model = Goods
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'

    def form_valid(self, form):
        goods = form.save()
        return redirect('crud:goods_detail', pk=goods.pk)


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods
    template_name = 'crud/goods_detail.html'

class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = reverse_lazy('crud:goods_create')

class GoodsDelete(generic.DeleteView):
    # フォームは必要なし
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = reverse_lazy('crud:goods_list')

# Create your views here.
