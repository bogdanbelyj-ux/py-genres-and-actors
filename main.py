import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Genre, Actor


def main() -> QuerySet:
    genre = ["Western", "Action", "Drama"]
    genre_obj = [Genre.objects.create(name=g) for g in genre]

    actors = [
        ("George", "klooney"),
        ("Kianu", "Reaves"),
        ("Scarlett", "Keegan"),
        ("Will", "Smith"),
        ("Jaden", "Smith"),
        ("Scarlett", "Johansson"),
    ]
    actor_obj = [
        Actor.objects.create(first_name=f, last_name=l) for f, l in actors
    ]

    print(genre_obj)
    print(actor_obj)

    Genre.objects.filter(
        name="Dramma"
    ).update(name="Drama")
    Actor.objects.filter(
        last_name="Klooney"
    ).update(last_name="Clooney")
    Actor.objects.filter(
        first_name="Kianu", last_name="Reaves"
    ).update(first_name="Keanu", last_name="Reeves")

    Genre.objects.filter(
        name="Action"
    ).delete()
    Actor.objects.filter(
        first_name="Scarlet"
    ).delete()

    return [
        Actor.objects.filter(last_name="Smith").order_by("first_name")
    ]
