# These are all the settings that are specific to a jurisdiction

###############################
# These settings are required #
###############################

import os

OCD_CITY_COUNCIL_ID = os.environ.get('COUNCILMATIC_OCD_COUNCIL_ID', 'ocd-organization/ef168607-9135-4177-ad8e-c1f7a4806c3a')
CITY_COUNCIL_NAME = os.environ.get('COUNCILMATIC_COUNCIL_NAME', 'Chicago City Council')
OCD_JURISDICTION_ID = os.environ.get('COUNCILMATIC_OCD_JURISDICTION_ID', 'ocd-jurisdiction/country:us/state:il/place:chicago/government')
# the last one in this list should be the current legislative session
LEGISLATIVE_SESSIONS = os.environ.get('COUNCILMATIC_LEGISLATIVE_SESSIONS', '2007,2011,2015').split(',')
CITY_NAME = os.environ.get('COUNCILMATIC_CITY_NAME', 'Chicago')
CITY_NAME_SHORT = os.environ.get('COUNCILMATIC_CITY_NAME_SHORT', CITY_NAME)

# VOCAB SETTINGS FOR FRONT-END DISPLAY
CITY_VOCAB = {
    'MUNICIPAL_DISTRICT': 'District',       # e.g. 'District'
    'SOURCE': 'San Francisco Clerk of The Board',
    'COUNCIL_MEMBER': 'Supervisor',       # e.g. 'Council Member'
    'COUNCIL_MEMBERS': 'Supervisors',      # e.g. 'Council Members'
    'EVENTS': 'Meetings',               # label for the events listing, e.g. 'Events'
}

APP_NAME = 'chicago'


#########################
# The rest are optional #
#########################

# this is for populating meta tags
SITE_META = {
    'site_name' : 'San Francisco Councilmatic',
    'site_desc' : 'Board of Supervisors, demystified. Keep tabs on San Francisco legislation, supervisors, & meetings.',
    'site_author' : 'DataMade',
    'site_url' : 'https://sfo.councilmatic.org',
    'twitter_site': '@DataMadeCo',
    'twitter_creator': '@DataMadeCo',
}

LEGISTAR_URL = 'https://sfgov.legistar.com/Legislation.aspx'


# this is for the boundaries of municipal districts, to add 
# shapes to posts & ultimately display a map with the council
# member listing. the boundary set should be the relevant
# slug from the ocd api's boundary service
# available boundary sets here: http://ocd.datamade.us/boundary-sets/
BOUNDARY_SET = None

# this is for configuring a map of council districts using data from the posts
# set MAP_CONFIG = None to hide map
MAP_CONFIG = None


FOOTER_CREDITS = [
    {
        'name':     'DataMade',
        'url':      'http://datamade.us/',
        'image':    'datamade-logo.png',
    },
    {
        'name':     'Sunlight Foundation',
        'url':      'http://sunlightfoundation.org/',
        'image':    'sunlight-logo.png',
    },
]

# this is the default text in search bars
SEARCH_PLACEHOLDER_TEXT = "police, zoning, O2015-7825, etc."



# these should live in APP_NAME/static/
IMAGES = {
    'favicon': 'images/favicon.ico',
    'logo': 'images/logo.png',
}




# THE FOLLOWING ARE VOCAB SETTINGS RELEVANT TO DATA MODELS, LOGIC
# (this is diff from VOCAB above, which is all for the front end)

# this is the name of the meetings where the entire city council meets
# as stored in legistar
CITY_COUNCIL_MEETING_NAME = 'Board of Supervisors'

# this is the name of the role of committee chairs, e.g. 'CHAIRPERSON' or 'Chair'
# as stored in legistar
# if this is set, committees will display chairs
COMMITTEE_CHAIR_TITLE = 'Chairman'

# this is the anme of the role of committee members,
# as stored in legistar
COMMITTEE_MEMBER_TITLE = 'Member'




