from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count, Max
from .models import Client, Seller, Product, Sale
from .forms import ClientForm, SellerForm, ProductForm, SaleForm

def business_dashboard(request):
    clients = Client.objects.all()
    sellers = Seller.objects.all()
    products = Product.objects.all()
    sales = Sale.objects.all().select_related('product', 'seller', 'buyer')

    report_type = request.GET.get('report_type')
    report_results = {}

    if report_type == "buyers_by_seller":
        s_id = request.GET.get('seller_id')
        if s_id:
            sales_f = Sale.objects.filter(seller_id=s_id).select_related('buyer')
            report_results['clients'] = list({sale.buyer for sale in sales_f})

    elif report_type == "sales_by_date":
        date_str = request.GET.get('date')
        if date_str:
            report_results['sales'] = Sale.objects.filter(sale_date=date_str).select_related('product', 'buyer', 'seller')

    elif report_type == "sellers_by_product":
        p_id = request.GET.get('product_id')
        if p_id:
            sales_f = Sale.objects.filter(product_id=p_id).select_related('seller')
            report_results['sellers'] = list({sale.seller for sale in sales_f})

    elif report_type == "buyers_by_product":
        p_id = request.GET.get('product_id')
        if p_id:
            sales_f = Sale.objects.filter(product_id=p_id).select_related('buyer')
            report_results['clients'] = list({sale.buyer for sale in sales_f})

    elif report_type == "total_amount_by_date":
        date_str = request.GET.get('date')
        if date_str:
            total = Sale.objects.filter(sale_date=date_str).aggregate(Sum('total_price'))['total_price__sum']
            report_results['total_sum'] = total or 0
            report_results['selected_date'] = date_str

    elif report_type == "top_product":
        top = Product.objects.annotate(num_sales=Sum('sales__quantity')).order_by('-num_sales').first()
        report_results['text'] = f"Самый продаваемый товар: {top.name} (Продано {top.num_sales or 0} шт.)" if top else "Данных нет"

    elif report_type == "top_seller":
        top = Seller.objects.annotate(total_revenue=Sum('sales__total_price')).order_by('-total_revenue').first()
        report_results['text'] = f"Лучший продавец: {top.full_name} (Сумма: ${top.total_revenue or 0})" if top else "Данных нет"

    elif report_type == "top_buyer":
        top = Client.objects.annotate(total_spent=Sum('purchases__total_price')).order_by('-total_spent').first()
        report_results['text'] = f"Лучший покупатель: {top.full_name} (Потрачено: ${top.total_spent or 0})" if top else "Данных нет"

    elif report_type == "top_product_range":
        start, end = request.GET.get('start_date'), request.GET.get('end_date')
        if start and end:
            top = Product.objects.filter(sales__sale_date__range=[start, end]).annotate(num_sales=Sum('sales__quantity')).order_by('-num_sales').first()
            report_results['text'] = f"Лидер продаж за период: {top.name} (Количество: {top.num_sales or 0} шт.)" if top else "За данный период продаж не было"

    elif report_type == "top_seller_range":
        start, end = request.GET.get('start_date'), request.GET.get('end_date')
        if start and end:
            top = Seller.objects.filter(sales__sale_date__range=[start, end]).annotate(total_revenue=Sum('sales__total_price')).order_by('-total_revenue').first()
            report_results['text'] = f"Лучший продавец за период: {top.full_name} (Выручка: ${top.total_revenue or 0})" if top else "Данных нет"

    elif report_type == "top_buyer_range":
        start, end = request.GET.get('start_date'), request.GET.get('end_date')
        if start and end:
            top = Client.objects.filter(purchases__sale_date__range=[start, end]).annotate(total_spent=Sum('purchases__total_price')).order_by('-total_spent').first()
            report_results['text'] = f"Топ-покупатель за период: {top.full_name} (Закупки на сумму: ${top.total_spent or 0})" if top else "Данных нет"

    context = {
        'clients': clients, 'sellers': sellers, 'products': products, 'sales': sales,
        'report_type': report_type, 'report_results': report_results,
    }
    return render(request, 'dashboard.html', context)


def edit_entity(request, entity_type, obj_id=None):
    config = {
        'client': (Client, ClientForm, 'client_form.html'),
        'seller': (Seller, SellerForm, 'seller_form.html'),
        'product': (Product, ProductForm, 'product_form.html'),
        'sale': (Sale, SaleForm, 'sale_form.html')
    }
    
    model_cls, form_cls, template_name = config[entity_type]
    instance = get_object_or_404(model_cls, id=obj_id) if obj_id else None

    if request.method == 'POST':
        form = form_cls(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('business_dashboard')
    else:
        form = form_cls(instance=instance)
        
    return render(request, template_name, {'form': form, 'entity_type': entity_type})


def delete_entity(request, entity_type, obj_id):
    config = {
        'client': Client, 
        'seller': Seller, 
        'product': Product, 
        'sale': Sale
    }
    obj = get_object_or_404(config[entity_type], id=obj_id)
    if request.method == 'POST':
        obj.delete()
    return redirect('business_dashboard')
