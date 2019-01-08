from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, exceptions, response
from .models import CharacterClass, Character
from .serializers import CharacterClassSerializers, CharacterSerializer
from .permissions import IsOwner
# Create your views here.


@csrf_exempt
def character_classes_list(request):
    classes = CharacterClass.objects.all()
    serializer = CharacterClassSerializers(classes, many=True)
    return JsonResponse(serializer.data, safe=False)


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner=request.user)
        serializer = CharacterSerializer(queryset, many=True)
        return response.Response(serializer.data)
        # if not request.user.is_authenticated:
            # return ex
    # permission_classes = (permissions.IsAuthenticated, IsOwner,)
    # permission_classes = permissions.IsAuthenticatedOrReadOnly


class CharacterClassViewSet(viewsets.ModelViewSet):
    queryset = CharacterClass.objects.all()
    serializer_class = CharacterClassSerializers
