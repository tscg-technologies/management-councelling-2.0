# -*- coding: utf-8 -*-
"""
Generator for the 18 Core Pages of Management Consulting Company
Includes Homepage (index.html), About, Services Overview, Industries, Methodology,
Case Studies, Team, Insights, Resources, Pricing, FAQ, Contact, Book Consultation,
Careers, Privacy Policy, Terms and Conditions.
"""

from generator_base import render_page, make_placeholder

# ==============================================================================
# 1. HOMEPAGE: index.html
# ==============================================================================
def build_index():
    body = f"""
    <!-- Executive Hero Section -->
    <section class="hero">
      <div class="container">
        <div class="hero-inner">
          <div class="hero-content">
            <div class="hero-eyebrow">
              <span class="badge badge-gold">Executive Advisory &bull; Management Consulting</span>
            </div>
            <h1 class="hero-title">TURN BUSINESS COMPLEXITY INTO CLEAR DIRECTION.</h1>
            <p class="hero-description">Strategic management consulting for organizations looking to strengthen leadership, improve performance, optimize operations, and prepare for their next stage of growth.</p>
            
            <div class="hero-actions">
              <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
              <a href="services.html" class="btn btn-outline btn-lg">Explore Our Expertise</a>
            </div>

            <div class="hero-meta">
              <div class="hero-meta-item">
                <h4>Objective Guidance</h4>
                <p>Data-informed decision frameworks free from internal politics.</p>
              </div>
              <div class="hero-meta-item">
                <h4>Structured Rhythms</h4>
                <p>Disciplined execution roadmaps with clear milestones.</p>
              </div>
              <div class="hero-meta-item">
                <h4>Sustainable Growth</h4>
                <p>Target operating models engineered for resilience.</p>
              </div>
            </div>
          </div>

          <div class="hero-visual">
            {make_placeholder("hero-management-consulting.webp", "ratio-16x9", "Executive Boardroom Strategy Session", "Recommended: 1280x720px | Executive Meeting Environment")}
          </div>
        </div>
      </div>
    </section>

    <!-- Business Challenges We Help Address Section -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-eyebrow">Executive Diagnosis</span>
          <h2 class="section-title">Critical Management Challenges We Help Solve</h2>
          <p class="section-subtitle">As organizations scale, operational complexity outpaces legacy management habits. We help leadership teams pinpoint and resolve structural friction.</p>
        </div>

        <div class="card-grid-3">
          <div class="card">
            <span class="badge badge-subtle mb-1">Challenge 01</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Strategic Drift &amp; Misalignment</h3>
            <p>Executive teams pursuing divergent departmental goals without a unified strategic roadmap or clear capital allocation priorities.</p>
            <div class="mt-auto">
              <a href="business-strategy.html" class="btn btn-sm btn-outline">Business Strategy &rarr;</a>
            </div>
          </div>

          <div class="card">
            <span class="badge badge-subtle mb-1">Challenge 02</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Operational Bottlenecks</h3>
            <p>Manual workflows, communication silos, and redundant approval layers slowing down customer fulfillment and eroding margins.</p>
            <div class="mt-auto">
              <a href="operations-consulting.html" class="btn btn-sm btn-outline">Operations Consulting &rarr;</a>
            </div>
          </div>

          <div class="card">
            <span class="badge badge-subtle mb-1">Challenge 03</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Organizational Role Ambiguity</h3>
            <p>Unclear reporting lines, overlapping responsibilities, and decision paralysis across expanding management teams.</p>
            <div class="mt-auto">
              <a href="organizational-development.html" class="btn btn-sm btn-outline">Organizational Design &rarr;</a>
            </div>
          </div>

          <div class="card">
            <span class="badge badge-subtle mb-1">Challenge 04</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Opaque Performance Metrics</h3>
            <p>Vanity reporting metrics that fail to highlight root-cause productivity issues, cost variances, or operational vulnerabilities.</p>
            <div class="mt-auto">
              <a href="performance-improvement.html" class="btn btn-sm btn-outline">Performance Systems &rarr;</a>
            </div>
          </div>

          <div class="card">
            <span class="badge badge-subtle mb-1">Challenge 05</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Change Resistance</h3>
            <p>Transformational investments and software rollouts stalling due to lack of frontline adoption and cultural resistance.</p>
            <div class="mt-auto">
              <a href="change-management.html" class="btn btn-sm btn-outline">Change Management &rarr;</a>
            </div>
          </div>

          <div class="card">
            <span class="badge badge-subtle mb-1">Challenge 06</span>
            <h3 style="font-size: 1.25rem; margin-bottom: 0.75rem;">Premature Expansion Risks</h3>
            <p>Entering new geographies or product lines without assessing operational readiness, cash flow impact, or supply chain resilience.</p>
            <div class="mt-auto">
              <a href="business-expansion.html" class="btn btn-sm btn-outline">Expansion Advisory &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Consulting Capabilities Section -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem;">
            <div>
              <span class="section-eyebrow">Consulting Practice Areas</span>
              <h2 class="section-title">Specialized Advisory Practices</h2>
              <p class="section-subtitle">Tailored management consulting capabilities designed for high-impact organizational leadership.</p>
            </div>
            <a href="services.html" class="btn btn-outline">View All 17 Practice Areas &rarr;</a>
          </div>
        </div>

        <div class="card-grid-3">
          <div class="service-card">
            <div class="service-card-image">
              {make_placeholder("business-strategy-planning.webp", "ratio-16x9", "Business Strategy Planning", "1200x675px")}
            </div>
            <div class="service-card-body">
              <h3 class="service-card-title"><a href="business-strategy.html">Business Strategy</a></h3>
              <p class="service-card-desc">Define clear competitive positioning, market opportunity priorities, and capital allocation frameworks for sustained advantage.</p>
              <div class="service-card-challenges">
                <h5>Key Deliverables</h5>
                <ul>
                  <li>Market Positioning Audit</li>
                  <li>Strategic Decision Framework</li>
                  <li>Multi-Year Execution Blueprint</li>
                </ul>
              </div>
              <div class="service-card-footer">
                <a href="business-strategy.html" class="btn btn-outline btn-sm">Explore Service</a>
                <a href="book-consultation.html" class="btn btn-gold btn-sm">Enquire</a>
              </div>
            </div>
          </div>

          <div class="service-card">
            <div class="service-card-image">
              {make_placeholder("operations-consulting-workshop.webp", "ratio-16x9", "Operations Consulting Workshop", "1200x675px")}
            </div>
            <div class="service-card-body">
              <h3 class="service-card-title"><a href="operations-consulting.html">Operations Consulting</a></h3>
              <p class="service-card-desc">Identify operational bottlenecks, streamline throughput, and standardize core workflows to achieve scalable capacity.</p>
              <div class="service-card-challenges">
                <h5>Key Deliverables</h5>
                <ul>
                  <li>Value Stream Workflow Maps</li>
                  <li>Capacity &amp; Resource Model</li>
                  <li>Standard Operating Procedures</li>
                </ul>
              </div>
              <div class="service-card-footer">
                <a href="operations-consulting.html" class="btn btn-outline btn-sm">Explore Service</a>
                <a href="book-consultation.html" class="btn btn-gold btn-sm">Enquire</a>
              </div>
            </div>
          </div>

          <div class="service-card">
            <div class="service-card-image">
              {make_placeholder("organizational-development-chart.webp", "ratio-16x9", "Organizational Development Design", "1200x675px")}
            </div>
            <div class="service-card-body">
              <h3 class="service-card-title"><a href="organizational-development.html">Organizational Development</a></h3>
              <p class="service-card-desc">Design agile reporting hierarchies, RACI decision matrices, and role charters that empower management accountability.</p>
              <div class="service-card-challenges">
                <h5>Key Deliverables</h5>
                <ul>
                  <li>Organizational Structure Blueprints</li>
                  <li>RACI Decision Rights Charters</li>
                  <li>Span of Control Optimization</li>
                </ul>
              </div>
              <div class="service-card-footer">
                <a href="organizational-development.html" class="btn btn-outline btn-sm">Explore Service</a>
                <a href="book-consultation.html" class="btn btn-gold btn-sm">Enquire</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Organizational Performance Framework (Interactive Dashboard) -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-eyebrow">Operating Architecture</span>
          <h2 class="section-title">Executive Management Operating Framework</h2>
          <p class="section-subtitle">We equip leadership teams with structured decision rhythms, diagnostic dashboards, and disciplined milestone governance.</p>
        </div>

        <div class="dashboard-container">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Executive Enterprise Dashboard Demo</h4>
              <p>Sample multi-metric management tracking suite integrating strategic goals, operational indicators, and governance status.</p>
            </div>
            <span class="demo-watermark">Illustrative Demo Data &bull; Not Actual Client Information</span>
          </div>

          <div class="metrics-grid">
            <div class="metric-card">
              <div class="metric-card-label">Strategic Milestone Completion</div>
              <div class="metric-card-val">87.5%</div>
              <div class="metric-card-status metric-status-good">On Schedule for Q4 Targets</div>
            </div>
            <div class="metric-card">
              <div class="metric-card-label">Workflow Throughput Index</div>
              <div class="metric-card-val">94.1%</div>
              <div class="metric-card-status metric-status-good">&uarr; +12% post-re-engineering</div>
            </div>
            <div class="metric-card">
              <div class="metric-card-label">Operating Margin Variance</div>
              <div class="metric-card-val">+3.4%</div>
              <div class="metric-card-status metric-status-good">Cost discipline baseline met</div>
            </div>
            <div class="metric-card">
              <div class="metric-card-label">Active Escalation Items</div>
              <div class="metric-card-val">2</div>
              <div class="metric-card-status metric-status-info">Under executive committee review</div>
            </div>
          </div>

          <div style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.5rem; margin-top: 1.5rem;">
            <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Core Executive Cadence &amp; Operating Rhythms</h5>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem;">
              <div style="background: #F8FAFC; padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--accent-blue);">
                <strong>Weekly Operational Standup</strong>
                <p style="font-size: 0.8rem; margin-top: 0.25rem; color: var(--secondary-text);">45-minute tactical review addressing active bottlenecks and immediate milestone SLA commitments.</p>
              </div>
              <div style="background: #F8FAFC; padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--muted-gold);">
                <strong>Monthly Management Review</strong>
                <p style="font-size: 0.8rem; margin-top: 0.25rem; color: var(--secondary-text);">Structured performance audit evaluating departmental OKRs, margin variance, and cross-team dependencies.</p>
              </div>
              <div style="background: #F8FAFC; padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--primary-navy);">
                <strong>Quarterly Strategy Horizon</strong>
                <p style="font-size: 0.8rem; margin-top: 0.25rem; color: var(--secondary-text);">Executive board review analyzing competitive shifts, capital allocation, and 90-day transformation priorities.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 5-Stage Consulting Methodology Section -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="section-eyebrow">Structured Execution</span>
          <h2 class="section-title">Our Five-Stage Consulting Methodology</h2>
          <p class="section-subtitle">A disciplined, reproducible problem-solving architecture designed to ensure organizational alignment and tangible outcomes.</p>
        </div>

        <div class="methodology-stages">
          <div class="stage-card">
            <span class="stage-badge">Stage 01</span>
            <h3 class="stage-title">Understand</h3>
            <p class="stage-objective">Establish clarity around leadership vision, core business model, current operating constraints, and engagement scope.</p>
            <ul class="stage-activities-list">
              <li>Executive stakeholder interviews</li>
              <li>Baseline documentation intake</li>
              <li>Charter definition &amp; governance</li>
            </ul>
          </div>

          <div class="stage-card">
            <span class="stage-badge">Stage 02</span>
            <h3 class="stage-title">Assess</h3>
            <p class="stage-objective">Perform comprehensive diagnostic reviews of workflows, reporting hierarchies, and departmental performance data.</p>
            <ul class="stage-activities-list">
              <li>Value stream workflow audits</li>
              <li>Organizational structure mapping</li>
              <li>Cost &amp; productivity diagnostics</li>
            </ul>
          </div>

          <div class="stage-card">
            <span class="stage-badge">Stage 03</span>
            <h3 class="stage-title">Diagnose</h3>
            <p class="stage-objective">Isolate root-cause bottlenecks, identify operational vulnerabilities, and quantify improvement potential.</p>
            <ul class="stage-activities-list">
              <li>Root-cause friction analysis</li>
              <li>Gap &amp; dependency synthesis</li>
              <li>Risk &amp; capability matrices</li>
            </ul>
          </div>

          <div class="stage-card">
            <span class="stage-badge">Stage 04</span>
            <h3 class="stage-title">Recommend</h3>
            <p class="stage-objective">Architect pragmatic strategic recommendations, operating model blueprints, and phased execution roadmaps.</p>
            <ul class="stage-activities-list">
              <li>Target operating model blueprints</li>
              <li>RACI decision matrices</li>
              <li>Phased 90-day execution plans</li>
            </ul>
          </div>

          <div class="stage-card">
            <span class="stage-badge">Stage 05</span>
            <h3 class="stage-title">Support</h3>
            <p class="stage-objective">Provide structured advisory support, governance check-ins, and milestone variance reviews during implementation.</p>
            <ul class="stage-activities-list">
              <li>Management review facilitation</li>
              <li>Milestone tracking &amp; governance</li>
              <li>Continuous refinement advisory</li>
            </ul>
          </div>
        </div>

        <div class="text-center mt-4">
          <a href="methodology.html" class="btn btn-primary">Read Full Methodology Details &rarr;</a>
        </div>
      </div>
    </section>

    <!-- Industries We Serve Section -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem;">
            <div>
              <span class="section-eyebrow">Industry Expertise</span>
              <h2 class="section-title">Industries We Serve</h2>
              <p class="section-subtitle">Tailoring strategic frameworks and operational best practices across key economic sectors.</p>
            </div>
            <a href="industries.html" class="btn btn-outline">Explore All 14 Industries &rarr;</a>
          </div>
        </div>

        <div class="card-grid-4">
          <div class="card">
            <h4 style="margin-bottom: 0.5rem;">Manufacturing</h4>
            <p style="font-size: 0.85rem;">Plant throughput, capacity planning, supply chain synchronization, and inventory holding optimization.</p>
            <a href="industries.html" class="btn btn-sm btn-outline mt-auto">Learn More &rarr;</a>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem;">Healthcare</h4>
            <p style="font-size: 0.85rem;">Patient flow management, administrative efficiency, departmental governance, and operational compliance.</p>
            <a href="industries.html" class="btn btn-sm btn-outline mt-auto">Learn More &rarr;</a>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem;">Technology &amp; SaaS</h4>
            <p style="font-size: 0.85rem;">Product operating models, customer onboarding workflows, post-sales alignment, and scaling governance.</p>
            <a href="industries.html" class="btn btn-sm btn-outline mt-auto">Learn More &rarr;</a>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem;">Logistics &amp; Supply</h4>
            <p style="font-size: 0.85rem;">Fleet routing protocols, warehouse handling standards, 3PL partner management, and delivery SLA controls.</p>
            <a href="industries.html" class="btn btn-sm btn-outline mt-auto">Learn More &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Case Studies Section -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem;">
            <div>
              <span class="section-eyebrow">Advisory Evidence</span>
              <h2 class="section-title">Illustrative Advisory Case Studies</h2>
              <p class="section-subtitle">Conceptual case demonstrations illustrating our analytical approach to enterprise challenges.</p>
            </div>
            <a href="case-studies.html" class="btn btn-outline">View All Case Studies &rarr;</a>
          </div>
        </div>

        <div class="card-grid-3">
          <div class="case-card">
            <div class="case-card-body">
              <span class="case-card-category">Business Strategy</span>
              <h3 class="case-card-title"><a href="case-study-details.html">Business Strategy Assessment Demo</a></h3>
              <p class="case-card-summary">Illustrative diagnosis of a multi-product enterprise addressing margin contraction through market repositioning and product line pruning.</p>
              <div class="case-demo-notice">
                <strong>Notice:</strong> Illustrative Demo Case Study &bull; Not an actual client engagement.
              </div>
              <div class="mt-auto">
                <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Case Summary &rarr;</a>
              </div>
            </div>
          </div>

          <div class="case-card">
            <div class="case-card-body">
              <span class="case-card-category">Operations Consulting</span>
              <h3 class="case-card-title"><a href="case-study-details.html">Operational Process Optimization Demo</a></h3>
              <p class="case-card-summary">Conceptual examination of a multi-site fulfillment operation experiencing severe delivery handoff delays and unstandardized workflows.</p>
              <div class="case-demo-notice">
                <strong>Notice:</strong> Illustrative Demo Case Study &bull; Not an actual client engagement.
              </div>
              <div class="mt-auto">
                <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Case Summary &rarr;</a>
              </div>
            </div>
          </div>

          <div class="case-card">
            <div class="case-card-body">
              <span class="case-card-category">Organizational Design</span>
              <h3 class="case-card-title"><a href="case-study-details.html">Organizational Structure Review Demo</a></h3>
              <p class="case-card-summary">Illustrative restructuring blueprint resolving overlapping executive roles, unclear decision rights, and excessive management layers.</p>
              <div class="case-demo-notice">
                <strong>Notice:</strong> Illustrative Demo Case Study &bull; Not an actual client engagement.
              </div>
              <div class="mt-auto">
                <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Case Summary &rarr;</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Management Insights & Thought Leadership Section -->
    <section class="section section-alt">
      <div class="container">
        <div class="section-header">
          <div style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 1rem;">
            <div>
              <span class="section-eyebrow">Thought Leadership</span>
              <h2 class="section-title">Management Insights &amp; Research</h2>
              <p class="section-subtitle">Editorial perspectives on strategy execution, operating model design, and leadership alignment.</p>
            </div>
            <a href="insights.html" class="btn btn-outline">View All Articles &rarr;</a>
          </div>
        </div>

        <div class="card-grid-3">
          <div class="article-card">
            <div class="article-card-body">
              <div class="article-card-meta">
                <span class="badge badge-subtle">Business Strategy</span>
                <span>8 Min Read</span>
              </div>
              <h3 class="article-card-title"><a href="article-details.html">How to Build a Practical Business Strategy</a></h3>
              <p class="article-card-excerpt">Why most corporate strategies fail during execution, and how to construct actionable frameworks that align daily operational decisions with executive ambition.</p>
              <div class="mt-auto">
                <a href="article-details.html" class="btn btn-outline btn-sm">Read Article &rarr;</a>
              </div>
            </div>
          </div>

          <div class="article-card">
            <div class="article-card-body">
              <div class="article-card-meta">
                <span class="badge badge-subtle">Organizational Design</span>
                <span>6 Min Read</span>
              </div>
              <h3 class="article-card-title"><a href="article-details.html">Why Organizational Structure Matters</a></h3>
              <p class="article-card-excerpt">An exploration of how ambiguous reporting lines, redundant management layers, and misaligned incentives quietly strangle organizational productivity.</p>
              <div class="mt-auto">
                <a href="article-details.html" class="btn btn-outline btn-sm">Read Article &rarr;</a>
              </div>
            </div>
          </div>

          <div class="article-card">
            <div class="article-card-body">
              <div class="article-card-meta">
                <span class="badge badge-subtle">Operations</span>
                <span>7 Min Read</span>
              </div>
              <h3 class="article-card-title"><a href="article-details.html">How to Improve Operational Efficiency</a></h3>
              <p class="article-card-excerpt">A systematic methodology for uncovering hidden process bottlenecks, eliminating non-value-adding manual steps, and establishing scalable SOPs.</p>
              <div class="mt-auto">
                <a href="article-details.html" class="btn btn-outline btn-sm">Read Article &rarr;</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("index.html", "Turn Business Complexity into Clear Direction", "Strategic management consulting company helping business leaders solve management challenges, improve organizational performance, and achieve sustainable growth.", body)

# ==============================================================================
# 2. ABOUT: about.html
# ==============================================================================
def build_about():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">About</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Corporate Advisory Philosophy</span>
          <h1>Helping Leaders Build More Effective Organizations.</h1>
          <p class="lead">An independent management consulting practice committed to objective analysis, structured problem-solving, and sustainable value creation.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="hero-inner" style="align-items: start; margin-bottom: 4rem;">
          <div>
            <span class="section-eyebrow">Our Philosophy</span>
            <h2 class="section-title">Objective Guidance for Complex Business Decisions</h2>
            <p>Every growing enterprise eventually encounters management friction. As customer demands increase, headcounts expand, and operational networks multiply, traditional leadership mechanisms begin to strain. Decisions slow down, priorities diverge, and operational costs climb.</p>
            <p>We exist to bring structural clarity to these moments. We do not offer pre-packaged templates or abstract academic theories. Instead, we work collaboratively alongside business owners, CEOs, and executive boards to systematically analyze root causes, design pragmatic operating models, and install the governance rhythms needed for long-term resilience.</p>
            <p>Our work is grounded in management discipline: clear accountability, transparent measurement, streamlined workflows, and unified executive direction.</p>
          </div>
          <div>
            {make_placeholder("management-team-discussion.webp", "ratio-4x3", "Executive Strategy Consultation", "1000x750px | Executive Meeting")}
          </div>
        </div>

        <!-- Mission & Vision -->
        <div class="card-grid-2 mb-4">
          <div class="card" style="border-top: 4px solid var(--primary-navy);">
            <span class="section-eyebrow">Our Mission</span>
            <h3 style="margin-bottom: 1rem;">Why We Advise</h3>
            <p>To empower business leaders with the strategic clarity, organizational frameworks, and operational discipline required to build resilient, high-performing enterprises that create enduring commercial and social value.</p>
          </div>

          <div class="card" style="border-top: 4px solid var(--muted-gold);">
            <span class="section-eyebrow">Our Vision</span>
            <h3 style="margin-bottom: 1rem;">What We Strive For</h3>
            <p>To be the trusted, objective management advisory partner of choice for ambitious leadership teams navigating pivotal stages of organizational growth, restructuring, and transformation.</p>
          </div>
        </div>

        <!-- Management Principles -->
        <div class="section-header" style="margin-top: 4.5rem;">
          <span class="section-eyebrow">Institutional Standards</span>
          <h2 class="section-title">Our Core Management Principles</h2>
          <p class="section-subtitle">The foundational standards that guide every diagnostic review, strategic recommendation, and client interaction.</p>
        </div>

        <div class="card-grid-3">
          <div class="card">
            <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">1. Analytical Objectivity</h4>
            <p style="font-size: 0.9rem;">We base recommendations on rigorous diagnostic data, workflow mapping, and operational facts—never internal politics or subjective assumptions.</p>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">2. Practical Implementability</h4>
            <p style="font-size: 0.9rem;">A strategy is only as valuable as the organization's capacity to execute it. We tailor every recommendation to realistic organizational resources.</p>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">3. Uncompromising Integrity</h4>
            <p style="font-size: 0.9rem;">We speak candidly to executive leadership regarding uncomfortable operational bottlenecks, margin leaks, and leadership misalignments.</p>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">4. Structural Accountability</h4>
            <p style="font-size: 0.9rem;">We design organizational systems where every milestone, workflow, and metric has an unambiguous owner and transparent review cadence.</p>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">5. Institutional Capability</h4>
            <p style="font-size: 0.9rem;">Our objective is not perpetual dependency; we build internal management capabilities that endure long after our advisory engagement concludes.</p>
          </div>
          <div class="card">
            <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">6. Long-Term Value Focus</h4>
            <p style="font-size: 0.9rem;">We prioritize sustainable operational health and lasting enterprise value over short-sighted cost-cutting or cosmetic reorganizations.</p>
          </div>
        </div>

        <!-- Approach to Problem Solving -->
        <div class="card mt-4" style="background: #F8FAFC; padding: 2.5rem;">
          <span class="section-eyebrow">Problem-Solving Architecture</span>
          <h3 style="margin-bottom: 1rem;">Leadership Alignment &amp; Value Creation</h3>
          <p>Successful management consulting requires deep empathy for the executive reality. CEOs and managing directors juggle commercial pressure, operational emergencies, and stakeholder expectations. Our advisory process is engineered to alleviate executive friction by introducing structured clarity:</p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
            <div>
              <strong style="color: var(--primary-navy); display: block; margin-bottom: 0.25rem;">Diagnostic Depth</strong>
              <p style="font-size: 0.85rem; color: var(--secondary-text);">Uncovering root causes rather than applying surface-level remedies to symptoms.</p>
            </div>
            <div>
              <strong style="color: var(--primary-navy); display: block; margin-bottom: 0.25rem;">Executive Consensus</strong>
              <p style="font-size: 0.85rem; color: var(--secondary-text);">Aligning the executive team around unambiguous priorities and shared milestones.</p>
            </div>
            <div>
              <strong style="color: var(--primary-navy); display: block; margin-bottom: 0.25rem;">Operational Governance</strong>
              <p style="font-size: 0.85rem; color: var(--secondary-text);">Establishing weekly and monthly review cadences that ensure continuous execution.</p>
            </div>
          </div>
        </div>

        <!-- Demonstration Notice -->
        <div class="case-demo-notice mt-4">
          <strong>Demonstration Identity Notice:</strong> This profile represents a generic management consulting company prototype designed for business evaluation. It does not fabricate corporate founding dates, historical milestones, executive biographies, or specific client testimonials.
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("about.html", "Helping Leaders Build More Effective Organizations", "Learn about our management consulting philosophy, principles, mission, and structured approach to executive advisory and organizational development.", body)

# ==============================================================================
# 3. SERVICES OVERVIEW: services.html
# ==============================================================================
def build_services_overview():
    # Import the 17 services from build_service_pages
    from build_service_pages import SERVICES

    cards_html = ""
    for s in SERVICES:
        cards_html += f"""
        <div class="service-card">
          <div class="service-card-image">
            {make_placeholder(s["image"], "ratio-16x9", s["title"], "1000x562px")}
          </div>
          <div class="service-card-body">
            <span class="badge badge-subtle mb-1">{s["eyebrow"]}</span>
            <h3 class="service-card-title"><a href="{s["slug"]}.html">{s["title"]}</a></h3>
            <p class="service-card-desc">{s["description"]}</p>
            
            <div class="service-card-challenges">
              <h5>Addressed Challenges</h5>
              <ul>
                <li>{s["challenges"][0]}</li>
                <li>{s["challenges"][1]}</li>
              </ul>
            </div>

            <div class="service-card-deliverables">
              <strong>Key Deliverables:</strong> {s["deliverables"][0]}; {s["deliverables"][1]}.
            </div>

            <div class="service-card-footer">
              <a href="{s["slug"]}.html" class="btn btn-outline btn-sm">Learn More &rarr;</a>
              <a href="book-consultation.html" class="btn btn-gold btn-sm">Book Consultation</a>
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Services</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Advisory Practice Portfolio</span>
          <h1>Management Consulting Solutions for Complex Business Challenges.</h1>
          <p class="lead">Explore our 17 specialized consulting practices covering corporate strategy, operations, governance, organizational architecture, and performance systems.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-eyebrow">Comprehensive Advisory</span>
          <h2 class="section-title">Our Consulting Practices</h2>
          <p class="section-subtitle">Every service is delivered using our disciplined five-stage methodology, with clear deliverables, executive milestones, and objective diagnostic metrics.</p>
        </div>

        <div class="card-grid-3">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("services.html", "Management Consulting Solutions for Complex Business Challenges", "Overview of our 17 management consulting practices: strategy, operations, governance, performance improvement, and organizational development.", body)

