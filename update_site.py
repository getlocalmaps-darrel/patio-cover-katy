"""
update_site.py — patio-cover-katy site-wide nav/footer/city-services update
Run: py update_site.py
"""

import os
import re

FOLDER = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# NEW NAV HTML
# ---------------------------------------------------------------------------
NEW_NAV = """<nav class="nav-links">
          <a href="/">Home</a>
          <div class="nav-dropdown">
            <a href="/#services" class="nav-dropdown-toggle">Services &#9662;</a>
            <div class="nav-dropdown-menu">
              <a href="/patio-covers.html">Patio Covers</a>
              <a href="/pergolas.html">Pergolas</a>
              <a href="/outdoor-kitchens.html">Outdoor Kitchens</a>
            </div>
          </div>
          <div class="nav-dropdown">
            <a href="/#service-area" class="nav-dropdown-toggle">Service Areas &#9662;</a>
            <div class="nav-dropdown-menu nav-dropdown-menu--wide">
              <a href="/katy-patio-covers.html">Katy</a>
              <a href="/cinco-ranch-patio-covers.html">Cinco Ranch</a>
              <a href="/fulshear-patio-covers.html">Fulshear</a>
              <a href="/richmond-patio-covers.html">Richmond</a>
              <a href="/cypress-patio-covers.html">Cypress</a>
              <a href="/sugar-land-patio-covers.html">Sugar Land</a>
              <a href="/brookshire-patio-covers.html">Brookshire</a>
              <a href="/west-houston-patio-covers.html">West Houston</a>
              <a href="/houston-patio-covers.html">Houston</a>
              <a href="/houston-heights-patio-covers.html">Houston Heights</a>
              <a href="/spring-patio-covers.html">Spring</a>
              <a href="/the-woodlands-patio-covers.html">The Woodlands</a>
              <a href="/humble-patio-covers.html">Humble</a>
              <a href="/simonton-patio-covers.html">Simonton</a>
            </div>
          </div>
          <a href="/gallery.html">Gallery</a>
          <a href="/reviews.html">Reviews</a>
          <a href="/blog/">Blog</a>
          <a href="/contact.html">Contact</a>
        </nav>"""

# ---------------------------------------------------------------------------
# NEW FOOTER HTML
# ---------------------------------------------------------------------------
NEW_FOOTER = """<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-brand">
      <img src="/images/logo.svg" alt="Patio Cover Katy" class="footer-logo-img" />
      <p class="footer-tagline">Custom patio covers, pergolas &amp; outdoor kitchens for the greater Houston area.</p>
      <p class="footer-nap"><strong>(281) 954-0079</strong><br>Katy, TX 77494<br><a href="mailto:info@patiocoverkaty.net">info@patiocoverkaty.net</a></p>
    </div>
    <div class="footer-col">
      <h4 class="footer-heading">Our Services</h4>
      <ul>
        <li><a href="/patio-covers.html">Patio Covers</a></li>
        <li><a href="/pergolas.html">Pergolas</a></li>
        <li><a href="/outdoor-kitchens.html">Outdoor Kitchens</a></li>
        <li><a href="/gallery.html">Project Gallery</a></li>
        <li><a href="/texas-patio-cover-engineering-guide.html">Engineering Guide</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4 class="footer-heading">Service Areas</h4>
      <ul>
        <li><a href="/katy-patio-covers.html">Katy Patio Covers</a></li>
        <li><a href="/cinco-ranch-patio-covers.html">Cinco Ranch</a></li>
        <li><a href="/fulshear-patio-covers.html">Fulshear</a></li>
        <li><a href="/richmond-patio-covers.html">Richmond</a></li>
        <li><a href="/cypress-patio-covers.html">Cypress</a></li>
        <li><a href="/sugar-land-patio-covers.html">Sugar Land</a></li>
        <li><a href="/brookshire-patio-covers.html">Brookshire</a></li>
        <li><a href="/west-houston-patio-covers.html">West Houston</a></li>
        <li><a href="/houston-patio-covers.html">Houston</a></li>
        <li><a href="/houston-heights-patio-covers.html">Houston Heights</a></li>
        <li><a href="/spring-patio-covers.html">Spring</a></li>
        <li><a href="/the-woodlands-patio-covers.html">The Woodlands</a></li>
        <li><a href="/humble-patio-covers.html">Humble</a></li>
        <li><a href="/simonton-patio-covers.html">Simonton</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4 class="footer-heading">Quick Links</h4>
      <ul>
        <li><a href="/reviews.html">Customer Reviews</a></li>
        <li><a href="/contact.html">Free Estimate</a></li>
        <li><a href="/blog/">Blog</a></li>
        <li><a href="/gallery.html">Gallery</a></li>
        <li><a href="https://www.instagram.com/patiocoverskaty/" target="_blank" rel="noopener">Instagram</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; <span class="footer-year"></span> Patio Cover Katy. All rights reserved. | WPI-8 Windstorm Certified Contractor | Serving Katy TX &amp; Greater Houston</p>
    <div class="footer-credit">
      <span>Website by</span>
      <a href="https://www.getlocalmaps.com" target="_blank" rel="noopener noreferrer">
        <img src="https://www.getlocalmaps.com/wp-content/uploads/2020/06/logo-1.png" alt="Get Local Maps" class="footer-logo" />
      </a>
    </div>
  </div>
</footer>"""

