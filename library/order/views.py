from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Order
from .forms import OrderForm
from .serializers import OrderSerializer


def all_orders(request):
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})

def order_by_id(request, id=0):
    order_by_id = Order.objects.get(id=id)
    return render(request, 'order/order_by_id.html', {'title': "Order by ID", "order_by_id": order_by_id})

def order_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
            return render(request, 'order/order_form_add.html', {'form': form})
        else:
            order = Order.objects.get(id=id)
            form = OrderForm(instance=order)
            return render(request, 'order/order_form.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(id=id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('orders')



def order_update(request):
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})


def order_delete(request, id=0):
    order = Order.objects.get(id=id)
    order.delete()
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