# ==============================================================================
# 21. INDUSTRIES: industries.html
# ==============================================================================
def build_industries():
    industries_data = [
        {"name": "Manufacturing", "image": "industry-manufacturing-plant.webp", "challenges": "Capacity bottlenecks, uneven machine utilization, production scheduling slippage, and supply chain holding costs.", "services": "Operations Consulting, Process Optimization, Supply Chain Alignment.", "improvements": "Value stream balancing, standardized maintenance SOPs, and dynamic inventory buffer models."},
        {"name": "Healthcare & Life Sciences", "image": "industry-healthcare-facility.webp", "challenges": "Patient flow bottlenecks, clinical administrative overhead, departmental scheduling conflicts, and regulatory compliance friction.", "services": "Process Optimization, Governance Advisory, Performance Systems.", "improvements": "Streamlined patient intake, digital scheduling governance, and clinical workflow standard operating procedures."},
        {"name": "Education & Academic Institutions", "image": "industry-education-campus.webp", "challenges": "Institutional role ambiguity, disjointed faculty administration, shifting enrollment dynamics, and operational cost pressures.", "services": "Organizational Development, Strategic Planning, Financial Performance.", "improvements": "Clarified administrative reporting hierarchies, enrollment scenario planning, and budget allocation frameworks."},
        {"name": "Real Estate & Development", "image": "industry-real-estate-architecture.webp", "challenges": "Capital allocation friction across multi-year development cycles, contractor coordination delays, and volatile market demand.", "services": "Project Management, Business Strategy, Risk Management.", "improvements": "Comprehensive milestone governance, contractor SLA monitoring, and capital allocation risk matrices."},
        {"name": "Retail & Consumer Goods", "image": "industry-retail-store-operations.webp", "challenges": "Store-level inventory shrinkage, uncoordinated promotional handoffs, multichannel fulfillment bottlenecks, and margin compression.", "services": "Operations Consulting, Performance Improvement, Change Management.", "improvements": "Omnichannel fulfillment standardization, regional stock replenishment rules, and store manager performance scorecards."},
        {"name": "E-Commerce & Digital Marketplaces", "image": "industry-ecommerce-fulfillment.webp", "challenges": "Order fulfillment latency during peak seasons, high returns processing costs, customer support backlog, and fragile unit economics.", "services": "Digital Transformation, Operations Consulting, Process Optimization.", "improvements": "Automated warehouse pick-and-pack routing, returns workflow re-engineering, and unit contribution margin visibility."},
        {"name": "Technology & Software (SaaS)", "image": "industry-technology-software-office.webp", "challenges": "Product development misaligned with sales commitments, post-sale implementation delays, customer churn, and rapid headcount sprawl.", "services": "Business Strategy, Organizational Development, Leadership Consulting.", "improvements": "Cross-functional product-sales governance, customer success onboarding SLAs, and span of control optimization."},
        {"name": "Financial Services & FinTech", "image": "industry-financial-services-boardroom.webp", "challenges": "Complex regulatory reporting overhead, fragmented customer onboarding workflows, legacy core system drag, and operational risk.", "services": "Risk Management, Process Optimization, Corporate Governance.", "improvements": "KYC/onboarding workflow compression, internal risk committee charters, and enterprise governance dashboards."},
        {"name": "Logistics & Supply Chain", "image": "industry-logistics-distribution-center.webp", "challenges": "Fleet turnaround idle time, 3PL supplier accountability gaps, freight rate volatility, and last-mile delivery tracking errors.", "services": "Operations Consulting, Performance Improvement, Project Management.", "improvements": "Fleet dispatch optimization algorithms, 3PL SLA vendor scorecards, and regional hub throughput monitoring."},
        {"name": "Hospitality & Tourism", "image": "industry-hospitality-hotel-operations.webp", "challenges": "Seasonal workforce turnover, guest service consistency variance across properties, food & beverage margin leakages.", "services": "Human Resource Management, Operations Consulting, Performance Improvement.", "improvements": "Standardized guest service checklists, seasonal staff onboarding pipelines, and departmental cost monitoring."},
        {"name": "Professional Services", "image": "industry-professional-services-firm.webp", "challenges": "Partner-level utilization imbalances, key-client concentration risk, scope creep on fixed-fee engagements, and associate turnover.", "services": "Management Advisory, Strategic Planning, Organizational Development.", "improvements": "Resource utilization tracking, project scope variation control procedures, and structured career ladder architectures."},
        {"name": "Startups & Emerging Ventures", "image": "industry-startup-innovation-hub.webp", "challenges": "Transitioning from founder-led improvisation to institutional management, runway discipline, and rapid organizational scaling.", "services": "Strategic Planning, Business Expansion, Organizational Development.", "improvements": "90-day execution roadmaps, milestone-based budget governance, and core management role definitions."},
        {"name": "Construction & Infrastructure", "image": "industry-construction-project-site.webp", "challenges": "Subcontractor timeline slippage, material price escalation, safety compliance reporting, and project cost overrun.", "services": "Project Management, Risk Management, Corporate Governance.", "improvements": "Weekly site milestone governance cadences, critical path contingency buffers, and safety audit protocols."},
        {"name": "Telecommunications", "image": "industry-telecommunications-infrastructure.webp", "challenges": "High capital infrastructure maintenance costs, customer churn in saturated markets, field technician routing inefficiencies.", "services": "Business Transformation, Operations Consulting, Digital Transformation.", "improvements": "Field service scheduling dispatch re-engineering, network asset maintenance roadmaps, and customer retention workflows."}
    ]

    cards_html = ""
    for ind in industries_data:
        cards_html += f"""
        <div class="industry-card">
          <div class="service-card-image">
            {make_placeholder(ind["image"], "ratio-16x9", ind["name"], "1000x562px")}
          </div>
          <div class="industry-card-body">
            <span class="badge badge-subtle mb-1">Sector Practice</span>
            <h3>{ind["name"]}</h3>
            <p class="desc">Navigating sector-specific regulatory, operational, and commercial pressures through structured management consulting.</p>
            
            <div class="industry-block">
              <h5>Common Management Challenges</h5>
              <p style="font-size: 0.8125rem; color: var(--secondary-text); margin-bottom: 0.5rem;">{ind["challenges"]}</p>
            </div>

            <div class="industry-block">
              <h5>Relevant Consulting Services</h5>
              <p style="font-size: 0.8125rem; color: var(--secondary-navy); font-weight: 500; margin-bottom: 0.5rem;">{ind["services"]}</p>
            </div>

            <div class="industry-block">
              <h5>Potential Areas of Improvement</h5>
              <p style="font-size: 0.8125rem; color: var(--secondary-text); margin-bottom: 0.5rem;">{ind["improvements"]}</p>
            </div>

            <div class="mt-auto pt-2" style="border-top: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
              <a href="book-consultation.html" class="btn btn-sm btn-gold">Discuss Sector Challenge</a>
              <a href="services.html" class="btn btn-sm btn-outline">Explore Solutions</a>
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Industries</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Sector Specialization</span>
          <h1>Tailored Consulting Frameworks Across Core Industries.</h1>
          <p class="lead">While management fundamentals are universal, industry context dictates operational velocity and risk tolerance. We adapt our frameworks to the realities of 14 key economic sectors.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="section-eyebrow">Industry Sectors</span>
          <h2 class="section-title">Industry-Specific Advisory Overview</h2>
          <p class="section-subtitle">Discover common operational challenges, relevant consulting practices, and typical diagnostic focal points across each industry.</p>
        </div>

        <div class="card-grid-2">
          {cards_html}
        </div>

        <div class="case-demo-notice mt-4">
          <strong>Demonstration Disclaimer:</strong> Sector representations illustrate typical consulting problem-solving frameworks. We do not claim fabricated past client names, commercial relationships, or proprietary industry accreditations.
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("industries.html", "Industry Consulting Practices across 14 Sectors", "Explore our industry management consulting practices covering manufacturing, healthcare, technology, logistics, retail, education, and financial services.", body)

# ==============================================================================
# 22. METHODOLOGY: methodology.html
# ==============================================================================
def build_methodology():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Methodology</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Analytical Rigor &amp; Execution</span>
          <h1>A Structured Approach to Better Management Decisions.</h1>
          <p class="lead">Our disciplined five-stage management consulting methodology guides organizations from initial diagnostic discovery through actionable roadmap architecture and governed implementation.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="hero-inner" style="align-items: start; margin-bottom: 4rem;">
          <div>
            <span class="section-eyebrow">Problem-Solving Architecture</span>
            <h2 class="section-title">Why a Structured Methodology Matters</h2>
            <p>Complex business problems cannot be resolved through intuition alone or pre-fabricated slide decks. When organizations face margin pressure, structural misalignment, or growth plateaus, premature solutions often worsen underlying bottlenecks.</p>
            <p>Our five-stage methodology enforces analytical discipline at every step: we ensure executive teams agree on root problems before debating answers, and establish clear measurement criteria before embarking on execution.</p>
            <div class="mt-3">
              <a href="book-consultation.html" class="btn btn-gold">Discuss an Engagement Approach</a>
            </div>
          </div>
          <div>
            {make_placeholder("management-case-study-workspace.webp", "ratio-4x3", "Methodology Discovery Session", "1000x750px | Strategic Advisory")}
          </div>
        </div>

        <!-- 5 Stages Detailed Deep Dive -->
        <div class="section-header" style="margin-top: 4.5rem;">
          <span class="section-eyebrow">The Five Stages</span>
          <h2 class="section-title">Stage-by-Stage Advisory Breakdown</h2>
          <p class="section-subtitle">Each phase delivers specific executive artifacts, answers precise managerial questions, and establishes clear decision gates.</p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 2.5rem;">
          <!-- Stage 1 -->
          <div class="card" style="border-left: 5px solid var(--accent-blue);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap;">
              <span class="badge badge-gold">Stage 01</span>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">Engagement Duration: Typical Weeks 1-2</span>
            </div>
            <h3 style="font-size: 1.5rem; color: var(--primary-navy); margin-bottom: 0.75rem;">Stage 1 — Understand</h3>
            <p><strong>Primary Objective:</strong> Establish a deep, objective understanding of the organization's business model, leadership objectives, management structure, and self-identified pain points.</p>
            <div class="card-grid-3 mt-3">
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Key Activities</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Confidential interviews with executive leadership</li>
                  <li>Intake of organization charts, financials, and SOPs</li>
                  <li>Initial stakeholder expectation alignment sessions</li>
                  <li>Engagement charter and scope confirmation</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Core Questions Addressed</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>What strategic outcome does leadership seek to achieve?</li>
                  <li>Where do executives perceive friction to exist?</li>
                  <li>What historical constraints have impeded progress?</li>
                  <li>Who are the critical internal decision stakeholders?</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Typical Deliverables</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Engagement Charter &amp; Governance Cadence</li>
                  <li>Executive Stakeholder Alignment Matrix</li>
                  <li>Diagnostic Discovery Plan &amp; Request List</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Stage 2 -->
          <div class="card" style="border-left: 5px solid var(--secondary-navy);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap;">
              <span class="badge badge-gold">Stage 02</span>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">Engagement Duration: Typical Weeks 3-4</span>
            </div>
            <h3 style="font-size: 1.5rem; color: var(--primary-navy); margin-bottom: 0.75rem;">Stage 2 — Assess</h3>
            <p><strong>Primary Objective:</strong> Systematically review frontline workflows, reporting hierarchies, operating models, unit economics, and available management performance data.</p>
            <div class="card-grid-3 mt-3">
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Key Activities</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Value stream workflow mapping across core units</li>
                  <li>Span of control and layer analysis</li>
                  <li>Departmental KPI and reporting audit</li>
                  <li>Frontline employee focus groups and observational audits</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Core Questions Addressed</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>How do actual workflows deviate from official SOPs?</li>
                  <li>Where are hand-off delays and idle queues accumulating?</li>
                  <li>How accurate and timely is executive reporting?</li>
                  <li>What is the true cost structure of core services?</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Typical Deliverables</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Current State Value Stream Map</li>
                  <li>Organizational Span of Control Audit</li>
                  <li>Management Information System Review</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Stage 3 -->
          <div class="card" style="border-left: 5px solid #EF4444;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap;">
              <span class="badge badge-gold">Stage 03</span>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">Engagement Duration: Typical Weeks 5-6</span>
            </div>
            <h3 style="font-size: 1.5rem; color: var(--primary-navy); margin-bottom: 0.75rem;">Stage 3 — Diagnose</h3>
            <p><strong>Primary Objective:</strong> Isolate root causes, identify capacity bottlenecks, evaluate enterprise risks, and quantify improvement opportunities.</p>
            <div class="card-grid-3 mt-3">
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Key Activities</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Root-cause friction synthesis and categorization</li>
                  <li>Cost of inefficiency and capacity loss modeling</li>
                  <li>5x5 Enterprise Risk matrix population</li>
                  <li>Organizational readiness and cultural resistance assessment</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Core Questions Addressed</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>What structural factors drive operational friction?</li>
                  <li>Which bottlenecks produce the greatest financial drag?</li>
                  <li>What change management hurdles will arise?</li>
                  <li>What capabilities must be built or augmented?</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Typical Deliverables</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Diagnostic Findings &amp; Root-Cause Report</li>
                  <li>Quantified Improvement Opportunity Matrix</li>
                  <li>Enterprise Risk &amp; Dependency Profile</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Stage 4 -->
          <div class="card" style="border-left: 5px solid var(--muted-gold);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap;">
              <span class="badge badge-gold">Stage 04</span>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">Engagement Duration: Typical Weeks 7-8</span>
            </div>
            <h3 style="font-size: 1.5rem; color: var(--primary-navy); margin-bottom: 0.75rem;">Stage 4 — Recommend</h3>
            <p><strong>Primary Objective:</strong> Construct actionable strategic recommendations, target operating model blueprints, RACI charters, and prioritized implementation roadmaps.</p>
            <div class="card-grid-3 mt-3">
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Key Activities</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Future State operating model blueprinting</li>
                  <li>RACI decision rights and charter definition</li>
                  <li>Initiative prioritization scoring (Impact vs. Effort)</li>
                  <li>Phased milestone and resource allocation modeling</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Core Questions Addressed</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>What is the optimal target operating model?</li>
                  <li>Who owns each critical decision and deliverable?</li>
                  <li>What is the prioritized sequence of rollout initiatives?</li>
                  <li>What quick wins can build momentum in the first 60 days?</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Typical Deliverables</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Target Operating Model (TOM) Architecture</li>
                  <li>Strategic Execution Roadmap &amp; 90-Day Plan</li>
                  <li>RACI Governance Charters &amp; SOP Templates</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Stage 5 -->
          <div class="card" style="border-left: 5px solid #10B981;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap;">
              <span class="badge badge-gold">Stage 05</span>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">Engagement Duration: Weeks 9+ (Where Scoped)</span>
            </div>
            <h3 style="font-size: 1.5rem; color: var(--primary-navy); margin-bottom: 0.75rem;">Stage 5 — Support</h3>
            <p><strong>Primary Objective:</strong> Support agreed implementation activities, facilitate executive governance rhythms, track milestone compliance, and refine roadmaps based on live execution feedback.</p>
            <div class="card-grid-3 mt-3">
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Key Activities</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Executive Project Management Office (PMO) facilitation</li>
                  <li>Bi-weekly milestone variance tracking</li>
                  <li>Leadership cadence chairing and review coaching</li>
                  <li>Continuous improvement calibration and post-rollout audit</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Core Questions Addressed</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Are milestones tracking according to agreed deadlines?</li>
                  <li>Are new workflows and SOPs being adopted by frontline staff?</li>
                  <li>What unforeseen execution hurdles require mid-course adjustment?</li>
                  <li>How are performance metrics evolving against baseline?</li>
                </ul>
              </div>
              <div style="background: #F8FAFC; padding: 1.25rem; border-radius: var(--radius-sm);">
                <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">Typical Deliverables</h5>
                <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text);">
                  <li>Bi-Weekly Executive Progress Scorecard</li>
                  <li>Milestone Variance &amp; Remediation Briefs</li>
                  <li>Institutional Knowledge Handover Protocol</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <div class="case-demo-notice mt-4">
          <strong>Framework Notice:</strong> This five-stage approach represents standard management consulting methodology. We do not invent proprietary trademarked titles or claim unverified third-party certifications.
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("methodology.html", "Our Five-Stage Management Consulting Methodology", "Learn about our structured five-stage management consulting methodology: Understand, Assess, Diagnose, Recommend, and Support.", body)

# ==============================================================================
# 23. CASE STUDIES: case-studies.html
# ==============================================================================
def build_case_studies():
    cases = [
        {"cat": "strategy", "cat_label": "Business Strategy", "title": "Business Strategy Assessment Demo", "desc": "Illustrative strategic repositioning and product portfolio pruning for a mid-market manufacturing enterprise facing margin compression.", "image": "case-strategy-assessment.webp"},
        {"cat": "org", "cat_label": "Organizational Development", "title": "Organizational Structure Review Demo", "desc": "Conceptual organizational design addressing overlapping management roles, excessive managerial layers, and unclear decision rights.", "image": "case-org-structure.webp"},
        {"cat": "operations", "cat_label": "Operational Excellence", "title": "Operational Process Optimization Demo", "desc": "Diagnostic value stream re-engineering for a distribution business experiencing delivery bottlenecks and high rework rates.", "image": "case-operations-optimization.webp"},
        {"cat": "performance", "cat_label": "Performance Improvement", "title": "Business Performance Framework Demo", "desc": "Design and installation of a cascading KPI architecture, executive dashboard, and monthly management review cadence.", "image": "case-performance-framework.webp"},
        {"cat": "digital", "cat_label": "Digital Transformation", "title": "Digital Transformation Roadmap Demo", "desc": "Phased technology roadmap aligning ERP platform modernization with core order-to-cash workflow standardization.", "image": "case-digital-roadmap.webp"},
        {"cat": "change", "cat_label": "Change Management", "title": "Change Management Planning Demo", "desc": "Stakeholder alignment and change enablement framework supporting enterprise operating model transition.", "image": "case-change-management.webp"},
        {"cat": "hr", "cat_label": "Organizational Development", "title": "Workforce Planning Demo", "desc": "Strategic workforce modeling aligning talent recruitment, retention mechanisms, and departmental expansion goals.", "image": "case-workforce-planning.webp"},
        {"cat": "expansion", "cat_label": "Business Strategy", "title": "Business Expansion Strategy Demo", "desc": "Feasibility assessment and multi-stage geographic market entry roadmap managing capital risk and supply chain resilience.", "image": "case-business-expansion.webp"}
    ]

    cards_html = ""
    for c in cases:
        cards_html += f"""
        <div class="case-card case-study-card-item" data-category="{c["cat"]}">
          <div class="service-card-image">
            {make_placeholder(c["image"], "ratio-16x9", c["title"], "1000x562px")}
          </div>
          <div class="case-card-body">
            <span class="case-card-category">{c["cat_label"]}</span>
            <h3 class="case-card-title"><a href="case-study-details.html">{c["title"]}</a></h3>
            <p class="case-card-summary">{c["desc"]}</p>
            <div class="case-demo-notice">
              <strong>Demo Notice:</strong> Illustrative Demo Case Study &bull; Not an actual client engagement.
            </div>
            <div class="mt-auto pt-2" style="border-top: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
              <a href="case-study-details.html" class="btn btn-outline btn-sm">Read Detailed Case Study &rarr;</a>
              <span style="font-size: 0.75rem; color: var(--secondary-text);">Conceptual Scenario</span>
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Case Studies</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Advisory Scenarios</span>
          <h1>Illustrative Management Consulting Case Studies.</h1>
          <p class="lead">Explore conceptual case studies demonstrating how our structured diagnostic methodologies analyze business friction, design operating frameworks, and guide organizational execution.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4" style="font-size: 0.85rem; padding: 1rem 1.25rem;">
          <strong>Authenticity Statement:</strong> In strict compliance with professional ethics, all case studies featured in this portfolio represent synthesized demonstration scenarios designed for educational and illustrative purposes. We do not fabricate real client names, company logos, confidential revenue metrics, or unverified statistical results.
        </div>

        <!-- Filter Tabs -->
        <div class="filter-tabs">
          <button class="filter-tab case-filter-tab active" data-filter="all">All Disciplines</button>
          <button class="filter-tab case-filter-tab" data-filter="strategy">Business Strategy</button>
          <button class="filter-tab case-filter-tab" data-filter="operations">Operational Excellence</button>
          <button class="filter-tab case-filter-tab" data-filter="org">Organizational Design</button>
          <button class="filter-tab case-filter-tab" data-filter="performance">Performance Systems</button>
          <button class="filter-tab case-filter-tab" data-filter="digital">Digital Transformation</button>
          <button class="filter-tab case-filter-tab" data-filter="change">Change Management</button>
        </div>

        <div class="card-grid-3">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("case-studies.html", "Illustrative Management Consulting Case Studies", "Explore illustrative case studies across business strategy, organizational development, operational excellence, and performance improvement.", body)

