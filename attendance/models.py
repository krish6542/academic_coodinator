from django.db import models
from programs.models import Program

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')]
    )

    def __str__(self):
        return f"{self.student_name} - {self.status}"

