from faker.providers.address.en import Provider as BaseProvider
import json
import random
import math
from pathlib import Path

ZIP_CODES = {}

WKDIR = Path(__file__).absolute().parent
ZIP_CODES_FILE = WKDIR / 'zip_codes.json'

with open(ZIP_CODES_FILE, 'r') as f:
    ZIP_CODES = json.load(f)


class Provider(BaseProvider):
    zip_codes = ZIP_CODES

    street_names = (
        '10th',
        '53rd',
        '1st',
        '2nd',
        '3rd',
        '4th',
        '6th',
        '8th',
        'Acacia',
        'Academy',
        'Adams',
        'Addison',
        'Airport',
        'Albany',
        'Alderwood',
        'Alton',
        'Amerige',
        'Amherst',
        'Anderson',
        'Andover',
        'Ann',
        'Annadale',
        'Applegate',
        'Arcadia',
        'Arch',
        'Argyle',
        'Arlington',
        'Armstrong',
        'Arnold',
        'Arrowhead',
        'Ashley',
        'Aspen',
        'Atlantic',
        'Augusta',
        'Baker',
        'Bald Hill',
        'Bank',
        'Bay',
        'Bay Meadows',
        'Bayberry',
        'Bayport',
        'Beach',
        'Beacon',
        'Bear Hill',
        'Beaver Ridge',
        'Bedford',
        'Beech',
        'Beechwood',
        'Bellevue',
        'Belmont',
        'Berkshire',
        'Big Rock Cove',
        'Birch Hill',
        'Birchpond',
        'Birchwood',
        'Bishop',
        'Blackburn',
        'Blue Spring',
        'Bohemia',
        'Border',
        'Boston',
        'Bow Ridge',
        'Bowman',
        'Bradford',
        'Branch',
        'Brandywine',
        'Brewery',
        'Briarwood',
        'Brickell',
        'Brickyard',
        'Bridge',
        'Bridgeton',
        'Bridle',
        'Broad',
        'Brook',
        'Brookside',
        'Brown',
        'Buckingham',
        'Buttonwood',
        'Cactus',
        'Cambridge',
        'Campfire',
        'Canal',
        'Canterbury',
        'Cardinal',
        'Carpenter',
        'Carriage',
        'Carson',
        'Catherine',
        'Cedar',
        'Cedar Swamp',
        'Cedarwood',
        'Cemetery',
        'Center',
        'Central',
        'Chapel',
        'Charles',
        'Cherry',
        'Cherry Hill',
        'Chestnut',
        'Church',
        'Circle',
        'Clark',
        'Clay',
        'Cleveland',
        'Clinton',
        'Cobblestone',
        'Coffee',
        'College',
        'Colonial',
        'Columbia',
        'Constitution',
        'Cooper',
        'Corona',
        'Cottage',
        'Country',
        'Country Club',
        'County',
        'Court',
        'Courtland',
        'Creek',
        'Creekside',
        'Crescent',
        'Cross',
        'Cypress',
        'Deerfield',
        'Del Monte',
        'Delaware',
        'Depot',
        'Devon',
        'Devonshire',
        'Division',
        'Dogwood',
        'Dunbar',
        'Durham',
        'Eagle',
        'East',
        'Edgefield',
        'Edgemont',
        'Edgewater',
        'Edgewood',
        'El Dorado',
        'Elizabeth',
        'Elm',
        'Elmwood',
        'Essex',
        'Euclid',
        'Evergreen',
        'Fairfield',
        'Fairground',
        'Fairview',
        'Fairway',
        'Fawn',
        'Fieldstone',
        'Fifth',
        'Fordham',
        'Forest',
        'Foster',
        'Foxrun',
        'Franklin',
        'Fremont',
        'Front',
        'Fulton',
        'Gainsway',
        'Galvin',
        'Garden',
        'Garfield',
        'Gartner',
        'Gates',
        'George',
        'Glen Creek',
        'Glen Eagles',
        'Glen Ridge',
        'Glendale',
        'Glenholme',
        'Glenlake',
        'Glenridge',
        'Glenwood',
        'Golden Star ',
        'Goldfield',
        'Golf',
        'Gonzales',
        'Grand',
        'Grandrose',
        'Grant',
        'Green',
        'Green Hill',
        'Green Lake',
        'Greenrose',
        'Greenview',
        'Gregory',
        'Greystone',
        'Griffin',
        'Grove',
        'Gulf',
        'Halifax',
        'Hall',
        'Hamilton',
        'Hanover',
        'Harrison',
        'Hartford',
        'Harvard',
        'Harvey',
        'Hawthorne',
        'Heather',
        'Helen',
        'Henry',
        'Henry Smith',
        'Heritage',
        'Hickory',
        'High',
        'High Noon',
        'High Point',
        'High Ridge',
        'Highland',
        'Hill',
        'Hill Field',
        'Hillcrest',
        'Hilldale',
        'Hillside',
        'Hilltop',
        'Holly',
        'Homestead',
        'Homewood',
        'Honey Creek',
        'Howard',
        'Hudson',
        'Illinois',
        'Indian Spring',
        'Indian Summer',
        'Inverness',
        'Iroquois',
        'Ivy',
        'Jackson',
        'James',
        'Jefferson',
        'Jennings',
        'Jockey Hollow',
        'John',
        'Johnson',
        'Jones',
        'Joy Ridge',
        'Kent',
        'Ketch Harbour',
        'King',
        'Kingston',
        'Kirkland',
        'La Sierra',
        'Lafayette',
        'Lafayette ',
        'Lake',
        'Lake Forest',
        'Lake View',
        'Lakeshore',
        'Lakeview',
        'Lakewood',
        'Lancaster',
        'Lantern',
        'Laurel',
        'Lawrence',
        'Leatherwood',
        'Lees Creek',
        'Leeton Ridge',
        'Lexington',
        'Liberty',
        'Lilac',
        'Lincoln',
        'Linda',
        'Linden',
        'Littleton',
        'Livingston',
        'Locust',
        'Logan',
        'Longbranch',
        'Longfellow',
        'Lookout',
        'Lower River',
        'Lyme',
        'Madison',
        'Magnolia',
        'Maiden',
        'Main',
        'Mammoth',
        'Manchester',
        'Manhattan',
        'Manor',
        'Manor Station',
        'Maple',
        'Marconi',
        'Market',
        'Marlborough',
        'Marsh',
        'Marshall',
        'Marvon',
        'Mayfair',
        'Mayfield',
        'Mayflower',
        'Meadow',
        'Meadowbrook',
        'Mechanic',
        'Middle River',
        'Miles',
        'Military',
        'Mill',
        'Mill Pond',
        'Miller',
        'Monroe',
        'Morris',
        'Mountainview',
        'Mulberry',
        'Myers',
        'Myrtle',
        'New',
        'New Saddle',
        'Newbridge',
        'Newcastle',
        'Newport',
        'Nichols',
        'Nicolls',
        'North',
        'Nut Swamp',
        'Oak',
        'Oak Meadow',
        'Oak Valley',
        'Oakland',
        'Oakwood',
        'Ocean',
        'Ohio',
        'Oklahoma',
        'Old York',
        'Olive',
        'Orange',
        'Orchard',
        'Overlook',
        'Oxford',
        'Pacific',
        'Paris Hill',
        'Park',
        'Parker',
        'Pawnee',
        'Peachtree',
        'Pearl',
        'Peg Shop',
        'Pendergast',
        'Peninsula',
        'Penn',
        'Pennington',
        'Pennsylvania',
        'Pheasant',
        'Philmont',
        'Pierce',
        'Pilgrim',
        'Pin Oak',
        'Pine',
        'Pineknoll',
        'Piper',
        'Pleasant',
        'Plumb Branch',
        'Plymouth',
        'Poor House',
        'Poplar',
        'Prairie',
        'Primrose',
        'Prince',
        'Princess',
        'Princeton',
        'Proctor',
        'Prospect',
        'Pulaski',
        'Pumpkin Hill',
        'Purple Finch',
        'Queen',
        'Race',
        'Railroad',
        'Ramblewood',
        'Randall Mill',
        'Redwood',
        'Richardson',
        'Ridge',
        'Ridgeview',
        'Ridgewood',
        'River',
        'Riverside',
        'Riverview',
        'Roberts',
        'Rock Creek',
        'Rock Maple',
        'Rockaway',
        'Rockcrest',
        'Rockland',
        'Rockledge',
        'Rockville',
        'Rockwell',
        'Rocky River',
        'Roehampton',
        'Roosevelt',
        'Rose',
        'Rosewood',
        'Ryan',
        'Sage',
        'San Carlos',
        'San Juan',
        'San Pablo',
        'Santa Clara',
        'Saxon',
        'Saxton',
        'School',
        'Schoolhouse',
        'Second',
        'Selby',
        'Shadow Brook',
        'Shady',
        'Sheffield',
        'Sherman',
        'Sherwood',
        'Shipley',
        'Shirley',
        'Shore',
        'Shub Farm',
        'Sierra',
        'Silver Spear',
        'Sleepy Hollow',
        'Smith',
        'Smith Store',
        'Smoky Hollow',
        'Snake Hill',
        'Somerset',
        'South',
        'Southampton',
        'Spring',
        'Spruce',
        'Squaw Creek',
        'St Louis',
        'St Margarets',
        'St Paul',
        'State',
        'Stillwater',
        'Stonybrook',
        'Strawberry',
        'Studebaker',
        'Sugar',
        'Sulphur Springs',
        'Summer',
        'Summerhouse',
        'Summit',
        'Sunbeam',
        'Sunnyslope',
        'Sunset',
        'Surrey',
        'Sussex',
        'Sutor',
        'Swanson',
        'Sycamore',
        'Tailwater',
        'Talbot',
        'Tallwood',
        'Tanglewood',
        'Tarkiln Hill',
        'Taylor',
        'Temple',
        'Thatcher',
        'Theatre',
        'Third',
        'Thomas',
        'Thompson',
        'Thorne',
        'Tower',
        'Trenton',
        'Trout',
        'Trusel',
        'Tunnel',
        'Union',
        'University',
        'Vale',
        'Valley',
        'Valley Farms',
        'Valley View',
        'Van Dyke',
        'Vermont',
        'Vernon',
        'Victoria',
        'Vine',
        'Virginia',
        'Wagon',
        'Wakehurst',
        'Wall',
        'Walnut',
        'Walnutwood',
        'Walt Whitman',
        'Warren',
        'Washington',
        'Water',
        'Wayne',
        'Wellington',
        'Wentworth',
        'West',
        'Westminster',
        'Westport',
        'White',
        'Whitemarsh',
        'Wild Horse',
        'Wild Rose',
        'William',
        'Williams',
        'Willow',
        'Wilson',
        'Winchester',
        'Windfall',
        'Winding Way',
        'Windsor',
        'Wintergreen',
        'Wood',
        'Woodland',
        'Woodside',
        'Woodsman',
        'Wrangler',
        'York',
        'Young',
        'Yukon'
    )

    street_prefixes = (
        'West',
        'South',
        'East',
        'North',
        'W.',
        'S.',
        'E.',
        'N.',
        'NE.',
        'NW.',
        'SE.',
        'SW.',
        'Old'
    )

    street_suffixes = (
        'St.',
        'Street',
        'Ave.',
        'Drive',
        'Dr.',
        'Lane',
        'Rd.',
        'Court',
        'Road',
        'Avenue',
        'Circle'
    )

    def street_suffix(self):
        p = math.floor(100 * random.random())
        i = 0
        if p < 25:
            return self.street_suffixes[i]
        elif p < 41:
            i += 1
            return self.street_suffixes[i]
        elif p < 56:
            i += 1
            return self.street_suffixes[i]
        elif p < 65:
            i += 1
            return self.street_suffixes[i]
        elif p < 74:
            i += 1
            return self.street_suffixes[i]
        elif p < 82:
            i += 1
            return self.street_suffixes[i]
        elif p < 87:
            i += 1
            return self.street_suffixes[i]
        elif p < 92:
            i += 1
            return self.street_suffixes[i]
        elif p < 96:
            i += 1
            return self.street_suffixes[i]
        elif p < 99:
            i +=1
            return self.street_suffixes[i]
        else:
            return self.street_suffixes[-1]

    def zip_code(self):
        return self.random_element(list(self.zip_codes.keys()))

    def street_name(self):
        return self.random_element(self.street_names)

    def city(self, zip_code: int = None):
        zip_code = zip_code or self.random_element(list(self.zip_codes.keys()))
        city, _ = self.zip_codes.get(zip_code).split(', ')
        return city

    def state(self, zip_code: int = None):
        zip_code = zip_code or self.random_element(list(self.zip_codes.keys()))
        _, state = self.zip_codes.get(zip_code).split(', ')
        return state

    def street_address(self):
        zip_code = self.zip_code()
        city, state = self.zip_codes.get(zip_code).split(', ')
        street_name = self.street_name()
        if 500 * random.random() < 100:
            street_prefix = self.random_element(self.street_prefixes)
            street_name = f"{street_prefix} {street_name}"
        street_suffix = self.street_suffix()
        street_number = self.random_int(1, 9999)
        if 1000 * random.random() < 100:
            street_letter = self.random_element(('A', 'B', 'C'))
            street_number = f"{street_number}{street_letter}"
        return f"{street_number} {street_name} {street_suffix},\n{city}, {state} {zip_code}"""

    def postal_address(self):
        return self.street_address()
