# proj3-ajax
Reimplement the RUSA ACP controle time calculator with flask and ajax

Jacob Lowen
jlowen@ix.cs.uoregon.edu/public_html/cis399/htbin/proj3-ajax

## Brevet Controles
Controles are certain locations in a brevet that must be passed through in order
 and within a specific range of time. These open and close times for these controles 
 are fixed based on the brevet's overall length and how far they are from the start
 There are a few key rules to this:

1) The first controle is always at 0km with an open time equivalent to the brevet's
      start time and a closing time 1 hour after that

2) The distance from the start to the last controle is at least equal to the listed
     brevet  length and at most 10% longer than that.  The final controle's 
     open and closing time are preset based on the listed brevet length and do not 
     necessarily match what the algorithm would suggest that they be.
     The possible Brevet Lengths are:
      200km
      300km
      400km
      600km
      1000km

3) Each segment of the course has a fixed minimum and maximum speed recorded in
     kilometers per hour. These ranges are:
     (0-200 km]          |  [15-34 km/hr]
     (200-400 km]     |  [15-32 km/hr]
     (400-600 km]     |  [15-30 km/hr]
     (600-1000 km]  |  [11.428-28 km/hr]
     (1000-1300 km]| [13.333-26 km/hr] 
 (Note that Since 1000 is the max brevet length, the last range is not used in practice)
  the open and closing times for controles assume that you are going between the
  speed limits corresponding to your distance at all times. For example, 
  a controle at 250km will assume that you traveled between 15-34 km/hr for the 
 first 200km and then between 15-32 km/hr for the following 50km.