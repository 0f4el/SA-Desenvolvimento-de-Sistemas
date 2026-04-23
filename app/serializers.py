from rest_framework import serializers

from .models import Notebook, Rack, Sala


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ["id", "nome", "bloco", "numero", "andar"]


class RackSerializer(serializers.ModelSerializer):
    sala_nome = serializers.CharField(source="sala.nome", read_only=True)

    class Meta:
        model = Rack
        fields = [
            "id",
            "identificador",
            "sala",
            "sala_nome",
            "status",
            "quantidade_slots",
            "temperatura",
        ]


class NotebookSerializer(serializers.ModelSerializer):
    rack_identificador = serializers.CharField(source="rack.identificador", read_only=True)
    sala_nome = serializers.CharField(source="rack.sala.nome", read_only=True)

    class Meta:
        model = Notebook
        fields = [
            "id",
            "tag",
            "modelo",
            "rack",
            "rack_identificador",
            "sala_nome",
            "numero_slot",
            "status",
            "ultima_atualizacao",
        ]
        read_only_fields = ["ultima_atualizacao"]

    def validate(self, attrs):
        rack = attrs.get("rack") or getattr(self.instance, "rack", None)
        numero_slot = attrs.get("numero_slot") or getattr(self.instance, "numero_slot", None)

        if rack and numero_slot and numero_slot > rack.quantidade_slots:
            raise serializers.ValidationError({
                "numero_slot": f"O rack possui apenas {rack.quantidade_slots} slots."
            })

        return attrs
