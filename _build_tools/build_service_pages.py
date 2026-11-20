# -*- coding: utf-8 -*-
"""
Generator for the 17 Management Consulting Service Pages
Each page includes deep corporate advisory text, custom visual framework/dashboard,
deliverables, challenges addressed, and explicit image placeholders.
"""

from generator_base import render_page, make_placeholder

SERVICES = [
    {
        "slug": "business-strategy",
        "title": "Business Strategy Consulting",
        "eyebrow": "Enterprise Strategy & Market Positioning",
        "headline": "Make Better Strategic Decisions for Your Business.",
        "description": "We help executive teams navigate competitive pressure, clarify market positioning, allocate capital effectively, and build actionable business strategies.",
        "image": "business-strategy-planning.webp",
        "challenges": [
            "Loss of differentiation in mature or shifting competitive markets",
            "Conflicting internal priorities diluting capital and operational focus",
            "Unclear market positioning leading to customer acquisition friction",
            "Lack of disciplined strategy execution beyond annual retreat slide decks"
        ],
        "deliverables": [
            "Comprehensive Strategic Diagnosis & Competitive Positioning Audit",
            "Enterprise Growth & Business Model Prioritization Blueprint",
            "Resource & Capital Allocation Decision Framework",
            "Executive Strategy Execution Roadmap & 90-Day Milestone Architecture"
        ],
        "framework_type": "strategy_framework"
    },
    {
        "slug": "strategic-planning",
        "title": "Strategic Planning Consulting",
        "eyebrow": "Roadmaps, Milestones & Strategic Alignment",
        "headline": "Give Your Organization a Clear Strategic Roadmap.",
        "description": "Transform broad organizational vision into measurable strategic milestones, structured cascading objectives, and clear accountability systems across departments.",
        "image": "strategic-roadmap-session.webp",
        "challenges": [
            "Vision statements disconnected from operational budgets and departmental goals",
            "Strategic initiatives stalling due to vague milestone ownership",
            "Difficulty measuring ongoing strategic progress between annual planning cycles",
            "Organizational fatigue caused by shifting executive priorities"
        ],
        "deliverables": [
            "Multi-Year Strategic Vision, Mission & Horizon Architecture",
            "Cascading Objectives & Key Results (OKR) Operating System",
            "Quarterly Strategic Review & Governance Rhythm Protocol",
            "Cross-Functional Strategic Roadmap & Initiative Portfolio Matrix"
        ],
        "framework_type": "roadmap"
    },
    {
        "slug": "business-transformation",
        "title": "Business Transformation Advisory",
        "eyebrow": "Operating Model Redesign & Enterprise Modernization",
        "headline": "Structured Enterprise Transformation for Long-Term Value.",
        "description": "We guide corporate leadership through end-to-end organizational, operating model, and technological transitions to unlock structural performance gains.",
        "image": "business-transformation-framework.webp",
        "challenges": [
            "Outdated operating models incapable of supporting business expansion",
            "Siloed departments creating massive communication and operational friction",
            "High transformation investment with low frontline adoption or cultural buy-in",
            "Inadequate governance causing scope drift and prolonged execution delays"
        ],
        "deliverables": [
            "Target Operating Model (TOM) Blueprint & Architecture",
            "Enterprise Transformation Roadmap: Current State to Future State",
            "Transformation Management Office (TMO) Governance Framework",
            "Change Impact Assessment & Frontline Adoption Enablement Protocol"
        ],
        "framework_type": "transformation_journey"
    },
    {
        "slug": "management-advisory",
        "title": "Management Advisory Services",
        "eyebrow": "Executive Guidance & Decision-Making Frameworks",
        "headline": "Practical Management Guidance for Better Business Execution.",
        "description": "Providing CEOs, boards, and senior executives with an objective, data-informed sounding board to pressure-test critical management decisions.",
        "image": "management-advisory-meeting.webp",
        "challenges": [
            "Executive isolation when confronting high-stakes organizational decisions",
            "Lack of objective external perspective free from internal political dynamics",
            "Inconsistent management cadence across senior leadership teams",
            "Slow executive consensus resulting in missed commercial windows"
        ],
        "deliverables": [
            "Executive Management Operating System & Cadence Design",
            "Strategic Decision-Making Frameworks & Escalation Matrices",
            "Executive Information System & Dashboard Architecture",
            "Board & Management Committee Governance Advisory"
        ],
        "framework_type": "management_framework"
    },
    {
        "slug": "organizational-development",
        "title": "Organizational Development Consulting",
        "eyebrow": "Organizational Structure & Role Alignment",
        "headline": "Align Organizational Structure With Your Strategic Ambition.",
        "description": "Design agile, clear, and accountable organizational structures that eliminate duplication, clarify reporting hierarchies, and empower departmental performance.",
        "image": "organizational-development-chart.webp",
        "challenges": [
            "Overlapping roles and ambiguous decision rights between business units",
            "Excessive managerial layers creating decision bottlenecks and high overhead",
            "Cultural resistance and fragmented team morale following growth phases",
            "Difficulty attracting and aligning specialized talent with key value drivers"
        ],
        "deliverables": [
            "Organizational Architecture & Reporting Structure Blueprints",
            "RACI Decision Rights Matrix & Role Charter Specifications",
            "Span of Control & Management Layer Optimization Analysis",
            "Organizational Capability Matrix & Talent Development Blueprint"
        ],
        "framework_type": "org_chart"
    },
    {
        "slug": "leadership-consulting",
        "title": "Leadership Consulting & Alignment",
        "eyebrow": "Executive Team Performance & Succession Architecture",
        "headline": "Strengthen Leadership. Align Teams. Improve Decisions.",
        "description": "Unify executive leadership around common objectives, build resilient decision-making standards, and cultivate strong institutional management capabilities.",
        "image": "leadership-consulting-boardroom.webp",
        "challenges": [
            "Misaligned executive priorities creating friction between departments",
            "Gaps in executive bench strength jeopardizing leadership continuity",
            "Inconsistent leadership communication during periods of change or crisis",
            "Subjective executive assessment lacking objective performance benchmarks"
        ],
        "deliverables": [
            "Executive Leadership Team Alignment Protocol & Diagnostic",
            "Management Competency Framework & Evaluation Architecture",
            "Institutional Succession Planning & Leadership Pipeline Model",
            "Executive Communication & Change Leadership Guidelines"
        ],
        "framework_type": "leadership_framework"
    },
    {
        "slug": "operations-consulting",
        "title": "Operations Consulting Practice",
        "eyebrow": "Operational Excellence & Capacity Optimization",
        "headline": "Streamline Core Operations for Scalable Business Efficiency.",
        "description": "Identify operational friction, optimize throughput, synchronize supply chain workflows, and establish scalable operating standards across your business.",
        "image": "operations-consulting-workshop.webp",
        "challenges": [
            "Capacity bottlenecks restricting fulfillment or project delivery",
            "Inconsistent operational quality across facilities, branches, or teams",
            "Opaque operating costs and lack of unit-level productivity visibility",
            "Supply chain vulnerability and inventory holding inefficiencies"
        ],
        "deliverables": [
            "End-to-End Operational Workflow Diagnostic & Value Stream Mapping",
            "Operational Capacity & Resource Allocation Optimization Plan",
            "Standard Operating Procedures (SOP) & Quality Assurance Protocols",
            "Operational Governance & Real-Time Performance Tracking System"
        ],
        "framework_type": "operations_dashboard"
    },
    {
        "slug": "performance-improvement",
        "title": "Performance Improvement Consulting",
        "eyebrow": "KPI Frameworks & Productivity Acceleration",
        "headline": "Create a More Effective, Accountable, Performance-Driven Organization.",
        "description": "Establish transparent KPI cascades, rigorous management review rhythms, and actionable accountability metrics that drive continuous organizational improvement.",
        "image": "performance-improvement-dashboard.webp",
        "challenges": [
            "Vanity metrics obscuring underlying operational or commercial weaknesses",
            "Lack of real-time management visibility into departmental performance gaps",
            "Absence of structured accountability and corrective action mechanisms",
            "Siloed reporting leading to conflicting versions of operational truth"
        ],
        "deliverables": [
            "Enterprise KPI Cascade & Balanced Scorecard Design",
            "Departmental Performance Review Cadence & Management Playbooks",
            "Productivity Diagnostic & Performance Gap Remediation Roadmap",
            "Executive Dashboard & Reporting Template Library"
        ],
        "framework_type": "performance_dashboard"
    },
    {
        "slug": "process-optimization",
        "title": "Business Process Optimization",
        "eyebrow": "Workflow Streamlining & Bottleneck Elimination",
        "headline": "Remove Waste. Eliminate Bottlenecks. Standardize Workflows.",
        "description": "Systematically analyze, re-engineer, and standardize critical workflows to reduce turnaround times, lower error rates, and prepare processes for automation.",
        "image": "process-optimization-mapping.webp",
        "challenges": [
            "Redundant manual steps multiplying operational turnaround times",
            "High error rates and rework cycles eroding departmental margins",
            "Key-person dependency where institutional knowledge is undocumented",
            "Premature software automation applied to broken or inefficient workflows"
        ],
        "deliverables": [
            "Current State vs. Future State Value Stream Workflow Maps",
            "Process Bottleneck & Waste Elimination Assessment",
            "Process Standardization Manuals & Digital Handover Protocols",
            "Automation Readiness Scorecard & Workflow Optimization Roadmap"
        ],
        "framework_type": "workflow_compare"
    },
    {
        "slug": "change-management",
        "title": "Change Management Consulting",
        "eyebrow": "Change Enablement & Stakeholder Adoption",
        "headline": "Help Your Organization Navigate Change With Confidence.",
        "description": "Minimize resistance, protect operational stability, and maximize adoption during structural, strategic, or technology-driven transformations.",
        "image": "change-management-strategy.webp",
        "challenges": [
            "High employee skepticism and passive resistance to leadership initiatives",
            "Productivity slumps and customer disruption during transition phases",
            "Breakdown of middle-management advocacy for executive mandates",
            "Reversion to obsolete practices once initial project consultants depart"
        ],
        "deliverables": [
            "Organizational Change Readiness & Stakeholder Impact Assessment",
            "Executive Change Communications Architecture & Messaging Matrix",
            "Change Champion Network & Middle-Management Enablement Kit",
            "Adoption Measurement Scorecard & Cultural Reinforcement Plan"
        ],
        "framework_type": "change_framework"
    },
    {
        "slug": "corporate-governance",
        "title": "Corporate Governance Advisory",
        "eyebrow": "Oversight, Accountability & Policy Architecture",
        "headline": "Institutionalize Clear Governance and Executive Accountability.",
        "description": "Establish balanced governance structures, transparent board oversight, and rigorous management reporting mechanisms tailored to growing enterprises.",
        "image": "corporate-governance-framework.webp",
        "challenges": [
            "Informal governance mechanisms outgrown by rapid enterprise expansion",
            "Ambiguity between board oversight mandates and operational executive duties",
            "Absence of standardized policy review and internal authorization matrix",
            "Inadequate reporting leaving leadership exposed to operational blind spots"
        ],
        "deliverables": [
            "Corporate Governance Framework & Board Committee Charters",
            "Delegation of Authority (DoA) & Management Approval Matrix",
            "Executive Management Oversight & Internal Reporting Protocols",
            "Governance Maturity Review & Policy Standardization Roadmap"
        ],
        "framework_type": "governance_framework"
    },
    {
        "slug": "business-expansion",
        "title": "Business Expansion Consulting",
        "eyebrow": "Market Entry, Scalability & Expansion Roadmaps",
        "headline": "Plan Your Next Stage of Business Expansion With Discipline.",
        "description": "Evaluate market feasibility, assess internal operational capacity, and construct step-by-step expansion roadmaps that protect core profitability while entering new horizons.",
        "image": "business-expansion-planning.webp",
        "challenges": [
            "Premature expansion straining existing core operations and cash reserves",
            "Incomplete market feasibility analysis leading to underperforming launches",
            "Inability to replicate service quality across geographic territories",
            "Misalignment between sales projections and operational delivery capacity"
        ],
        "deliverables": [
            "Market Opportunity Assessment & Expansion Feasibility Framework",
            "Territory & Business Model Entry Strategy Blueprint",
            "Operational Scalability Audit & Resource Requirement Model",
            "Expansion Risk Assessment & Phased Milestone Rollout Schedule"
        ],
        "framework_type": "expansion_roadmap"
    },
    {
        "slug": "financial-performance",
        "title": "Financial Performance & Cost Strategy",
        "eyebrow": "Cost Structure Optimization & Management Accounting",
        "headline": "Strengthen Cost Discipline and Operational Profitability.",
        "description": "Optimize operating cost structures, refine budgeting methodologies, and build managerial financial dashboards that illuminate true margin drivers across business lines.",
        "image": "financial-performance-analysis.webp",
        "challenges": [
            "Growing revenue accompanied by eroding operating margins",
            "Opaque overhead allocation obscuring unprofitable product or service lines",
            "Rigid annual budgets that cannot adapt to commercial volatility",
            "Lack of management-level cash flow predictability and working capital drag"
        ],
        "deliverables": [
            "Operational Cost Structure Diagnostic & Margin Optimization Review",
            "Management Accounting & Product/Service Profitability Framework",
            "Rolling Forecast & Dynamic Budgeting Protocol Design",
            "Executive Working Capital & Cash Flow Management Guidelines"
        ],
        "framework_type": "financial_dashboard"
    },
    {
        "slug": "human-resource-management",
        "title": "Strategic Human Resource Advisory",
        "eyebrow": "Workforce Architecture & Talent Management Systems",
        "headline": "Align Workforce Strategy With Long-Term Business Objectives.",
        "description": "Design modern workforce planning models, objective performance management architectures, and strategic talent development systems that support sustainable organizational growth.",
        "image": "workforce-planning-strategy.webp",
        "challenges": [
            "Workforce shortages and skill gaps in critical revenue-generating roles",
            "Subjective appraisal processes creating disengagement and high turnover",
            "Misalignment between business expansion goals and recruitment capacity",
            "Fragmented HR policies failing to protect institutional culture"
        ],
        "deliverables": [
            "Strategic Workforce Planning & Capacity Modeling Framework",
            "Objective Performance Management & Appraisal Architecture",
            "Talent Retention Strategy & High-Potential Development Model",
            "HR Operational Audit & Policy Standardization Playbook"
        ],
        "framework_type": "hr_dashboard"
    },
    {
        "slug": "project-management",
        "title": "Project Management Advisory",
        "eyebrow": "Project Governance & Portfolio Delivery Control",
        "headline": "Deliver Critical Strategic Initiatives On Time and Within Scope.",
        "description": "Establish structured Project Management Office (PMO) frameworks, milestone governance, and cross-functional coordination protocols to ensure high-stakes projects succeed.",
        "image": "project-governance-dashboard.webp",
        "challenges": [
            "Major capital or transformation projects suffering chronic scope creep",
            "Lack of unified progress visibility across multiple competing initiatives",
            "Poor risk escalation leading to last-minute delivery failures",
            "Resource contention between business-as-usual and strategic projects"
        ],
        "deliverables": [
            "Project Management Office (PMO) Charter & Governance Framework",
            "Project Risk Identification, Tracking & Escalation Protocols",
            "Multi-Project Portfolio Prioritization & Resource Balancing Matrix",
            "Executive Milestone Dashboard & Progress Reporting Templates"
        ],
        "framework_type": "pm_dashboard"
    },
    {
        "slug": "risk-management",
        "title": "Enterprise Risk Management Advisory",
        "eyebrow": "Risk Identification, Assessment & Mitigation Frameworks",
        "headline": "Identify, Assess, and Mitigate Operational and Strategic Risks.",
        "description": "Build proactive enterprise risk management architectures that identify vulnerabilities, establish mitigation controls, and protect business continuity.",
        "image": "risk-management-matrix.webp",
        "challenges": [
            "Unidentified operational dependencies creating catastrophic single points of failure",
            "Reactive crisis response rather than proactive risk anticipation",
            "Absence of a shared risk taxonomy across different business departments",
            "Risk registers viewed as compliance paperwork rather than strategic tools"
        ],
        "deliverables": [
            "Enterprise Risk Identification Taxonomy & Assessment Matrix",
            "Operational Vulnerability & Key Dependency Diagnostic",
            "Business Continuity & Disaster Resilience Framework",
            "Risk Governance Cadence & Executive Risk Committee Charters"
        ],
        "framework_type": "risk_matrix"
    },
    {
        "slug": "digital-transformation",
        "title": "Digital Transformation Advisory",
        "eyebrow": "Technology Strategy, Digitization & Process Modernization",
        "headline": "Align Technology, People, and Processes for Sustainable Digital Value.",
        "description": "Help business leadership define pragmatic digital roadmaps, select scalable enterprise software, modernize core workflows, and avoid costly failed technology rollouts.",
        "image": "digital-transformation-roadmap.webp",
        "challenges": [
            "Disjointed legacy software platforms trapping critical operational data",
            "Heavy technology expenditures without measurable operational productivity gains",
            "Employee resistance to new digital platforms and ERP systems",
            "Lack of clear technology roadmaps aligned with business strategy"
        ],
        "deliverables": [
            "Digital Maturity Assessment & Technology Architecture Diagnostic",
            "Enterprise Software Selection & Vendor Evaluation Governance Matrix",
            "Process Digitization & Workflow Modernization Blueprint",
            "Digital Adoption & Change Enablement Implementation Plan"
        ],
        "framework_type": "digital_roadmap"
    }
]

