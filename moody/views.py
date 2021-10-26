from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, Point
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .filters import MoodProximityFilter
from .models import Users, Moods
from .serializers import UsersSerializer, MoodsSerializer

from fer import FER
import matplotlib.pyplot as plt


def get_mood(picture):
    test_image_one = plt.imread("image.jpg")
    emo_detector = FER(mtcnn=True)
    # Capture all the emotions on the image
    captured_emotions = emo_detector.detect_emotions(test_image_one)
    # Print all captured emotions with the image
    print(captured_emotions)
    plt.imshow(test_image_one)

    # Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    print(dominant_emotion, emotion_score)

    return dominant_emotion


class MoodsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MoodsSerializer
    queryset = Moods.objects.all()


class UsersViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    filterset_class = MoodProximityFilter
    filter_backends = [filters.DjangoFilterBackend]

    @action(detail=False, methods=['get'])
    def get_nearest_moods(self, request):
        x_coords = request.GET.get('x', None)
        y_coords = request.GET.get('y', None)
        if x_coords and y_coords:
            user_location = Point(float(x_coords), float(y_coords), srid=4326)
            # mood_location = Moods.location
            nearest_moods = Users.objects.annotate(
                distance=Distance('geom', user_location)).order_by('distance')[:5]
            serializer = self.get_serializer_class()
            serialized = serializer(nearest_moods, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
