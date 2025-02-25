# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Charting library for Weblate."""

from typing import Optional

from django.http import JsonResponse

from weblate.metrics.models import Metric
from weblate.metrics.wrapper import MetricsWrapper


def monthly_activity_json(
    request,
    project: Optional[str] = None,
    component: Optional[str] = None,
    lang: Optional[str] = None,
    user: Optional[str] = None,
):
    """Return monthly activity for matching changes as json."""
    metrics = MetricsWrapper(None, Metric.SCOPE_GLOBAL, 0)
    return JsonResponse(data=metrics.daily_activity, safe=False)
