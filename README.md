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

:pushpin:  
TODO

- [x] Login function
- [x] Scroll Function
- [x] Write Country URL to text file
- [ ] Write event URL to text file
- [ ] Read from Country file and create function to automate
- [ ] Read from Event file and create function to automate
- [x] Create CSV file of event details/per country \*\* Note, data is there and writing, but I need to clean up the structure a bit

# Issues/Bugs

main.py

- get_event_urls_by_country() Only bringing in max 400 URLS from France/UK
  Solution, use date range on events page to move through events.

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

---

<!-- <script> source URI is not allowed in this document:  (Firefox) While browsing, No scrapper -->

Loading failed for the <script> with source “https://www.googletagmanager.com/gtm.js?id=GTM-MMVJS3”. france:1:1
[first-contentful-paint] 00:00:283 utility.js:20:3436
[Service Worker] Sucess: https://10times.com/ utility.js:20:26778
Loading failed for the <script> with source “https://cdn.onesignal.com/sdks/OneSignalSDK.js”. france:1:1
Loading failed for the <script> with source “https://pagead2.googlesyndication.com/tag/js/gpt.js”. france:1:1
Uncaught (in promise)
error { target: script, isTrusted: true, srcElement: script
, eventPhase: 0, bubbles: false, cancelable: false, returnValue: true, defaultPrevented: false, composed: false, timeStamp: 1244, … }

Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8525015516580200. (Reason: CORS request did not succeed).

<script> source URI is not allowed in this document: “https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8525015516580200”. france:1:1
Uncaught (in promise) 
error { target: script, isTrusted: true, srcElement: script
, eventPhase: 0, bubbles: false, cancelable: false, returnValue: true, defaultPrevented: false, composed: false, timeStamp: 1250, … }

This site appears to use a scroll-linked positioning effect. This may not work well with asynchronous panning; see https://firefox-source-docs.mozilla.org/performance/scroll-linked_effects.html for further details and to join the discussion on related tools and features!
