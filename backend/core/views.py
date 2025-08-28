import joblib, os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SchedulingProblemSerializer
from core.data_processing.solver.scheduler import solve_with_model
from core.data_processing.parser.output_parser import output_parser

MODEL_PATH = os.path.join(os.path.dirname(__file__), "scheduler_selector.pkl")
ai_model_tuple = joblib.load(MODEL_PATH)

class ScheduleTaskView(APIView):
    def post(self, request):
        serializer = SchedulingProblemSerializer(data=request.data)

        if serializer.is_valid():
            problem_input = serializer.validated_data

            try:
                manager, heuristic_used = solve_with_model(problem_input, ai_model_tuple)
                parsed_output = output_parser(manager)
                result = {
                    "blocks": problem_input["blocks"],
                    "intervals": problem_input["intervals"],
                    "heuristic": heuristic_used,
                    "schedule": parsed_output["schedule"]
                    
                }
                return Response(result, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
