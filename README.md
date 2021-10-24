# Tentimes-scraper :spider:

## Table of Contents

- [Data to Collect](https://github.com/accrue-nuclius-scrappers/tentimes-scraper/tree/france-ms#data-to-collect-dart)
- [Todo](https://github.com/accrue-nuclius-scrappers/tentimes-scraper/tree/france-ms#todo-pushpin)

- [Website Information](https://github.com/accrue-nuclius-scrappers/tentimes-scraper/tree/france-ms#website-information-%E2%84%B9%EF%B8%8F)
  - [Robots.txt](https://github.com/accrue-nuclius-scrappers/tentimes-scraper/tree/france-ms#robotstxt-robot)
- [Issues/bugs-Code](https://github.com/accrue-nuclius-scrappers/tentimes-scraper/tree/france-ms#issuesbugs-bugexclamation)
- [Console Errors](https://github.com/accrue-nuclius-scrappers/tentimes-scraper/tree/france-ms#errors-in-console-warning)

---

## Data to collect :dart:

- [x] List of all Country URL's
- [x] All Event URL's for EACH Country
- [x] Event Details page collect:

  - [x] Event Name
  - [x] Format Type
  - [x] Start Date
  - [x] End Date
  - [x] Location
  - [x] Event Venue
  - [x] Event Address
  - [x] Description
  - [x] Timings
  - [x] Entry Fees
  - [x] Estimated Turnout
  - [x] Catagory
  - [x] Type (Same as Format I believe)
  - [ ] Offical Links
  - [x] Frequency
  - [x] Organizer
  - [x] Editions
  - [ ] Different Located Editions

---

## TODO :pushpin:

- [x] Login function
- [x] Scroll Function
- [x] Write Country URL to text file
- [x] Write Event URL to text file
- [x] Read from countries.txt file and add date ranges (one year prev, monthy increment) to urls
- [x] Read from countries.txt file and add date ranges (one week, increment) to urls. Changed to one week because Months were too big in some instances, and maxed out at 200 without login.
- [x] Create CSV file of event details/per country \*\* Note, data is there and writing, but I need to clean up the structure a bit
- [ ] Read from event_data_range.txt and automate in scraper to visit each url.
- [ ] create function, tie together with scroll to grab all events in date range per country
- [ ] Clean up data structure for event details being added to csv

---

## Issues/Bugs :bug::exclamation:

:bug: Country URL def Not bringing in smaller countries, because source is dropdown that may not include them.

:bulb: Possible Solution

- [ ] FIX Grab Countries from table instead when View all clicked for countries

---

:bug: get_event_urls_by_country() Only bringing in max 400 URLS from France/UK

:bulb: Possible Solution

- [ ] use date range on events page to move through events.

:white_check_mark: Solved
date_picker.py created function to generate date ranges for urls.

---

## Website Information ℹ️

- If not logged in, Country specific event pages only allow 200 max events to be viewed. 10-23-2021 Behavior changed on scroll, now allowing 141 events before login in to continue scroll?

### Robots.txt :robot:

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

---

---

## Errors in Console :warning:

:warning: GET https://cm.g.doubleclick.net/pixel?google_nid=fluct_eb&google_push=AYg5qPL1ifOWeVQxHWhCzlJmOCU-YMOnhOYb0hE7-vwTydNWT4ZmYCFX85T0YiBDOALAaOXnLoFV0qfYf2eksatyUw-DR6Oxbfc&google_hm=523b3b7b1a86ec89e96f510d742a6daa net::ERR_TOO_MANY_REDIRECTS

:point_right: https://www.drivereasy.com/knowledge/how-to-fix-err-too-many-redirects-error/

---

:warning: Cross-Origin Read Blocking (CORB) blocked cross-origin response https://ads.pubmatic.com/AdServer/js/user_sync.html?predirect=https://cs.adingo.jp/sync/%3Ffrom%3Dpubm%26id%3D with MIME type text/html. See https://www.chromestatus.com/feature/5629709824032768 for more details.

:point_right: https://www.chromium.org/Home/chromium-security/corb-for-developers

---

:warning: Failed to load resource: the server responded with a status of 502 ()
tag.crsspxl.com/m.gif?oxid=a20b5470-8786-4ac4-8b8d-624ee6d2af95:1

---
