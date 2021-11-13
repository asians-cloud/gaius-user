# -*- coding: utf-8 -*-
from django.db import models

try:
    from cms.models import CMSPlugin

    class User(CMSPlugin):
        label = models.CharField(
            blank=True,
            max_length=200,
        )

        def __str__(self):
            return self.label

except ModuleNotFoundError as err:
    # Error handling
    # print(err)
    pass

