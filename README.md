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

#### NOTES:

##### Entry Fees

- If "View Details" link is present, links to a table at bottom of event page with different Entry fees based off general, public, exhibitor, ages, booth, etc and can be quite extensive.
- If "Check Offical Website" is present, info is blocked behind a login linked to external website.

##### Event Venue Address and Name

- Do not access through anchor tag (Inconsistent), target map ID.
- If Map ID isnt present the event is Virtual, and no venue name or address will be provided.

##### Official Link

- We decided to leave this out, all links are to external websites.

##### Editions

- Additional Editions previous years (if applicable) located in a popup modal when clicking on link text e.g. "+ 6 more editions"

---

- [x] List of all Country URL's
- [x] All Event URL's for EACH Country
- [x] Event Details page

  - [x] Event Name
  - [x] Format Type
  - [x] Start Date
  - [x] End Date
  - [x] Location
  - [x] Event Venue Name
  - [x] Event Venue Address
  - [x] Description
  - [x] Timings
  - [x] Entry Fees
  - [x] Estimated Turnout
  - [x] Catagories
  - [x] Frequency
  - [x] Organizer
  - [x] Editions
  - [ ] Offical Links

---

## TODO :pushpin:

- [x] Login function
- [x] Scroll Function
- [x] Write Country URL to text file
- [x] Write Event URL to text file
- [x] Read from countries.txt file and add date ranges (one year prev, monthy increment) to urls
- [x] Read from countries.txt file and add date ranges (one week, increment) to urls. Changed to one week because Months were too big in some instances, and maxed out at 200 without login.
- [x] Create CSV file of event details/per country \*\* Note, data is there and writing, but I need to clean up the structure a bit
- [x] Read from event_data_range.txt and automate in scraper to visit each url.
- [x] create function, tie together with scroll to grab all events in date range per country
- [x] Clean up data structure for event details being added to csv
- [ ] Seperate data pulled by country.

- [ ] Refactor into classes
- [ ] Pull country and date range from date_range_urls to add to CSV of data collected on events.
- [ ] Adjust reading from text file with date_range_urls

---

## Website Behavior ℹ️

_Information to help with different behaviors observed while scraping the website._

We chose to use Date ranges to avoid a lot of the behaviors that made scraping this site difficult. Date ranges will have to adjust depending on the size and activity of the country. Most countries seem to work well with a one week date range. Larger countries most likely will need a much smaller range. USA I imagine may need a 1 -3 day range max during busiest times.

- Previous events **Only goes back one year** based off Today's date.
- Upcoming Events listed up to 5 years based off Today's date.
- If a Search in a specific date range for events does not have any upcoming events, the website will fill with previous random events. I added a search for the element (text) that if present, that page will be skipped, and move onto the next one, otherwise the data is no good. I originally targetd ID=12, but occasionally a page does not have this present, so it was inconsistent, and skipping pages with legitimate events.
- If not logged in, Country specific event pages only allow 200 max events to be viewed, and only 400 max for date ranges.
  - Scrolling behaviors as well as Max events shown has changed slightly, instead of 40 events views per scroll, there seems to be about 140 or so before login is prompted.
- https://10times.com/events/by-country Events number per country is the Total Events, previous and upcoming per country.
- https://10times.com/{country} Each Country events page, left column, listed countries (These numbers represent Upcoming events)
- Data collecting can differ from one event page to another, as far as what to target to collect data. I've had to adjust targeted elements as I run the scrapper, because a handful of events have a slightly different structure to them.

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

## Issues/Bugs :bug::exclamation:

:bug: Country URL def Not bringing in smaller countries, because source is dropdown that may not include them.

:bulb: Possible Solution

- [x] FIX Grab Countries from table instead when View all clicked for countries

---

:bug: get_event_urls_by_country() Only bringing in max 400 URLS from France/UK

:bulb: Possible Solution

- [x] use date range on events page to move through events.

:white_check_mark: Solved
date_picker.py created function to generate date ranges for urls.

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
