# Es wird die Zeit ausgerechnet bis zum Veröffentlichungstermin von AC Valhalla
import datetime
today = datetime.date.today()
someday = datetime.date(2020,11,17)
diff = someday - today
print (diff.days)
print ("Noch {} Tage bis Assassins Creed Valhalla erscheint".format(diff.days))
