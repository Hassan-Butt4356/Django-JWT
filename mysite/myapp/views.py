from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse,JsonResponse
from .forms import BookCreateForm


# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTAuthentication,))
def home(request):
    data={"response":"This is Response Data"}
    return JsonResponse({"response":"This is Response Data"})

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTAuthentication,))
def new_home(request):
    data={"response":"This is Again for testing purpose Home View"}
    return JsonResponse(data)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JWTAuthentication,))
def createBook(request):
    if request.method=='POST':
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('name')
            price=form.cleaned_data.get('price')
            data={"Book Name":name,'Book Price':price}
            return JsonResponse(data)
        data={"Response":"Something Went Wrong"}
        return JsonResponse(data)