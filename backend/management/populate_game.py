from faker import Faker
from account.models import CustomizeUser
from game.models import Game

import numpy as np
from random import randint
import random

game_types = ('Football', 'Basketball', 'Tennis', 'Badminton', 'Hiking', 'Running')
court_status = ['Book', 'Not Book']
location1 = ['Lavana', 'UM', 'UKM', 'UPM', 'ABM', 'Stadium Melawati', 'Stadium Hang Jebat', 
             'Stadium Kajang', 'Stadium Maybank', 'Stadium Sime Darby', 'Stadium Putrajaya']
location2 = ['Putrajaya', 'Kajang', 'Bangi', 'Serdang', 'Subang Jaya', 'Petaling Jaya', 'Puchong',
             'Shah Alam', 'Bangsar', 'Sungai Besi', 'Ampang']

def random_date_generator(start_date, range_in_days):
    days_to_add = np.arange(0, range_in_days)
    random_date = np.datetime64(start_date) + np.random.choice(days_to_add)
    return str(random_date)

court_name = ['A1', 'A2', 'A3', 
              'B1', 'B2', 'B3',
              'C1', 'C2', 'C3',
              'D1', 'D2', 'D3']

fake = Faker()

for i in range(1000):
    game = Game(
        sport_type = random.choice(game_types),
        location1 = random.choice(location1),
        location2 = random.choice(location2),
        date = random_date_generator("2022-08-23", 65),
        arranger = CustomizeUser.objects.get(pk=randint(1,16)),
        occupied_player = randint(10, 22),
        player_needed = randint(1,5),
        court_status = random.choice(court_status),
        court_name = random.choice(court_name),
        court_price = randint(40, 150),
        price_per_player = randint(10, 20)
    )
    game.save()
    