# ==============================================================================
# 24. CASE STUDY DETAILS: case-study-details.html
# ==============================================================================
def build_case_study_details():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li><a href="case-studies.html">Case Studies</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Case Study Deep Dive</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Illustrative Demonstration Scenario</span>
          <h1>Business Strategy &amp; Operational Alignment Demo</h1>
          <p class="lead">An in-depth conceptual case examination illustrating our diagnostic approach, strategic recommendations, and governance architecture.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4">
          <strong>Mandatory Demo Disclaimer:</strong> Illustrative Demo Case Study &bull; Not an actual client engagement. All figures, timelines, and corporate structures represent synthesized educational models.
        </div>

        <div class="hero-inner" style="align-items: start; margin-bottom: 3.5rem;">
          <div style="flex: 1.2;">
            <span class="section-eyebrow">Engagement Overview</span>
            <h2 class="section-title">Business Context &amp; Management Challenge</h2>
            <p><strong>Sector:</strong> Industrial Manufacturing &amp; Wholesale Distribution</p>
            <p><strong>Enterprise Profile:</strong> Multi-facility operation with 350+ employees experiencing steady top-line revenue expansion accompanied by sharp operating margin compression.</p>
            <p><strong>Primary Management Challenge:</strong> The enterprise had grown organically through acquisitions over a five-year period. However, operating units remained siloed, utilizing divergent production workflows, conflicting inventory systems, and overlapping management hierarchies. Key executives were spending excessive time resolving daily operational emergencies rather than executing strategic initiatives.</p>
          </div>
          <div style="flex: 0.8;">
            {make_placeholder("case-study-detailed-workspace.webp", "ratio-4x3", "Strategic Diagnosis Workshop", "1000x750px | Executive Review")}
          </div>
        </div>

        <!-- Consulting Objectives & Assessment Approach -->
        <div class="card-grid-2 mb-4">
          <div class="card">
            <h4 style="color: var(--primary-navy); margin-bottom: 0.75rem;">Consulting Objectives</h4>
            <ul style="font-size: 0.9rem; padding-left: 1.25rem; list-style: disc; color: var(--secondary-text); line-height: 1.7;">
              <li>Perform end-to-end diagnostic of core quote-to-fulfillment workflows</li>
              <li>Identify structural drivers of margin variance across product lines</li>
              <li>Redesign organizational reporting lines to eliminate approval bottlenecks</li>
              <li>Establish an executive KPI dashboard and monthly governance cadence</li>
            </ul>
          </div>

          <div class="card">
            <h4 style="color: var(--primary-navy); margin-bottom: 0.75rem;">Assessment Approach</h4>
            <ul style="font-size: 0.9rem; padding-left: 1.25rem; list-style: disc; color: var(--secondary-text); line-height: 1.7;">
              <li>Conducted 24 structured executive and plant manager interviews</li>
              <li>Audited 12 months of production log sheets, scrap rates, and overtime logs</li>
              <li>Mapped cross-facility value streams and identified 6 critical idle bottlenecks</li>
              <li>Analyzed departmental span of control across 4 managerial tiers</li>
            </ul>
          </div>
        </div>

        <!-- Diagnostic Findings & Strategic Recommendations -->
        <div class="card p-4 mb-4" style="background: #F8FAFC;">
          <h3 style="color: var(--primary-navy); margin-bottom: 1rem;">Diagnostic Findings &amp; Root Causes</h3>
          <p>The diagnostic phase revealed three interconnected root-cause friction points:</p>
          <div class="card-grid-3 mt-3">
            <div style="background: #FFFFFF; padding: 1.25rem; border-radius: var(--radius-sm); border-top: 3px solid #EF4444;">
              <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">1. Product Over-Proliferation</h5>
              <p style="font-size: 0.85rem; color: var(--secondary-text);">The firm offered 420+ custom SKUs, 40% of which generated less than 4% of gross revenue while driving 65% of plant changeover downtime.</p>
            </div>
            <div style="background: #FFFFFF; padding: 1.25rem; border-radius: var(--radius-sm); border-top: 3px solid #F59E0B;">
              <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">2. Triple-Tier Sign-Off Delays</h5>
              <p style="font-size: 0.85rem; color: var(--secondary-text);">Routine purchase orders required three separate managerial approvals, delaying material intake by an average of 4.5 days per order.</p>
            </div>
            <div style="background: #FFFFFF; padding: 1.25rem; border-radius: var(--radius-sm); border-top: 3px solid var(--accent-blue);">
              <h5 style="color: var(--primary-navy); margin-bottom: 0.5rem;">3. Siloed Inventory Buffers</h5>
              <p style="font-size: 0.85rem; color: var(--secondary-text);">Each regional facility hoarded independent safety stock due to lack of shared inventory visibility, inflating carrying costs.</p>
            </div>
          </div>
        </div>

        <!-- Strategic Recommendations & Implementation Roadmap -->
        <div class="section-header" style="margin-top: 4rem;">
          <span class="section-eyebrow">Remediation Architecture</span>
          <h2 class="section-title">Strategic Recommendations &amp; Implementation Roadmap</h2>
        </div>

        <div class="roadmap-flow">
          <div class="roadmap-phase active">
            <div class="phase-number">Phase 1 &bull; 30 Days</div>
            <div class="phase-title">Rationalization &amp; Quick Wins</div>
            <ul class="phase-items">
              <li>Prune bottom 25% unprofitable custom SKUs</li>
              <li>Institute single-manager approval threshold (&lt;$10,000)</li>
              <li>Launch weekly plant throughput standups</li>
            </ul>
          </div>

          <div class="roadmap-phase">
            <div class="phase-number">Phase 2 &bull; 60 Days</div>
            <div class="phase-title">Operating Model Redesign</div>
            <ul class="phase-items">
              <li>Centralize procurement across regional facilities</li>
              <li>Establish shared digital inventory visibility</li>
              <li>Publish standardized production SOP manuals</li>
            </ul>
          </div>

          <div class="roadmap-phase">
            <div class="phase-number">Phase 3 &bull; 90 Days</div>
            <div class="phase-title">Governance &amp; KPI Rollout</div>
            <ul class="phase-items">
              <li>Implement monthly executive performance review</li>
              <li>Calibrate balanced scorecard metrics</li>
              <li>Institutionalize ongoing SKU margin reviews</li>
            </ul>
          </div>

          <div class="roadmap-phase">
            <div class="phase-number">Ongoing</div>
            <div class="phase-title">Long-Term Resilience</div>
            <ul class="phase-items">
              <li>Quarterly board strategic horizon reviews</li>
              <li>Continuous capacity re-balancing</li>
              <li>Annual operating model health check</li>
            </ul>
          </div>
        </div>

        <!-- Lessons & Observations -->
        <div class="card mt-4" style="background: #FFFFFF; border-left: 4px solid var(--muted-gold);">
          <h4 style="margin-bottom: 0.5rem; color: var(--primary-navy);">Key Executive Lessons &amp; Observations</h4>
          <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 0.5rem;">1. <strong>Top-line growth often masks operational drag:</strong> Expanding volume without disciplined operating model standardization creates exponential complexity.</p>
          <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 0.5rem;">2. <strong>Product discipline protects margins:</strong> Pruning low-margin customizations typically improves total plant throughput without sacrificing high-value client relationships.</p>
          <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 0;">3. <strong>Clear decision rights eliminate delays:</strong> Simplifying approval thresholds empowers middle management and immediately reduces idle lead times.</p>
        </div>

        <div class="text-center mt-4">
          <a href="case-studies.html" class="btn btn-outline">&larr; Back to Case Study Gallery</a>
          <a href="book-consultation.html" class="btn btn-gold" style="margin-left: 0.75rem;">Discuss Your Organization's Scenario</a>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("case-study-details.html", "Illustrative Case Study Details: Strategic Alignment Demo", "In-depth conceptual case study demonstrating the diagnostic approach, root-cause findings, and implementation roadmap of a management consulting engagement.", body)