def render_framework_html(framework_type, service_title):
    if framework_type == "risk_matrix":
        return f"""
        <div class="dashboard-container">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Interactive 5x5 Enterprise Risk Matrix</h4>
              <p>Illustrative decision support framework for categorizing strategic, operational, and technological vulnerabilities.</p>
            </div>
            <span class="demo-watermark">Illustrative Demo Framework</span>
          </div>
          
          <p style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 0.75rem;">
            <em>Click on any matrix cell below to inspect its illustrative risk scenario and consulting mitigation approach:</em>
          </p>

          <table class="risk-matrix-table" aria-label="5x5 Risk Assessment Matrix">
            <thead>
              <tr>
                <th style="width: 12%;">Likelihood \\ Impact</th>
                <th style="width: 17%;">Insignificant (1)</th>
                <th style="width: 17%;">Minor (2)</th>
                <th style="width: 17%;">Moderate (3)</th>
                <th style="width: 17%;">Major (4)</th>
                <th style="width: 20%;">Catastrophic (5)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th>Almost Certain (5)</th>
                <td class="risk-cell risk-medium risk-interactive-cell" data-likelihood="Almost Certain" data-impact="Insignificant" data-severity="Medium" data-example="Minor daily inventory discrepancy" data-mitigation="Automated daily cycle counting & reconciliation SOP">Medium</td>
                <td class="risk-cell risk-high risk-interactive-cell" data-likelihood="Almost Certain" data-impact="Minor" data-severity="High" data-example="Vendor delivery slippage of 24h" data-mitigation="Dual-sourcing secondary supplier contract">High</td>
                <td class="risk-cell risk-critical risk-interactive-cell" data-likelihood="Almost Certain" data-impact="Moderate" data-severity="Critical" data-example="Key frontline staff turnover in busy season" data-mitigation="Cross-training program & retention incentive pool">Critical</td>
                <td class="risk-cell risk-critical risk-interactive-cell" data-likelihood="Almost Certain" data-impact="Major" data-severity="Critical" data-example="Core production line capacity bottleneck" data-mitigation="Line re-balancing and maintenance shift redesign">Critical</td>
                <td class="risk-cell risk-critical risk-interactive-cell" data-likelihood="Almost Certain" data-impact="Catastrophic" data-severity="Critical" data-example="Regulatory shutdown due to non-compliance" data-mitigation="Immediate governance audit and independent review">Critical</td>
              </tr>
              <tr>
                <th>Likely (4)</th>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Likely" data-impact="Insignificant" data-severity="Low" data-example="Standard software patch delay" data-mitigation="Monthly scheduled IT maintenance window">Low</td>
                <td class="risk-cell risk-medium risk-interactive-cell" data-likelihood="Likely" data-impact="Minor" data-severity="Medium" data-example="Localized customer service backlog" data-mitigation="Dynamic queue routing & escalation playbook">Medium</td>
                <td class="risk-cell risk-high risk-interactive-cell" data-likelihood="Likely" data-impact="Moderate" data-severity="High" data-example="Scope creep on internal improvement project" data-mitigation="PMO change control board approval gate">High</td>
                <td class="risk-cell risk-critical risk-interactive-cell" data-likelihood="Likely" data-impact="Major" data-severity="Critical" data-example="Key enterprise customer contract renegotiation" data-mitigation="Executive account review and multi-level relationship mapping">Critical</td>
                <td class="risk-cell risk-critical risk-interactive-cell" data-likelihood="Likely" data-impact="Catastrophic" data-severity="Critical" data-example="Primary logistics network failure" data-mitigation="Regional hub redundancy and 3PL buffer agreements">Critical</td>
              </tr>
              <tr>
                <th>Possible (3)</th>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Possible" data-impact="Insignificant" data-severity="Low" data-example="Minor data reporting formatting errors" data-mitigation="Data validation rules in reporting system">Low</td>
                <td class="risk-cell risk-medium risk-interactive-cell" data-likelihood="Possible" data-impact="Minor" data-severity="Medium" data-example="Brief IT downtime in non-peak hours" data-mitigation="Redundant server failover testing">Medium</td>
                <td class="risk-cell risk-medium risk-interactive-cell" data-likelihood="Possible" data-impact="Moderate" data-severity="Medium" data-example="Currency fluctuation affecting raw materials" data-mitigation="Quarterly forward-hedging and price indexation clauses">Medium</td>
                <td class="risk-cell risk-high risk-interactive-cell" data-likelihood="Possible" data-impact="Major" data-severity="High" data-example="Competitor aggressive price war in key territory" data-mitigation="Value-proposition sharpening and bundling strategy">High</td>
                <td class="risk-cell risk-critical risk-interactive-cell" data-likelihood="Possible" data-impact="Catastrophic" data-severity="Critical" data-example="Strategic acquisition integration failure" data-mitigation="Structured post-merger integration framework">Critical</td>
              </tr>
              <tr>
                <th>Unlikely (2)</th>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Unlikely" data-impact="Insignificant" data-severity="Low" data-example="Temporary stationery supply disruption" data-mitigation="Standard office manager procurement">Low</td>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Unlikely" data-impact="Minor" data-severity="Low" data-example="Single delivery vehicle breakdown" data-mitigation="Fleet reserve vehicle pool">Low</td>
                <td class="risk-cell risk-medium risk-interactive-cell" data-likelihood="Unlikely" data-impact="Moderate" data-severity="Medium" data-example="Sudden utility outage at branch facility" data-mitigation="On-site generator backup power protocols">Medium</td>
                <td class="risk-cell risk-high risk-interactive-cell" data-likelihood="Unlikely" data-impact="Major" data-severity="High" data-example="Executive leadership departure without successor" data-mitigation="Documented interim authority & succession plan">High</td>
                <td class="risk-cell risk-high risk-interactive-cell" data-likelihood="Unlikely" data-impact="Catastrophic" data-severity="High" data-example="Major cyber ransom incident" data-mitigation="Zero-trust architecture, offline cold backups, incident response protocols">High</td>
              </tr>
              <tr>
                <th>Rare (1)</th>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Rare" data-impact="Insignificant" data-severity="Low" data-example="Incidental billing typo resolved same day" data-mitigation="Clerk peer review">Low</td>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Rare" data-impact="Minor" data-severity="Low" data-example="Minor branch exterior property damage" data-mitigation="Commercial insurance coverage">Low</td>
                <td class="risk-cell risk-low risk-interactive-cell" data-likelihood="Rare" data-impact="Moderate" data-severity="Low" data-example="Regional weather closure for 24 hours" data-mitigation="Remote work protocol activation">Low</td>
                <td class="risk-cell risk-medium risk-interactive-cell" data-likelihood="Rare" data-impact="Major" data-severity="Medium" data-example="National port strike halting overseas supplies" data-mitigation="90-day safety stock buffer of critical inputs">Medium</td>
                <td class="risk-cell risk-high risk-interactive-cell" data-likelihood="Rare" data-impact="Catastrophic" data-severity="High" data-example="Total destruction of primary datacenter" data-mitigation="Multi-region cloud infrastructure & active-active replication">High</td>
              </tr>
            </tbody>
          </table>

          <div id="risk-cell-details">
            <div style="background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.25rem; margin-top: 1rem;">
              <span class="badge badge-subtle mb-1">Interactive Diagnostic</span>
              <p style="font-size: 0.85rem; margin-bottom: 0;">Click on any cell in the 5x5 matrix above to display an illustrative corporate risk scenario and mitigation blueprint.</p>
            </div>
          </div>
          <div style="font-size: 0.75rem; color: var(--secondary-text); margin-top: 0.75rem; text-align: right;">
            <strong>Disclaimer:</strong> Illustrative Demo Framework &bull; Not regulated actuarial, legal, or statutory compliance assurance.
          </div>
        </div>
        """
    elif framework_type == "org_chart":
        return f"""
        <div class="dashboard-container">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Illustrative Organizational Architecture</h4>
              <p>Sample functional hierarchy designed to eliminate duplication, clarify reporting lines, and establish unambiguous span of control.</p>
            </div>
            <span class="demo-watermark">Illustrative Demo Structure</span>
          </div>

          <div class="org-chart-wrapper">
            <div class="org-tree">
              <!-- Level 1: Executive Management -->
              <div class="org-level">
                <div class="org-node exec">
                  <div class="org-role">Executive Leadership Team</div>
                  <div class="org-focus">Enterprise Strategy &amp; Capital Allocation</div>
                </div>
              </div>

              <div class="org-connector-v"></div>
              <div class="org-connector-h"></div>

              <!-- Level 2: Functional Directors -->
              <div class="org-level" style="margin-top: 1rem;">
                <div class="org-node">
                  <div class="org-role">Strategic Operations</div>
                  <div class="org-focus">Process Standards &amp; Delivery</div>
                </div>
                <div class="org-node">
                  <div class="org-role">Commercial &amp; Markets</div>
                  <div class="org-focus">Growth &amp; Client Retention</div>
                </div>
                <div class="org-node">
                  <div class="org-role">Finance &amp; Governance</div>
                  <div class="org-focus">Capital, Risk &amp; Controls</div>
                </div>
                <div class="org-node">
                  <div class="org-role">People &amp; Capability</div>
                  <div class="org-focus">Talent &amp; Culture Architecture</div>
                </div>
              </div>

              <div class="org-connector-v"></div>
              <div class="org-connector-h" style="width: 85%;"></div>

              <!-- Level 3: Department Leads & Functional Teams -->
              <div class="org-level" style="margin-top: 1rem;">
                <div class="org-node" style="min-width: 140px; padding: 0.6rem 0.8rem;">
                  <div class="org-role" style="font-size: 0.8rem;">Core Workflows</div>
                  <div class="org-focus" style="font-size: 0.7rem;">SOPs &amp; Quality</div>
                </div>
                <div class="org-node" style="min-width: 140px; padding: 0.6rem 0.8rem;">
                  <div class="org-role" style="font-size: 0.8rem;">Supply Chain</div>
                  <div class="org-focus" style="font-size: 0.7rem;">Procurement &amp; Logistics</div>
                </div>
                <div class="org-node" style="min-width: 140px; padding: 0.6rem 0.8rem;">
                  <div class="org-role" style="font-size: 0.8rem;">Account Strategy</div>
                  <div class="org-focus" style="font-size: 0.7rem;">Revenue Management</div>
                </div>
                <div class="org-node" style="min-width: 140px; padding: 0.6rem 0.8rem;">
                  <div class="org-role" style="font-size: 0.8rem;">Cost Analytics</div>
                  <div class="org-focus" style="font-size: 0.7rem;">Budget Variance</div>
                </div>
                <div class="org-node" style="min-width: 140px; padding: 0.6rem 0.8rem;">
                  <div class="org-role" style="font-size: 0.8rem;">Talent Pipeline</div>
                  <div class="org-focus" style="font-size: 0.7rem;">Recruitment &amp; Retention</div>
                </div>
              </div>
            </div>
          </div>
          <div style="font-size: 0.75rem; color: var(--secondary-text); margin-top: 0.75rem;">
            <strong>Illustrative Note:</strong> Actual organizational models are customized based on business scale, geographic presence, and functional complexity.
          </div>
        </div>
        """
    elif framework_type == "performance_dashboard":
        return f"""
        <div class="dashboard-container">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Illustrative Business Performance Dashboard</h4>
              <p>Executive management monitoring view tracking operational velocity, efficiency index, and margin variance.</p>
            </div>
            <span class="demo-watermark">Illustrative Demo Data</span>
          </div>

          <div class="metrics-grid">
            <div class="metric-card">
              <div class="metric-card-label">Operational Efficiency Index</div>
              <div class="metric-card-val">84.2%</div>
              <div class="metric-card-status metric-status-good">&uarr; +6.8% vs. Baseline</div>
            </div>
            <div class="metric-card">
              <div class="metric-card-label">Process Turnaround Time</div>
              <div class="metric-card-val">4.2 Days</div>
              <div class="metric-card-status metric-status-good">&darr; -38% Cycle Time</div>
            </div>
            <div class="metric-card">
              <div class="metric-card-label">Capacity Utilization</div>
              <div class="metric-card-val">91.5%</div>
              <div class="metric-card-status metric-status-good">Optimal Operating Zone</div>
            </div>
            <div class="metric-card">
              <div class="metric-card-label">Unresolved Action Items</div>
              <div class="metric-card-val">3</div>
              <div class="metric-card-status metric-status-info">Within Governance SLA</div>
            </div>
          </div>

          <div style="background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.25rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
              <h5 style="font-size: 0.9rem; color: var(--primary-navy);">Performance Trajectory: Baseline vs. Optimized (Illustrative Trend)</h5>
              <div style="font-size: 0.75rem; display: flex; gap: 1rem;">
                <span style="color: #477BB7; font-weight: 600;">&bull; Optimized Intervention</span>
                <span style="color: #B69A65; font-weight: 600;">-- Baseline Model</span>
              </div>
            </div>
            <canvas id="performanceTrendCanvas" style="width: 100%; height: 200px; display: block;"></canvas>
          </div>
          <div style="font-size: 0.75rem; color: var(--secondary-text); margin-top: 0.75rem; text-align: right;">
            All metrics represent synthesized demo data for advisory conceptualization purposes only.
          </div>
        </div>
        """
    elif framework_type == "workflow_compare":
        return f"""
        <div class="dashboard-container">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Before vs. After Workflow Optimization Comparison</h4>
              <p>Illustrative value stream re-engineering demonstrating bottleneck elimination and handoff simplification.</p>
            </div>
            <span class="demo-watermark">Illustrative Diagnostic</span>
          </div>

          <div class="workflow-compare">
            <div class="workflow-column">
              <div class="workflow-col-title" style="color: #B91C1C;">
                <span>Current State (Pre-Consulting)</span>
                <span>8 Steps &bull; High Friction</span>
              </div>
              <div class="workflow-step workflow-step-interactive bottleneck" data-title="Manual Work Order Intake" data-bottleneck="Unstandardized intake via email leading to missing parameters" data-solution="Introduce structured intake webform with mandatory criteria">
                <div>
                  <strong>1. Unstructured Request Intake</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">High rework, 38% missing data</div>
                </div>
                <span class="badge" style="background: #FEE2E2; color: #991B1B;">Friction</span>
              </div>
              <div class="workflow-step workflow-step-interactive bottleneck" data-title="Multi-Layer Departmental Review" data-bottleneck="3 redundant managerial sign-offs adding 48 hours idle time" data-solution="Establish pre-approved threshold rules and single approval gate">
                <div>
                  <strong>2. Triple Tier Manual Sign-Off</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">48 hours average idle approval queue</div>
                </div>
                <span class="badge" style="background: #FEE2E2; color: #991B1B;">Bottleneck</span>
              </div>
              <div class="workflow-step workflow-step-interactive" data-title="Manual Data Entry to ERP" data-bottleneck="Duplicate entry between spreadsheet and core system" data-solution="Direct API integration / single data repository">
                <div>
                  <strong>3. Duplicate Spreadsheet Entry</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">Keying errors and data drift</div>
                </div>
                <span class="badge badge-subtle">Manual</span>
              </div>
              <div class="workflow-step workflow-step-interactive bottleneck" data-title="Uncoordinated Fulfillment Delivery" data-bottleneck="No real-time status visibility across frontline teams" data-solution="Automated kanban workflow and status notifications">
                <div>
                  <strong>4. Fragmented Fulfillment Hand-Off</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">Uncertain SLA tracking</div>
                </div>
                <span class="badge" style="background: #FEE2E2; color: #991B1B;">Delay</span>
              </div>
            </div>

            <div class="workflow-column">
              <div class="workflow-col-title" style="color: #047857;">
                <span>Future State (Optimized Architecture)</span>
                <span>4 Steps &bull; Streamlined</span>
              </div>
              <div class="workflow-step workflow-step-interactive optimized" data-title="Standardized Intake Portal" data-bottleneck="None" data-solution="Auto-validated inputs and immediate routing">
                <div>
                  <strong>1. Standardized Digital Intake</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">100% parameter completeness guaranteed</div>
                </div>
                <span class="badge" style="background: #D1FAE5; color: #065F46;">Clean</span>
              </div>
              <div class="workflow-step workflow-step-interactive optimized" data-title="Rule-Based Decision Gate" data-bottleneck="None" data-solution="Automated threshold bypass for standard orders">
                <div>
                  <strong>2. Automated Rule-Based Approval</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">Instant clearance under defined value thresholds</div>
                </div>
                <span class="badge" style="background: #D1FAE5; color: #065F46;">Instant</span>
              </div>
              <div class="workflow-step workflow-step-interactive optimized" data-title="Synchronized Execution Queue" data-bottleneck="None" data-solution="Direct operational assignment with clear SLA timer">
                <div>
                  <strong>3. Direct Production Scheduling</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">Zero manual re-keying; automated dispatch</div>
                </div>
                <span class="badge" style="background: #D1FAE5; color: #065F46;">Synced</span>
              </div>
              <div class="workflow-step workflow-step-interactive optimized" data-title="Automated Quality & Review" data-bottleneck="None" data-solution="Closed-loop verification and stakeholder notification">
                <div>
                  <strong>4. Closed-Loop Verification &amp; SLA Close</strong>
                  <div style="font-size: 0.75rem; color: var(--secondary-text);">Automated customer confirmation and logging</div>
                </div>
                <span class="badge" style="background: #D1FAE5; color: #065F46;">Verified</span>
              </div>
            </div>
          </div>

          <div id="workflow-step-inspector" class="mt-2">
            <div style="background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1rem 1.25rem;">
              <span class="badge badge-subtle mb-1">Diagnostic Detail</span>
              <p style="font-size: 0.85rem; margin-bottom: 0;">Click on any workflow stage above to inspect the specific operational friction and consulting remediation strategy.</p>
            </div>
          </div>
        </div>
        """
    else:
        # Generic Strategic Roadmap / Framework
        return f"""
        <div class="dashboard-container">
          <div class="dashboard-header">
            <div class="dashboard-title-group">
              <h4>Strategic Advisory Implementation Roadmap</h4>
              <p>Phased consulting execution architecture tailored to manage risk and deliver structured milestones.</p>
            </div>
            <span class="demo-watermark">Illustrative Demo Roadmap</span>
          </div>

          <div class="roadmap-flow">
            <div class="roadmap-phase active">
              <div class="phase-number">Phase 1 &bull; Weeks 1-3</div>
              <div class="phase-title">Diagnostic &amp; Discovery</div>
              <ul class="phase-items">
                <li>Leadership alignment interviews</li>
                <li>Current-state operational review</li>
                <li>Core data and metric gathering</li>
                <li>Friction &amp; bottleneck identification</li>
              </ul>
            </div>

            <div class="roadmap-phase">
              <div class="phase-number">Phase 2 &bull; Weeks 4-6</div>
              <div class="phase-title">Strategy &amp; Architecture</div>
              <ul class="phase-items">
                <li>Future-state blueprint design</li>
                <li>Resource &amp; capacity modeling</li>
                <li>Governance &amp; decision rights mapping</li>
                <li>Prioritized initiative scoring</li>
              </ul>
            </div>

            <div class="roadmap-phase">
              <div class="phase-number">Phase 3 &bull; Weeks 7-10</div>
              <div class="phase-title">Enablement &amp; Rollout</div>
              <ul class="phase-items">
                <li>Pilot program execution</li>
                <li>Standard operating procedure rollout</li>
                <li>Leadership cadence launch</li>
                <li>KPI tracking &amp; baseline calibration</li>
              </ul>
            </div>

            <div class="roadmap-phase">
              <div class="phase-number">Phase 4 &bull; Ongoing</div>
              <div class="phase-title">Review &amp; Governance</div>
              <ul class="phase-items">
                <li>Monthly executive review rhythm</li>
                <li>Milestone variance analysis</li>
                <li>Continuous optimization loop</li>
                <li>Long-term capability institutionalization</li>
              </ul>
            </div>
          </div>
          <div style="font-size: 0.75rem; color: var(--secondary-text); margin-top: 0.75rem; text-align: right;">
            Illustrative implementation schedule &bull; Tailored to individual organizational complexity upon proposal.
          </div>
        </div>
        """

