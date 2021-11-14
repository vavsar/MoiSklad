from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView

from .models import Sale
from .tables import SalesTable


class SalesListView(LoginRequiredMixin, SingleTableView):
    model = Sale
    table_class = SalesTable
    template_name = 'index.html'
    paginate_by = 10