# ==============================================================================
# 25. TEAM: team.html
# ==============================================================================
def build_team():
    roles = [
        {"role": "Strategy Practice Lead", "focus": "Enterprise Strategy &amp; Capital Allocation", "bio": "Focuses on competitive market positioning, growth horizon planning, and strategic capital prioritization for enterprise leadership teams.", "image": "team-profile-strategy-lead.webp"},
        {"role": "Operations Practice Lead", "focus": "Operational Excellence &amp; Supply Chain", "bio": "Specializes in end-to-end workflow re-engineering, capacity modeling, and standard operating procedure institutionalization.", "image": "team-profile-operations-lead.webp"},
        {"role": "Organizational Development Lead", "focus": "Org Structure &amp; Role Architecture", "bio": "Advises executive teams on span of control optimization, RACI decision matrices, and departmental hierarchy redesign.", "image": "team-profile-org-lead.webp"},
        {"role": "Leadership Advisory Lead", "focus": "Executive Alignment &amp; Governance", "bio": "Guides CEOs and management boards through executive alignment protocols, decision rhythms, and succession frameworks.", "image": "team-profile-leadership-lead.webp"},
        {"role": "Business Transformation Lead", "focus": "Operating Model Modernization", "bio": "Leads complex enterprise transformation programs, change adoption architectures, and cross-functional project management offices.", "image": "team-profile-transformation-lead.webp"},
        {"role": "Performance Systems Lead", "focus": "KPI Architecture &amp; Analytics", "bio": "Specializes in balanced scorecard design, managerial accounting frameworks, and executive performance dashboard systems.", "image": "team-profile-performance-lead.webp"}
    ]

    cards_html = ""
    for r in roles:
        cards_html += f"""
        <div class="team-card">
          <div class="service-card-image">
            {make_placeholder(r["image"], "ratio-3x4", r["role"], "600x800px | Portrait")}
          </div>
          <div class="team-card-body">
            <span class="badge badge-demo mb-1">Demo Profile</span>
            <div class="team-card-role">{r["role"]}</div>
            <h3 class="team-card-title">{r["focus"]}</h3>
            <p class="team-card-desc">{r["bio"]}</p>
            <div class="team-card-focus">
              <strong>Core Capability:</strong> Advisory diagnostics, framework design, and executive workshop facilitation.
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Team</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Advisory Capabilities</span>
          <h1>Executive Leadership &amp; Advisory Capabilities.</h1>
          <p class="lead">Our practice brings together specialized management consulting capabilities across corporate strategy, operations, governance, organizational architecture, and performance improvement.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4">
          <strong>Authenticity Notice:</strong> In accordance with project identity standards, all team entries below represent generic role-based advisory capabilities. We do not invent fictitious individual names, educational degrees, previous corporate employers, or fabricated consultant biographies.
        </div>

        <div class="section-header">
          <span class="section-eyebrow">Practice Leadership</span>
          <h2 class="section-title">Functional Practice Leads</h2>
          <p class="section-subtitle">Structured role profiles outlining the specialized advisory disciplines that support our client engagements.</p>
        </div>

        <div class="card-grid-3">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("team.html", "Executive Leadership & Advisory Capabilities", "Learn about our generic role-based management consulting capabilities across strategy, operations, governance, and organizational development.", body)

# ==============================================================================
# 26. INSIGHTS: insights.html
# ==============================================================================
def build_insights():
    articles = [
        {"cat": "strategy", "cat_label": "Business Strategy", "time": "8 Min Read", "title": "How to Build a Practical Business Strategy", "desc": "Why most corporate strategies fail during execution, and how to construct actionable frameworks that align daily operational decisions with executive ambition.", "image": "insight-practical-strategy.webp"},
        {"cat": "management", "cat_label": "Management Advisory", "time": "6 Min Read", "title": "Common Management Challenges in Growing Organizations", "desc": "Analyzing the predictable operational and cultural bottlenecks that arise when headcounts double and legacy communication habits break down.", "image": "insight-growing-orgs.webp"},
        {"cat": "org", "cat_label": "Organizational Development", "time": "7 Min Read", "title": "Why Organizational Structure Matters", "desc": "An examination of how ambiguous reporting lines, redundant managerial layers, and misaligned incentives quietly strangle organizational productivity.", "image": "insight-org-structure.webp"},
        {"cat": "operations", "cat_label": "Operations Consulting", "time": "9 Min Read", "title": "How to Improve Operational Efficiency", "desc": "A systematic methodology for uncovering hidden process bottlenecks, eliminating non-value-adding manual steps, and establishing scalable SOPs.", "image": "insight-operational-efficiency.webp"},
        {"cat": "performance", "cat_label": "Performance Improvement", "time": "6 Min Read", "title": "Building Effective Performance Management Systems", "desc": "Moving beyond vanity metrics to construct balanced scorecards, transparent KPI cascades, and structured monthly management review cadences.", "image": "insight-performance-systems.webp"},
        {"cat": "change", "cat_label": "Change Management", "time": "8 Min Read", "title": "Managing Organizational Change Without Disrupting Operations", "desc": "How executive teams can overcome cultural resistance, protect customer fulfillment, and achieve high frontline adoption during major transitions.", "image": "insight-change-management.webp"},
        {"cat": "leadership", "cat_label": "Leadership Consulting", "time": "5 Min Read", "title": "How Leadership Alignment Supports Business Growth", "desc": "Why departmental conflict begins at the executive table, and how structured alignment protocols create decisive, unified leadership.", "image": "insight-leadership-alignment.webp"},
        {"cat": "transformation", "cat_label": "Business Transformation", "time": "10 Min Read", "title": "Developing a Business Transformation Roadmap", "desc": "A step-by-step guide to assessing digital readiness, redesigning core operating models, and governing multi-stage modernization programs.", "image": "insight-transformation-roadmap.webp"},
        {"cat": "operations", "cat_label": "Process Optimization", "time": "7 Min Read", "title": "Understanding Business Process Optimization", "desc": "Why automating broken workflows multiplies errors, and how value stream mapping reveals true opportunities for standard operating procedures.", "image": "insight-process-optimization.webp"},
        {"cat": "governance", "cat_label": "Corporate Governance", "time": "6 Min Read", "title": "How to Build Better Management Reporting", "desc": "Designing concise executive information systems that deliver actionable insights rather than overwhelming decision-makers with raw data.", "image": "insight-management-reporting.webp"}
    ]

    cards_html = ""
    for a in articles:
        cards_html += f"""
        <div class="article-card insight-card-item" data-category="{a["cat"]}">
          <div class="service-card-image">
            {make_placeholder(a["image"], "ratio-16x9", a["title"], "1000x562px")}
          </div>
          <div class="article-card-body">
            <div class="article-card-meta">
              <span class="badge badge-subtle">{a["cat_label"]}</span>
              <span>{a["time"]}</span>
            </div>
            <h3 class="article-card-title"><a href="article-details.html">{a["title"]}</a></h3>
            <p class="article-card-excerpt">{a["desc"]}</p>
            <div class="mt-auto pt-2" style="border-top: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
              <a href="article-details.html" class="btn btn-outline btn-sm">Read Article &rarr;</a>
              <span style="font-size: 0.75rem; color: var(--secondary-text);">Educational Insight</span>
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Insights</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Executive Thought Leadership</span>
          <h1>Management Insights &amp; Strategic Perspectives.</h1>
          <p class="lead">Research-backed perspectives, framework guides, and executive commentary on strategy execution, operating model redesign, and organizational performance.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <!-- Featured Article Banner -->
        <div class="card mb-4" style="padding: 2.5rem; background: linear-gradient(135deg, #FAFBFD 0%, #EEF4FA 100%); border-left: 5px solid var(--accent-blue);">
          <div class="hero-inner" style="align-items: center;">
            <div>
              <span class="badge badge-gold mb-1">Featured Research Piece</span>
              <h2 style="font-size: 2rem; margin-bottom: 0.75rem;"><a href="article-details.html">How to Build a Practical Business Strategy</a></h2>
              <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 1.5rem;">Corporate strategies often fail not from poor conceptualization, but because they remain isolated in slide decks disconnected from departmental resource budgets and daily operating choices. Read our comprehensive framework for linking executive ambition to operational reality.</p>
              <a href="article-details.html" class="btn btn-primary">Read Featured Article &rarr;</a>
            </div>
            <div>
              {make_placeholder("insight-featured-strategy-banner.webp", "ratio-16x9", "Featured Strategy Article", "1200x675px")}
            </div>
          </div>
        </div>

        <!-- Search & Filter Controls -->
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem;">
          <div class="filter-tabs" style="margin-bottom: 0;">
            <button class="filter-tab insight-filter-tab active" data-filter="all">All Topics</button>
            <button class="filter-tab insight-filter-tab" data-filter="strategy">Strategy</button>
            <button class="filter-tab insight-filter-tab" data-filter="operations">Operations</button>
            <button class="filter-tab insight-filter-tab" data-filter="org">Org Design</button>
            <button class="filter-tab insight-filter-tab" data-filter="leadership">Leadership</button>
            <button class="filter-tab insight-filter-tab" data-filter="performance">Performance</button>
            <button class="filter-tab insight-filter-tab" data-filter="change">Change</button>
          </div>

          <div class="search-box-wrap" style="margin-bottom: 0;">
            <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" class="search-input insights-search-input" placeholder="Search insights &amp; topics...">
          </div>
        </div>

        <!-- Articles Grid -->
        <div class="card-grid-3">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("insights.html", "Management Insights & Strategic Perspectives", "Editorial insights, research articles, and frameworks on business strategy, operational efficiency, leadership alignment, and change management.", body)

