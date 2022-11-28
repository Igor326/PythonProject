from django.db import models
from django.db.models import CharField


class Specialization(models.Model):
    spec_id = models.IntegerField('Id', null=False, db_index=True, primary_key=True, unique=True)
    spec_title = models.CharField('Назва спеціалізації', max_length=50,)

    def __str__(self):
        return self.spec_title

    def __int__(self):
        return self.spec_id

    class Meta:
        verbose_name = 'Спеціалізація'
        verbose_name_plural = 'Спеціалізації'


class Disease(models.Model):
    dis_id = models.IntegerField('Id',  unique=True, default='0' )
    dis_name = models.CharField('Лікування', max_length=60)
    profylaxy = models.CharField('Профілактика', max_length=200)
    treatment= models.CharField('Назва хвороби', max_length=200)

    def __int__(self):
        return self.dis_id

    def __str__(self):
        return self.dis_name

    def __str__(self):
        return self.profylaxy

    def __str__(self):
        return self.treatment


    class Meta:
        verbose_name = 'Хвороба'
        verbose_name_plural = 'Хвороби'


class Patient(models.Model):
    pat_id = models.IntegerField('Id', null=True, unique=True)
    fullName = models.CharField("Номер паспорту", max_length=100)
    adress = models.CharField("Адреса проживання", max_length=200)
    phoneNumber = models.CharField('Номер телефону',max_length=15)
    insurancepolicy = models.CharField('Страховий поліс', max_length=60)
    passportId = models.CharField("Повне ім'я", max_length=45)

    def __int__(self):
        return self.pat_id

    def __str__(self):
        return self.fullName

    def __str__(self):
        return self.adress

    def __str__(self):
        return self. phoneNumber

    def __str__(self):
        return self.insurancepolicy

    def __str__(self):
        return self.passportId

    class Meta:
        verbose_name = 'Пацієнт'
        verbose_name_plural = 'Пацієнти'


class Doctor(models.Model):
    doc_id = models.IntegerField('Id', null=True, unique=True)
    fullName = models.CharField("Номер телефону", max_length=45)
    position = models.CharField("Посада", max_length=45)
    spec = models.ForeignKey(Specialization, to_field='spec_id', on_delete=models.CASCADE, null= True)
    workExp = models.CharField("Досвід роботи", max_length=45)
    adress = models.CharField("Адреса проживання", max_length=100)
    phoneNumber = models.CharField("Повне ім'я", max_length=15)
    spec.verbose_name = "Спеціалізація"
    def __int__(self):
        return self.doc_id

    def __str__(self):
        return self.fullName

    def __str__(self):
        return self.position

    def __int__(self):
        return self.spec

    def __str__(self):
        return self.workExp

    def __str__(self):
        return self.adress

    def __str__(self):
        return self.phoneNumber

    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'

class Diagnosis(models.Model):
    diag_id = models.IntegerField('Id', null=False, unique=True)
    patient = models.ForeignKey(Patient, to_field='pat_id', on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, to_field='dis_id', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, to_field='doc_id', on_delete=models.CASCADE)
    dateOfApplication = models.CharField("Дата запису", max_length=45)
    dateOfRecovery = models.CharField("Дата одужання", max_length=45)
    patient.verbose_name ='Пацієнт'
    disease.verbose_name = 'Хвороба'
    doctor.verbose_name = 'Лікар'
    def __int__(self):
        return self.diag_id

    def __int__(self):
        return self.patient

    def __int__(self):
        return self.disease

    def __int__(self):
        return self.doctor

    def __str__(self):
        return self.dateOfApplication

    def __str__(self):
        return self.dateOfRecovery

    class Meta:
        verbose_name = 'Діагноз'
        verbose_name_plural = 'Діагнози'




