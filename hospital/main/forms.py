from .models import Specialization, Disease, Patient, Doctor, Diagnosis
from django.forms import ModelForm, TextInput, Textarea

class SpecForm(ModelForm):
    class Meta:
        model = Specialization
        fields = ["spec_id", "spec_title"]
        widgets ={'spec_id': TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Введіть Id'
        }),
            'spec_title' : TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Введіть назву спеціалізації'
        })
        }

class DisForm(ModelForm):
    class Meta:
        model = Disease
        fields = ["dis_id", "dis_name", "profylaxy", "treatment"]
        widgets ={'dis_id': TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Введіть Id'
        }),
            'treatment' : TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Введіть назву хвороби'
        }),
            'profylaxy': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть профілактику'
            }),
            'dis_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть лікування'
            })
        }

class PatForm(ModelForm):
            class Meta:
                model = Patient
                fields = ["pat_id", "fullName", "adress", "phoneNumber", "insurancepolicy", "passportId"]
                widgets = {'pat_id': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введіть Id'
                }),
                    'passportId': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': "Введіть повне ім'я пацієнта"
                    }),
                    'adress': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введіть адресу пацієнта'
                    }),
                    'phoneNumber': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введіть номер телефону пацієнта'
                    }),
                    'insurancepolicy': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введіть номер страхового полісу'
                    }),
                    'fullName': TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введіть номер паспорту пацієнта'
                    })
                }


class DocForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ["doc_id", "fullName", "position", "spec", "workExp", "adress", "phoneNumber"]
        widgets = {'doc_id': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть Id'
        }),
            'phoneNumber': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть повне ім'я лікаря"
            }),
            'position': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть посаду лікаря'
            }),
            'spec': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть спеціальність лікаря'
            }),
            'workExp': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть досвід роботи лікаря'
            }),
            'adress': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть адресу проживання лікаря'
            }),
            'fullName': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть номер телефону лікаря'
            })
        }


class DiagForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = ["diag_id", "patient", "disease", "doctor", "dateOfApplication", "dateOfRecovery"]
        widgets = {'diag_id': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть Id'
        }),
            'patient': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть пацієнта"
            }),
            'disease': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть хворобу'
            }),
            'doctor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть лікаря'
            }),
            'dateOfApplication': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть дату запису'
            }),
            'dateOfRecovery': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть дату одужання'
            })
        }