import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('FLASK_SECRET') or 'shhh-they-will-never-know'

    SESSION_TYPE = "sqlalchemy"
    SESSION_USE_SIGNER = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_SQLALCHEMY_TABLE = "session"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "session.db")


choice_type = {
        "binary": ["Yes", "No"]
        }


questions = [
    {
        "question":
            "Are your outputs business critical?",
        "choices": choice_type["binary"],
        "next_index":1
        },
    {
        "question":
            "Are users of your code able to program in the appropriate"
            " language?",
        "choices": choice_type["binary"],
        "next_index": None
      }
]


default_scores = {
        "documentation": 0,
        "peer_review": 0,
        "testing": 0,
        }


class Question(object):
    def __init__(
            self,
            question,
            question_type,
            choices,
            next_question
            ):
        self.question = question
        self.question_type = question_type,
        self.choices = choices
        self.next_question = next_question

    def add_choices(self):
        pass

    def set_next_question(self, next_question):
        pass
