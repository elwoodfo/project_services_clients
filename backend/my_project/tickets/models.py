from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class TicketStatus(models.Model):
    name = models.CharField(max_length=100)

class TicketPriority(models.Model):
    name = models.CharField(max_length=100)

class TicketCategory(models.Model):
    name = models.CharField(max_length=100)

class Channel(models.Model):
    name = models.CharField(max_length=100)

class Role(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(TicketStatus, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(TicketPriority, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(TicketCategory, on_delete=models.SET_NULL, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True)
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=255)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)