from faker.providers import BaseProvider
import random

class Provider(BaseProvider):
    tiers = (
        ('Beginner', 'Intermediate', 'Advanced', 'Expert'),
        ('Essential', 'Team', 'Corporate', 'Enterprise'),
        ('Starter', 'Basic', 'Professional', 'Premium'),
        ('Personal', 'Partnership', 'Company', 'Group'),
        ('Good', 'Better', 'Best', 'Ultimate'),
        ('Basic', 'Standard', 'Super', 'Ultra'),
        ('Nano', 'Micro', 'Mega', 'Giga'),
        ('Bronze', 'Silver', 'Gold', 'Platinum'),
        ('Silver', 'Ruby', 'Golden', 'Diamond'),
        ('Emerald', 'Ruby', 'Sapphire', 'Diamond'),
        ('Hamlet', 'Village', 'Town', 'City'),
        ('The Gods', 'Grand Circle', 'Royal Circle', 'Stalls'),
        ('League Two', 'League One', 'Championship', 'Premier'),
        ('Hare', 'Antelope', 'Cheetah', 'Falcon'),
        ('Seed', 'Shoot', 'Sapling', 'Tree')
    )

    def subscription_level(self):
        return self.random_element(self.random_element(self.tiers))

    def subscription_upgrade(self):
        tiers = self.random_element(self.tiers)
        a, b = random.sample(range(len(tiers)), 2)
        if a > b:
            a, b = b, a
        return (tiers[a], tiers[b])

    def subscriptin_downgrade(self):
        tiers = self.random_element(self.tiers)
        a, b = random.sample(range(len(tiers)), 2)
        if a < b:
            a, b = b, a
        return (tiers[a], tiers[b])

