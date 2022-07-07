from rest_framework import viewsets
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from basics.models import T_1, T_2, T_3
from basics.serializers import T1Serializer, T2Serializer, T3Serializer

@login_required()
def index(request):
    context = {"allowed_items": []}
    if request.user.groups.filter(name="П1"):
        context["allowed_items"].extend(["ПМ1", "ПМ2", "ПМ3"])
    elif request.user.groups.filter(name="П2"):
        context["allowed_items"].extend(["ПМ1", "ПМ2"])
    if request.user.groups.filter(name="П3"):
        context["allowed_items"].extend(["ПМ2", "ПМ3"])

    return render(request, "index.html", context=context)


class T1ViewSet(viewsets.GenericViewSet):
    queryset = T_1.objects.all()
    serializer_class = T1Serializer

    def get_queryset(self):
        return self.queryset.filter(responsible_group__in=self.request.user.groups.all())

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


class T2ViewSet(viewsets.GenericViewSet):
    queryset = T_2.objects.all()
    serializer_class = T2Serializer

    def get_queryset(self):
        return self.queryset.filter(responsible_group__in=self.request.user.groups.all())

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


class T3ViewSet(viewsets.GenericViewSet):
    queryset = T_3.objects.all()
    serializer_class = T3Serializer

    def get_queryset(self):
        return self.queryset.filter(responsible_group__in=self.request.user.groups.all())

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
