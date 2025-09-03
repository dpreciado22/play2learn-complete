import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import GameScore

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

@method_decorator(login_required, name="dispatch")
class SubmitScoreView(View):
    def post(self, request):
        try:
            payload = json.loads(request.body.decode("utf-8"))
            game_type   = payload["game_type"]
            final_score = int(payload["final_score"])
            settings    = payload.get("settings", {})
        except Exception:
            return HttpResponseBadRequest("Invalid JSON")

        GameScore.objects.create(
            user=request.user,
            game_type=game_type,
            final_score=final_score,
            settings=settings,
            finished_at=timezone.now(),
        )
        return JsonResponse({"ok": True})