# this is for convenience, & used to populate a table
# describing legislation types on the about page template
LEGISLATION_TYPE_DESCRIPTIONS = [
    {
        'name': 'Ordinance',
        'search_term': 'Ordinance',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': 'Ordinances are proposed changes to Chicago’s local laws. Some of these are changes to Chicago’s Municipal Code and others, called uncompiled statutes, are recorded in the Council’s Journal of Proceedings.',

    },
    {
        'name': 'Claim',
        'search_term': 'Claim',
        'fa_icon': 'dollar',
        'html_desc': True,
        'desc': "If you are harmed by the City of Chicago, you can make a claim against the City for your costs. Minor harms, like personal injury or automotive damage, are settled through City Council as Claims. If you sue the City for harm and come to a settlement, the settlement must also be approved by the Council.",

    },
    {
        'name': 'Resolution',
        'search_term': 'Resolution',
        'fa_icon': 'commenting-o',
        'html_desc': True,
        'desc': "Resolutions are typically symbolic, non-binding documents used for calling someone or some organization to take an action, statements announcing the City Council's intentions or honoring an individual.",

    },
    {
        'name': 'Order',
        'search_term': 'Order',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': "Orders direct a City Agency to do or not do something. They are typically used for ward matters like issuing business permits, designating parking zones and installing new signs and traffic signals.",

    },
    {
        'name': 'Appointment',
        'search_term': 'Appointment',
        'fa_icon': 'user',
        'html_desc': True,
        'desc': "Used for appointing individuals to positions within various official City of Chicago and intergovernmental boards.",

    },
    {
        'name': 'Report',
        'search_term': 'Report',
        'fa_icon': 'file-text-o',
        'html_desc': True,
        'desc': "Submissions of official reports by departments, boards and sister agencies. ",

    },
    {
        'name': 'Communication',
        'search_term': 'Communication',
        'fa_icon': 'bullhorn',
        'html_desc': True,
        'desc': "Similar to reports and used for notifying City Council of intentions or actions.",

    },
    {
        'name': 'Oath Of Office',
        'search_term': 'Oath Of Office',
        'fa_icon': 'user',
        'html_desc': True,
        'desc': "Official swearing in of individuals to leadership positions at the City of Chicago, including Aldermen and board members.",

    },
]

# these keys should match committee slugs
COMMITTEE_DESCRIPTIONS = {
        'san-francisco-board-of-supervisors': 'Blah',
        'budget-and-finance-committee': 'Blah blah blah',
        }

ABOUT_BLURBS = {
    "COMMITTEES" : "<p>Most meaningful legislative activity happens in committee meetings, where committee members debate proposed legislation. These meetings are open to the public.</p>\
                    <p>Each committee is has a Chair, who controls the committee meeting agenda (and thus, the legislation to be considered).</p>\
                    <p>Committee jurisdiction, memberships, and appointments all require City Council approval.</p>",
    "EVENTS":       "<p>There are two types of meetings: committee meetings and full city council meetings.</p>\
                    <p>Most of the time, meaningful legislative debate happens in committee meetings, which occur several times a month.</p>\
                    <p>Meetings of the entire City Council generally occur once a month at City Hall.</p>\
                    <p>All City Council meetings are open to public participation.</p>",
    "COUNCIL_MEMBERS": "" 
    
}

