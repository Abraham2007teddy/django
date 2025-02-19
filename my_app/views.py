from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    content = """<div style='width:100%; height:100vh; display:flex;justify-content:center;align-items:center'>
                    <h1 style='font-size: 4rem; color:purple'>Hello my name is Ibo</h1>
                </div>"""
    return HttpResponse(content)