# ==============================================================================
# 27. ARTICLE DETAILS: article-details.html
# ==============================================================================
def build_article_details():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li><a href="insights.html">Insights</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">How to Build a Practical Business Strategy</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Business Strategy Practice</span>
          <h1>How to Build a Practical Business Strategy</h1>
          <p class="lead">Why most corporate strategies fail during execution, and how to construct actionable frameworks that align daily operational decisions with executive ambition.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div style="display: grid; grid-template-columns: 260px 1fr; gap: 3rem; align-items: start;">
          <!-- Left: Table of Contents & Metadata -->
          <aside style="position: sticky; top: 100px; background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.5rem;">
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted-gold); font-weight: 700; margin-bottom: 0.75rem;">Article Metadata</div>
            <p style="font-size: 0.85rem; margin-bottom: 0.35rem;"><strong>Category:</strong> Business Strategy</p>
            <p style="font-size: 0.85rem; margin-bottom: 0.35rem;"><strong>Reading Time:</strong> 8 Minutes</p>
            <p style="font-size: 0.85rem; margin-bottom: 1.25rem;"><strong>Audience:</strong> CEOs &amp; Managing Directors</p>
            
            <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--primary-navy); font-weight: 700; margin-bottom: 0.75rem; border-top: 1px solid var(--border-light); padding-top: 1rem;">Table of Contents</div>
            <ul style="font-size: 0.85rem; display: flex; flex-direction: column; gap: 0.5rem;">
              <li><a href="#toc-trap" style="color: var(--secondary-text);">The Strategic Execution Trap</a></li>
              <li><a href="#toc-foundations" style="color: var(--secondary-text);">Foundations of Pragmatic Strategy</a></li>
              <li><a href="#toc-framework" style="color: var(--secondary-text);">The 4-Part Strategic Framework</a></li>
              <li><a href="#toc-cascading" style="color: var(--secondary-text);">Cascading into Operations</a></li>
              <li><a href="#toc-governance" style="color: var(--secondary-text);">The Governance Cadence</a></li>
            </ul>

            <div class="mt-4 pt-3" style="border-top: 1px solid var(--border-light);">
              <a href="book-consultation.html" class="btn btn-gold btn-sm" style="width: 100%;">Discuss Strategy</a>
            </div>
          </aside>

          <!-- Right: Article Body Content -->
          <article>
            <div style="margin-bottom: 2rem;">
              {make_placeholder("insight-article-detail-visual.webp", "ratio-16x9", "Strategic Planning Environment", "1200x675px")}
            </div>

            <section id="toc-trap" class="mb-4">
              <h2 style="font-size: 1.85rem; margin-bottom: 1rem;">1. The Strategic Execution Trap</h2>
              <p>Every year, leadership teams invest hundreds of hours developing multi-year corporate strategy decks. Yet surveys across international management research consistently reveal that over 65% of well-formulated strategies fail to produce their intended business outcomes.</p>
              <p>The failure rarely stems from a lack of market ambition or intellectual horsepower. Rather, it occurs because traditional strategic plans remain detached from the daily realities of operational execution. When frontline managers are confronted with competing daily fires and vague quarterly mandates, they default to legacy operating habits. Without structured alignment mechanisms, strategy quickly evaporates into corporate rhetoric.</p>
            </section>

            <section id="toc-foundations" class="mb-4">
              <h2 style="font-size: 1.85rem; margin-bottom: 1rem;">2. Foundations of Pragmatic Strategy</h2>
              <p>A practical business strategy is not a wishlist of aspirational goals. It is a disciplined set of choices regarding what the organization will—and critically, what it will <em>not</em>—do. To deliver real commercial advantage, a strategy must satisfy three foundational tests:</p>
              <ul style="padding-left: 1.25rem; list-style: disc; margin: 1rem 0; color: var(--secondary-text); line-height: 1.7;">
                <li><strong>Clear Differentiation:</strong> Unambiguous clarity on why clients choose your organization over competitors in a defined market space.</li>
                <li><strong>Operational Feasibility:</strong> Strict alignment with actual organizational capability, capital reserves, and managerial bandwidth.</li>
                <li><strong>Explicit Trade-offs:</strong> Willingness to abandon unprofitable product extensions, non-core service lines, or distracting commercial ventures.</li>
              </ul>
            </section>

            <section id="toc-framework" class="mb-4">
              <h2 style="font-size: 1.85rem; margin-bottom: 1rem;">3. The Four-Part Strategic Decision Framework</h2>
              <p>To bridge the divide between high-level ambition and operational realities, we recommend organizing strategic choices around four structured pillars:</p>
              
              <div class="dashboard-container" style="margin: 1.5rem 0;">
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.25rem;">
                  <div style="background: #F8FAFC; padding: 1.25rem; border-left: 4px solid var(--accent-blue);">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.35rem;">Pillar 1: Where to Play</h4>
                    <p style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 0;">Target customer segments, geographic boundaries, and market niches where your firm holds a structural efficiency or quality advantage.</p>
                  </div>
                  <div style="background: #F8FAFC; padding: 1.25rem; border-left: 4px solid var(--muted-gold);">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.35rem;">Pillar 2: How to Win</h4>
                    <p style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 0;">The specific value proposition, pricing structure, and service delivery model that sets your offering apart from alternatives.</p>
                  </div>
                  <div style="background: #F8FAFC; padding: 1.25rem; border-left: 4px solid var(--primary-navy);">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.35rem;">Pillar 3: Capabilities Required</h4>
                    <p style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 0;">The institutional skills, technologies, and workflow standards that must be built or modernized to execute the value proposition.</p>
                  </div>
                  <div style="background: #F8FAFC; padding: 1.25rem; border-left: 4px solid #10B981;">
                    <h4 style="font-size: 1.05rem; margin-bottom: 0.35rem;">Pillar 4: Management Systems</h4>
                    <p style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 0;">The review cadences, KPIs, and accountability structures that measure progress and govern milestone compliance.</p>
                  </div>
                </div>
              </div>
            </section>

            <section id="toc-cascading" class="mb-4">
              <h2 style="font-size: 1.85rem; margin-bottom: 1rem;">4. Cascading Strategy into Operations</h2>
              <p>Once executive consensus is achieved on the core pillars, the strategy must be translated into departmental milestones. This is achieved through the creation of 90-day initiative portfolios:</p>
              <p>Every strategic initiative must possess an unambiguous executive owner, a quantitative target metric, and a defined list of cross-departmental dependencies. If an initiative lacks a named individual accountable for delivery, it is merely a corporate aspiration.</p>
            </section>

            <section id="toc-governance" class="mb-4">
              <h2 style="font-size: 1.85rem; margin-bottom: 1rem;">5. The Governance Cadence</h2>
              <p>Finally, no strategy survives without a disciplined governance rhythm. Executive committees should separate weekly operational firefighting meetings from monthly strategic variance reviews.</p>
              <p>During the monthly review, leadership examines whether agreed strategic milestones were hit, analyzes root causes for slippage, and recalibrates resources. By treating strategy as an ongoing management operating rhythm rather than an annual event, organizations turn strategic ambition into tangible commercial results.</p>
            </section>

            <!-- Related Articles -->
            <div style="border-top: 1px solid var(--border-color); padding-top: 2rem; margin-top: 3rem;">
              <h4 style="margin-bottom: 1rem;">Related Management Reading</h4>
              <div class="card-grid-2">
                <div class="card" style="padding: 1.25rem;">
                  <span class="badge badge-subtle mb-1">Organizational Design</span>
                  <h5 style="margin-bottom: 0.35rem;"><a href="insights.html">Why Organizational Structure Matters</a></h5>
                  <p style="font-size: 0.8rem; margin-bottom: 0;">How ambiguous reporting lines silently sabotage strategy execution.</p>
                </div>
                <div class="card" style="padding: 1.25rem;">
                  <span class="badge badge-subtle mb-1">Operations</span>
                  <h5 style="margin-bottom: 0.35rem;"><a href="insights.html">How to Improve Operational Efficiency</a></h5>
                  <p style="font-size: 0.8rem; margin-bottom: 0;">Systematic value stream re-engineering to remove friction.</p>
                </div>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("article-details.html", "How to Build a Practical Business Strategy", "Learn how to build an actionable business strategy that bridges the gap between executive vision and frontline operational execution.", body)

