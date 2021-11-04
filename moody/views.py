import json

from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry, Point
from rest_framework.decorators import action
from django_filters import rest_framework as filters

from .filters import MoodProximityFilter
from .models import Users, Locations, Moods
from .serializers import UsersSerializer, LocationsSerializer, MoodsSerializer

from fer import FER
import matplotlib.pyplot as plt


def get_mood(picture):
    test_image_one = plt.imread("photos/image.jpg")
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


class UsersViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class = UsersSerializer
    queryset = Users.objects.all()

    # add custom endpoint
    @action(detail=False, methods=["get"])
    def featured(self, request):
        users = self.get_queryset().filter(name='david')
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def create_if(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['name'] == 'Alesul':
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response = Response('not created', status=status.HTTP_400_BAD_REQUEST)

        return response


class LocationsViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    serializer_class = LocationsSerializer
    queryset = Locations.objects.all()

    @action(detail=False, methods=["get"])
    def happy(self, request):
        id = int(request.data['user_id'])
        user = Users.objects.get(id=id)

        happy_moods = {}
        for user_mood in user.moods.all():
            if user_mood.type == 'happy':
                proximity_to_locations = {}
                for user_location in user.locations.all():
                    proximity_to_locations[user_location.name] = user_location.poly.distance(user_mood.mood_addr)
                happy_moods[user_mood.picture_name] = proximity_to_locations

        return Response(data=json.dumps(happy_moods, indent=4), status=200)


class MoodsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = MoodsSerializer
    queryset = Moods.objects.all()

    def upload_capture(self):
        pass
        '''
        - save photo in /photos for now
        - apply fer to it to find mood type
        - save mood in db
        '''

    def mood_frequency(self):
        pass
        '''
        return mood distribution for a user
        '''

    def proximity_to_location(self):
        pass
        '''
        query all moods (point) that are within or close to user address (polygon) 
        '''
