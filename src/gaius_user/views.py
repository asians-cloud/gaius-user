from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def check_sso(request):
    html = """<html>
<body>
    <script>
        parent.postMessage(location.href, location.origin)
    </script>
</body>
</html>"""
    return HttpResponse(html)