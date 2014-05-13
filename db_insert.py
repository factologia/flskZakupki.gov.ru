import feedparser
from app import db, models

d = feedparser.parse('http://zakupki.gov.ru/epz/order/extendedsearch/rss?sortDirection=false&sortBy=UPDATE_DATE&recordsPerPage=_10&pageNo=1&searchString=%D1%81%D0%BE%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5&placeOfSearch=FZ_44%2CFZ_223&searchType=ORDERS&morphology=true&strictEqual=false&orderPriceCurrencyId=-1&okdpWithSubElements=false&districtIds=5277377&regionIds=5277381&orderStages=AF%2CCA&headAgencyWithSubElements=false&smallBusinessSubject=I&rnpData=I&executionRequirement=I&penalSystemAdvantage=I&disabilityOrganizationsAdvantage=I&russianGoodsPreferences=I&orderPriceCurrencyId=-1&okvedWithSubElements=false&jointPurchase=false&byRepresentativeCreated=false&selectedMatchingWordPlace223=NOTICE_AND_DOCS&matchingWordPlace94=NOTIFICATIONS&changeParameters=true&showLotsInfo=false&law44.okpd.withSubElements=false')
for e in d.entries:
	
	z = models.Zakup(title=e.title,author=e.author,link=e.link,published = e.published,summary = e.summary)
	db.session.add(z)
db.session.commit()

