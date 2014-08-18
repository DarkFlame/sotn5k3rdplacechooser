import random, sys, time, os

# Seed the random number generator with the time in seconds since the epoch
seed = time.time()


# See if we're skipping all the extra text
skip = True
if len(sys.argv) > 1 and sys.argv[1] == '-noskip':
    skip = False
else:
    os.system("cls")



# Use these lines to test the seed yourself if you don't trust me
# seed = 5000 # Remove this line to turn on randomness
# print "USING PRESET SEED %i"%seed
# print "The result will always be the same in this mode."
# print "MODIFY Entries.py TO TURN ON RANDOMNESS"

print "Seed: %s" % seed
random.seed(seed)

# The list of usernames of people who reblogged the post, including duplicates
reblogs_RAW = [
    "askstripes",
    "rawiltshire103",
    "poniesandninjas",
    "eagle-eye-the-dashite",
    "ask-blitz",
    "dachickendog",
    "ask-coco-stripe",
    "sparkymidnight",
    "destinedbrony",
    "ask-king-lasselol1299",
    "stormmodblog",
    "omni-jerk",
    "bottle-top",
    "hasikon",
    "neverlandreferences",
    "pony-facade-mod",
    "level1cleric",
    "robdirt01",
    "ask-cloud-skipper",
    "hywther",
    "alahmnat",
    "libra-windrunner",
    "tlmoonguardian",
    "mystical-mod-mod",
    "ask-mage-wing",
    "twispartupla",
    "cougar0403",
    "kingarthur5",
    "pandomia",
    "vincenttascratch",
    "m3reel",
    "elfartsparkle",
    "asksugardip",
    "otter38",
    "linkofequestria",
    "juststrikerstar",
    "phoenixcrashbolt",
    "pegasusmeteors",
    "masteraura",
    "ask-bones-the-grave-keeper",
    "liirian",
    "the-artist-in-training",
    "drawingpatchmod",
    "nekotigerfire",
    "thisiswaht",
    "arkanik7th",
    "oscardarla",
    "acaciaride",
    "libeika14",
    "victor300universe",
    "ask-yin-shade",
    "ykfinch",
    "moonraven-sparrow-summerpalette",
    "chip-cybercorn",
    "blubbershy",
    "psycojosho",
    "lordburn",
    "midnightmusique",
    "goth-dicax",
    "askkagaminetatiana",
    "shadowthewhitewolf",
    "fluttercheer",
    "superashwinrox",
    "mane6swag",
    "nittany-tiger",
    "drageon101",
    "sweetiebellepictures",
    "slayercookie",
    "abacusa",
    "my-life-is-a-bunch-of-reblogs",
    "thexormak",
    "great-file-piles-of-hell",
    "cecilthebigfattigercat",
    "a-dark-mod",
    "linktoreality",
    "the-bluearrow",
    "rainbowsassistant",
    "airfeu",
    "randomwaffle23",
    "shadowdashthebat",
    "mysticlitningposts",
    "doctorderpystuff",
    "timey-world",
    "ask-ariabliss",
    "ask-humanwoodentoaster",
    "ajxks35",
    "dracarys-blackfyre",
    "annstigly",
    "ask-theworldoftheruins",
    "ask-king-lasselol1299",
    "skyshale1",
    "ask-sketchbook",
    "boss-hoss1",
    "thediscordedcelestia",
    "ask-midnight-glow",
    "cyfrostan",
    "soaringpaws",
    "modtea",
    "alliecraft",
    "harvest-pony",
    "member1221",
    "2mahnas",
    "luna-is-best-pony-ever",
    "gwg01",
    "ask-straight-razor",
    "my-life-is-a-bunch-of-reblogs",
    "blackshadow945",
    "dominatorofgames",
    "dragonmoth",
    "moonpony",
    "chinodoll",
    "27canislupus",
    "timley-narelle",
    "screwdonkarules",
    "poismod",
    "oldgooey",
    "airfeu",
    "tireless-twilight",
    "ask-soaring-spirit",
    "lpsfreak",
    "libra-windrunner",
    "bonmod",
    "ask-king-lasselol1299",
    "tmntrocksm",
    "aarrowom",
    "ams201421",
    "thecooolgirl889",
    "huskymod",
    "infinityrise1",
    "username-required",
    "agsilver47",
    "pitch-black-111",
    "obsessedfanofmanythings",
    "valcun2u",
    "djseras",
    "bookmarkponee",
    "askmagicaltwilight",
    "ask-bmoknows",
    "princess-cadencemlp",
    "bbonet98",
    "captainblackmane",
    "voidguardiannat",
    "kmousemusic",
    "reeddash",
    "my-life-is-a-bunch-of-reblogs",
    "amvnightmare",
    "wishful-downpours",
    "tehscootfrry",
    "wolverine585",
    "tailsnick",
    "nekotamer92",
    "ask-novelty",
    "thehoodieninjax",
    "duke-mod",
    "ponybytes",
    "ask-mage-wing",
    "aarrowom",
    "ask-ganymead",
    "bloodprincess13",
    "winter-mod",
    "dragonoffrost",
    "ad-magnum-ingenium",
    "lordburn",
    "firecharge",
    "arielpie",
    "daddy-donte",
    "shadowdragonprincess",
    "infinite-scratch",
    "cyan-brush",
    "lemminluv",
    "drhoofsing",
    "lordxzero",
    "asktheportalwalkers",
    "crytictroll",
    "crimsonmonsterhunterussr",
    "tavocopy",
    "ask-kuleco-mod",
    "wolfnamedtango",
    "polaris-23",
    "cherryhazelfuckers",
    "phoenixwolf343",
    "phoneyphoenix",
    "corralfur",
    "nextgenconsoleponies",
    "ask-arienne-stuff",
    "asksnowflakestar",
    "cephf",
    "ponesaurus",
    "pandoracutie",
    "ask--lazy--cloud",
    "askmeflutterbat",
    "bassnettohikari2",
    "ask-hoodwink-mlp",
    "dumbscar",
    "aarrowom",
    "baneofeurope",
    "neon-moondust",
    "hottspinner",
    "amotherfuckingviking",
    "scoota-luna",
    "nepetas-guard",
    "lunarphoenix",
    "askblueblitz-and-friends",
    "ask-cloud-skipper",
    "answerdarkhooves"
]

