from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index(request):
    return render(request, 'birthday_app/index.html')

@csrf_exempt
def notify_button_click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Thông báo từ người dùng:", data.get('message'))
        # Xử lý logic tại đây, ví dụ lưu thông tin vào cơ sở dữ liệu
        return JsonResponse({'status': 'success', 'message': 'Thông báo đã nhận!'})
    return JsonResponse({'status': 'error', 'message': 'Yêu cầu không hợp lệ.'}, status=400)