MANUAL_HEADSHOTS = {
    'arena-john':           {'source': '45th Ward Office', 'image': 'manual-headshots/arena-john.jpg' },
    'beale-anthony':        {'source': '@Alderman_Beale, Twitter', 'image': 'manual-headshots/beale-anthony.jpg' },
    'burns-william-d':      {'source': 'Masp360', 'image': 'manual-headshots/burns-william-d.jpg' },
    'cappleman-james':      {'source': 'james46.org', 'image': 'manual-headshots/cappleman-james.jpg' },
    'cochran-willie':       {'source': 'williebcochran.com', 'image': 'manual-headshots/cochran-willie.jpg' },
    'harris-michelle-a':    {'source': 'www.aldermanmichelleharris.net', 'image': 'manual-headshots/harris-michelle-a.jpg' },
    'mell-deborah':         {'source': 'www.33rdward.org', 'image': 'manual-headshots/mell-deborah.jpg' },
    'mitchell-gregory-i':   {'source': 'mitchellforalderman.com', 'image': 'manual-headshots/mitchell-gregory-i.jpg' },
    'moore-joseph':         {'source': 'participatorybudgeting49.wordpress.com', 'image': 'manual-headshots/moore-joseph.jpg' },
    'munoz-ricardo':        {'source': 'www.munoz22.com', 'image': 'manual-headshots/munoz-ricardo.jpg' },
    'napolitano-anthony-v': {'source': 'www.norwoodpark.org', 'image': 'manual-headshots/napolitano-anthony-v.jpg' },
    'oshea-matthew-j':      {'source': 'takebackchicago.org', 'image': 'manual-headshots/oshea-matthew-j.jpg' },
    'osterman-harry':       {'source': '48thward.org', 'image': 'manual-headshots/osterman-harry.jpg' },
    'ramirez-rosa-carlos':  {'source': 'www.aldermancarlosrosa.org', 'image': 'manual-headshots/ramirez-rosa-carlos.jpg' },
    'reboyras-ariel':       {'source': 'www.reboyras.com', 'image': 'manual-headshots/reboyras-ariel.jpg' },
    'sadlowski-garza-susan':{'source': 'calumetareaindustrial.com', 'image': 'manual-headshots/sadlowski-garza-susan.jpg' },
    'sawyer-roderick-t':    {'source': '@rodericktsawyer, Twitter', 'image': 'manual-headshots/sawyer-roderick-t.jpg' },
    'silverstein-debra-l':  {'source': 'ppiachicago.org', 'image': 'manual-headshots/silverstein-debra-l.jpg' },
    'solis-daniel':         {'source': 'ward25.com', 'image': 'manual-headshots/solis-daniel.jpg' },
    'taliaferro-chris':     {'source': 'Facebook', 'image': 'manual-headshots/taliaferro-chris.jpg' },
    'villegas-gilbert':     {'source': '@gilbert36ward, Twitter', 'image': 'manual-headshots/villegas-gilbert.jpg' },
    # 'moreno-proco-joe':     {'source': '', 'image': 'manual-headshots/moreno-proco-joe.jpg' },
    # 'waguespack-scott':     {'source': '', 'image': 'manual-headshots/waguespack-scott.jpg' },
    # 'zalewski-michael-r':   {'source': '', 'image': 'manual-headshots/zalewski-michael-r.jpg' },
    # 'austin-carrie-m':      {'source': '', 'image': 'manual-headshots/austin-carrie-m.jpg' },
    'thompson-patrick-d':   {'source': 'www.ward11.org', 'image': 'manual-headshots/thompson-patrick-d.jpg' },
    # 'tunney-thomas':        {'source': '', 'image': 'manual-headshots/tunney-thomas.jpg' },
    # 'brookins-jr-howard':   {'source': '', 'image': 'manual-headshots/brookins-jr-howard.jpg' },
    # 'burke-edward-m':       {'source': '', 'image': 'manual-headshots/burke-edward-m.jpg' },
    # 'burnett-jr-walter':    {'source': '', 'image': 'manual-headshots/burnett-jr-walter.jpg' },
    # 'cardenas-george-a':    {'source': '', 'image': 'manual-headshots/cardenas-george-a.jpg' },
    'curtis-derrick-g':     {'source': 'Chicago City Clerk', 'image': 'manual-headshots/curtis-derrick-g.jpg' },
    # 'dowell-pat':           {'source': '', 'image': 'manual-headshots/dowell-pat.jpg' },
    'ervin-jason-c':        {'source': '@aldermanervin, Twitter', 'image': 'manual-headshots/ervin-jason-c.jpg' },
    # 'foulkes-toni':         {'source': '', 'image': 'manual-headshots/foulkes-toni.jpg' },
    # 'hairston-leslie-a':    {'source': '', 'image': 'manual-headshots/hairston-leslie-a.jpg' },
    'hopkins-brian':        {'source': '@aldermanhopkins, Twitter', 'image': 'manual-headshots/hopkins-brian.jpg' },
    # 'laurino-margaret':     {'source': '', 'image': 'manual-headshots/laurino-margaret.jpg' },
    'lopez-raymond-a':      {'source': '@rlopez15thward, Twitter', 'image': 'manual-headshots/lopez-raymond-a.jpg' },
    # 'maldonado-roberto':    {'source': '', 'image': 'manual-headshots/maldonado-roberto.jpg' },
    # 'mitts-emma':           {'source': '', 'image': 'manual-headshots/mitts-emma.jpg' },
    'moore-david-h':        {'source': 'Chicago City Clerk', 'image': 'manual-headshots/moore-david-h.jpg' },
    # 'oconnor-patrick':      {'source': '', 'image': 'manual-headshots/oconnor-patrick.jpg' },
    'pawar-ameya':          {'source': 'chicago47.org', 'image': 'manual-headshots/pawar-ameya.jpg' },
    'quinn-marty':          {'source': 'Chicago City Clerk', 'image': 'manual-headshots/quinn-marty.jpg' },
    # 'reilly-brendan':       {'source': '', 'image': 'manual-headshots/reilly-brendan.jpg' },
    'santiago-milagros-s':  {'source': 'Chicago City Clerk', 'image': 'manual-headshots/santiago-milagros-s.jpg' },
    'scott-jr-michael':     {'source': 'citizensformichaelscottjr.com/', 'image': 'manual-headshots/scott-jr-michael.jpg' },
    'smith-michele':        {'source': '@aldermansmith43, Twitter', 'image': 'manual-headshots/smith-michele.jpg' },
    'sposato-nicholas':     {'source': 'aldermansposato.com', 'image': 'manual-headshots/sposato-nicholas.png' },
    'emanuel-rahm':         {'source': 'cityofchicago.org', 'image': 'manual-headshots/emanuel-rahm.jpg' },
    'mendoza-susana-a':     {'source': 'chicityclerk.com', 'image': 'manual-headshots/mendoza-susana-a.jpg' },
}


