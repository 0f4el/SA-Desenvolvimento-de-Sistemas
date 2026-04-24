from django.shortcuts import render


class CustomErrorPagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/api/"):
            return self.get_response(request)

        try:
            response = self.get_response(request)
        except Exception:
            return render(request, "error_500.html", status=500)

        if response.status_code == 404:
            return render(request, "error_404.html", {"rota": request.path}, status=404)

        if response.status_code == 500:
            return render(request, "error_500.html", status=500)

        return response
