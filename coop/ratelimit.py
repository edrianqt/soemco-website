"""Tiny per-IP rate limiter for POST requests (uses Django's cache)."""
from functools import wraps
from django.core.cache import cache
from django.http import HttpResponse


def ratelimit(limit=5, seconds=60):
    def deco(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if request.method == "POST":
                ip = request.META.get("REMOTE_ADDR", "unknown")
                key = f"rl:{view.__name__}:{ip}"
                cache.add(key, 0, seconds)
                try:
                    count = cache.incr(key)
                except ValueError:
                    cache.set(key, 1, seconds)
                    count = 1
                if count > limit:
                    return HttpResponse("Too many requests. Please wait a minute and try again.", status=429)
            return view(request, *args, **kwargs)
        return wrapper
    return deco
