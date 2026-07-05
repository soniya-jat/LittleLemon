from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
