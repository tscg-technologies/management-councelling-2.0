# Management Consulting Company — Website Documentation

## 1. Overview
This project is a complete, multi-page static website for a generic **MANAGEMENT CONSULTING COMPANY**. Built with a focus on executive authority, structured thinking, operational depth, and high-impact advisory positioning, the website is designed for presentation to CEOs, business owners, managing directors, enterprise executives, and corporate boards.

In accordance with strict brand identity guidelines:
- The website uses only the generic identity **"MANAGEMENT CONSULTING COMPANY"**.
- An abstract geometric logo symbol is used throughout without invented brand names.
- Dummy contact coordinates and sample advisory profiles are clearly identified.
- All metrics, case studies, dashboards, and organizational frameworks are labeled as **"Illustrative Demo Data / Concept"**.
- No real or fabricated client logos, testimonials, corporate history, or regulatory assurances are included.

---

## 2. Technology Stack & Hosting Compatibility
- **Markup:** Semantic HTML5 (W3C validated structure, accessible ARIA attributes).
- **Styling:** Modular CSS3 (Custom design tokens, CSS Grid, Flexbox, responsive layouts, subtle animations).
- **Interactions:** Vanilla JavaScript (ES6+), zero external libraries or frameworks (no React, Vue, jQuery, Bootstrap, or Tailwind).
- **Visuals:** SVG vector diagrams, Canvas-rendered trend visualizations, and responsive image placeholders.
- **Hosting:** 100% static hosting compatible (Hostinger, GitHub Pages, Netlify, Cloudflare Pages, AWS S3 / CloudFront, Apache, Nginx).

---

## 3. Project Structure
```text
management-consulting/
│
├── index.html                           # Executive Homepage
├── about.html                           # Firm Philosophy, Principles, Mission & Vision
├── services.html                        # Services Portfolio Overview (All 17 Practices)
│
├── business-strategy.html               # Practice 01: Business Strategy
├── strategic-planning.html              # Practice 02: Strategic Planning
├── business-transformation.html         # Practice 03: Business Transformation
├── management-advisory.html             # Practice 04: Management Advisory
├── organizational-development.html      # Practice 05: Organizational Development
├── leadership-consulting.html           # Practice 06: Leadership Consulting
├── operations-consulting.html           # Practice 07: Operations Consulting
├── performance-improvement.html         # Practice 08: Performance Improvement
├── process-optimization.html            # Practice 09: Process Optimization
├── change-management.html               # Practice 10: Change Management
├── corporate-governance.html            # Practice 11: Corporate Governance
├── business-expansion.html              # Practice 12: Business Expansion
├── financial-performance.html           # Practice 13: Financial Performance
├── human-resource-management.html       # Practice 14: Human Resource Management
├── project-management.html              # Practice 15: Project Management
├── risk-management.html                 # Practice 16: Risk Management
├── digital-transformation.html          # Practice 17: Digital Transformation
│
├── industries.html                      # 14 Sector Consulting Overviews
├── methodology.html                     # Structured 5-Stage Consulting Methodology
├── case-studies.html                    # Illustrative Demo Case Studies Gallery
├── case-study-details.html              # Reusable Detailed Case Study Template
├── team.html                            # Executive Advisory Leadership & Roles
├── insights.html                        # Thought Leadership & Editorial Articles Hub
├── article-details.html                 # Reusable Article Layout Template
├── resources.html                       # Management Frameworks, Checklists & Templates
├── pricing.html                         # Engagement Models & Comparison Presentation
├── faq.html                             # Categorized Frequently Asked Questions
├── contact.html                         # Corporate Contact Coordinates & Inquiry Form
├── book-consultation.html               # 6-Step Consultation Enquiry Wizard
├── careers.html                         # Advisory Roles & Demo Application Form
├── privacy-policy.html                  # Demonstration Privacy Policy
├── terms-and-conditions.html            # Website Terms & Conditions
│
├── assets/
│   ├── css/
│   │   ├── style.css                    # Design tokens, typography, header, footer, cards, dashboards
│   │   ├── responsive.css               # Breakpoint styling (360px up to 1920px)
│   │   └── animations.css               # Subtle transitions & reduced-motion support
│   │
│   ├── js/
│   │   ├── main.js                      # Sticky nav, mobile drawer, active link tracking, back-to-top
│   │   ├── interactions.js              # FAQ accordion, case study filtering, insights live search
│   │   ├── forms.js                     # 6-Step consultation wizard, contact form validation
│   │   └── charts.js                    # Canvas performance trend charts, risk matrix inspector
│   │
│   ├── images/                          # Destination folder for Google Flow generated images
│   └── icons/                           # Reusable SVG vector assets
│
├── IMAGE-GENERATION-GUIDE.md            # Master Image Catalog & Google Flow Prompts
├── sitemap.xml                          # Complete XML Sitemap (All 35 Pages)
├── robots.txt                           # Search Engine Crawler Instructions
└── README.md                            # Comprehensive Website Documentation
```

