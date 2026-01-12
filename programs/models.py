from django.db import models

class Program(models.Model):
    PROGRAM_TYPE = (
        ('course', 'Course'),
        ('internship', 'Internship'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
