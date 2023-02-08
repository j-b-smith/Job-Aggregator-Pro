from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scraper.dummy_jobs import jobs
from .helpers import find_object_by_id

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/jobs/',
        '/jobs/create/',
        '/jobs/delete/<id>/',
        '/jobs/update/<id>/',
        '/companies/',
        '/companies/create/',       
        '/companies/delete/<id>/',
        '/companies/update/<id>/', 
    ]
    return Response(routes)

@api_view(['GET'])
def getJobs(request):
    return Response(jobs)

@api_view(['GET'])
def getJob(request, pk):
    job = find_object_by_id(id=pk, object_list=jobs)
    return Response(job)