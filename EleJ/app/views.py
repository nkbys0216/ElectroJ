#ビューの作成　モデルからテンプレートに受け渡しをする機能

#検索画面、詳細画面、登録画面、更新画面、削除画面、ファイルのビューを作成

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#詳細画面で使用
from django.views.generic import ListView, DetailView

#登録更新削除で使用
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#検索画面で使用
from django_filters.views import FilterView

from .models import Item
from .filters import ItemFilter
from .forms import ItemForm

#以下没
#from django.shortcuts import render, redirect
#from django.template.context_processors import csrf
#from django.conf import settings
#from upload_form.models import FileNameModel
#import sys, os
#UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'



# 検索画面のビュー
class ItemFilterView(LoginRequiredMixin, FilterView):
    model = Item
    filterset_class = ItemFilter
    # デフォルトの並び順を新しい順とする
    queryset = Item.objects.all().order_by('-created_at')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')

#以下没（ファイル　以下ファイル名を修正１）

#def form(request):
#    if request.method != 'POST':
#        return render(request, 'app/item_form.html')

#    file = request.FILES['file']
#    path = os.path.join(UPLOADE_DIR, file.name)
#    destination = open(path, 'wb')

#    for chunk in file.chunks():
#        destination.write(chunk)

#    insert_data = FileNameModel(file_name = file.name)
#    insert_data.save()

#    return redirect('app:complete') #あってる？

#def complete(request):
#    return render(request, 'app/item_detail.html')
