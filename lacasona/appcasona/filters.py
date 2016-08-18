import django_filters as df
from .models import Inventario, Ingredientes, Orden

class MessageListFilter(df.FilterSet):
    class Meta:
        model = 
        fields = ['recipientmsisdn', 'sendermsisdn']