# ==============================================================================
# 28. RESOURCES: resources.html
# ==============================================================================
def build_resources():
    resources_list = [
        {"cat": "Strategy", "title": "Business Strategy Planning Checklist", "desc": "A 10-point diagnostic checklist evaluating strategic alignment, competitive positioning, and capital trade-offs.", "image": "resource-strategy-checklist.webp"},
        {"cat": "Management", "title": "Management Assessment Checklist", "desc": "Executive evaluation guide assessing decision-making velocity, managerial meeting hygiene, and accountability structures.", "image": "resource-management-checklist.webp"},
        {"cat": "Organization", "title": "Organizational Structure Review Template", "desc": "Diagnostic worksheet for mapping reporting lines, span of control ratios, and role duplication across business units.", "image": "resource-org-review.webp"},
        {"cat": "Performance", "title": "Business Performance Dashboard Template", "desc": "Executive layout framework integrating financial metrics, operational velocity, and governance variance scorecards.", "image": "resource-performance-template.webp"},
        {"cat": "Operations", "title": "Process Optimization Checklist", "desc": "Step-by-step workflow audit guide for identifying idle queues, redundant handoffs, and automation opportunities.", "image": "resource-process-checklist.webp"},
        {"cat": "Change", "title": "Change Management Planning Template", "desc": "Stakeholder impact mapping matrix and communication architecture for enterprise operating model shifts.", "image": "resource-change-template.webp"},
        {"cat": "Leadership", "title": "Leadership Alignment Checklist", "desc": "Executive team assessment protocol ensuring shared strategic priorities, unified messaging, and decision rights clarity.", "image": "resource-leadership-checklist.webp"},
        {"cat": "Transformation", "title": "Business Transformation Roadmap", "desc": "Phased 4-horizon execution blueprint outlining discovery, target architecture, pilot launch, and enterprise scaling.", "image": "resource-transformation-roadmap.webp"},
        {"cat": "Risk", "title": "Risk Assessment Worksheet", "desc": "5x5 Likelihood vs. Impact scoring framework for categorizing operational, strategic, and technological enterprise risks.", "image": "resource-risk-worksheet.webp"},
        {"cat": "Governance", "title": "Project Governance Checklist", "desc": "Project Management Office (PMO) milestone audit tool tracking scope variation, dependency friction, and delivery SLAs.", "image": "resource-project-checklist.webp"}
    ]

    cards_html = ""
    for r in resources_list:
        cards_html += f"""
        <div class="resource-card">
          <div class="service-card-image">
            {make_placeholder(r["image"], "ratio-16x9", r["title"], "1000x562px")}
          </div>
          <div class="resource-card-body">
            <span class="resource-card-tag">{r["cat"]} Framework</span>
            <h3 class="resource-card-title">{r["title"]}</h3>
            <p class="resource-card-desc">{r["desc"]}</p>
            <div class="mt-auto pt-2" style="border-top: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center;">
              <span class="badge badge-subtle">Demo Preview</span>
              <a href="book-consultation.html" class="btn btn-outline btn-sm">Enquire on Framework &rarr;</a>
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Resources</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Advisory Framework Library</span>
          <h1>Management Frameworks, Checklists &amp; Templates.</h1>
          <p class="lead">A curated repository of practical management tools, diagnostic worksheets, and governance templates developed to assist business leaders in structuring complex organizational decisions.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4">
          <strong>Resource Library Notice:</strong> These preview resources represent synthesized advisory frameworks utilized during client engagements. In accordance with static hosting design standards, previews are displayed below for conceptual review rather than simulated download links.
        </div>

        <div class="card-grid-3">
          {cards_html}
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("resources.html", "Management Consulting Resources & Framework Library", "Explore practical management consulting checklists, diagnostic worksheets, and operating templates for business leaders.", body)

# ==============================================================================
# 29. PRICING: pricing.html
# ==============================================================================
def build_pricing():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Engagement Models</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Transparent Advisory Scoping</span>
          <h1>Structured Consulting Engagement Models.</h1>
          <p class="lead">We tailor consulting engagements to your organization's specific scale, operational complexity, and strategic objectives through clear, structured engagement models.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4" style="font-size: 0.85rem; padding: 1rem 1.25rem;">
          <strong>Pricing Disclosure:</strong> Final consulting fees depend on business complexity, engagement scope, duration, expertise required, and agreed deliverables. We provide bespoke engagement proposals following an initial confidential discovery consultation.
        </div>

        <div class="section-header text-center">
          <span class="section-eyebrow">Engagement Options</span>
          <h2 class="section-title">Three Illustrative Engagement Models</h2>
          <p class="section-subtitle">Select the advisory model that best aligns with your organization's current priorities and operational timeline.</p>
        </div>

        <div class="card-grid-3">
          <!-- Model 1 -->
          <div class="card">
            <span class="badge badge-subtle mb-1">Model 01</span>
            <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem;">Management Assessment</h3>
            <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.25rem;">A focused diagnostic review designed to identify operational bottlenecks, evaluate organizational structure, and establish baseline strategic priorities.</p>
            <div style="background: #F8FAFC; padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1.25rem;">
              <strong style="color: var(--primary-navy); display: block; font-size: 0.85rem;">Typical Duration:</strong>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">2 to 4 Weeks</span>
            </div>
            <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text); line-height: 1.7; margin-bottom: 1.5rem;">
              <li>Executive stakeholder interviews</li>
              <li>Core workflow &amp; SOP diagnostic audit</li>
              <li>Organizational structure review</li>
              <li>Quantified Opportunity Matrix</li>
              <li>Executive Findings Presentation</li>
            </ul>
            <div class="mt-auto">
              <a href="book-consultation.html" class="btn btn-outline" style="width: 100%;">Request Proposal &rarr;</a>
            </div>
          </div>

          <!-- Model 2 -->
          <div class="card" style="border: 2px solid var(--accent-blue); position: relative; box-shadow: var(--shadow-md);">
            <div style="position: absolute; top: -12px; right: 20px; background: var(--accent-blue); color: #FFFFFF; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; padding: 0.2rem 0.6rem; border-radius: var(--radius-sm);">Most Requested</div>
            <span class="badge badge-gold mb-1">Model 02</span>
            <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem;">Focused Consulting</h3>
            <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.25rem;">Deep-dive consulting focused on solving a specific organizational challenge, such as process optimization, KPI design, or structural realignment.</p>
            <div style="background: #F8FAFC; padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1.25rem;">
              <strong style="color: var(--primary-navy); display: block; font-size: 0.85rem;">Typical Duration:</strong>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">6 to 10 Weeks</span>
            </div>
            <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text); line-height: 1.7; margin-bottom: 1.5rem;">
              <li>Everything in Management Assessment</li>
              <li>Target Operating Model architecture</li>
              <li>RACI decision matrices &amp; role charters</li>
              <li>Process re-engineering &amp; new SOPs</li>
              <li>Detailed 90-Day Execution Roadmap</li>
              <li>Executive workshop facilitation</li>
            </ul>
            <div class="mt-auto">
              <a href="book-consultation.html" class="btn btn-gold" style="width: 100%;">Request Proposal &rarr;</a>
            </div>
          </div>

          <!-- Model 3 -->
          <div class="card">
            <span class="badge badge-subtle mb-1">Model 03</span>
            <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem;">Strategic Transformation</h3>
            <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.25rem;">Comprehensive enterprise transformation supporting end-to-end organizational redesign, operating model overhaul, and multi-quarter implementation governance.</p>
            <div style="background: #F8FAFC; padding: 1rem; border-radius: var(--radius-sm); margin-bottom: 1.25rem;">
              <strong style="color: var(--primary-navy); display: block; font-size: 0.85rem;">Typical Duration:</strong>
              <span style="font-size: 0.85rem; color: var(--secondary-text);">3 to 6+ Months</span>
            </div>
            <ul style="font-size: 0.85rem; padding-left: 1rem; list-style: disc; color: var(--secondary-text); line-height: 1.7; margin-bottom: 1.5rem;">
              <li>Full-scope enterprise diagnostic &amp; strategy</li>
              <li>Cross-functional operating model overhaul</li>
              <li>Transformation Management Office (TMO)</li>
              <li>Change management &amp; adoption enablement</li>
              <li>Bi-weekly milestone governance &amp; coaching</li>
              <li>Ongoing post-rollout performance reviews</li>
            </ul>
            <div class="mt-auto">
              <a href="book-consultation.html" class="btn btn-primary" style="width: 100%;">Request Proposal &rarr;</a>
            </div>
          </div>
        </div>

        <!-- Comparison Table -->
        <div class="section-header" style="margin-top: 4.5rem;">
          <span class="section-eyebrow">Engagement Comparison</span>
          <h2 class="section-title">Scope &amp; Deliverables Comparison Table</h2>
        </div>

        <div class="comparison-table-wrapper">
          <table class="comparison-table" aria-label="Consulting Engagement Models Comparison">
            <thead>
              <tr>
                <th style="width: 35%;">Consulting Deliverables &amp; Activities</th>
                <th style="width: 20%;">Management Assessment</th>
                <th class="highlight" style="width: 25%;">Focused Consulting</th>
                <th style="width: 20%;">Strategic Transformation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Executive Leadership Interviews</td>
                <td>Included</td>
                <td class="highlight">Included</td>
                <td>Included</td>
              </tr>
              <tr>
                <td>Current State Workflow &amp; SOP Audit</td>
                <td>High-level review</td>
                <td class="highlight">Detailed value stream audit</td>
                <td>End-to-end cross-functional audit</td>
              </tr>
              <tr>
                <td>Organizational Span of Control Review</td>
                <td>Included</td>
                <td class="highlight">Included</td>
                <td>Included</td>
              </tr>
              <tr>
                <td>RACI Decision Rights Charters</td>
                <td>Optional add-on</td>
                <td class="highlight">Included</td>
                <td>Included</td>
              </tr>
              <tr>
                <td>Target Operating Model (TOM) Design</td>
                <td>Recommendations only</td>
                <td class="highlight">Full architecture blueprint</td>
                <td>Enterprise multi-unit architecture</td>
              </tr>
              <tr>
                <td>Process Standardization Manuals</td>
                <td>Gap analysis only</td>
                <td class="highlight">Included for focus area</td>
                <td>Comprehensive SOP suite</td>
              </tr>
              <tr>
                <td>Implementation Roadmap Architecture</td>
                <td>High-level priorities</td>
                <td class="highlight">Phased 90-day plan</td>
                <td>Multi-horizon master roadmap</td>
              </tr>
              <tr>
                <td>Governance &amp; PMO Support</td>
                <td>Not included</td>
                <td class="highlight">Milestone check-ins</td>
                <td>Active PMO chairing &amp; reviews</td>
              </tr>
              <tr>
                <td>Change Management Enablement</td>
                <td>Not included</td>
                <td class="highlight">Core adoption kit</td>
                <td>Full stakeholder &amp; change program</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("pricing.html", "Consulting Engagement Models & Scope Presentation", "Explore our structured management consulting engagement models: Management Assessment, Focused Consulting, and Strategic Transformation.", body)

# ==============================================================================
# 30. FAQ: faq.html
# ==============================================================================
def build_faq():
    faqs = [
        {"q": "What does a management consulting company do?", "a": "A management consulting company helps business owners, CEOs, and executive directors identify operational bottlenecks, clarify strategic direction, design effective organizational structures, and implement disciplined governance rhythms that drive sustainable performance."},
        {"q": "How can management consulting help a business?", "a": "Management consulting provides objective, data-backed diagnostic clarity free from internal corporate politics. It helps leadership teams resolve margin leaks, eliminate redundant approval layers, align cross-departmental priorities, and install reliable management reporting systems."},
        {"q": "What types of management challenges can be addressed?", "a": "Our practices address a broad spectrum of enterprise challenges, including strategic drift, declining operating margins, workflow bottlenecks, organizational role ambiguity, high employee turnover, failed digital tool adoption, and premature expansion risks."},
        {"q": "Do you work with small and medium-sized businesses?", "a": "Yes. While we advise mid-market and enterprise corporations, our structured frameworks are frequently deployed for ambitious small and medium-sized enterprises (SMEs) reaching inflection points where founder-led improvisation must transition to institutional management systems."},
        {"q": "Can you help develop a business strategy?", "a": "Yes. Our Business Strategy and Strategic Planning practices work closely with executive teams to assess competitive differentiation, prioritize market opportunities, make disciplined capital trade-offs, and construct actionable 90-day execution roadmaps."},
        {"q": "Do you provide organizational development consulting?", "a": "Yes. We evaluate organizational reporting hierarchies, assess managerial span of control, design RACI decision rights charters, and streamline functional handoffs to eliminate bottlenecks and empower team accountability."},
        {"q": "Can you review business processes?", "a": "Yes. Our Operations and Process Optimization practices map end-to-end value streams to uncover idle queues, duplicate manual data entry, and procedural friction, establishing standardized operating procedures that improve turnaround times."},
        {"q": "Do you support business transformation?", "a": "Yes. We guide organizations through Target Operating Model (TOM) redesigns, technology modernization roadmaps, and stakeholder change enablement to ensure major structural transitions achieve sustainable frontline adoption."},
        {"q": "How does a consulting engagement begin?", "a": "Engagements begin with an initial confidential consultation where we discuss your organization's core challenges, current operating context, and desired outcomes. Following this discussion, we construct a tailored engagement proposal detailing scope, timeline, deliverables, and fees."},
        {"q": "What information is needed for an assessment?", "a": "Typical discovery intake includes current organizational charts, recent financial performance summaries, existing SOP manuals, departmental KPI reports, and access to key leadership stakeholders for structured 45-minute diagnostic interviews."},
        {"q": "How long does a consulting engagement take?", "a": "Engagement durations depend on scope: a focused Management Assessment typically spans 2 to 4 weeks; a targeted Focused Consulting engagement runs 6 to 10 weeks; and complex Strategic Transformations run 3 to 6+ months with ongoing governance support."},
        {"q": "How are consulting fees calculated?", "a": "Fees are structured around clear deliverables and milestone scopes rather than unpredictable hourly billing. Final fees depend on organizational complexity, required specialist capabilities, duration, and whether active implementation governance support is requested."},
        {"q": "Do you support implementation?", "a": "Yes. Where scoped in our advisory models, Stage 5 (Support) provides hands-on Project Management Office (PMO) facilitation, bi-weekly milestone reviews, executive coaching, and continuous optimization adjustments during rollout."},
        {"q": "Can consulting services be customized?", "a": "Every consulting engagement is tailored to your organization's specific commercial realities, industry regulatory requirements, and resource availability while adhering to our disciplined five-stage methodology."}
    ]

    faq_html = ""
    for i, item in enumerate(faqs):
        faq_html += f"""
        <div class="faq-item {'is-open' if i == 0 else ''}">
          <button class="faq-question" aria-expanded="{'true' if i == 0 else 'false'}">
            <span>{item["q"]}</span>
            <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </button>
          <div class="faq-answer">
            <p>{item["a"]}</p>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">FAQ</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Executive Advisory Inquiries</span>
          <h1>Frequently Asked Questions.</h1>
          <p class="lead">Clear answers to common questions regarding management consulting practices, methodology, engagement scoping, and implementation support.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container container-narrow">
        <div class="section-header text-center">
          <span class="section-eyebrow">Advisory Clarifications</span>
          <h2 class="section-title">Frequently Asked Questions</h2>
          <p class="section-subtitle">Click any question below to inspect detailed explanations of our consulting approach and operational deliverables.</p>
        </div>

        <div class="faq-list">
          {faq_html}
        </div>

        <div class="card mt-4 p-4 text-center" style="background: #F8FAFC;">
          <h4 style="margin-bottom: 0.5rem;">Have a Specific Management Question Not Covered Above?</h4>
          <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.25rem;">Our advisory practice leads are available for initial confidential discovery discussions.</p>
          <a href="contact.html" class="btn btn-primary">Contact Advisory Office</a>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("faq.html", "Frequently Asked Questions: Management Consulting Practice", "Read frequently asked questions regarding our management consulting services, methodologies, pricing models, and implementation support.", body)