---

## 4. How to Open and Test Locally

### Option A: Direct Browser Opening
Double-click `index.html` or right-click and select **Open with > Chrome / Firefox / Edge / Safari**.

### Option B: Local Web Server (Recommended)
Using Python's built-in HTTP server:
```bash
# In the project directory:
python -m http.server 8000
```
Then navigate to: `http://localhost:8000`

---

## 5. How to Edit Website Content

### Updating Firm Information & Navigation Links
- Global Header & Footer: Standardized HTML structure located in every `.html` page.
- Modifying Text: Open any `.html` file in your preferred code editor and edit semantic text directly inside `<p>`, `<h1>`–`<h6>`, and `<li>` elements.

### Updating Dummy Contact Details
Locate the contact items in `contact.html` and in the footer of all 35 pages:
- **Phone:** Replace `0000000000` with the actual business phone number.
- **Email:** Replace `demo@example.com` with your production advisory inbox.
- **Address:** Replace `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000` with your registered office address.

---

## 6. Image Asset Integration
All 71 generated corporate images are now installed and active across the website:
- **Primary Image Directory:** `images/` (Directly referenced by all 35 HTML pages).
- **Secondary Image Directory:** `assets/images/` (Mirrored repository with both `.jpeg` and modern `.webp` formats).
- **Responsive Wrapper:** Each image is wrapped in a responsive `.img-placeholder-wrapper` container with predetermined aspect ratios (`ratio-16x9`, `ratio-4x3`, `ratio-3x4`), ensuring zero cumulative layout shift (CLS), smooth hover transitions, and optimal visual hierarchy.
- **Loading Optimization:** Hero and above-the-fold banners use `loading="eager"`, while secondary and below-the-fold cards utilize `loading="lazy"` for fast initial page load times.

---

## 7. How to Deploy to Hostinger Static Hosting

Hostinger provides simple static hosting via its File Manager or Git integration:

### Method 1: Hostinger hPanel File Manager
1. Log in to your Hostinger Control Panel (hPanel).
2. Navigate to **Websites > Manage > File Manager**.
3. Access the `public_html` directory.
4. Upload all files from this project (all `.html` files, `sitemap.xml`, `robots.txt`, and the entire `assets/` directory).
5. Ensure `index.html` is located directly in the root of `public_html`.
6. Visit your domain to verify immediate site availability.

### Method 2: Git Deployment
1. Initialize a repository and push your project to GitHub or GitLab.
2. In Hostinger hPanel, navigate to **Advanced > Git**.
3. Link your repository, set the branch to `main`, and specify `/public_html` as the deployment directory.
4. Deploy with one click.

---

## 8. How to Update SEO Metadata
Each page contains individual SEO metadata in the `<head>` section:
```html
<title>Page Title | MANAGEMENT CONSULTING COMPANY</title>
<meta name="description" content="Concise executive description...">
<link rel="canonical" href="https://yourdomain.com/filename.html">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
```
When moving to your live custom domain, update the canonical URLs in all HTML files and in `sitemap.xml`.

---

## 9. Quality Assurance & Standards Verification
- **Total HTML Pages:** 35 complete, fully linked pages.
- **Total Unique Placeholders:** 71 images cataloged with dedicated Google Flow prompts.
- **Responsiveness Tested:** 360px, 390px, 768px, 1024px, 1440px, 1920px.
- **Accessibility:** Semantic landmarks, ARIA attributes, skip links, contrast ratios, and `prefers-reduced-motion` compliance.
- **Integrity:** Zero external CDN requests, zero framework overhead, zero data transmission on demonstration forms.
