import os
import glob
import re

html_files = sorted(glob.glob("*.html"))
print(f"Updating header in {len(html_files)} HTML files...")

# The old header pattern in the HTML files:
# from <nav class="main-nav" id="mainNav" ...> to </header>
old_nav_pattern = re.compile(
    r'<nav class="main-nav" id="mainNav" aria-label="Primary Navigation">.*?</header>',
    re.DOTALL
)

new_nav_html = """<nav class="main-nav" id="mainNav" aria-label="Primary Navigation">
        <ul class="nav-list">
          <li class="nav-item"><a href="index.html" class="nav-link">Home</a></li>
          
          <li class="nav-item has-dropdown">
            <a href="services.html" class="nav-link" aria-haspopup="true" aria-expanded="false">
              Services
              <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <div class="mega-menu" aria-label="Consulting Services Menu">
              <div>
                <div class="mega-menu-col-title">Strategy &amp; Transformation</div>
                <div class="mega-menu-list">
                  <a href="business-strategy.html" class="mega-menu-link">
                    <span class="item-title">Business Strategy</span>
                    <span class="item-desc">Market positioning &amp; strategic priorities</span>
                  </a>
                  <a href="strategic-planning.html" class="mega-menu-link">
                    <span class="item-title">Strategic Planning</span>
                    <span class="item-desc">Execution roadmaps &amp; milestones</span>
                  </a>
                  <a href="business-transformation.html" class="mega-menu-link">
                    <span class="item-title">Business Transformation</span>
                    <span class="item-desc">Enterprise operating model redesign</span>
                  </a>
                  <a href="business-expansion.html" class="mega-menu-link">
                    <span class="item-title">Business Expansion</span>
                    <span class="item-desc">Market opportunity &amp; growth planning</span>
                  </a>
                  <a href="digital-transformation.html" class="mega-menu-link">
                    <span class="item-title">Digital Transformation</span>
                    <span class="item-desc">Technology &amp; workflow modernization</span>
                  </a>
                </div>
              </div>

              <div>
                <div class="mega-menu-col-title">Operations &amp; Governance</div>
                <div class="mega-menu-list">
                  <a href="management-advisory.html" class="mega-menu-link">
                    <span class="item-title">Management Advisory</span>
                    <span class="item-desc">Executive decision frameworks</span>
                  </a>
                  <a href="operations-consulting.html" class="mega-menu-link">
                    <span class="item-title">Operations Consulting</span>
                    <span class="item-desc">Operating efficiency &amp; capacity review</span>
                  </a>
                  <a href="process-optimization.html" class="mega-menu-link">
                    <span class="item-title">Process Optimization</span>
                    <span class="item-desc">Bottleneck removal &amp; workflow mapping</span>
                  </a>
                  <a href="corporate-governance.html" class="mega-menu-link">
                    <span class="item-title">Corporate Governance</span>
                    <span class="item-desc">Oversight, policy &amp; reporting alignment</span>
                  </a>
                  <a href="risk-management.html" class="mega-menu-link">
                    <span class="item-title">Risk Management</span>
                    <span class="item-desc">Operational &amp; business risk frameworks</span>
                  </a>
                  <a href="project-management.html" class="mega-menu-link">
                    <span class="item-title">Project Management</span>
                    <span class="item-desc">Portfolio governance &amp; delivery control</span>
                  </a>
                </div>
              </div>

              <div>
                <div class="mega-menu-col-title">People &amp; Performance</div>
                <div class="mega-menu-list">
                  <a href="organizational-development.html" class="mega-menu-link">
                    <span class="item-title">Organizational Development</span>
                    <span class="item-desc">Structure, roles &amp; organizational design</span>
                  </a>
                  <a href="leadership-consulting.html" class="mega-menu-link">
                    <span class="item-title">Leadership Consulting</span>
                    <span class="item-desc">Executive alignment &amp; accountability</span>
                  </a>
                  <a href="performance-improvement.html" class="mega-menu-link">
                    <span class="item-title">Performance Improvement</span>
                    <span class="item-desc">KPI architecture &amp; management reviews</span>
                  </a>
                  <a href="change-management.html" class="mega-menu-link">
                    <span class="item-title">Change Management</span>
                    <span class="item-desc">Transition planning &amp; stakeholder adoption</span>
                  </a>
                  <a href="financial-performance.html" class="mega-menu-link">
                    <span class="item-title">Financial Performance</span>
                    <span class="item-desc">Cost analysis &amp; budgeting frameworks</span>
                  </a>
                  <a href="human-resource-management.html" class="mega-menu-link">
                    <span class="item-title">Human Resource Management</span>
                    <span class="item-desc">Workforce planning &amp; talent systems</span>
                  </a>
                </div>
              </div>

              <div class="mega-menu-featured">
                <div>
                  <span class="badge badge-gold mb-1">Advisory Diagnostic</span>
                  <h4>Need an Engagement Assessment?</h4>
                  <p>Explore how our structured five-stage methodology diagnoses friction and unlocks organizational clarity.</p>
                </div>
                <a href="book-consultation.html" class="btn btn-primary btn-sm">Schedule Discussion</a>
              </div>
            </div>
          </li>

          <li class="nav-item has-dropdown">
            <a href="about.html" class="nav-link" aria-haspopup="true" aria-expanded="false">
              Company
              <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <div class="dropdown-menu" aria-label="Company Submenu">
              <a href="about.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">About Our Firm</span>
                  <span class="dropdown-link-desc">Philosophy, principles &amp; advisory standards</span>
                </div>
              </a>
              <a href="industries.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Industries Served</span>
                  <span class="dropdown-link-desc">Tailored consulting across 14 economic sectors</span>
                </div>
              </a>
              <a href="methodology.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Our Methodology</span>
                  <span class="dropdown-link-desc">Structured 5-stage diagnostic approach</span>
                </div>
              </a>
              <a href="team.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Advisory Leadership</span>
                  <span class="dropdown-link-desc">Executive practice leads &amp; capabilities</span>
                </div>
              </a>
              <a href="careers.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Careers &amp; Internships</span>
                  <span class="dropdown-link-desc">Advisory roles &amp; consulting opportunities</span>
                </div>
              </a>
              <a href="contact.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Contact Advisory Office</span>
                  <span class="dropdown-link-desc">Office coordinates &amp; confidential inquiries</span>
                </div>
              </a>
            </div>
          </li>

          <li class="nav-item has-dropdown">
            <a href="insights.html" class="nav-link" aria-haspopup="true" aria-expanded="false">
              Insights
              <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </a>
            <div class="dropdown-menu" aria-label="Insights Submenu">
              <a href="insights.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Management Insights</span>
                  <span class="dropdown-link-desc">Executive research &amp; strategic commentary</span>
                </div>
              </a>
              <a href="case-studies.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Case Studies Gallery</span>
                  <span class="dropdown-link-desc">Illustrative diagnostic scenarios &amp; results</span>
                </div>
              </a>
              <a href="resources.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Resource Library</span>
                  <span class="dropdown-link-desc">Practical checklists, templates &amp; frameworks</span>
                </div>
              </a>
              <a href="pricing.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Engagement Models</span>
                  <span class="dropdown-link-desc">Transparent scoping &amp; advisory structures</span>
                </div>
              </a>
              <a href="faq.html" class="dropdown-link">
                <div class="dropdown-link-icon">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                </div>
                <div class="dropdown-link-text">
                  <span class="dropdown-link-title">Frequently Asked Questions</span>
                  <span class="dropdown-link-desc">Answers to common advisory inquiries</span>
                </div>
              </a>
            </div>
          </li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="contact.html" class="btn btn-outline btn-sm header-contact-btn">Contact</a>
        <a href="book-consultation.html" class="btn btn-gold btn-sm">Book a Consultation</a>
        <button class="mobile-menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </div>
</header>"""

updated_count = 0
for f in html_files:
    with open(f, "r", encoding="utf-8") as fp:
        content = fp.read()

    new_content, count = old_nav_pattern.subn(new_nav_html, content)
    if count > 0:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        updated_count += 1
        print(f"Updated header in: {f}")
    else:
        print(f"Warning: could not match header in: {f}")

print(f"Header update completed for {updated_count}/{len(html_files)} files.")