# ==============================================================================
# 31. CONTACT: contact.html
# ==============================================================================
def build_contact():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Contact</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Executive Advisory Office</span>
          <h1>Let's Discuss Your Organization's Next Challenge.</h1>
          <p class="lead">Connect with our management consulting practice to explore how our structured diagnostics and strategic advisory frameworks can assist your leadership team.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4">
          <strong>Demonstration Environment Notice:</strong> All contact information provided on this page represents placeholder demonstration data. Form submissions are validated and processed in frontend demonstration mode; no information is transmitted or stored on remote servers.
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1.35fr; gap: 3.5rem; align-items: start;">
          <!-- Left: Contact Details -->
          <div>
            <span class="section-eyebrow">Advisory Office</span>
            <h2 class="section-title">Confidential Executive Contact</h2>
            <p style="margin-bottom: 2rem;">We welcome inquiries from CEOs, business owners, managing directors, and senior corporate executives looking to evaluate management advisory engagements.</p>

            <div style="background: #FFFFFF; border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.75rem; margin-bottom: 1.75rem;">
              <h4 style="font-size: 1rem; color: var(--primary-navy); margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Office Coordinates</h4>
              
              <div class="footer-contact-item" style="color: var(--main-text); margin-bottom: 1rem;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                <div>
                  <div style="font-weight: 600;">Telephone Inquiries</div>
                  <div style="font-size: 0.85rem; color: var(--secondary-text);">Primary: 0000000000</div>
                  <div style="font-size: 0.85rem; color: var(--secondary-text);">Alternative: 0000000000</div>
                </div>
              </div>

              <div class="footer-contact-item" style="color: var(--main-text); margin-bottom: 1rem;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                <div>
                  <div style="font-weight: 600;">Executive Email</div>
                  <div style="font-size: 0.85rem; color: var(--secondary-text);"><a href="mailto:demo@example.com">demo@example.com</a></div>
                </div>
              </div>

              <div class="footer-contact-item" style="color: var(--main-text); margin-bottom: 1rem;">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                <div>
                  <div style="font-weight: 600;">Demonstration Office Address</div>
                  <div style="font-size: 0.85rem; color: var(--secondary-text);">Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000, India</div>
                </div>
              </div>

              <div class="footer-contact-item" style="color: var(--main-text);">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                <div>
                  <div style="font-weight: 600;">Practice Working Hours</div>
                  <div style="font-size: 0.85rem; color: var(--secondary-text);">Monday &ndash; Saturday: 9:00 AM &ndash; 6:00 PM IST</div>
                </div>
              </div>
            </div>

            <div class="card p-3" style="background: #F8FAFC;">
              <span class="badge badge-gold mb-1">Interactive Wizard</span>
              <h4 style="font-size: 1rem; margin-bottom: 0.35rem;">Prefer a Structured Scoping Process?</h4>
              <p style="font-size: 0.85rem; margin-bottom: 0.75rem;">Complete our multi-step consultation enquiry to submit detailed organizational parameters.</p>
              <a href="book-consultation.html" class="btn btn-gold btn-sm">Open Multi-Step Wizard &rarr;</a>
            </div>
          </div>

          <!-- Right: Interactive Contact Form -->
          <div class="card" style="padding: 2.5rem; box-shadow: var(--shadow-md);">
            <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Advisory Inquiry Form</h3>
            <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.75rem;">Please provide high-level context regarding your organization and current management challenge.</p>

            <form id="general-contact-form" novalidate>
              <div class="form-row">
                <div class="form-group">
                  <label for="contact-name">Full Name <span class="required">*</span></label>
                  <input type="text" id="contact-name" class="form-control" placeholder="Executive Name">
                </div>
                <div class="form-group">
                  <label for="contact-email">Corporate Email <span class="required">*</span></label>
                  <input type="email" id="contact-email" class="form-control" placeholder="name@company.com">
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="contact-phone">Phone Number <span class="required">*</span></label>
                  <input type="tel" id="contact-phone" class="form-control" placeholder="Direct Contact Number">
                </div>
                <div class="form-group">
                  <label for="contact-org">Organization Name <span class="required">*</span></label>
                  <input type="text" id="contact-org" class="form-control" placeholder="Company / Enterprise Name">
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="contact-industry">Industry Sector</label>
                  <select id="contact-industry" class="form-control">
                    <option value="">Select Industry</option>
                    <option value="Manufacturing">Manufacturing</option>
                    <option value="Healthcare">Healthcare</option>
                    <option value="Technology">Technology &amp; Software</option>
                    <option value="Logistics">Logistics &amp; Supply Chain</option>
                    <option value="Retail">Retail &amp; Consumer Goods</option>
                    <option value="Education">Education</option>
                    <option value="Financial">Financial Services</option>
                    <option value="Other">Other Sector</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="contact-designation">Executive Designation</label>
                  <input type="text" id="contact-designation" class="form-control" placeholder="e.g. CEO, MD, VP Operations">
                </div>
              </div>

              <div class="form-group">
                <label for="contact-service">Consulting Service Required</label>
                <select id="contact-service" class="form-control">
                  <option value="General Strategic Advisory">General Strategic Advisory</option>
                  <option value="Business Strategy">Business Strategy</option>
                  <option value="Operations Consulting">Operations Consulting</option>
                  <option value="Organizational Development">Organizational Development</option>
                  <option value="Performance Improvement">Performance Improvement</option>
                  <option value="Change Management">Change Management</option>
                  <option value="Business Transformation">Business Transformation</option>
                </select>
              </div>

              <div class="form-group">
                <label for="contact-message">Brief Description of the Business Challenge <span class="required">*</span></label>
                <textarea id="contact-message" class="form-control" rows="4" placeholder="Summarize your organization's primary inflection point or operational bottleneck..."></textarea>
              </div>

              <div class="form-group">
                <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">Submit Demonstration Inquiry</button>
              </div>
              <div style="font-size: 0.75rem; color: var(--secondary-text); text-align: center;">
                Frontend demo simulation only &bull; No personal information is stored or transmitted.
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("contact.html", "Let's Discuss Your Organization's Next Challenge", "Contact our management consulting practice to discuss business strategy, operations, governance, or organizational development.", body)

# ==============================================================================
# 32. BOOK CONSULTATION: book-consultation.html
# ==============================================================================
def build_book_consultation():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Book a Consultation</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Executive Advisory Scoping</span>
          <h1>Start With a Conversation. Build a Clearer Business Direction.</h1>
          <p class="lead">Complete our structured multi-step inquiry to outline your organization's management challenge and schedule an initial confidential advisory discussion.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container container-narrow">
        <div class="case-demo-notice mb-4">
          <strong>Demonstration Application:</strong> This multi-step wizard simulates the executive consultation scoping workflow. It operates entirely on the frontend without connecting to live calendars, external APIs, or database storage.
        </div>

        <div class="wizard-container">
          <!-- Wizard Progress Bar Header -->
          <div class="wizard-progress">
            <div class="wizard-steps-indicator">
              <div class="wizard-step-node active" data-step-target="1">
                <div class="node-circle">1</div>
                <div class="node-title">Contact</div>
              </div>
              <div class="wizard-step-node" data-step-target="2">
                <div class="node-circle">2</div>
                <div class="node-title">Organization</div>
              </div>
              <div class="wizard-step-node" data-step-target="3">
                <div class="node-circle">3</div>
                <div class="node-title">Challenge</div>
              </div>
              <div class="wizard-step-node" data-step-target="4">
                <div class="node-circle">4</div>
                <div class="node-title">Outcomes</div>
              </div>
              <div class="wizard-step-node" data-step-target="5">
                <div class="node-circle">5</div>
                <div class="node-title">Schedule</div>
              </div>
              <div class="wizard-step-node" data-step-target="6">
                <div class="node-circle">6</div>
                <div class="node-title">Review</div>
              </div>
            </div>
          </div>

          <!-- Wizard Body -->
          <div class="wizard-content">
            <!-- STEP 1: Contact Information -->
            <div class="wizard-step-pane active" data-step="1">
              <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Step 1: Executive Contact Information</h3>
              <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.75rem;">Please provide your direct executive contact coordinates for our practice office.</p>

              <div class="form-row">
                <div class="form-group">
                  <label for="wizard-name">Full Name <span class="required">*</span></label>
                  <input type="text" id="wizard-name" class="form-control" placeholder="Executive Full Name">
                </div>
                <div class="form-group">
                  <label for="wizard-email">Corporate Email <span class="required">*</span></label>
                  <input type="email" id="wizard-email" class="form-control" placeholder="name@company.com">
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="wizard-phone">Direct Phone <span class="required">*</span></label>
                  <input type="tel" id="wizard-phone" class="form-control" placeholder="+91 0000000000">
                </div>
                <div class="form-group">
                  <label for="wizard-org">Organization Name <span class="required">*</span></label>
                  <input type="text" id="wizard-org" class="form-control" placeholder="Company Name">
                </div>
              </div>
            </div>

            <!-- STEP 2: Organization Details -->
            <div class="wizard-step-pane" data-step="2">
              <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Step 2: Organization Scale &amp; Stage</h3>
              <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.75rem;">Understanding your enterprise size and business stage helps us assign the relevant practice lead.</p>

              <div class="form-row">
                <div class="form-group">
                  <label for="wizard-industry">Primary Industry <span class="required">*</span></label>
                  <select id="wizard-industry" class="form-control">
                    <option value="">Select Industry</option>
                    <option value="Manufacturing">Manufacturing</option>
                    <option value="Healthcare">Healthcare &amp; Life Sciences</option>
                    <option value="Technology">Technology &amp; Software (SaaS)</option>
                    <option value="Logistics">Logistics &amp; Supply Chain</option>
                    <option value="Retail">Retail &amp; Consumer Goods</option>
                    <option value="Education">Education</option>
                    <option value="Financial">Financial Services</option>
                    <option value="Professional Services">Professional Services</option>
                    <option value="Other">Other Enterprise Sector</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="wizard-org-size">Organization Size (Headcount) <span class="required">*</span></label>
                  <select id="wizard-org-size" class="form-control">
                    <option value="">Select Size</option>
                    <option value="1-50 Employees">1 &ndash; 50 Employees (Emerging)</option>
                    <option value="51-200 Employees">51 &ndash; 200 Employees (Mid-Market)</option>
                    <option value="201-1000 Employees">201 &ndash; 1,000 Employees (Growth Enterprise)</option>
                    <option value="1000+ Employees">1,000+ Employees (Large Corporate)</option>
                  </select>
                </div>
              </div>

              <div class="form-row">
                <div class="form-group">
                  <label for="wizard-org-stage">Business Growth Stage <span class="required">*</span></label>
                  <select id="wizard-org-stage" class="form-control">
                    <option value="">Select Stage</option>
                    <option value="Scaling & Expansion">Rapid Scaling &amp; Expansion</option>
                    <option value="Mature & Optimizing">Mature &bull; Operating Model Optimization</option>
                    <option value="Restructuring & Turnaround">Restructuring &bull; Margin Recovery</option>
                    <option value="Digital Transformation">Digital / Operational Transformation</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="wizard-designation">Your Executive Designation <span class="required">*</span></label>
                  <input type="text" id="wizard-designation" class="form-control" placeholder="e.g. CEO, Managing Director, COO">
                </div>
              </div>
            </div>

            <!-- STEP 3: Management Challenge -->
            <div class="wizard-step-pane" data-step="3">
              <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Step 3: Management Challenge Area</h3>
              <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.75rem;">Select all operational and strategic areas that apply to your current organizational inflection point:</p>

              <div class="option-tiles-grid">
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Business Strategy">
                  <div>
                    <span class="option-tile-title">Business Strategy</span>
                    <span class="option-tile-desc">Market positioning &amp; growth priorities</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Leadership Alignment">
                  <div>
                    <span class="option-tile-title">Leadership Alignment</span>
                    <span class="option-tile-desc">Executive decision clarity &amp; consensus</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Organizational Structure">
                  <div>
                    <span class="option-tile-title">Organizational Structure</span>
                    <span class="option-tile-desc">Role clarity, RACI &amp; reporting lines</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Operational Efficiency">
                  <div>
                    <span class="option-tile-title">Operational Efficiency</span>
                    <span class="option-tile-desc">Bottlenecks, throughput &amp; SOP standards</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Performance Improvement">
                  <div>
                    <span class="option-tile-title">Performance Improvement</span>
                    <span class="option-tile-desc">KPI architecture &amp; management cadence</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Change Management">
                  <div>
                    <span class="option-tile-title">Change Management</span>
                    <span class="option-tile-desc">Adoption &amp; transition enablement</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Digital Transformation">
                  <div>
                    <span class="option-tile-title">Digital Transformation</span>
                    <span class="option-tile-desc">Technology &amp; workflow modernization</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Business Expansion">
                  <div>
                    <span class="option-tile-title">Business Expansion</span>
                    <span class="option-tile-desc">Market entry &amp; scalability planning</span>
                  </div>
                </label>
                <label class="option-tile">
                  <input type="checkbox" name="challenges" value="Risk Management">
                  <div>
                    <span class="option-tile-title">Risk Management</span>
                    <span class="option-tile-desc">Vulnerability &amp; continuity controls</span>
                  </div>
                </label>
              </div>
            </div>

            <!-- STEP 4: Business Requirements -->
            <div class="wizard-step-pane" data-step="4">
              <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Step 4: Business Requirements &amp; Target Outcomes</h3>
              <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.75rem;">Describe the primary organizational bottleneck and what success looks like for leadership.</p>

              <div class="form-group">
                <label for="wizard-main-challenge">Primary Management Challenge <span class="required">*</span></label>
                <textarea id="wizard-main-challenge" class="form-control" rows="3" placeholder="Describe the core operational or strategic challenge your organization is confronting..."></textarea>
              </div>

              <div class="form-group">
                <label for="wizard-desired-outcome">Target Desired Outcome <span class="required">*</span></label>
                <textarea id="wizard-desired-outcome" class="form-control" rows="3" placeholder="What specific commercial or operational improvements do you aim to achieve?"></textarea>
              </div>

              <div class="form-group">
                <label for="wizard-notes">Additional Context (Optional)</label>
                <input type="text" id="wizard-notes" class="form-control" placeholder="Timeline constraints, active board mandates, or historical initiatives...">
              </div>
            </div>

            <!-- STEP 5: Consultation Preferences -->
            <div class="wizard-step-pane" data-step="5">
              <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Step 5: Consultation Format &amp; Scheduling</h3>
              <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.75rem;">Select your preferred consultation delivery mode and indicative date/time.</p>

              <div class="form-group mode-options">
                <label>Consultation Mode <span class="required">*</span></label>
                <div style="display: flex; gap: 1.5rem; margin-top: 0.5rem;">
                  <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer;">
                    <input type="radio" name="consultation_mode" value="Online Video Conference (MS Teams / Zoom)" checked>
                    <span>Online Video Conference</span>
                  </label>
                  <label style="display: flex; align-items: center; gap: 0.5rem; cursor: pointer;">
                    <input type="radio" name="consultation_mode" value="In-Person Executive Meeting">
                    <span>In-Person Executive Meeting</span>
                  </label>
                </div>
              </div>

              <div class="form-row mt-3">
                <div class="form-group">
                  <label for="wizard-date">Preferred Discussion Date <span class="required">*</span></label>
                  <input type="date" id="wizard-date" class="form-control">
                </div>
                <div class="form-group">
                  <label for="wizard-time">Preferred Time Window <span class="required">*</span></label>
                  <select id="wizard-time" class="form-control">
                    <option value="">Select Time Window</option>
                    <option value="Morning (9:30 AM - 12:00 PM)">Morning (9:30 AM &ndash; 12:00 PM)</option>
                    <option value="Afternoon (2:00 PM - 4:30 PM)">Afternoon (2:00 PM &ndash; 4:30 PM)</option>
                    <option value="Late Afternoon (4:30 PM - 6:00 PM)">Late Afternoon (4:30 PM &ndash; 6:00 PM)</option>
                  </select>
                </div>
              </div>
            </div>

            <!-- STEP 6: Review & Submit -->
            <div class="wizard-step-pane" data-step="6">
              <h3 style="font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Step 6: Review Engagement Summary</h3>
              <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.5rem;">Please review your submitted parameters before finalizing your consultation brief.</p>

              <div id="wizard-review-container">
                <!-- Dynamically populated by assets/js/forms.js -->
              </div>
            </div>

            <!-- Wizard Navigation Actions -->
            <div class="wizard-actions">
              <button type="button" class="btn btn-outline wizard-prev-btn" style="display: none;">&larr; Previous Step</button>
              <div style="margin-left: auto;">
                <button type="button" class="btn btn-gold wizard-next-btn">Next Step &rarr;</button>
                <button type="button" class="btn btn-primary wizard-submit-btn" style="display: none;">Submit Consultation Enquiry</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("book-consultation.html", "Start With a Conversation: Multi-Step Consultation Enquiry", "Complete our 6-step consultation enquiry to outline your organization's management challenge and schedule an initial advisory discussion.", body)