# notable positions that aren't district representatives, e.g. mayor & city clerk
# keys should match person slugs
EXTRA_TITLES = {
    'mendoza-susana-a': 'City Clerk',
    'emanuel-rahm': 'Mayor',
}


TOPIC_HIERARCHY = [
    {
        'name': 'Citywide matters',
        'children': [
            {
                'name': 'Municipal Code',
                'children': [],
            },
            {
                'name': 'City businesses',
                'children': [   {'name': 'Getting and Giving Land'},
                                {'name': 'Intergovernmental Agreement'},
                                {'name': 'Lease Agreement'},
                                {'name': 'Vacation of Public Street'},],
            },
            {
                'name': 'Finances',
                'children': [ {'name': 'Bonds'} ],
            },
            {
                'name': 'Appointment',
                'children': [],
            },
            {
                'name': 'Oath of Office',
                'children': [],
            },
            {
                'name': 'Airports',
                'children': [],
            },
            {
                'name': 'Special Funds',
                'children': [   {'name': 'Open Space Impact Funds'} ],
            },
            {
                'name': 'Inspector General',
                'children': [],
            },
            {
                'name': 'Council Matters',
                'children': [   {'name': 'Call for Action'},
                                {'name': 'Transfer of Committee Funds'},
                                {'name': 'Correction of City Council Journal'},
                                {'name': 'Next Meeting'},],
            },
        ]

    },
    {
        'name': 'Ward matters',
        'children': [
            {
                'name': 'Business Permits and Privileges',
                'children': [   {'name': 'Grant of privilege in public way'},
                                {'name': 'Awnings'},
                                {'name': 'Sign permits'},
                                {'name': 'Physical barrier exemption'},
                                {'name': 'Canopy'}],
            },
            {
                'name': 'Residents',
                'children': [   {'name': 'Handicapped Parking Permit'},
                                {'name': 'Residential permit parking'},
                                {'name': 'Condo Refuse Claim'},
                                {'name': 'Senior citizen sewer refund'},],
            },
            {
                'name': 'Land Use',
                'children': [   {'name': 'Zoning Reclassification'},
                                {'name': 'Liquor and Package Store Restrictions'},],
            },
            {
                'name': 'Parking',
                'children': [   {'name': 'Loading/Standing/Tow Zone'},
                                {'name': 'Parking Restriction'},],
            },
            {
                'name': 'Economic Development',
                'children': [   {'name': 'Special Service Area'},
                                {'name': 'Tax Incentives'},
                                {'name': 'Tax Increment Financing'},],
            },
            {
                'name': 'Traffic',
                'children': [   {'name': 'Traffic signs and signals'},
                                {'name': 'Vehicle Weight Limitation'},],
            },
            {
                'name': 'Churches and Non-Profits',
                'children': [   {'name': 'Tag Day Permits'} ],
            },
            {
                'name': 'Redevelopment Agreement',
                'children': [],
            },
        ],
    },
    {
        'name': 'Individual matters',
        'children': [
            {
                'name': 'Small Claims',
                'children': [   {'name': 'Damage to vehicle claim'},
                                {'name': 'Damage to property claim'},
                                {'name': 'Settlement of Claims'},
                                {'name': 'Excessive water rate claim'},],
            },
            {
                'name': 'Honorifics',
                'children': [   {'name': 'Honorific Resolution'},
                                {'name': 'Honorary street'},],
            },
        ],
    }
]

