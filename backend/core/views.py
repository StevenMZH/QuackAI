from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import FileResponse
import os
from math import radians
import uuid
import shutil
from pathlib import Path

from .serializers import ScenePostSerializer
        
        