# ---------------------------------------------------------------------------
# FOOTER YEAR SCRIPT (injected before </body>)
# ---------------------------------------------------------------------------
YEAR_SCRIPT = """  <script>
    document.querySelectorAll('.footer-year').forEach(function(el) {
      el.textContent = new Date().getFullYear();
    });
  </script>"""

# ---------------------------------------------------------------------------
# CITY PAGES — city name map
# ---------------------------------------------------------------------------
CITY_PAGES = {
    "katy-patio-covers.html": "Katy",
    "cinco-ranch-patio-covers.html": "Cinco Ranch",
    "fulshear-patio-covers.html": "Fulshear",
    "richmond-patio-covers.html": "Richmond",
    "cypress-patio-covers.html": "Cypress",
    "sugar-land-patio-covers.html": "Sugar Land",
    "brookshire-patio-covers.html": "Brookshire",
    "west-houston-patio-covers.html": "West Houston",
    "houston-patio-covers.html": "Houston",
    "houston-heights-patio-covers.html": "Houston Heights",
    "spring-patio-covers.html": "Spring",
    "the-woodlands-patio-covers.html": "The Woodlands",
    "humble-patio-covers.html": "Humble",
    "simonton-patio-covers.html": "Simonton",
}


def city_services_section(city):
    """Build the city services grid section for a given city name."""
    return f"""      <!-- SERVICES IN THIS CITY -->
      <section class="city-services-grid" style="padding:3rem 1.5rem;background:#f8fafc;margin:2rem 0;">
        <div style="max-width:1200px;margin:0 auto;">
          <p class="section-kicker" style="text-align:center;">Everything We Build in {city}</p>
          <h2 class="section-title" style="text-align:center;margin-bottom:2rem;">Outdoor Living Services in {city}, TX</h2>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;">
            <a href="/patio-covers.html" style="display:block;background:#fff;border-radius:16px;padding:2rem;box-shadow:0 4px 20px rgba(15,23,42,0.08);text-decoration:none;color:inherit;border:2px solid #2979ff;">
              <div style="font-size:2rem;margin-bottom:0.75rem;">&#127968;</div>
              <h3 style="color:#2979ff;margin-bottom:0.5rem;font-size:1.1rem;">{city} Patio Covers</h3>
              <p style="color:#64748b;font-size:0.9rem;line-height:1.5;">Solid-roof patio covers and roof extensions. WPI-8 windstorm certified, 130 mph rated. Custom framed or Alumawood insulated aluminum.</p>
              <span style="color:#2979ff;font-size:0.875rem;font-weight:600;">Learn More &#8594;</span>
            </a>
            <a href="/pergolas.html" style="display:block;background:#fff;border-radius:16px;padding:2rem;box-shadow:0 4px 20px rgba(15,23,42,0.08);text-decoration:none;color:inherit;">
              <div style="font-size:2rem;margin-bottom:0.75rem;">&#127807;</div>
              <h3 style="color:#1e293b;margin-bottom:0.5rem;font-size:1.1rem;">{city} Pergolas</h3>
              <p style="color:#64748b;font-size:0.9rem;line-height:1.5;">Western Red Cedar pergolas, attached or freestanding. Custom-cut to your patio - never catalog kits. HOA-approved designs.</p>
              <span style="color:#2979ff;font-size:0.875rem;font-weight:600;">Learn More &#8594;</span>
            </a>
            <a href="/outdoor-kitchens.html" style="display:block;background:#fff;border-radius:16px;padding:2rem;box-shadow:0 4px 20px rgba(15,23,42,0.08);text-decoration:none;color:inherit;">
              <div style="font-size:2rem;margin-bottom:0.75rem;">&#128293;</div>
              <h3 style="color:#1e293b;margin-bottom:0.5rem;font-size:1.1rem;">{city} Outdoor Kitchens</h3>
              <p style="color:#64748b;font-size:0.9rem;line-height:1.5;">Custom BBQ islands and full outdoor kitchens. Built-in grills, granite counters, storage, bar seating - complete backyard cooking setups.</p>
              <span style="color:#2979ff;font-size:0.875rem;font-weight:600;">Learn More &#8594;</span>
            </a>
          </div>
        </div>
      </section>
      <!-- FAQ -->"""


