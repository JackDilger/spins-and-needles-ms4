# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Spins & Needles is a Django e-commerce site selling vinyl records with an integrated events/blog system. The site uses Stripe for payments, AWS S3 for media storage, and is deployed on Heroku with PostgreSQL.

**Live Site:** https://spins-and-needles.herokuapp.com/

## Current Focus: 2025 Visual Refresh

**Goal:** Small, focused visual improvements to modernize the site's appearance for 2025 while keeping Bootstrap 4 and the existing architecture intact.

**Approach:**
- NO performance optimizations or major refactors
- NO Bootstrap 5 migration or framework changes
- Focus on visual polish: better spacing, modern colors, subtle animations, improved typography
- Make incremental changes one page/component at a time
- Keep all existing functionality working

**Priority:** Make the site look more appealing and contemporary with minimal risk of breaking existing features.

### Design Template: About Page Refresh (COMPLETED ✓)

The About page refresh serves as the **design template** for modernizing other pages. Use these principles and patterns when updating remaining pages.

#### Key Design Improvements Applied

**1. Hero Section with Impact**
- Large, full-width hero banner (500px height, 400px on mobile)
- Background image with intentional 2px blur to mask low resolution and create modern aesthetic
- Dark overlay (rgba(0, 0, 0, 0.5)) for text contrast
- Prominent tagline using Squada One font (4rem desktop, 2.2rem mobile)
- Strong text shadows for readability over images
- Animated scroll indicator (bouncing orange chevron) to encourage interaction

