from django.db import models

class ServerList(models.Model):
    ID = models.BigAutoField(primary_key=True)
    ServerID = models.BigIntegerField(null = True)
    ServerName = models.CharField(max_length=100)
    HostName = models.CharField(max_length=100)
    IPAddress = models.CharField(max_length=100)
    ServerToken = models.CharField(max_length=255)

    def __str__(self):
     return self.ServerName

class ServerStatus(models.Model):
    ID = models.BigAutoField(primary_key=True)
    ServerID= models.BigIntegerField(null = True)
    date =  models.DateField()
    time = models.TimeField()
    CPUUsage = models.FloatField()
    MemoryUsage = models.FloatField()
    DiskUsage = models.FloatField()
    UpTime = models.CharField(max_length=20)
    Health = models.BooleanField()

    def __str__(self):
        return str(self.ServerID)

class ServerActivity(models.Model):
    ServerID= models.BigIntegerField(null = True)
    Hostname = models.CharField(max_length=100 , null=True)
    date =  models.DateField()
    time = models.TimeField()
    StartActivity = models.TimeField()
    EndActivity = models.TimeField()
    Activity = models.CharField(max_length=400)
    Status = models.CharField(max_length=20)

    def __str__(self):
        return str(self.ServerID)