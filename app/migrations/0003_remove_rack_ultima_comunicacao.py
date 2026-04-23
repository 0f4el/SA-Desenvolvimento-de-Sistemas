from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_sala_rack_notebook"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rack",
            name="ultima_comunicacao",
        ),
    ]
