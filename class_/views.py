from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from class_.models import Class, ClassJoined, Stream, Comment
from student.models import Student
from django.contrib import messages
# Create your views here.


def requeststudent(request, id):
    all_id = [x.student_id for x in ClassJoined.objects.filter(
        class_join_id=id, is_accept=True)]
    reqeust_id = [x.student_id for x in ClassJoined.objects.filter(
        class_join_id=id, is_accept=False)]
    context = {
        'class': Class.objects.get(id=id),
        'student': Student.objects.filter(id__in=all_id),
        'request_student': Student.objects.filter(id__in=reqeust_id),
    }
    return render(request, 'class_/class_student_request.html', context)


def classRemove(request, id):
    class_ = Class.objects.get(id=id)
    class_.delete()
    return redirect(reverse_lazy('teacher_dashboard'))


def requestAccept(request, class_id, student_id):
    classJoin = ClassJoined.objects.get(
        class_join_id=class_id, student_id=student_id)
    classJoin.is_accept = True
    classJoin.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def studentRemoveFromClass(request, class_id, student_id):
    print(class_id)
    print(student_id)
    classJoin = ClassJoined.objects.get(
        class_join_id=class_id, student_id=student_id)
    classJoin.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def stream(request):
    if request.method == 'GET':
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        try:
            content = request.POST.get('content')
            file = request.FILES.get('file')
            class_id = request.POST.get('class_id')
            s = Stream(content=content, file=file, class_stream_id=class_id)
            s.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except:
            messages.add_message(request, messages.ERROR, 'some error occured')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def comment(request):
    if request.method == 'GET':
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        try:
            comment = request.POST.get('comment')
            stream_id = request.POST.get('stream_id')
            s = Comment(comment=comment, stream_id=stream_id,
                        user_id=request.user.id)
            s.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except:
            messages.add_message(request, messages.ERROR, 'some error occured')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def getClassId(code):
    print(code)
    c = Class.objects.get(code=code)
    return c.id


class ClassDetailView(DetailView):
    model = Class
    slug_field = 'code'

    def get_context_data(self, **kwargs):
        context = super(ClassDetailView, self).get_context_data(**kwargs)
        class_id = getClassId(self.kwargs['slug'])
        s = Stream.objects.filter(class_stream_id=class_id)
        c = Comment.objects.all()
        context['stream'] = s
        context['comment'] = c
        return context
