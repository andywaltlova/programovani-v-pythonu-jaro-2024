# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/balicky-z-internetu/lesson


# Faker
from faker import Faker
fake = Faker('cs_CZ')

for _ in range(3):
  print(fake.name_female())
  print(fake.address())
  print()


from faker.providers import internet

fake.add_provider(internet)
print(fake.email())

# je treba doinstalovat balicek faker_music
# pip install faker_music

from faker_music import MusicProvider

fake.add_provider(MusicProvider)
print(fake.music_genre())