# The list of usernames of people who submitted fanart. 
fanarts_RAW = [
    "askdeathbeat",
    "ask-bulk",
    "asksugardip",
    "mysticlitningposts",
    "thisiswaht",
    "rainbowninjajms",
    "Tatiana Means",
    "arainbowofcolour",
    "sweetiebellepictures",
    "thexormak",
    "crazzymawile5",
    "ask-scootalin",
    "nekotigerfire",
    "Tatiana Means",
    "ask-ariabliss",
    "ajxks35",
    "annstigly",
    "sphinx-the-dragon-pony",
    "jankrys00blr",
    "scootamad",
    "ajuethemod",
    "metalgeartwilight",
    "Joshua",
    "thediscordedcelestia",
    "thecooolgirl889",
    "reeddash",
    "voidguardiannat",
    "catopia26",
    "cyan-brush",
    "corralfur",
    "askchordcatcher",
    "danshawgraphics",
    "superscratchkat",
    "NadnerbD",
    "ask-blitz",
    "tireless-twilight",
    "cbooster",
    "tireless-twilight",
    "Snowflake Star",
    "starlightdrawsstuff",
    "postcrusade-mod",
    "libeika14",
    "asktheartemployees",
    "scoota-luna"
]

if not skip:
    print "Number of raw reblog entries: %i"%len(reblogs_RAW)
    print "Number of raw fanart entries: %i"%len(fanarts_RAW)
    print
    
# Set this to False if you want to include duplicate reblog entries
skip_duplicate_reblogs = True

reblogs_filtered = []
reblogs_duplicates = []
# Filter out the duplicate reblogs
for i in reblogs_RAW:
    if not i in reblogs_filtered:
        reblogs_filtered.append(i)
    else:
        if not skip: print "Duplicate: %s"%i
        if not i in reblogs_duplicates:
            reblogs_duplicates.append(i)
        reblogs_duplicates.append(i)
if not skip_duplicate_reblogs:
    # If we're including duplicates, just stuff all the raw reblogs back into the list
    reblogs_filtered = reblogs_RAW[:]
        

if not skip:        
    print
    print "Number of filtered reblog entries: %i."%(len(reblogs_filtered))
    print
    reblogs_duplicates.sort()
    print "%i Duplicates:"%(len(reblogs_RAW)-len(reblogs_filtered))
    print "(This includes the non-duplicate reblog)"
    print
    for i in reblogs_duplicates:
        print "    " + i

        
if not skip:
    print "People who both submitted fanart and reblogged:"
    print
    
numoflegitdupes = 0

for i in fanarts_RAW:
    if i in reblogs_filtered:
        if not skip: print "    " + i
        numoflegitdupes += 1
        
        
# Combine reblog and fanart submission entries into one list, including appropriate duplicates        
entries = reblogs_filtered[:]
entries.extend(fanarts_RAW)
print "Total entries: %i"%len(entries)
print "%i reblogs and %i fanart submissions with %i people doing both"%(len(reblogs_filtered),len(fanarts_RAW),numoflegitdupes)

    
print
print
print "There are three winners for third place."
print "They are..."
print

# An option for me. Doesn't change the results at all, only the way they're printed
html_output = True

for winner in range(0,3):
    choice = random.choice(entries)
    # If we're outputting it into an HTML link, we need to exclude the names that don't have a tumblr URL
    if html_output and choice not in ["Tatiana Means","Joshua","NadnerbD","Snowflake Star"]:
        choice = "<a href=\"http://%s.tumblr.com\">%s</a>"%(choice, choice)
    print "      %i. "%(winner+1) + choice
    while choice in entries:
        entries.remove(choice)

print
print
print
raw_input("Press ENTER to quit")