def process_file(filepath, filename):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    original = content
    changes = []

    # ------------------------------------------------------------------
    # 1. Replace nav
    # ------------------------------------------------------------------
    nav_pattern = re.compile(r'<nav class="nav-links">.*?</nav>', re.DOTALL)
    new_content, count = nav_pattern.subn(NEW_NAV, content)
    if count:
        content = new_content
        changes.append(f"nav replaced ({count})")
    else:
        changes.append("nav NOT FOUND")

    # ------------------------------------------------------------------
    # 2. Replace footer
    # ------------------------------------------------------------------
    footer_pattern = re.compile(r'<footer[^>]*>.*?</footer>', re.DOTALL)
    new_content, count = footer_pattern.subn(NEW_FOOTER, content)
    if count:
        content = new_content
        changes.append(f"footer replaced ({count})")
    else:
        changes.append("footer NOT FOUND")

    # ------------------------------------------------------------------
    # 3. Inject year script before </body> (only if not already present)
    # ------------------------------------------------------------------
    if "footer-year" in content and YEAR_SCRIPT not in content:
        content = content.replace("</body>", YEAR_SCRIPT + "\n</body>", 1)
        changes.append("year script injected")

    # ------------------------------------------------------------------
    # 4. City services grid (city pages only, before <!-- FAQ -->)
    # ------------------------------------------------------------------
    if filename in CITY_PAGES:
        city = CITY_PAGES[filename]
        faq_marker = "<!-- FAQ -->"
        if faq_marker in content:
            # Only inject if the services grid isn't already there
            if "city-services-grid" not in content:
                content = content.replace(
                    faq_marker,
                    city_services_section(city),
                    1,
                )
                changes.append(f"city services grid injected for {city}")
            else:
                changes.append("city services grid already present — skipped")
        else:
            changes.append("<!-- FAQ --> marker NOT FOUND")

    # Write back only if changed
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True, changes
    else:
        return False, changes


def main():
    html_files = sorted(
        f for f in os.listdir(FOLDER) if f.endswith(".html")
    )
    print(f"Found {len(html_files)} HTML files\n")

    updated = 0
    skipped = 0
    for filename in html_files:
        filepath = os.path.join(FOLDER, filename)
        changed, changes = process_file(filepath, filename)
        status = "UPDATED" if changed else "SKIPPED"
        if changed:
            updated += 1
        else:
            skipped += 1
        print(f"[{status}] {filename}")
        for c in changes:
            print(f"         {c}")

    print(f"\nDone. {updated} files updated, {skipped} skipped.")


if __name__ == "__main__":
    main()
