from django.shortcuts import render
from .models import GroceryKit, Order, Payment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Home page
def home(request):
    kits = GroceryKit.objects.all()
    return render(request, 'home.html', {'kits': kits})


# ✅ CREATE ORDER API
@api_view(['POST'])
def create_order(request):
    try:
        kit_id = request.data.get('kit_id')
        quantity = int(request.data.get('quantity', 1))
        payment_type = request.data.get('payment_type')
        delivery_date = request.data.get('delivery_date')

        # Get kit
        kit = GroceryKit.objects.get(id=kit_id)

        total_amount = kit.price * quantity

        # Create order
        order = Order.objects.create(
            kit=kit,
            quantity=quantity,
            total_amount=total_amount,
            payment_type=payment_type,
            delivery_date=delivery_date
        )

        # ✅ Payment Logic
        if payment_type == "weekly":
            weekly_amount = total_amount // 4

            for i in range(4):
                Payment.objects.create(
                    order=order,
                    amount=weekly_amount,
                    week_number=i + 1,
                    status='pending'
                )
        else:
            Payment.objects.create(
                order=order,
                amount=total_amount,
                status='pending'
            )

        return Response({
            "message": "Order Created Successfully",
            "order_id": order.id
        }, status=status.HTTP_201_CREATED)

    except GroceryKit.DoesNotExist:
        return Response({"error": "Kit not found"}, status=404)

    except Exception as e:
        return Response({"error": str(e)}, status=500)


# ✅ GET ALL KITS API
@api_view(['GET'])
def get_kits(request):
    kits = GroceryKit.objects.all()

    data = []
    for kit in kits:
        data.append({
            "id": kit.id,
            "title": kit.title,
            "badge": kit.badge,
            "tag": kit.tag,
            "members": kit.members,
            "rating": kit.rating,
            "reviews": kit.reviews,
            "price": kit.price,
            "description": kit.description,
            "image": kit.image
        })

    return Response(data)


@api_view(['GET'])
def get_payments(request, order_id):
    payments = Payment.objects.filter(order_id=order_id)

    data = []
    for p in payments:
        data.append({
            "id": p.id,
            "amount": p.amount,
            "week_number": p.week_number,
            "status": p.status
        })

    return Response(data)