from django.shortcuts import render, redirect
from django.http import HttpResponse
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64
from collections import defaultdict
from user.models import signup
from tracker.models import Transaction
from django.db.models import Sum

def get_graph():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return graph

def analysis(request):
    username = request.session.get('username')
    if not username:
        return redirect('signin')

    user = signup.objects.get(username=username)
    transactions = Transaction.objects.filter(user=user, transaction_type='SEND')

    # 🥧 Product-wise Pie Chart
    product_expense = defaultdict(float)
    for tx in transactions:
        for product in tx.product_names.split(','):
            product_expense[product.strip()] += float(tx.amount)

    if product_expense:
        plt.figure(figsize=(6,6))
        products = list(product_expense.keys())
        values = list(product_expense.values())

        # Use pastel colors and labels with product + amount
        colors = sns.color_palette('pastel')[:len(products)]
        labels = [f"{prod} ₹{product_expense[prod]:.2f}" for prod in products]

        plt.pie(values, labels=labels, colors=colors, startangle=140)
        plt.title("🛍️ Product-wise Spending")
        pie_chart = get_graph()
        plt.clf()
    else:
        pie_chart = None

    # ⚫ Scatter Plot: Product vs Expense
    if product_expense:
        plt.figure(figsize=(6,4))
        products = list(product_expense.keys())
        values = list(product_expense.values())

        sns.scatterplot(x=products, y=values, s=100, color='blue')
        plt.xticks(rotation=45)
        plt.title("📊 Product-wise Expense (Scatter)")
        plt.xlabel("Products")
        plt.ylabel("Amount ₹")
        scatter_chart = get_graph()
        plt.clf()
    else:
        scatter_chart = None

    return render(request, 'analysis.html', {
        'username': username,
        'pie_chart': pie_chart,
        'scatter_chart': scatter_chart
    })