**2. Stats/Feature Section**
- Black background (#000) with orange accent color (#ff914d)
- Three-column stat boxes with consistent structure:
  - Large orange numbers (Squada One font, 3rem)
  - Descriptive labels below in cream color (#f8f0e3)
  - Balanced visual hierarchy (Established / Years / Collection size)

**3. Content Sections with Visual Hierarchy**
- Timeline design for story/history:
  - Vertical orange line with circular markers
  - Year labels in darker orange (#c44d0e) for better contrast (WCAG AA)
  - Progressive disclosure of information
- Feature cards grid:
  - Clean white cards with subtle shadows
  - Orange icons (3rem) at top
  - Hover effects: translateY(-5px) with enhanced shadow
  - Responsive grid (auto-fit minmax(250px, 1fr))
  - Uses h3 headings (proper semantic hierarchy)

**4. Mission/Call-to-Action Sections**
- Bold black boxes with orange accent headings
- Orange CTA buttons using darker shade (#c44d0e) for accessibility
- Black secondary buttons for visual balance
- Hover animations (translateY, shadow enhancement)

**5. Accessibility Considerations (100% Lighthouse Score)**
- Color contrast ratios meet WCAG AA standards:
  - Timeline years: #c44d0e (darker orange) instead of #ff914d
  - CTA buttons: #c44d0e with bold text (font-weight: 700)
- Proper heading hierarchy (h1 → h2 → h3, no skips)
- Semantic HTML structure
- Text shadows for readability over images
- Keyboard navigation support

**6. Brand Consistency**
- Primary colors: Black (#000), Orange (#ff914d for icons, #c44d0e for text/buttons), Cream (#f8f0e3)
- Typography: Squada One for headings, Roboto for body text
- Letter spacing for display text (1-2px)
- Consistent spacing (3rem sections, 2rem between elements)

**7. Modern Visual Patterns**
- Subtle animations (2s ease for hover effects)
- Box shadows for depth (0 4px 6px for cards, 0 8px 15px on hover)
- Border radius (10px) for softness
- CSS pseudo-elements (::before, ::after) for layered backgrounds
- Transform scale(1.1) to prevent blur edge artifacts

#### Implementation Notes
- All styling contained in `{% block extra_css %}` for page-specific customization
- No external CSS files needed (keeps it simple)
- Mobile-first responsive design with @media queries at 768px breakpoint
- Font Awesome icons for visual interest
- Background images optimized with blur to hide low resolution

#### Files Modified
- [home/templates/home/about.html](home/templates/home/about.html)

#### Pages Still Needing Refresh
Apply the same design principles to:
1. **Homepage** - Add hero section, update layout with feature cards
2. **Events/Blog** - Modernize post cards, add visual hierarchy
3. **Products** - Update product cards with better shadows/spacing
4. **Checkout** - Improve form styling, add visual feedback
5. **Auth pages** - Modernize login/signup forms with better spacing

When updating these pages:
- Start with hero sections (if applicable)
- Use the same color palette and typography
- Apply consistent spacing and shadows
- Ensure accessibility (contrast, hierarchy)
- Add subtle animations for interactivity
- Test with Lighthouse for 100% accessibility score

## Development Setup

### Environment Setup
```bash
# Navigate to the main project directory
cd spins-and-needles-ms4

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

### Required Environment Variables
Create `env.py` in the project root (`spins-and-needles-ms4/`) with:
```python
import os

os.environ['SECRET_KEY'] = 'your-secret-key'
os.environ['DEVELOPMENT'] = 'True'
os.environ['STRIPE_PUBLIC_KEY'] = 'your-stripe-public-key'
os.environ['STRIPE_SECRET_KEY'] = 'your-stripe-secret-key'
os.environ['STRIPE_WH_SECRET'] = 'your-stripe-webhook-secret'
```

For production (Heroku), also set:
- `DATABASE_URL` - PostgreSQL connection string
- `USE_AWS` - Enable S3 storage
- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
- `EMAIL_HOST_USER` and `EMAIL_HOST_PASS` (Gmail SMTP)

### Running the Development Server
```bash
# From spins-and-needles-ms4/
python3 manage.py runserver

# Or specify custom port
python3 manage.py runserver 8001
```

### Database Management
```bash
# Apply migrations
python3 manage.py migrate

# Create superuser for admin access
python3 manage.py createsuperuser

# For production database updates (do NOT use for local dev):
# Make sure DATABASE_URL is set, then run migrations
```

## Testing

### Running Tests
```bash
# Run all tests
python3 manage.py test

# Run tests for a specific app
python3 manage.py test products
python3 manage.py test bag
python3 manage.py test home
```

### Test Files
- [bag/test_views.py](bag/test_views.py)
- [products/test_views.py](products/test_views.py)
- [home/test_views.py](home/test_views.py)
- Each app has a `tests.py` file

### Code Quality
```bash
# Python linting is handled by pycodestyle (pep8)
# Check for PEP8 violations in VSCode's PROBLEMS tab
# Or manually run checks in GitPod with pycodestyle extension
```

## Architecture

### Django Apps Structure

**Core E-commerce Apps:**
- **products** - Product catalog with Genre and Product models. Products have SKU, name, artist, release_year, price, record_label, and images.
- **bag** - Shopping cart with session-based storage. Includes custom context processor for cart contents available globally.
- **checkout** - Order processing with Stripe integration. Order model uses UUID for order numbers. Includes webhook handler for Stripe events.
- **profiles** - User profiles linked to django-allauth. Stores default delivery info and order history.

**Content Apps:**
- **blog** - Events system with Post and Comment models. Posts represent music events at the store. Comments require admin approval (active=False by default).
- **home** - Landing page and about page.

### Key Models

**Product (products/models.py:16-31)**
- ForeignKey to Genre
- Fields: sku, name, description, release_year, price, artist, record_label, image, image_url

**Order (checkout/models.py:13-70)**
- UUID-based order_number generated via `_generate_order_number()`
- ForeignKey to UserProfile (nullable)
- Tracks delivery_cost, order_total, grand_total
- `update_total()` method recalculates totals including delivery (10% under £50 threshold)

**Post (blog/models.py:12-30)** - Events/blog posts
- STATUS choices: (0, "Draft"), (1, "Publish")
- Fields: title, slug, author (FK to User), image, content, event_date, event_price, location

**Comment (blog/models.py:33-46)** - Event comments
- ForeignKey to Post
- `active` field (default False) - requires admin approval

### Important Settings

**Database (spins_and_needles/settings.py:134-144)**
- Uses PostgreSQL in production (`DATABASE_URL` env var)
- SQLite for local development (db.sqlite3)

**Static/Media Files (spins_and_needles/settings.py:194-216)**
- AWS S3 for production (`USE_AWS` env var triggers custom_storages.py)
- Local storage for development (static/ and media/ directories)

**Delivery Thresholds (spins_and_needles/settings.py:223-224)**
- `FREE_DELIVERY_THRESHOLD = 50` (£50)
- `STANDARD_DELIVERY_PERCENTAGE = 10` (10%)

**Security (spins_and_needles/settings.py:247-270)**
- Custom SecurityHeadersMiddleware (spins_and_needles/middleware.py:6-47) adds COOP and CSP headers
- HSTS enabled in production (1 year)
- Stripe-specific CSP rules for payment processing

### Authentication

Uses **django-allauth** with custom configuration:
- Email verification mandatory (`ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`)
- Can login with username or email (`ACCOUNT_AUTHENTICATION_METHOD = 'username_email'`)
- Minimum username length: 4 characters
- Email required and must be entered twice on signup

### Template Structure

**Base Template:** [templates/base.html](templates/base.html)
- Contains toast notifications (Bootstrap 5 - recently migrated from BS4)
- Navigation with account dropdown and shopping bag icon
- Includes Stripe JS for checkout pages

**Crispy Forms:** Bootstrap 5 templates (`CRISPY_TEMPLATE_PACK = 'bootstrap5'`)

**Context Processors:**
- `bag.contexts.bag_contents` - Makes shopping bag data available in all templates

## Current Migration: Bootstrap 5 Upgrade

See [BOOTSTRAP5_MIGRATION_PLAN.md](../BOOTSTRAP5_MIGRATION_PLAN.md) for detailed progress.

**Phase 1 Complete:** CDN links updated, crispy-bootstrap5 installed, base template migrated

**In Progress:** Page-by-page migration (About → Homepage → Events → Products → Checkout → Auth)

**Key BS4 → BS5 Changes:**
- `data-toggle` → `data-bs-toggle`
- `data-target` → `data-bs-target`
- `.ml-*/.mr-*` → `.ms-*/.me-*`
- `.form-group` removed (use margin utilities)
- jQuery toast → Bootstrap 5 vanilla JS Toast API

## Known Issues & Considerations

### JavaScript Validation (from testing.md)
Some JavaScript remains inline in HTML files due to functionality breaking when extracted:
- bag/templates - update_remove_script.js
- products/templates - image_field_edit_script.js, image_field_add_script.js

### Security Notes
- Custom middleware adds CSP headers for XSS protection (spins_and_needles/middleware.py)
- Stripe domains whitelisted in CSP for payment processing
- AWS S3 bucket URLs allowed for static/media files
- Admin panel uses default Django admin at `/admin/`

### Email Configuration
- **Development:** Console backend (emails printed to terminal)
- **Production:** Gmail SMTP (requires app-specific password)

## Deployment

**Platform:** Heroku with Heroku Postgres add-on

**Build Process:**
1. Heroku reads `Procfile`: `web: gunicorn spins_and_needles.wsgi:application`
2. Installs from `requirements.txt`
3. Uses Python 3.x (specified in `runtime.txt`)
4. Runs with gunicorn web server

**Static Files:**
- In production: Served from AWS S3 via `custom_storages.py`
- `DISABLE_COLLECTSTATIC` should NOT be set in production

**Stripe Webhooks:**
- Endpoint: `/checkout/wh/` (checkout/webhooks.py)
- Handler: checkout/webhook_handler.py (WebhookHandler class)
- Secret: `STRIPE_WH_SECRET` env var

## Admin Tasks

### Managing Events
Events (blog posts) and comments are managed via Django admin at `/admin/`:
- Events: Create, edit, delete posts (set status to 1 to publish)
- Comments: Approve comments by setting `active=True`

### Managing Products
Superusers can add/edit/delete products via the site:
- Add: Navigate to "Product Management" in account dropdown
- Edit/Delete: Buttons appear on product cards when logged in as admin

## Working Directory Note

The main Django project is in `spins-and-needles-ms4/` subdirectory. When running commands, ensure you're in this directory:
```bash
cd spins-and-needles-ms4
# Then run Django commands
```

## Git Commit Guidelines

**IMPORTANT:** Never add Claude Code attribution to git commits. This includes:
- Do NOT add "Generated with Claude Code" or similar text to commit messages
- Do NOT add "Co-Authored-By: Claude" trailers
- Keep commit messages professional and focused on the actual changes made
- Follow the existing commit message style in the repository
