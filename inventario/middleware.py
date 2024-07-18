# from django.http import HttpResponseForbidden
# from django.shortcuts import redirect

# class SuperUserRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.path.startswith('/inventario/') and not request.user.is_superuser:
#             if request.user.is_authenticated:
#                 return HttpResponseForbidden("You do not have permission to access this page.")
#             else:
#                 return redirect('admin:login')  
#         return self.get_response(request)