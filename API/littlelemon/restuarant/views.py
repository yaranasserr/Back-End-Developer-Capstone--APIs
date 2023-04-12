from rest_framework.decorators import api_view
from .models import MenuItem ,Booking ,Menu
from .serializers import MenuItemSerializer ,BookingSerializer ,MenuSerializer
from rest_framework import generics ,viewsets
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

# Create your views here. 
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
        
# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]