# SOEMCO Website – Python / Django

A Python rebuild of the SOEMCO (Socorro Empowered People's Cooperative) website: public pages,
member accounts, membership and loan applications, a staff dashboard, and a full admin panel.

## Stack
- Python 3.12+ and Django 5.1/5.2
- SQLite for development, PostgreSQL for production (switch with environment variables)
- Server-rendered Django templates and plain CSS, with no front-end build step
- Gunicorn and Docker for deployment

## Features
| Area | What it does |
|---|---|
| Public site | Home with animated figures, services, 11 branches with province filter, news, FAQs, member stories, forms, loan calculator, contact form |
| Accounts | Register / log in with email (10+ character passwords, Django's password validators) |
| Applications | Members apply for membership or a loan and track status under "My applications" |
| Staff dashboard | `/dashboard/`: counts by status, filter by type, change status inline, recent messages |
| Admin panel | `/admin/`: create and edit branches, products, news, FAQs, stories, forms (with PDF upload), applications and messages |
| Language | EN / Cebuano toggle for navigation and main buttons |
| Security | CSRF on every form, per-IP rate limiting on contact/register/login, secure cookies and HSTS when `DJANGO_DEBUG=0` |
| Ops | `/health/` endpoint, `seed` command, Dockerfile, tests |

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations coop   # first time only
python manage.py migrate
python manage.py seed                  # loads branches, services, news, FAQs, stories
python manage.py import_photos         # copies the logo and photos from soemco.org.ph
python manage.py createsuperuser       # your admin login (use your email as the username)
python manage.py runserver
```
Open http://127.0.0.1:8000. Staff users (`is_staff`) see the Dashboard link; the admin panel is at `/admin/`.

Run the tests with `python manage.py test`.

## Production
Set these environment variables (see `.env.example`):
- `DJANGO_SECRET_KEY`: a long random value
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS=www.yourdomain.ph`
- `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`: to use PostgreSQL

With Docker: `docker compose up -d --build`, then `docker compose exec web python manage.py import_photos` to load the photos.
The rate limiter uses an in-memory cache, so with several servers, switch `CACHES` to Redis.
Serve `media/` (uploaded forms) from your web server or object storage.

## Content
All text comes from soemco.org.ph and lives in `coop/content.py`:
- **Services:** 6 categories, 14 programs and 41 individual products, with eligibility. Loan programs link to a pre-filled online application.
- **News:** 15 full articles with photo galleries, tag filter and paging.
- **Stories:** 6 member testimonials in their original Cebuano/English.
- **FAQs:** searchable, including membership and loan requirements.
- **Forms:** 7 downloadable Word/PDF forms, copied into the site by `import_photos`.
- **Contact:** form with topic, branch and mobile number, plus the office directory and a map. When `NOTIFY_EMAILS` is set,
  staff get an email for every new message and application.
- **Announcements:** advisory box on the home page, switched on or off in `/admin/`.

`python manage.py seed --replace` reloads services, news, stories, FAQs and forms from `content.py`
(branches, accounts, applications and messages are kept).

## Photos
`import_photos` downloads the SOEMCO logo, the six banner photos, and the photos for services, all 11 branches,
news posts and member stories from soemco.org.ph. It resizes each one to at most 1600 px wide.
Run it again with `--force` to re-download. Change or add photos any time in `/admin/`
(Hero slides, Branches, Products, News posts, Testimonials).

## Content rules
Branch, product and news content comes from the public SOEMCO website (checked October 2026).
Confirm branch heads and the main office address ("Cordita St." vs "A. Lasala St.") before launch.
Do not publish unverified loan rates, fees, officers or policies.
