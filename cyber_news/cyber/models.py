from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    name = models.CharField(max_length=100)
    founder_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Gamer(models.Model):
    full_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100 , unique=True)
    rating = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='static/assets/avatars/')
    game = models.ForeignKey(Game , on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image_logo = models.ImageField(upload_to='static/assets/images/')

class Gamer_Group(models.Model):
    name = models.CharField(max_length=100)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    gamer_id = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Game_Club(models.Model):
    name = models.CharField(max_length=100)
    address  = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/assets/images/')

class Battle(models.Model):
    battle_data = models.DateTimeField(auto_now_add=True)
    game_club_id = models.ForeignKey(Game_Club, on_delete=models.CASCADE)
    battle_time = models.IntegerField()
    group_1_id = models.ForeignKey(Gamer_Group, on_delete=models.CASCADE)
    group_2_id = models.ForeignKey(Gamer_Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Battle_News(models.Model):
    battle_id = models.ForeignKey(Battle, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Battle_News_Images(models.Model):
    image = models.ImageField(upload_to='static/assets/images/')
    battle_id = models.ForeignKey(Battle, on_delete=models.CASCADE)
    battle_news_id = models.ForeignKey(Battle_News, on_delete=models.CASCADE)

class Updata_news(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='static/assets/videos/')
    image = models.ImageField(upload_to='static/assets/images/')