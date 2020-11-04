from django.db import models


class Resume(models.Model):
    resume_name = models.CharField(max_length=25)

    @property
    def education(self):
        return Education.objects.filter(resume=self)

    @property
    def skills(self):
        return Skills.objects.filter(resume=self)

    @property
    def honours(self):
        return Honours.objects.filter(resume=self)

    def __str__(self):
        return self.resume_name


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    college_name = models.CharField(max_length=50, blank=False)
    course = models.CharField(max_length=50, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.college_name


class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=15)

    def __str__(self):
        return self.skill_name


class Honours(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    issue_date = models.DateField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title
