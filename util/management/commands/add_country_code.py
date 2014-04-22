from django.core.management.base import BaseCommand, CommandError

from FaraData.models import Location

class Command(BaseCommand):
	def handle(self, *args, **options):
		countries = get_countries()
		for location in Location.objects.all():
			if countries.has_key(location.country_grouping):
				location.country_code = countries[location.country_grouping]
				location.save() 
			else:
				if countries.has_key(location.location):
					location.country_code = countries[location.location]
					location.save()

				else: 
				 print "miss ", location, location.id  

def get_countries():
	countries = {'Canada': 'CAN', 'Syrian Arab Republic (Syria)': 'SYR', 'Sao Tome and Principe': 'STP', "Cote d'Ivoire": 'CIV', 'Guinea-Bissau': 'GNB', 'Saint Helena': 'SHN', 'Lao PDR': 'LAO', 'Lithuania': 'LTU', 'Cambodia': 'KHM', 'Saint Kitts and Nevis': 'KNA', 'Switzerland': 'CHE', 'Ethiopia': 'ETH', 'Aruba': 'ABW', 'Swaziland': 'SWZ', 'Svalbard and Jan Mayen Islands': 'SJM', 'Argentina': 'ARG', 'Bolivia': 'BOL', 'Cameroon': 'CMR', 'Burkina Faso': 'BFA', 'Turkmenistan': 'TKM', 'Ghana': 'GHA', 'Saudi Arabia': 'SAU', 'Rwanda': 'RWA', 'Togo': 'TGO', 'Japan': 'JPN', 'American Samoa': 'ASM', 'Montserrat': 'MSR', 'United States Minor Outlying Islands': 'UMI', 'Cocos (Keeling) Islands': 'CCK', 'Pitcairn': 'PCN', 'Guatemala': 'GTM', 'United States of America': 'USA', 'Bosnia and Herzegovina': 'BIH', 'Kuwait': 'KWT', 'Russian Federation': 'RUS', 'Jordan': 'JOR', 'Dominica': 'DMA', 'Liberia': 'LBR', 'Maldives': 'MDV', 'Micronesia, Federated States of': 'FSM', 'Jamaica': 'JAM', 'Oman': 'OMN', 'Martinique': 'MTQ', 'Holy See (Vatican City State)': 'VAT', 'Reunion': 'REU', 'Christmas Island': 'CXR', 'French Guiana': 'GUF', 'Niue': 'NIU', 'Monaco': 'MCO', 'Samoa': 'WSM', 'New Zealand': 'NZL', 'Yemen': 'YEM', 'Jersey': 'JEY', 'Andorra': 'AND', 'Albania': 'ALB', 'Congo (Brazzaville)': 'COG', 'Norfolk Island': 'NFK', 'United Arab Emirates': 'ARE', 'Guam': 'GUM', 'India': 'IND', 'Azerbaijan': 'AZE', 'Lesotho': 'LSO', 'Kenya': 'KEN', 'Tajikistan': 'TJK', 'Turkey': 'TUR', 'Afghanistan': 'AFG', 'Bangladesh': 'BGD', 'Mauritania': 'MRT', 'Solomon Islands': 'SLB', 'Turks and Caicos Islands': 'TCA', 'Saint Lucia': 'LCA', 'Saint Vincent and Grenadines': 'VCT', 'San Marino': 'SMR', 'Tonga': 'TON', 'French Polynesia': 'PYF', 'France': 'FRA', 'Bermuda': 'BMU', 'Slovakia': 'SVK', 'Somalia': 'SOM', 'Peru': 'PER', 'Vanuatu': 'VUT', 'Nauru': 'NRU', 'Seychelles': 'SYC', 'Norway': 'NOR', 'Malawi': 'MWI', 'Cook Islands': 'COK', 'Benin': 'BEN', 'Western Sahara': 'ESH', 'Cuba': 'CUB', 'Iran, Islamic Republic of': 'IRN', 'Falkland Islands (Malvinas)': 'FLK', 'Mayotte': 'MYT', 'Taiwan, Republic of China': 'TWN', 'China': 'CHN', 'Armenia': 'ARM', 'Timor-Leste': 'TLS', 'Dominican Republic': 'DOM', 'Ukraine': 'UKR', 'Bahrain': 'BHR', 'Tanzania, United Republic of': 'TZA', 'Finland': 'FIN', 'Libya': 'LBY', 'Cayman Islands': 'CYM', 'Central African Republic': 'CAF', 'New Caledonia': 'NCL', 'Mauritius': 'MUS', 'Liechtenstein': 'LIE', 'Australia': 'AUS', 'British Virgin Islands': 'VGB', 'Mali': 'MLI', 'Sweden': 'SWE', 'Bulgaria': 'BGR', 'Romania': 'ROU', 'Angola': 'AGO', 'French Southern Territories': 'ATF', 'Chad': 'TCD', 'South Africa': 'ZAF', 'Tokelau': 'TKL', 'Cyprus': 'CYP', 'South Georgia and the South Sandwich Islands': 'SGS', 'Brunei Darussalam': 'BRN', 'Qatar': 'QAT', 'Malaysia': 'MYS', 'Austria': 'AUT', 'Mozambique': 'MOZ', 'Uganda': 'UGA', 'Hungary': 'HUN', 'Niger': 'NER', 'Isle of Man': 'IMN', 'Brazil': 'BRA', 'Faroe Islands': 'FRO', 'Guinea': 'GIN', 'Panama': 'PAN', 'Korea, Republic of': 'KOR', 'Congo, Democratic Republic of the': 'COD', 'Costa Rica': 'CRI', 'Luxembourg': 'LUX', 'Cape Verde': 'CPV', 'Bahamas': 'BHS', 'Virgin Islands, US': 'VIR', 'Gibraltar': 'GIB', 'Ireland': 'IRL', 'Pakistan': 'PAK', 'Palau': 'PLW', 'Nigeria': 'NGA', 'Ecuador': 'ECU', 'Czech Republic': 'CZE', 'Macedonia, Republic of': 'MKD', 'Viet Nam': 'VNM', 'Belarus': 'BLR', 'Algeria': 'DZA', 'Slovenia': 'SVN', 'El Salvador': 'SLV', 'Tuvalu': 'TUV', 'Saint Pierre and Miquelon': 'SPM', 'Marshall Islands': 'MHL', 'Chile': 'CHL', 'Puerto Rico': 'PRI', 'Belgium': 'BEL', 'Kiribati': 'KIR', 'Haiti': 'HTI', 'Belize': 'BLZ', 'Sierra Leone': 'SLE', 'Saint-Martin (French part)': 'MAF', '': '', 'Georgia': 'GEO', 'Gambia': 'GMB', 'Philippines': 'PHL', 'Moldova': 'MDA', 'Morocco': 'MAR', 'Croatia': 'HRV', 'Mongolia': 'MNG', 'Guernsey': 'GGY', 'Thailand': 'THA', 'Namibia': 'NAM', 'Grenada': 'GRD', 'Wallis and Futuna Islands': 'WLF', 'Iraq': 'IRQ', 'Portugal': 'PRT', 'Estonia': 'EST', 'Uruguay': 'URY', 'Bouvet Island': 'BVT', 'Lebanon': 'LBN', 'Uzbekistan': 'UZB', 'Tunisia': 'TUN', 'Djibouti': 'DJI', 'Greenland': 'GRL', 'Antigua and Barbuda': 'ATG', 'Spain': 'ESP', 'Colombia': 'COL', 'Burundi': 'BDI', 'Montenegro': 'MNE', 'Fiji': 'FJI', 'Barbados': 'BRB', 'Madagascar': 'MDG', 'Italy': 'ITA', 'Bhutan': 'BTN', 'Sudan': 'SDN', 'Nepal': 'NPL', 'Malta': 'MLT', 'Suriname\xca*': 'SUR', 'Netherlands': 'NLD', 'Northern Mariana Islands': 'MNP', 'Anguilla': 'AIA', 'Netherlands Antilles': 'ANT', 'Saint-Barthelemy': 'BLM', 'Aland Islands': 'ALA', 'Israel': 'ISR', 'Indonesia': 'IDN', 'Macao, Special Administrative Region of China': 'MAC', 'Iceland': 'ISL', 'Zambia': 'ZMB', 'Venezuela\xca(Bolivarian Republic of)': 'VEN', 'Senegal': 'SEN', 'Papua New Guinea': 'PNG', 'Trinidad and Tobago': 'TTO', 'Zimbabwe': 'ZWE', 'Germany': 'DEU', 'Denmark': 'DNK', 'Kazakhstan': 'KAZ', 'Poland': 'POL', 'Eritrea': 'ERI', 'Kyrgyzstan': 'KGZ', 'British Indian Ocean Territory': 'IOT', "Korea, Democratic People's Republic of": 'PRK', 'Mexico': 'MEX', 'Sri Lanka': 'LKA', 'Latvia': 'LVA', 'South Sudan': 'SSD', 'Guyana': 'GUY', 'Guadeloupe': 'GLP', 'Honduras': 'HND', 'Myanmar': 'MMR', 'Equatorial Guinea': 'GNQ', 'Egypt': 'EGY', 'Nicaragua': 'NIC', 'Singapore': 'SGP', 'Serbia': 'SRB', 'Botswana': 'BWA', 'United Kingdom': 'GBR', 'Antarctica': 'ATA', 'Heard Island and Mcdonald Islands': 'HMD', 'Greece': 'GRC', 'Paraguay': 'PRY', 'Gabon': 'GAB', 'Palestine':'PSE', 'Palestinian Territory, Occupied': 'PSE', 'Comoros': 'COM', 'Hong Kong, Special Administrative Region of China': 'HKG'}
	return countries