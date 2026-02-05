# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static HTML website for **Patio Cover Katy**, a patio cover and outdoor living contractor serving Katy, Texas and surrounding areas.

**Business Info:**
- Name: Patio Cover Katy
- Phone: (281) 954-0079
- Instagram: @patiocoverskaty
- Service Area: Katy, Cinco Ranch, Fulshear, Richmond, Cypress, Sugar Land, Brookshire, West Houston

## Technology Stack

- Static HTML/CSS/JavaScript
- No build system required - files are served directly
- Contact form submits to `/api/contact.js` (Vercel serverless function)

## Development

To preview the site locally:
```bash
npx serve .
```

## Project Structure

```
/
├── index.html          # Homepage with services, gallery preview, reviews, FAQ
├── contact.html        # Contact form and business info
├── gallery.html        # Project photo gallery
├── reviews.html        # Customer reviews page
├── styles.css          # Main stylesheet
├── favicon.png         # Site favicon
├── api/
│   └── contact.js      # Serverless contact form handler
├── images/
│   ├── logo.svg        # SVG logo
│   ├── hero-main.jpg   # Hero background
│   └── *.jpg           # Project photos
└── CLAUDE.md
```

## SEO Implementation

- LocalBusiness schema with NAP data on all pages
- Geo-targeted keywords: "patio cover Katy", "Katy outdoor kitchen", "Cinco Ranch pergola"
- Open Graph meta tags for social sharing
- Semantic HTML structure with proper heading hierarchy

## Design System

CSS uses custom properties defined in `:root`:
- `--primary-blue: #2979ff` - Primary brand color
- `--primary-blue-dark: #1c55b8` - Darker accent
- `--max-width: 1180px` - Content container width
- `--radius-lg: 18px` / `--radius-xl: 26px` - Border radii
