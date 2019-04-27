from django_filters import filters
from django_filters import FilterSet
from .models import Item


#検索画面の設定フィルターを利用した

#並びを決める
class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):
#フィルターの定義を決める。charfilterはテキストの検索。containsは部分一致を表している。
    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='概要', lookup_expr='contains')

#並べ替え。ソート順の指定。field(モデルフィールド,パラメータ値)
    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('name', 'name'),
            ('age', 'age'),
        ),
        field_labels={
            'name': '氏名',
            'age': '年齢',
        },
        label='順番'
    )

    class Meta:
#フィルタを列挙。
        model = Item
        fields = ('name','ronbunt','ronbun', 'memo',)

