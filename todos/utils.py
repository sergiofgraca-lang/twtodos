from django.contrib.auth import get_user_model

def create_default_superuser():
    User = get_user_model()

    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@email.com",
            password="admin123"
        )
        print("Superusuário criado automaticamente.")
    else:
        print("Superusuário já existe.")