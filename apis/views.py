# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import partial
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.BasePermission,))
def api_sign_in(request):
	return Response({"result": "hello world1"}, status=status.HTTP_200_OK)
