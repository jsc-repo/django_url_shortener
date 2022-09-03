import random
import string
from .models import Question


def shorten(url):
    random_hash = "".join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
        for _ in range(7)
    )

    return random_hash


def load_url(url_hash):
    get_question_obj = Question.objects.get(hash=url_hash)

    return get_question_obj
