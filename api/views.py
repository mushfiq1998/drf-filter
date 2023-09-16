from .models import Student
from .serializers import StudentSerializer 
from rest_framework.generics import ListAPIView

class StudentList(ListAPIView): 
    # Retrieve all students from Student table
    # queryset = Student.objects.all()

    # Retrieve the students passed by the user KMR
    # queryset = Student.objects.filter(passby='KMR')
    serializer_class = StudentSerializer

    # Filter data based on current logged in user
    # For this override get_queryset()
    def get_queryset(self):
        # print('request: ', self.request)
        # self.request contains current logged in user
        user = self.request.user
        return Student.objects.filter(passby=user)
        # students = Student.objects.filter(passby=user)
        # return students