def build_service_page(service):
    slug = service["slug"]
    filename = f"{slug}.html"
    title = service["title"]
    desc = service["description"]
    eyebrow = service["eyebrow"]
    headline = service["headline"]
    img_name = service["image"]
    challenges = service["challenges"]
    deliverables = service["deliverables"]
    framework_type = service["framework_type"]

    challenges_html = "".join([f"<li><strong>{c.split(' ', 2)[0]} {c.split(' ', 2)[1] if len(c.split(' ', 2))>1 else ''}:</strong> {c}</li>" for c in challenges])
    deliverables_html = "".join([f"<li><strong>{d.split(' ', 2)[0]} {d.split(' ', 2)[1] if len(d.split(' ', 2))>1 else ''}:</strong> {d}</li>" for d in deliverables])
    framework_html = render_framework_html(framework_type, title)

    body = f"""
    <!-- Page Header -->
    <section class="page-header">
      <div class="container">
        <div class="page-header-content">
          <nav class="breadcrumbs" aria-label="Breadcrumb">
            <ol>
              <li><a href="index.html">Home</a></li>
              <li><span>&rsaquo;</span></li>
              <li><a href="services.html">Services</a></li>
              <li><span>&rsaquo;</span></li>
              <li class="current" aria-current="page">{title}</li>
            </ol>
          </nav>
          <span class="badge badge-gold mb-1">{eyebrow}</span>
          <h1>{headline}</h1>
          <p class="lead">{desc}</p>
        </div>
      </div>
    </section>

    <!-- Main Service Content Section -->
    <section class="section">
      <div class="container">
        <div class="hero-inner" style="align-items: start; margin-bottom: 3.5rem;">
          <div>
            <span class="section-eyebrow">Advisory Capability</span>
            <h2 class="section-title">Strategic Clarity for Complex Management Scenarios</h2>
            <p>Organizations reach inflection points where historical operating habits no longer yield required performance. Whether facing market turbulence, organizational friction, or aggressive expansion goals, sustainable progress demands rigorous diagnosis, objective structural clarity, and disciplined execution.</p>
            <p>Our management consulting approach pairs analytical rigor with practical operational realities. We do not provide abstract theory; we design actionable frameworks, clear governance mechanisms, and transparent accountability systems that leadership teams can confidently implement.</p>

            <div class="mt-3">
              <a href="book-consultation.html" class="btn btn-gold">Discuss This Service With an Advisor</a>
              <a href="services.html" class="btn btn-outline" style="margin-left: 0.5rem;">Explore All 17 Services</a>
            </div>
          </div>

          <div>
            {make_placeholder(img_name, "ratio-4x3", title, "Recommended: 1000x750px | Executive Environment")}
          </div>
        </div>

        <!-- Challenges Addressed Grid -->
        <div class="section-header" style="margin-top: 4rem;">
          <span class="section-eyebrow">Executive Diagnosis</span>
          <h2 class="section-title">Common Business Challenges We Address</h2>
          <p class="section-subtitle">Leadership teams frequently engage our management consulting practice when confronting one or more of these core organizational inflection points:</p>
        </div>

        <div class="card-grid-2">
          <div class="card" style="border-left: 4px solid #EF4444;">
            <h4 style="margin-bottom: 1rem; color: var(--primary-navy);">Core Organizational Symptoms</h4>
            <ul style="font-size: 0.9375rem; color: var(--secondary-text); padding-left: 1.25rem; list-style: disc; line-height: 1.7;">
              {challenges_html}
            </ul>
          </div>

          <div class="card" style="border-left: 4px solid var(--accent-blue);">
            <h4 style="margin-bottom: 1rem; color: var(--primary-navy);">Consulting Deliverables &amp; Artifacts</h4>
            <ul style="font-size: 0.9375rem; color: var(--secondary-text); padding-left: 1.25rem; list-style: disc; line-height: 1.7;">
              {deliverables_html}
            </ul>
          </div>
        </div>

        <!-- Visual Framework / Dashboard Component -->
        <div style="margin-top: 4.5rem;">
          <div class="section-header">
            <span class="section-eyebrow">Framework Architecture</span>
            <h2 class="section-title">Consulting Framework &amp; Operating Model</h2>
            <p class="section-subtitle">A structured, reproducible methodology for diagnosing friction, defining target states, and governing execution.</p>
          </div>
          {framework_html}
        </div>

        <!-- 5-Stage Methodology Integration Notice -->
        <div class="card mt-4" style="background: #F8FAFC; border-color: var(--border-color);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem;">
            <div>
              <span class="badge badge-gold mb-1">Our Methodology</span>
              <h4 style="margin-bottom: 0.35rem;">How We Execute This Consulting Practice</h4>
              <p style="font-size: 0.9rem; margin-bottom: 0;">This advisory service follows our rigorous five-stage consulting methodology: Understand, Assess, Diagnose, Recommend, and Support.</p>
            </div>
            <a href="methodology.html" class="btn btn-outline">Explore Five-Stage Approach &rarr;</a>
          </div>
        </div>

        <!-- Case Study Linkage -->
        <div class="card mt-3" style="background: #FFFFFF; border-left: 4px solid var(--muted-gold);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1.5rem;">
            <div>
              <span class="badge badge-demo mb-1">Demonstration Case Study</span>
              <h4 style="margin-bottom: 0.35rem;">Review an Illustrative Advisory Case Study</h4>
              <p style="font-size: 0.9rem; margin-bottom: 0;">Examine how our structured diagnostic and strategic recommendations are packaged into an executive engagement summary.</p>
            </div>
            <a href="case-study-details.html" class="btn btn-primary btn-sm">Read Sample Case Study &rarr;</a>
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

    render_page(filename, title, desc, body)

if __name__ == "__main__":
    for s in SERVICES:
        build_service_page(s)
    print(f"Successfully generated all {len(SERVICES)} service pages.")
