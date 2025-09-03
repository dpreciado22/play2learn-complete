from django.urls import path

from games.views import MathFactsView, AnagramHuntView

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path("api/submit-score/", SubmitScoreView.as_view(), name="submit-score"),
]