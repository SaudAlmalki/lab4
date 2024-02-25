from django.shortcuts import render
from django.http import HttpResponse
tax_rate = 0.15  

   def default_view(request):
       return render(request, 'default.html')

   def calculate_tax(request, price):
       total_with_tax = float(price) * (1 + tax_rate)
       return render(request, 'calculate_tax.html', {'total_with_tax': total_with_tax})

   def tax_rate_view(request):
       return render(request, 'tax_rate.html', {'tax_rate': tax_rate})


# Create your views here.
