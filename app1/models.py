from django.db import models

class College(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=200)

    def __str__(self):

        return self.name


class Batch(models.Model):
    batch_id = models.IntegerField()
    year_from = models.CharField(max_length=10)
    year_to = models.CharField(max_length=10)

    class Meta(object):
        ordering = ['id']

    def __str__(self):
        return self.year_from+' - '+self.year_to


class Semester(models.Model):
    sem = models.CharField(max_length=10)

    class Meta(object):
        ordering = ['id']

    def __str__(self):
        return self.sem


class Section(models.Model):
    sec_id = models.IntegerField()
    section = models.CharField(max_length=10)

    class Meta(object):
        ordering = ['id']

    def __str__(self):
        return self.section


class Department(models.Model):
    code = models.IntegerField()
    department = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    class Meta(object):
        ordering = ['code']

    def __str__(self):
        return self.department


class Designation(models.Model):
    designation_id = models.IntegerField()
    designation = models.CharField(max_length=100)

    class Meta(object):
        ordering = ['designation_id']

    def __str__(self):
        return self.designation


class Staff(models.Model):
    staff_id = models.IntegerField()
    name = models.CharField(max_length=100)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta(object):
        ordering = ['staff_id']

    def __str__(self):                                                  
        return '{}, {}'.format(self.name, self.designation)


class Student(models.Model):
    register_no = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        r = str(self.id)
        self.register_no = '{}{}{}{}'.format(self.department.college.code,self.batch.batch_id,self.department.code,'00'+r)
        super(Student, self).save(*args, **kwargs)

    # def register_id(self):
    #     # stud = Student()
    #     r = '00'+str(self.id)
    #     # stud.register_no = str(self.department.college.code) + str(self.batch.batch_id) + str(self.department.code) + str(r)
    #     # stud.save()
        
    #     return '{}{}{}{}'.format(self.department.college.code,self.batch.batch_id,self.department.code,r)

    def __str__(self):
         return '{}'.format(self.register_no)

    class Meta(object):
        ordering = ['id']


class Subject(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta(object):
        ordering = ['id']

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)


class Mark(models.Model):
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def student_register_no(self):
        return self.student.name

    class Meta(object):
        ordering = ['sem']

    def __str__(self):
        return '{}, {}'.format(self.department, self.student.register_no)


class Rank(models.Model):
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)

    def student_register_no(self):
        return self.student.name

    class Meta(object):
        ordering = ['id']

    def __str__(self):
       return '{}, {}'.format(self.department, self.student.register_no)

