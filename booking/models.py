from django.db import models

# Create your models here.

class Vacancy(models.Model):
    date = models.CharField(max_length=8)
    time = models.IntegerField()
    vacancy = models.IntegerField()

    def __str__(self):
        if self.time == 1:
            time = "中午"
        else:
            time = "晚上"
        return f"{self.date[4:6]} / {self.date[6:8]} {time} 尚有 {self.vacancy} 桌空位"


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    sex = models.BooleanField()
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=60)
    staff = models.BooleanField()

    def __str__(self):
        if self.sex == True:
            sex = "先生"
        else:
            sex = "女士"
        return f"{self.name} {sex}"

class Booking(models.Model):
    date = models.CharField(max_length=8)
    time = models.IntegerField()
    user = models.IntegerField()
    name = models.CharField(max_length=60)
    sex = models.BooleanField()
    mobile = models.CharField(max_length=20)
    number = models.IntegerField()
    steak = models.IntegerField()
    fish = models.IntegerField()
    chicken = models.IntegerField()

    def __str__(self):
        if self.time == 1:
            time = "中午"
        else:
            time = "晚上"
        return f"{self.name} 在 {self.date[4:6]} / {self.date[6:8]} {time} 預訂{self.number}位"

'''
class Post(models.Model):
    # related to User
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # attributes
    content = models.fields.TextField(blank=True)
    liked = models.fields.PositiveIntegerField(default=0)

    created = models.fields.DateTimeField(default=timezone.now)
    last_updated = models.fields.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ":" + str(self.content)
'''