# ==============================================================================
# 33. CAREERS: careers.html
# ==============================================================================
def build_careers():
    roles = [
        {"title": "Management Consultant (Strategy & Operations)", "type": "Full-Time Advisory Role", "desc": "Lead diagnostic workstreams, conduct value stream mapping, and construct implementation roadmaps alongside enterprise leadership teams.", "req": "Experience in structured business analysis, operational modeling, and executive presentation."},
        {"title": "Senior Business Analyst (Performance Systems)", "type": "Full-Time Analytical Role", "desc": "Analyze operational throughput data, design balanced scorecard metrics, and support executive dashboard implementation.", "req": "Proficiency in management accounting, process mapping, and quantitative operational diagnostics."},
        {"title": "Organizational Development Consultant", "type": "Full-Time Advisory Role", "desc": "Evaluate reporting structures, design RACI decision rights charters, and facilitate leadership alignment workshops.", "req": "Experience in organizational design, span of control analysis, and change management frameworks."},
        {"title": "Management Consulting Research Intern", "type": "6-Month Advisory Internship", "desc": "Support senior consultants in competitive landscape research, industry benchmarking, and diagnostic interview documentation.", "req": "Strong analytical problem-solving aptitude, written communication skills, and commercial curiosity."}
    ]

    cards_html = ""
    for r in roles:
        cards_html += f"""
        <div class="card">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
            <span class="badge badge-demo">Illustrative Opportunity</span>
            <span style="font-size: 0.75rem; color: var(--secondary-text);">{r["type"]}</span>
          </div>
          <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--primary-navy);">{r["title"]}</h3>
          <p style="font-size: 0.9rem; margin-bottom: 1rem;">{r["desc"]}</p>
          <div style="background: #F8FAFC; padding: 0.75rem 1rem; border-radius: var(--radius-sm); font-size: 0.8rem; margin-bottom: 1.25rem;">
            <strong>Core Focus:</strong> {r["req"]}
          </div>
          <div class="mt-auto">
            <a href="#application-section" class="btn btn-outline btn-sm" style="width: 100%;">View Application Details</a>
          </div>
        </div>
        """

    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Careers</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Professional Advisory Practice</span>
          <h1>Careers in Management Consulting.</h1>
          <p class="lead">Explore illustrative professional consulting opportunities across strategy research, operational diagnostics, organizational development, and management analysis.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="case-demo-notice mb-4">
          <strong>Demonstration Careers Notice:</strong> All role profiles and internships listed on this page are illustrative demonstration placeholders. We do not invent actual active corporate vacancies, salary figures, employee benefits, or guaranteed recruitment offers.
        </div>

        <div class="section-header">
          <span class="section-eyebrow">Advisory Practice Opportunities</span>
          <h2 class="section-title">Illustrative Consulting Roles</h2>
          <p class="section-subtitle">Sample professional profiles reflecting the analytical disciplines and consulting capabilities required in our practice.</p>
        </div>

        <div class="card-grid-2">
          {cards_html}
        </div>

        <!-- Frontend Application Form -->
        <div id="application-section" class="card mt-4" style="padding: 2.5rem; max-width: 760px; margin-left: auto; margin-right: auto; box-shadow: var(--shadow-md);">
          <span class="badge badge-demo mb-1">Demonstration Form</span>
          <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem; color: var(--primary-navy);">Submit Demonstration Application</h3>
          <p style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 1.5rem;">Simulate submitting an application for a management consulting role. (No data is transmitted or saved).</p>

          <form id="career-application-form">
            <div class="form-row">
              <div class="form-group">
                <label for="career-name">Full Name <span class="required">*</span></label>
                <input type="text" id="career-name" class="form-control" required placeholder="Your Full Name">
              </div>
              <div class="form-group">
                <label for="career-email">Email Address <span class="required">*</span></label>
                <input type="email" id="career-email" class="form-control" required placeholder="name@example.com">
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label for="career-phone">Contact Phone</label>
                <input type="tel" id="career-phone" class="form-control" placeholder="Phone Number">
              </div>
              <div class="form-group">
                <label for="career-role">Role of Interest</label>
                <select id="career-role" class="form-control">
                  <option value="Management Consultant">Management Consultant (Strategy &amp; Operations)</option>
                  <option value="Senior Business Analyst">Senior Business Analyst</option>
                  <option value="Organizational Development">Organizational Development Consultant</option>
                  <option value="Consulting Intern">Research Internship</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label for="career-summary">Brief Professional Summary</label>
              <textarea id="career-summary" class="form-control" rows="3" placeholder="Outline your consulting experience, analytical focus, or academic background..."></textarea>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Demo Application</button>
            <div style="font-size: 0.75rem; color: var(--secondary-text); text-align: center; margin-top: 0.5rem;">
              Static demo prototype &bull; Does not process resumes or store personal information.
            </div>
          </form>
        </div>
      </div>
    </section>

    <!-- Consultation CTA Banner -->
    <section class="cta-banner">
      <div class="container text-center">
        <h2>Start With a Conversation. Build a Clearer Business Direction.</h2>
        <p style="margin: 0 auto 2rem;">Schedule an initial confidential discussion to review your organization's challenges, explore engagement scopes, and determine fit.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="book-consultation.html" class="btn btn-gold btn-lg">Book a Consultation</a>
          <a href="contact.html" class="btn btn-outline-white btn-lg">Contact Advisory Office</a>
        </div>
      </div>
    </section>
    """
    render_page("careers.html", "Careers in Management Consulting: Advisory Opportunities", "Explore illustrative career opportunities in management consulting, business analysis, organizational development, and research internships.", body)

# ==============================================================================
# 34. PRIVACY POLICY: privacy-policy.html
# ==============================================================================
def build_privacy():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Privacy Policy</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Legal Disclosures</span>
          <h1>Privacy Policy</h1>
          <p class="lead">Sample privacy disclosure statements for website visitors and demonstration inquiries.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container container-narrow">
        <div class="case-demo-notice mb-4">
          <strong>Notice for Legal Review:</strong> This document represents a generic sample privacy policy created for a demonstration management consulting website prototype. It does not constitute formal legal advice and must undergo professional legal and regulatory review before commercial publication.
        </div>

        <div class="card p-4">
          <h3 style="margin-bottom: 1rem; color: var(--primary-navy);">1. Information Entered in Demonstration Forms</h3>
          <p>This static website prototype provides interactive contact and consultation inquiry forms solely for demonstration, user experience evaluation, and visual presentation. All form submissions are handled strictly via client-side JavaScript in local memory.</p>
          <p><strong>This website does NOT transmit, collect, or store any personal information</strong> entered into forms, including names, email addresses, telephone numbers, corporate designations, or business descriptions, on any remote server, database, or third-party CRM service.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">2. Data Transmission &amp; Storage</h3>
          <p>Because this is a static website hosted on static infrastructure, there are no backend database servers or server-side scripts (such as PHP, Node.js, or MySQL) processing or archiving your data. Refreshing the browser page immediately clears all local state.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">3. Cookies &amp; Local Tracking</h3>
          <p>This website does not set commercial advertising cookies, tracking pixels, or intrusive tracking scripts. Standard browser session functionality may temporarily store user navigation preferences (such as accordion states) strictly within your local browser session.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">4. Analytics &amp; Web Hosting Logs</h3>
          <p>Standard web hosting servers (such as Hostinger static web servers) may record routine technical server access logs (such as IP address, browser type, referring page, and timestamp) strictly for server diagnostics, security monitoring, and uptime verification.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">5. Contact for Policy Inquiries</h3>
          <p>For questions regarding this demonstration privacy policy or the website prototype, please contact our demonstration office via the designated contact coordinates:</p>
          <ul style="font-size: 0.9rem; padding-left: 1.25rem; list-style: disc; color: var(--secondary-text);">
            <li>Email: <a href="mailto:demo@example.com">demo@example.com</a></li>
            <li>Telephone: 0000000000</li>
            <li>Address: Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000, India</li>
          </ul>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">6. Policy Updates</h3>
          <p>This sample policy was last updated in November 2026. Any future revisions to this static demonstration framework will be reflected directly on this page.</p>
        </div>
      </div>
    </section>
    """
    render_page("privacy-policy.html", "Privacy Policy: Demonstration Website Disclosures", "Privacy policy and data handling disclosures for the generic management consulting website demonstration prototype.", body)

# ==============================================================================
# 35. TERMS AND CONDITIONS: terms-and-conditions.html
# ==============================================================================
def build_terms():
    body = f"""
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">Terms and Conditions</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">Terms of Usage</span>
          <h1>Terms and Conditions</h1>
          <p class="lead">Sample terms and conditions governing the use of this management consulting website prototype.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container container-narrow">
        <div class="case-demo-notice mb-4">
          <strong>Notice for Legal Review:</strong> This document represents a generic sample terms and conditions framework created for a demonstration management consulting website. It does not constitute formal legal counsel and must be reviewed by qualified legal advisors prior to commercial use.
        </div>

        <div class="card p-4">
          <h3 style="margin-bottom: 1rem; color: var(--primary-navy);">1. Website Usage &amp; Demonstration Scope</h3>
          <p>This website is provided solely as a generic management consulting conceptual demonstration. The website identity "MANAGEMENT CONSULTING COMPANY" is a generic placeholder and does not refer to any specific registered legal entity.</p>
          <p>All content, case study summaries, organizational frameworks, dashboard mockups, and metric illustrations are published for informational, educational, and conceptual demonstration purposes only.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">2. Non-Advisory &amp; Regulatory Disclaimers</h3>
          <p><strong>This website does NOT provide licensed legal, financial, accounting, investment, tax, or statutory audit advice.</strong> The materials and consulting frameworks displayed on this site represent general management advisory concepts and must not be relied upon as substitutes for regulated professional advice.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">3. Consulting Service Proposals &amp; Scopes of Work</h3>
          <p>Information presented on this website does not constitute a binding legal offer or contract. Formal management consulting engagements require an executed Master Services Agreement (MSA) and a mutually agreed Scope of Work (SOW) detailing verified deliverables, schedules, and fee arrangements.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">4. Intellectual Property &amp; Frameworks</h3>
          <p>The layout, visual design, custom CSS frameworks, SVG diagrams, and editorial text contained on this website are the intellectual property of the website creators. Unauthorized duplication for competing commercial purposes is prohibited.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">5. Limitation of Liability</h3>
          <p>In no event shall the website owners, creators, or authors be liable for any direct, indirect, incidental, consequential, or special damages arising out of the use of, or inability to use, the sample information, diagrams, or calculators presented on this demonstration website.</p>

          <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: var(--primary-navy);">6. Contact Coordinates</h3>
          <p>For questions regarding these terms, please contact the advisory demonstration office at <a href="mailto:demo@example.com">demo@example.com</a> or telephone 0000000000.</p>
        </div>
      </div>
    </section>
    """
    render_page("terms-and-conditions.html", "Terms and Conditions of Website Usage", "Terms and conditions governing the use and disclaimers of the generic management consulting company website demonstration prototype.", body)

if __name__ == "__main__":
    build_index()
    build_about()
    build_services_overview()
    build_industries()
    build_methodology()
    build_case_studies()
    build_case_study_details()
    build_team()
    build_insights()
    build_article_details()
    build_resources()
    build_pricing()
    build_faq()
    build_contact()
    build_book_consultation()
    build_careers()
    build_privacy()
    build_terms()
    print("All 18 core pages generated successfully.")
