from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from applications.models import Application
from programs.models import Program
from .models import Attendance


def mark_attendance(request):
	"""List approved applications (enrolled students) and record attendance.

	- GET: show approved students for a chosen program (or all programs)
	- POST: save attendance records for submitted students
	"""
	program_id = request.GET.get('program')
	programs = Program.objects.filter(is_active=True)

	if program_id:
		try:
			program = Program.objects.get(id=program_id)
		except Program.DoesNotExist:
			program = None
	else:
		program = None

	# Only approved applications count as enrolled
	apps_qs = Application.objects.filter(status='approved')
	if program:
		apps_qs = apps_qs.filter(program=program)

	if request.method == 'POST':
		# Expected POST format: attendance_<app_id> = present|absent|late
		saved = 0
		today = timezone.now().date()
		for app in apps_qs:
			key = f'attendance_{app.id}'
			status = request.POST.get(key)
			if status:
				# avoid duplicate records for same student on same date
				existing = Attendance.objects.filter(student_id=str(app.id), date=today).first()
				if existing:
					existing.status = status
					existing.save()
				else:
					Attendance.objects.create(
						student_name=app.student_name,
						student_id=str(app.id),
						program=app.program,
						status=status,
					)
				saved += 1

		messages.success(request, f'Saved {saved} attendance records.')
		# redirect to avoid duplicate POST on refresh
		if program:
			return redirect(f'?program={program.id}')
		return redirect('attendance:mark_attendance')

	return render(request, 'attendance/mark.html', {
		'programs': programs,
		'selected_program': program,
		'applications': apps_qs,
	})
