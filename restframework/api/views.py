from api.serializers import StudentSerializer
from api.models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    #print(stu)
    serializer = StudentSerializer(stu)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')
    
    
    
def student_list(request):
    stu = Student.objects.all()
    #print(stu)
    serializer = StudentSerializer(stu,many = True)
    #print(serializer)
    #print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')
