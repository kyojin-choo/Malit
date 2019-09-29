### profanity.py -*- please dont be offended, just a compilation and weights of profane words -*-
##
##  Author: Daniel Choo
##  Date:   09/28/19


def badwords():

	"""
  Scaling of curse words
 *-----------------------*
  Racial profanity: 1
  Sexist profanity: 0.6
  Gray territory: 0.4
  Normal curse words: 0.1
	"""
	# Here we go..

	profane = { 
		"ass" : 0.1, 
		"asshat" : 0.1,
		"asshole" : 0.1,
		"aryan" : 1,
		"bastard" : 0.1,
		"bimbo" : 0.6, 
		"bitch" : 0.4,
		"bullshit" : 0.1,
		"cockhead" : 0.4,
		"coochie" : 0.3,
		"chink" : 1.0, 
		"chinaman" : 1.0,
		"chode" : 0.4,
		"clusterfuck" : 0.1,
		"cuck" : 0.1,
		"cunt" : 0.6,
		"damn" : 0.1,
		"dick" : 0.1,
		"dipshit" : 0.1, 
		"dumbfuck" : 0.1,
		"fag" : 0.6,
		"faggot" : 0.6,
		"fuck" : 0.1,
		"fucked" : 0.1,
		"fucking" : 0.1,
		"gigolo" : 0.3,
 		"goddamnit" : 0.1,
		"godamnit" : 0.1,
		"gook" : 1.0,
		"gyp" : 1.0,
		"gypped" : 1.0,
		"jackass" : 0.1,
		"jap" : 1.0,
		"jipped" : 1.0,
		"jigga" : 1.0,
		"jiggaboo" : 1.0,
		"jigger" : 1.0,
		"jiggers" : 1.0,
		"kike" : 1.0,
		"kikes" : 1.0,
		"kyke" : 1.0,
		"kykes" : 1.0,
		"kkk" : 0.4,
		"kys" : 0.4,
		"lynch" : 0.4,
		"nazi" : 0.4,
		"negro" : 1.0,
		"negros" : 1.0,
		"nig" : 1.0,
		"nigger" : 1.0,
		"niggers" : 1.0,
		"nigga" : 0.4,
		"niglet" : 1.0,
		"piss" : 0.1,
		"pussy" : 0.4,
		"queer" : 0.4, 
		"shit" : 0.1,
		"slut" : 0.6,
		"whore" : 0.6,
	}

	return profane

badwords()
