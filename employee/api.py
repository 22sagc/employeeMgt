from employee.serializers import Managerserialize, Employeeserialize, Userserialize
from employee.models import Employee
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['POST'])
def saveUser(request):
    if request.method == "POST":
        saveserialize = Userserialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def saveManager(request):
    if request.method == "POST":
        saveserialize = Managerserialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def saveEmp(request):
    if request.method == "POST":
        saveserialize = Employeeserialize(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status=status.HTTP_201_CREATED)
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def showEmp(request):
    if request.method == "GET":
        results = Employee.objects.filter(is_deleted=False)
        serialize = Employeeserialize(results, many=True)
        return Response(serialize.data)


class saveEmployeeApi(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        empobj = self.get_object(pk)
        serializeobj = Employeeserialize(empobj)
        return Response(serializeobj.data)

    def put(self, request, pk):
        empobj = self.get_object(pk)
        empserialize = Employeeserialize(empobj, data=request.data)
        if empserialize.is_valid():
            empserialize.save()
            return Response(empserialize.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
