from django.shortcuts import render, get_object_or_404, redirect
from .models import FinancialData
from .forms import FinancialDataForm

def financial_data_list(request):
    financial_data = FinancialData.objects.all()
    return render(request, 'myapp/financial_data_list.html', {'financial_data': financial_data})

def financial_data_detail(request, pk):
    data = get_object_or_404(FinancialData, pk=pk)
    return render(request, 'myapp/financial_data_detail.html', {'data': data})

def financial_data_new(request):
    if request.method == "POST":
        form = FinancialDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('financial_data_detail', pk=data.pk)
    else:
        form = FinancialDataForm()
    return render(request, 'myapp/financial_data_edit.html', {'form': form})

def financial_data_edit(request, pk):
    data = get_object_or_404(FinancialData, pk=pk)
    if request.method == "POST":
        form = FinancialDataForm(request.POST, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('financial_data_detail', pk=data.pk)
    else:
        form = FinancialDataForm(instance=data)
    return render(request, 'myapp/financial_data_edit.html', {'form': form})

def financial_data_delete(request, pk):
    data = get_object_or_404(FinancialData, pk=pk)
    data.delete()
    return redirect('financial_data_list')
