from django.db import models
from teacher.models import Teacher
from student.models import Student
from account.models import Account
# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=3,null=True,blank=True)
    subject = models.CharField(max_length=150,null=True,blank=True)
    code = models.CharField(max_length=10,unique=True)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ClassJoined(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    class_join = models.ForeignKey(Class,on_delete=models.CASCADE)
    is_accept = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name
    class Meta:
        db_table = 'class_join'
        unique_together = ('student','class_join',)


class Stream(models.Model):
    content = models.TextField()
    file = models.FileField(upload_to='stream/')
    class_stream = models.ForeignKey(Class,on_delete=models.CASCADE)

    def __str__(self):
        return self.class_stream.name


class Comment(models.Model):
    comment = models.TextField()
    stream = models.ForeignKey(Stream,on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email