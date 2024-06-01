from django.shortcuts import render, get_object_or_404
from . import models

def techno_view(request):
    if request.method == "GET":
        techno = models.TechnoDom.objects.filter().order_by("-id")
        video_content = models.VideoContent.objects.filter().order_by("-id")
        return render(
            request,
            template_name="techno.html",
            context={"techno": techno, "video_content": video_content},
        )

def techno_detail_view(request, id):
    if request.method == "GET":
        techno_id = get_object_or_404(models.TechnoDom, id=id)
        return render(
            request,
            template_name="techno.html",
            context={"techno_id": techno_id},
        )


# class TechnoDomView(generic.ListView):
#     model = models.TechnoDom
#     template_name = 'techno.html'
#     context_object_name = 'techno'
#     ordering = ['-id']
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['video_content'] = models.VideoContent.objects.order_by('-id')
#         return context