from rest_framework import viewsets
from .models import Teacher, Course, Student
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, SignupSerializer, LoginSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .helpers import get_tokens_for_user
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                res_data = get_tokens_for_user(
                    User.objects.get(username=username))
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "success",
                    "data": res_data
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                response = {
                    "status": status.HTTP_401_UNAUTHORIZED,
                    "message": "Invalid Email or Password",
                }
                return Response(response, status=status.HTTP_401_UNAUTHORIZED)

        response = {
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "bad request",
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'status': status.HTTP_201_CREATED}
            return Response(res, status=status.HTTP_201_CREATED)
        res = {'status': status.HTTP_400_BAD_REQUEST, 'data': serializer.errors}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    #permission_classes=[IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
