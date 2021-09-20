# tentimes-scraper

#### Robots.txt

```
User-agent: \*
Disallow: /cgi/
Disallow: /rss-feeds/
Disallow: /xml*feeds/
Disallow: /includes/
Disallow: /search/
Disallow: /json/
Disallow: /dashboard/
Disallow: /servicequery
Disallow: /organiserenquiry
Disallow: /notificationlisting
Disallow: /notificationdetail
Disallow: /ajax*?_
Disallow: /_?_ajax
Disallow: /visitorregister_
Disallow: /registeruser
Disallow: /venues/search
Disallow: /\*/stall-book
Disallow: /gold-premium$
```

### Data to collect

- [x] Country event page URL
- [x] Specific event page URL

##### On each event page

- [x] Event Name
- [x] Format Type
- [x] Start Date
- [x] End Date
- [ ] Location
- [x] Event Venue
- [ ] Event Address
- [x] Description
- [x] Timings
- [x] Entry Fees
- [x] Estimated Turnout
- [x] Catagory
- [ ] Offical Links
- [x] Frequency
- [ ] Organizer

:pushpin:  
TODO

- [x] Login function
- [x] Scroll Function
- [x] Write Country URL to text file
- [ ] Write event URL to text file
- [ ] Read from Country file and create function to automate
- [ ] Read from Event file and create function to automate
- [ ] Create CSV file of event details/per country
- [ ] Create CSV file of event details/per country

#Errors

:warning:
GET https://cm.g.doubleclick.net/pixel?google_nid=fluct_eb&google_push=AYg5qPL1ifOWeVQxHWhCzlJmOCU-YMOnhOYb0hE7-vwTydNWT4ZmYCFX85T0YiBDOALAaOXnLoFV0qfYf2eksatyUw-DR6Oxbfc&google_hm=523b3b7b1a86ec89e96f510d742a6daa net::ERR_TOO_MANY_REDIRECTS

:point_right:
https://www.drivereasy.com/knowledge/how-to-fix-err-too-many-redirects-error/

---

:warning:
Cross-Origin Read Blocking (CORB) blocked cross-origin response https://ads.pubmatic.com/AdServer/js/user_sync.html?predirect=https://cs.adingo.jp/sync/%3Ffrom%3Dpubm%26id%3D with MIME type text/html. See https://www.chromestatus.com/feature/5629709824032768 for more details.

:point_right:
https://www.chromium.org/Home/chromium-security/corb-for-developers

---

:warning:
Failed to load resource: the server responded with a status of 502 ()
tag.crsspxl.com/m.gif?oxid=a20b5470-8786-4ac4-8b8d-624ee6d2af95:1
:warning:
Failed to load resource: net::ERR_EMPTY_RESPONSE
