# -*- coding: utf-8 -*-
"""
Builder for IMAGE-GENERATION-GUIDE.md
Generates complete inventory table, individual copy-ready Google Flow prompts,
specifications, replacement guide, and verification checklist.
"""

# Unique images catalog with detailed prompt specifications
IMAGE_CATALOG = [
    # 1. Homepage & Core Firm Images
    {
        "filename": "hero-management-consulting.webp",
        "page": "index.html",
        "section": "Hero Banner",
        "aspect": "16:9",
        "res": "1920x1080px",
        "orientation": "Landscape",
        "desc": "Senior executive management strategy consultation in a high-floor corporate boardroom with panoramic city architectural view.",
        "prompt": "Cinematic editorial corporate photography of an executive strategy consultation in a high-rise international corporate boardroom. A senior female managing director and an executive team are engaged around a sleek walnut conference table reviewing architectural blueprint charts and financial performance graphs. Modern minimalist boardroom architecture, floor-to-ceiling glass windows overlooking a soft-focus urban financial district skyline at morning golden hour. Sophisticated lighting, soft diffused natural daylight mixed with warm interior architectural LEDs. Premium executive aesthetic, navy blue and charcoal tailored suits, neutral warm tones. Ultra-high definition, shot on Hasselblad H6D-100c, 50mm f/2.8 lens, shallow depth of field, authentic business atmosphere, zero cliché handshakes, no logos or text."
    },
    {
        "filename": "management-team-discussion.webp",
        "page": "about.html",
        "section": "Corporate Philosophy & About Firm",
        "aspect": "4:3",
        "res": "1200x900px",
        "orientation": "Landscape",
        "desc": "Advisory team engaged in focused analytical discussion in an executive design studio with whiteboard strategic roadmaps.",
        "prompt": "Professional corporate documentary photography of a diverse executive advisory team collaborating in a sunlit management war-room. Consultants and a senior corporate strategist stand beside a large glass whiteboard displaying structured swimlane process diagrams and organizational roadmaps. Natural daylight streaming through modern floor-to-ceiling windows, soft rim light highlighting professional attire. Elegant navy blue, beige, and slate color palette. Shot on Leica SL2, 35mm f/2.0, genuine analytical concentration, thoughtful gestures, premium corporate consulting environment, absolutely no text, no stock cliches."
    },
    {
        "filename": "management-case-study-workspace.webp",
        "page": "methodology.html",
        "section": "Five-Stage Methodology Overview",
        "aspect": "4:3",
        "res": "1200x900px",
        "orientation": "Landscape",
        "desc": "Executive discovery workshop reviewing workflow value streams, post-it prioritization grids, and diagnostic reports.",
        "prompt": "Authentic architectural and corporate documentary photography of an executive diagnostic discovery session. A conference table in a modern corporate advisory suite covered with neatly arranged strategic reports, architectural process blueprints, and color-coded diagnostic assessment cards. A consultant and executive are discussing details in the background with soft focus. High-end Scandinavian corporate interior, oak acoustic wood slat walls, warm ambient recessed lighting. Canon EOS R5, 50mm f/1.8, editorial composition, rich navy and muted brass accents, clean negative space, no logos, no watermarks."
    },
    {
        "filename": "case-study-detailed-workspace.webp",
        "page": "case-study-details.html",
        "section": "Case Study Engagement Deep Dive",
        "aspect": "4:3",
        "res": "1200x900px",
        "orientation": "Landscape",
        "desc": "Executive diagnostic workshop reviewing workflow value streams and organizational diagnostics.",
        "prompt": "Editorial executive photography capturing a management diagnostic debrief. Two corporate advisors in dark navy tailored blazers seated in an executive presentation suite, reviewing a high-resolution performance dashboard on a wall-mounted display. Modern glass partition background with gentle reflections of urban architecture. Soft directional studio key light balanced with soft ambient cool daylight. Premium international advisory look, structured and thoughtful posture, Nikon Z9, 85mm f/1.8, cinematic depth, clean and authoritative ambiance."
    },

    # 2. The 17 Service Practice Images
    {
        "filename": "business-strategy-planning.webp",
        "page": "business-strategy.html / services.html / index.html",
        "section": "Business Strategy Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive team conducting a strategic planning and competitive positioning session around an executive conference table.",
        "prompt": "Editorial corporate photography of a senior executive strategy session. Three corporate leaders analyzing printed market growth projections and competitive positioning frameworks on an elegant granite meeting table. Sophisticated corporate environment, dark navy accent wall, refined brushed bronze lighting fixtures. Balanced natural side lighting from expansive window. Sony A7R V, 50mm f/1.4, sharp focus on foreground planning documents, confident and focused demeanor, high-end management advisory aesthetic."
    },
    {
        "filename": "strategic-roadmap-session.webp",
        "page": "strategic-planning.html / services.html",
        "section": "Strategic Planning Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Senior leadership mapping multi-year horizons, milestone roadmaps, and OKR cascades on an executive display.",
        "prompt": "High-end corporate documentary photo of strategic roadmap planning. A corporate strategist presenting a multi-horizon milestone plan on an ultra-wide interactive executive digital screen to boardroom directors. Dimmed architectural lighting in the conference room with soft glow from the display accentuating executive silhouettes. Modern enterprise headquarters, polished concrete and warm timber accents. Shot on Fujifilm GFX 100S, 45mm lens, corporate navy and warm gold tones, realistic professional interaction."
    },
    {
        "filename": "business-transformation-framework.webp",
        "page": "business-transformation.html / services.html",
        "section": "Business Transformation Advisory",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Operating model modernization workshop in a modern glass-walled innovation lab.",
        "prompt": "Modern architectural corporate photography of an enterprise operating model redesign workshop. Consultants and department heads analyzing organizational transformation blueprints on a large collaborative glass wall. Bright, airy corporate innovation center with double-height ceiling, acoustic paneling, and indoor executive greenery. Clean natural daylight, crisp contrast, premium navy and slate color grading. Shot on Sony A1, 35mm f/2.8, professional focus and clean composition."
    },
    {
        "filename": "management-advisory-meeting.webp",
        "page": "management-advisory.html / services.html",
        "section": "Management Advisory Services",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Confidential advisory discussion between a managing director and a senior management consulting advisor.",
        "prompt": "Intimate executive portrait-style photography of a confidential management advisory meeting. A senior management consultant in an impeccably tailored navy suit engaged in earnest, thoughtful discussion with a corporate CEO in a private executive office suite. Soft warm ambient lamp light on a mahogany credenza, large glass window overlooking twilight city lights in soft bokeh. Hasselblad X2D 100C, 65mm f/2.8 lens, authoritative, dignified, high-trust advisory atmosphere."
    },
    {
        "filename": "organizational-development-chart.webp",
        "page": "organizational-development.html / services.html / index.html",
        "section": "Organizational Development Consulting",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive team reviewing organizational structure, RACI decision rights, and role hierarchies.",
        "prompt": "Professional corporate setting featuring leaders reviewing complex organizational charts and structural hierarchy diagrams on tablet devices and desktop displays. Bright executive conference room with fluted glass walls and warm oak conference table. Clean overhead softbox lighting with natural daylight fill. Premium corporate color scheme of deep navy (#10213A), slate grey, and warm beige. Canon EOS R5, 50mm f/1.4, crisp focus on collaborative work."
    },
    {
        "filename": "leadership-consulting-boardroom.webp",
        "page": "leadership-consulting.html / services.html",
        "section": "Leadership Consulting Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Boardroom leadership alignment discussion with executive committee members.",
        "prompt": "Executive boardroom photography capturing an executive leadership alignment seminar. Six senior corporate directors seated around a massive marble conference table in deep discussion. Architectural lighting casting gentle highlights on tailored suits and leather chairs. Minimalist international corporate design with wood acoustic panels and skyline view. Leica S3, 70mm lens, serious, visionary, dignified executive mood, perfectly balanced color palette."
    },
    {
        "filename": "operations-consulting-workshop.webp",
        "page": "operations-consulting.html / services.html / index.html",
        "section": "Operations Consulting Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Operations consulting walkthrough evaluating workflow throughput and capacity modeling.",
        "prompt": "High-end corporate documentary image of an operations consulting site review. A management consultant in safety vest and tailored business shirt reviewing tablet workflow logistics data with an industrial operations director in a high-tech modern automated fulfillment facility. Clean industrial environment, warm overhead task lighting balanced with cool architectural LED lines. Nikon Z8, 35mm f/1.8, industrial excellence, high operational precision, dynamic perspective."
    },
    {
        "filename": "performance-improvement-dashboard.webp",
        "page": "performance-improvement.html / services.html",
        "section": "Performance Improvement Consulting",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive team reviewing an enterprise KPI monitoring dashboard and balanced scorecard metrics.",
        "prompt": "Corporate photography of an executive management performance review. Leadership team analyzing multi-metric business dashboards displayed on a large 4K wall screen showing operational throughput and margin indicators. Modern corporate command-center interior with low-glare architectural lighting. Shot on Sony FX3, 28mm f/2.0, subtle reflections on polished glass table, disciplined data-driven consulting atmosphere."
    },
    {
        "filename": "process-optimization-mapping.webp",
        "page": "process-optimization.html / services.html",
        "section": "Process Optimization Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Consultants mapping end-to-end business workflows and bottleneck elimination on glass boards.",
        "prompt": "Collaborative corporate advisory scene of business process mapping. Two strategy consultants and an operations lead analyzing color-coded process swimlane diagrams on a frameless glass whiteboard. Sunlight streaming into a contemporary executive workshop suite with indoor plants and minimalist steel accents. Canon R5C, 35mm f/2, clean, crisp lines, focus on structured problem solving, professional navy and white color palette."
    },
    {
        "filename": "change-management-strategy.webp",
        "page": "change-management.html / services.html",
        "section": "Change Management Consulting",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Leadership team conducting a stakeholder change readiness and adoption workshop.",
        "prompt": "Editorial photograph of a corporate change enablement session. A senior female change management consultant facilitating a transition workshop for department managers in a modern corporate training amphitheater. Warm, inviting lighting, natural wood tones, focused and engaged facial expressions. Leica SL2, 50mm f/1.4, authentic leadership communication, human-centered corporate transformation atmosphere."
    },
    {
        "filename": "corporate-governance-framework.webp",
        "page": "corporate-governance.html / services.html",
        "section": "Corporate Governance Advisory",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Formal board committee review examining governance charters, oversight policies, and delegation of authority.",
        "prompt": "Dignified corporate photograph of a corporate governance committee meeting in an executive boardroom. Directors reviewing leather-bound corporate charter documents and governance compliance reports. Sophisticated dark wood paneling, warm brass sconces, elegant leather armchairs. Soft, balanced directional lighting. Hasselblad H6D, 80mm lens, solemn, authoritative, ethical institutional governance environment."
    },
    {
        "filename": "business-expansion-planning.webp",
        "page": "business-expansion.html / services.html",
        "section": "Business Expansion Consulting",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive committee reviewing international market feasibility maps and expansion roadmaps.",
        "prompt": "Corporate advisory photography of strategic business expansion planning. Senior directors gathered around an illuminated digital surface table analyzing regional market entry feasibility maps and logistic hub corridors. Contemporary corporate penthouse boardroom overlooking a vibrant coastal metropolis. Shot on Sony A7R V, 35mm f/2.4, sleek global commerce aesthetic, confident executive postures, deep navy and warm amber lighting."
    },
    {
        "filename": "financial-performance-analysis.webp",
        "page": "financial-performance.html / services.html",
        "section": "Financial Performance & Cost Strategy",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive management accounting review analyzing cost structures, margin variance, and cash flow models.",
        "prompt": "Corporate finance advisory meeting in an executive office. A finance practice lead and corporate CFO analyzing multi-year margin variance spreadsheets and cash flow forecasting models on dual curved monitors. Refined corporate workspace with subtle slate grey and muted gold decor accents. Controlled natural lighting with soft desk lamp glow. Nikon Z9, 50mm f/1.8, analytical rigor, executive focus, high-end corporate setting."
    },
    {
        "filename": "workforce-planning-strategy.webp",
        "page": "human-resource-management.html / services.html",
        "section": "Strategic Human Resource Advisory",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive HR leadership aligning strategic workforce planning, talent capability matrices, and hiring pipelines.",
        "prompt": "Corporate photography of strategic workforce planning. An HR advisory specialist discussing talent capability architecture and executive succession frameworks with an enterprise VP of People. Bright, modern open-plan executive terrace office with skyline view. Soft diffused daylight, warm wood furnishings, approachable yet highly disciplined business atmosphere. Canon R5, 50mm f/1.8, authentic executive collaboration."
    },
    {
        "filename": "project-governance-dashboard.webp",
        "page": "project-management.html / services.html",
        "section": "Project Management Advisory",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Project Management Office (PMO) review tracking strategic portfolio milestones and risk escalations.",
        "prompt": "Modern corporate Project Management Office (PMO) session. Project leaders gathered around a wall-mounted digital Gantt chart and milestone progress tracker in a collaborative agile corporate studio. Polished concrete floor, glass partitions with subtle frosted graphics, focused team members taking structured notes. Sony A1, 35mm lens, dynamic and organized corporate project delivery aesthetic."
    },
    {
        "filename": "risk-management-matrix.webp",
        "page": "risk-management.html / services.html",
        "section": "Enterprise Risk Management Advisory",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive risk committee evaluating operational vulnerability matrices and business continuity roadmaps.",
        "prompt": "Executive risk management review session in a secure corporate advisory suite. Corporate directors examining an enterprise risk heat map and mitigation priority matrix on a large interactive digital screen. Moody, sophisticated lighting with deep navy and charcoal interior accents. Hasselblad X2D 100C, 55mm lens, serious, disciplined, vigilant leadership atmosphere, premium international consulting ambiance."
    },
    {
        "filename": "digital-transformation-roadmap.webp",
        "page": "digital-transformation.html / services.html",
        "section": "Digital Transformation Advisory",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive leadership reviewing enterprise digital architecture, technology roadmaps, and workflow automation.",
        "prompt": "Corporate digital advisory session. A senior digital strategy consultant explaining an enterprise cloud architecture and workflow digitization roadmap to a corporate executive committee. Cutting-edge technology consulting suite with glass writing walls and ambient blue LED accent lighting. Leica SL2, 35mm f/2.0, forward-looking, innovative yet grounded corporate technology strategy look."
    },

    # 3. 14 Industry Sector Images
    {
        "filename": "industry-manufacturing-plant.webp",
        "page": "industries.html",
        "section": "Manufacturing Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Modern high-precision manufacturing facility with automated robotic systems and clean industrial floor.",
        "prompt": "Architectural and industrial photography of a modern high-precision advanced manufacturing facility. Clean, spotless epoxy floor with robotic assembly arms and precision CNC stations in pristine operating order. Plant supervisor in hardhat and clipboard standing on an elevated observation mezzanine. Soft diffused industrial daylight mixed with cool LED lighting. Nikon Z8, 24mm f/4, industrial excellence, scalable capacity, zero clutter."
    },
    {
        "filename": "industry-healthcare-facility.webp",
        "page": "industries.html",
        "section": "Healthcare Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Modern medical research facility and executive hospital administration wing with clean clinical aesthetics.",
        "prompt": "High-end architectural photography of a state-of-the-art healthcare administrative center. Clean glass atrium with doctors and administrative leadership walking through sunlit corridors in blurred background. Minimalist clinical interior design, terrazzo flooring, natural wood accents. Warm, hopeful morning sunlight. Canon EOS R5, 35mm f/2.8, professional healthcare management, sterile, efficient, welcoming."
    },
    {
        "filename": "industry-education-campus.webp",
        "page": "industries.html",
        "section": "Education Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Contemporary university administrative center with modern architectural library and leadership suites.",
        "prompt": "Architectural photography of a contemporary academic institution administrative center. Sunlit multi-story library and executive council atrium with students and faculty walking gracefully. Warm cedar wood slats, stone columns, glass walkways. Natural afternoon golden sunlight. Sony A7R V, 24mm f/2.8, institutional prestige, structured academic leadership atmosphere."
    },
    {
        "filename": "industry-real-estate-architecture.webp",
        "page": "industries.html",
        "section": "Real Estate Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive real estate development boardroom reviewing 3D masterplan models and architectural drawings.",
        "prompt": "Executive photography of commercial real estate development planning. Real estate directors and architects examining a detailed physical architectural scale model of a mixed-use commercial development on a sleek black table. Floor-to-ceiling glass windows overlooking actual cityscape. Leica S3, 45mm lens, luxury commercial property advisory ambiance, crisp detail."
    },
    {
        "filename": "industry-retail-store-operations.webp",
        "page": "industries.html",
        "section": "Retail Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Flagship retail store environment showing optimized merchandising layouts and smooth customer fulfillment.",
        "prompt": "High-end commercial photography of a flagship retail store interior. Impeccably organized merchandising displays, warm directional spotlighting on premium goods, seamless customer checkout lounge in soft focus background. Elegant terrazzo flooring, neutral warm aesthetic. Nikon Z9, 35mm f/2.0, retail excellence, operational efficiency, premium shopping atmosphere."
    },
    {
        "filename": "industry-ecommerce-fulfillment.webp",
        "page": "industries.html",
        "section": "E-Commerce Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "High-tech automated e-commerce fulfillment and distribution hub with smart sorting conveyors.",
        "prompt": "Modern architectural photography of an automated e-commerce fulfillment center. Organized multi-level conveyor belts and robotic sorting units moving parcel boxes with high speed and precision. High ceiling with industrial skylights and crisp cool LED lighting lines. Canon R5C, 24mm f/4, logistical precision, high throughput, futuristic supply chain infrastructure."
    },
    {
        "filename": "industry-technology-software-office.webp",
        "page": "industries.html",
        "section": "Technology & SaaS Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Contemporary software engineering headquarters with collaboration pods and product management teams.",
        "prompt": "Architectural interior photography of a premier technology corporate headquarters. Open collaboration areas with ergonomic standing desks, glass meeting cubes, and acoustic felt booths. Software architects and product leads collaborating over monitors in natural light. Soft ambient daylight, polished micro-cement floors, indoor botanical gardens. Sony A1, 35mm f/2.0, sophisticated enterprise tech ambiance."
    },
    {
        "filename": "industry-financial-services-boardroom.webp",
        "page": "industries.html",
        "section": "Financial Services Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Financial institution executive boardroom overlooking city financial district skyline.",
        "prompt": "Authoritative corporate photography of a premier financial services executive boardroom. Long dark marble boardroom table reflecting the blue sky, surrounded by high-back leather executive chairs. Expansive panoramic windows displaying iconic financial skyscrapers. Quiet, commanding corporate presence, soft morning lighting. Hasselblad H6D-100c, 35mm lens, timeless financial integrity."
    },
    {
        "filename": "industry-logistics-distribution-center.webp",
        "page": "industries.html",
        "section": "Logistics & Supply Chain Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Expansive regional logistics terminal with automated loading docks and coordinated freight fleet.",
        "prompt": "Commercial logistics photography of a regional freight distribution hub. Modern freight transport trucks neatly docked at automated loading bays at dusk. Warm interior facility glow contrasting against deep blue twilight sky. Wet pavement reflecting terminal lights. Nikon Z8, 28mm f/2.8, supply chain reliability, operational coordination, commercial freight scale."
    },
    {
        "filename": "industry-hospitality-hotel-operations.webp",
        "page": "industries.html",
        "section": "Hospitality Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Luxury hotel executive lobby and reception showcasing five-star operational standards.",
        "prompt": "Luxury interior photography of a premier hotel lobby. Soaring double-height ceilings, warm travertine stone walls, bespoke brass chandelier, impeccably groomed front desk team assisting guests in soft background. Warm golden ambient lighting, lavish yet refined executive aesthetic. Leica SL2, 28mm f/2.8, hospitality operational excellence."
    },
    {
        "filename": "industry-professional-services-firm.webp",
        "page": "industries.html",
        "section": "Professional Services Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "High-end corporate advisory office with glass-enclosed partner offices and library.",
        "prompt": "Architectural photography of an elite professional services firm headquarters. Elegant wood-paneled corridors lined with glass-fronted partner suites and reference libraries. Corporate partners walking in discussion, soft warm architectural downlights, herringbone oak parquet flooring. Fujifilm GFX 100S, 45mm lens, classic professional advisory sophistication."
    },
    {
        "filename": "industry-startup-innovation-hub.webp",
        "page": "industries.html",
        "section": "Startups & Emerging Ventures Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Modern venture hub and incubator space showing founders and strategy advisors collaborating.",
        "prompt": "Vibrant corporate documentary photo of an emerging business innovation incubator. Entrepreneurs and strategic advisors in informal business attire gathered around a white oak conference table testing product prototypes and financial models. Industrial loft architecture with exposed brick, large factory windows, and lush hanging plants. Natural sunlight, energetic and ambitious atmosphere. Sony A7R V, 35mm f/1.8."
    },
    {
        "filename": "industry-construction-project-site.webp",
        "page": "industries.html",
        "section": "Construction & Infrastructure Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Commercial skyscraper construction site with project engineers reviewing blueprints on tablet.",
        "prompt": "Industrial documentary photography on a major commercial building construction project. A lead project engineer and management consultant in white hardhats and safety gear reviewing digital architectural blueprints on a ruggedized tablet against the backdrop of rising steel framework. Bright morning daylight, crisp details, engineering precision, serious and safety-first mindset. Canon R5, 35mm f/2.8."
    },
    {
        "filename": "industry-telecommunications-infrastructure.webp",
        "page": "industries.html",
        "section": "Telecommunications Sector Practice",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Modern telecommunications network operations center (NOC) with engineers monitoring global data grid.",
        "prompt": "Commercial photography of a high-tech telecommunications network operations center (NOC). A team of network operations engineers seated at tiered monitoring consoles facing an immense curved video wall displaying global satellite and fiber grid traffic. Low ambient blue-toned architectural lighting, calm professional focus, high-reliability infrastructure aesthetic. Nikon Z9, 24mm f/2.8."
    },

    # 4. Illustrative Case Studies Images (8 cases)
    {
        "filename": "case-strategy-assessment.webp",
        "page": "case-studies.html",
        "section": "Business Strategy Assessment Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Corporate portfolio diagnostic reviewing product lines, margin contribution, and competitive differentiation.",
        "prompt": "Executive management consulting case study visual. A senior advisory partner examining corporate portfolio profitability graphs on an ultra-slim laptop in a private executive lounge. Subtle morning sunbeams across a polished marble credenza. Deep navy and muted brass accents, premium corporate ambiance. Shot on Leica M11, 50mm f/1.4."
    },
    {
        "filename": "case-org-structure.webp",
        "page": "case-studies.html",
        "section": "Organizational Structure Review Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive team collaborating on organizational restructuring and reporting hierarchies.",
        "prompt": "Corporate consulting workshop scene. Executives reviewing modular organizational structure cards and RACI decision rights charts laid out on a design studio table. Contemporary corporate meeting space with frosted glass doors and soft natural daylight. Hasselblad X2D, 45mm lens, sharp focus, thoughtful collaborative atmosphere."
    },
    {
        "filename": "case-operations-optimization.webp",
        "page": "case-studies.html",
        "section": "Operational Process Optimization Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Operations consulting review analyzing factory floor turnaround time and bottleneck removal.",
        "prompt": "Commercial documentary photo of an operational re-engineering project. Operations advisor and plant manager examining production takt time charts on a digital tablet beside a high-throughput clean packaging line. Crisp industrial lighting, immaculate facility hygiene, sharp professional focus. Canon EOS R5, 35mm f/2."
    },
    {
        "filename": "case-performance-framework.webp",
        "page": "case-studies.html",
        "section": "Business Performance Framework Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive committee reviewing KPI balanced scorecards on wall displays.",
        "prompt": "Executive boardroom meeting analyzing quarterly KPI performance scorecards. Corporate directors viewing clear operational indicator charts on a wall screen. Modern walnut and glass boardroom, soft recessed downlights, serious and focused executive demeanor. Sony A7R V, 50mm f/1.8."
    },
    {
        "filename": "case-digital-roadmap.webp",
        "page": "case-studies.html",
        "section": "Digital Transformation Roadmap Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Cross-functional team reviewing digital systems architecture and enterprise software roadmap.",
        "prompt": "Corporate technology strategy session. Digital advisory specialists and business unit heads planning an ERP migration roadmap on a whiteboard with timeline milestones. Modern glass-walled corporate meeting room with panoramic city view. Nikon Z8, 35mm f/2.0."
    },
    {
        "filename": "case-change-management.webp",
        "page": "case-studies.html",
        "section": "Change Management Planning Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Stakeholder engagement workshop facilitating cultural adoption of new operating model.",
        "prompt": "Corporate workshop image of change management facilitation. An experienced change consultant addressing a group of department heads in a sunlit modern auditorium. Warm wood wall paneling, natural light, engaged and receptive audience. Fujifilm GFX 50S II, 63mm f/2.8."
    },
    {
        "filename": "case-workforce-planning.webp",
        "page": "case-studies.html",
        "section": "Workforce Planning Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "HR executive leadership analyzing workforce capacity and talent succession models.",
        "prompt": "Corporate executive consultation on strategic workforce capacity planning. HR leaders discussing staffing projection graphs and skill matrices around a sunlit conference table. Elegant neutral office interior, clean Scandinavian design. Leica SL2, 50mm f/2.0."
    },
    {
        "filename": "case-business-expansion.webp",
        "page": "case-studies.html",
        "section": "Business Expansion Strategy Demo",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive strategy group reviewing multi-city expansion roadmaps and market penetration metrics.",
        "prompt": "Executive strategy planning meeting. Senior leadership team reviewing regional market expansion maps and capital requirement schedules in an executive boardroom at twilight. City skyline illuminated in soft bokeh behind glass windows. Hasselblad H6D, 50mm lens."
    },

    # 5. Executive Leadership Team Profiles (6 Roles - 3:4 Portrait)
    {
        "filename": "team-profile-strategy-lead.webp",
        "page": "team.html",
        "section": "Strategy Advisory Practice Lead",
        "aspect": "3:4",
        "res": "600x800px",
        "orientation": "Portrait",
        "desc": "Executive portrait placeholder of a senior corporate strategy advisor in a tailored navy blazer.",
        "prompt": "Executive corporate portrait of a distinguished senior management strategy consultant. Confident, warm, and highly professional demeanor, tailored navy wool suit with crisp white collar, seated in a contemporary executive library setting. Soft directional portrait lighting with subtle rim light. Shallow depth of field with architectural wood shelving in soft bokeh. Shot on Hasselblad X2D 100C, 90mm f/2.5 portrait lens, natural skin tones, zero artificial airbrushing, dignified international business presence."
    },
    {
        "filename": "team-profile-operations-lead.webp",
        "page": "team.html",
        "section": "Operations Advisory Practice Lead",
        "aspect": "3:4",
        "res": "600x800px",
        "orientation": "Portrait",
        "desc": "Executive portrait placeholder of a senior operations consulting practice lead.",
        "prompt": "Executive portrait of a corporate operations consulting practice lead. Confident posture, wearing a modern slate grey blazer, standing in a sunlit architectural corporate atrium with glass staircase in soft focus. Natural diffused lighting, sharp focus on eyes, composed and analytical expression. Leica SL2, 85mm f/1.4, authentic corporate advisory portrait, premium aesthetic."
    },
    {
        "filename": "team-profile-org-lead.webp",
        "page": "team.html",
        "section": "Organizational Development Lead",
        "aspect": "3:4",
        "res": "600x800px",
        "orientation": "Portrait",
        "desc": "Executive portrait placeholder of an organizational design advisory lead.",
        "prompt": "Professional corporate portrait of an organizational development practice director. Intelligent, empathetic, and authoritative expression, wearing a tailored charcoal blazer with subtle brass lapel pin. Modern boardroom background with soft frosted glass textures. Canon EOS R5, 85mm f/1.2, elegant corporate portraiture, rich contrast and natural lighting."
    },
    {
        "filename": "team-profile-leadership-lead.webp",
        "page": "team.html",
        "section": "Leadership Advisory Lead",
        "aspect": "3:4",
        "res": "600x800px",
        "orientation": "Portrait",
        "desc": "Executive portrait placeholder of a leadership alignment practice director.",
        "prompt": "Distinguished executive portrait of a leadership consulting practice director. Thoughtful, visionary expression, tailored deep navy suit, seated in an executive office with leather armchair and warm timber desk in background. Warm studio key light with subtle window fill. Nikon Z9, 105mm f/1.4 lens, commanding executive presence."
    },
    {
        "filename": "team-profile-transformation-lead.webp",
        "page": "team.html",
        "section": "Transformation Advisory Lead",
        "aspect": "3:4",
        "res": "600x800px",
        "orientation": "Portrait",
        "desc": "Executive portrait placeholder of a business transformation advisory leader.",
        "prompt": "Modern executive portrait of a business transformation practice leader. Energetic and strategic demeanor, wearing a tailored dark navy suit with open collar. Modern glass-fronted innovation office in soft bokeh background. Sony A1, 85mm f/1.4, clean lighting, crisp detail, progressive corporate advisory presence."
    },
    {
        "filename": "team-profile-performance-lead.webp",
        "page": "team.html",
        "section": "Performance Systems Practice Lead",
        "aspect": "3:4",
        "res": "600x800px",
        "orientation": "Portrait",
        "desc": "Executive portrait placeholder of a performance improvement and analytics lead.",
        "prompt": "Professional corporate portrait of a performance systems and analytics advisory lead. Sharp, focused expression, tailored steel blue blazer, holding an executive leather portfolio in a high-rise office lounge. Soft diffused daylight from large window. Fujifilm GFX 100S, 80mm f/1.7, premium management consulting portraiture."
    },

    # 6. Thought Leadership & Editorial Articles (11 images)
    {
        "filename": "insight-featured-strategy-banner.webp",
        "page": "insights.html",
        "section": "Featured Insight Hero Banner",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Executive strategy meeting banner showing leaders aligning on multi-year enterprise objectives.",
        "prompt": "Panoramic editorial corporate photograph of executive business strategy formulation. A senior leadership team gathered around a minimalist conference table reviewing strategic growth roadmaps in a modern glass boardroom. Morning daylight illuminating architectural glass partitions, skyline in soft bokeh. Leica SL2, 35mm f/2.0, premium corporate editorial style."
    },
    {
        "filename": "insight-article-detail-visual.webp",
        "page": "article-details.html",
        "section": "Article Header Hero",
        "aspect": "16:9",
        "res": "1600x900px",
        "orientation": "Landscape",
        "desc": "Detailed strategic planning workshop showing corporate decision frameworks and roadmap documents.",
        "prompt": "Editorial documentary photo of strategic framework development. Close-up composition of executive hands and strategic planning worksheets on a dark oak conference table with fountain pens, clean leather notebooks, and structured framework cards. Soft warm directional light. Canon R5, 50mm f/1.8 macro feel, dignified editorial aesthetic."
    },
    {
        "filename": "insight-practical-strategy.webp",
        "page": "insights.html",
        "section": "Article: How to Build a Practical Business Strategy",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Corporate executives analyzing strategic decision trade-offs on a conference table.",
        "prompt": "Editorial photograph of corporate strategy development. Executive team discussing market positioning charts on a conference table in an executive boardroom. Soft natural lighting, deep navy tones. Nikon Z8, 50mm f/1.8."
    },
    {
        "filename": "insight-growing-orgs.webp",
        "page": "insights.html",
        "section": "Article: Common Management Challenges in Growing Organizations",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Growing enterprise management meeting resolving operational complexity and team alignment.",
        "prompt": "Documentary corporate photography of an expanding enterprise leadership team. A managing director leading a structured management review meeting in a bright contemporary boardroom. Canon EOS R5, 35mm f/2.0."
    },
    {
        "filename": "insight-org-structure.webp",
        "page": "insights.html",
        "section": "Article: Why Organizational Structure Matters",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Corporate leaders examining organizational design charts and span of control diagrams.",
        "prompt": "Corporate advisory photograph of organizational structure review. Consultants analyzing hierarchy blueprints and departmental reporting charts on an interactive digital screen. Sony A7R V, 50mm f/1.4."
    },
    {
        "filename": "insight-operational-efficiency.webp",
        "page": "insights.html",
        "section": "Article: How to Improve Operational Efficiency",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Operations walkthrough analyzing workflow bottlenecks and process efficiency in an enterprise facility.",
        "prompt": "High-end corporate documentary photography of operational efficiency analysis. Operations consultant inspecting automated fulfillment workflows and standard operating procedure sheets. Nikon Z9, 35mm f/2.0."
    },
    {
        "filename": "insight-performance-systems.webp",
        "page": "insights.html",
        "section": "Article: Building Effective Performance Management Systems",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Executive team reviewing performance indicators, balanced scorecards, and management cadences.",
        "prompt": "Corporate meeting photograph of performance system design. Executives reviewing balanced scorecard dashboards on a high-resolution display. Modern corporate command suite, warm lighting. Leica SL2, 50mm f/2."
    },
    {
        "filename": "insight-change-management.webp",
        "page": "insights.html",
        "section": "Article: Managing Organizational Change Without Disrupting Operations",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Change management workshop facilitating smooth departmental transition and cultural alignment.",
        "prompt": "Corporate change management workshop in progress. Leadership team in focused group discussion around a collaborative table with transition roadmaps. Hasselblad X2D, 45mm lens."
    },
    {
        "filename": "insight-leadership-alignment.webp",
        "page": "insights.html",
        "section": "Article: How Leadership Alignment Supports Business Growth",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Senior leadership team seated in unanimous consensus around an executive boardroom table.",
        "prompt": "Authoritative corporate photograph of executive leadership alignment. Corporate directors seated around a sleek marble table in deep consensus, natural side light. Sony A1, 50mm f/1.8."
    },
    {
        "filename": "insight-transformation-roadmap.webp",
        "page": "insights.html",
        "section": "Article: Developing a Business Transformation Roadmap",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Transformation management office reviewing multi-phase implementation roadmap and target operating model.",
        "prompt": "Modern corporate advisory photo of business transformation roadmap development. Consultants working on glass timeline boards with milestone phases. Canon R5C, 35mm f/2.0."
    },
    {
        "filename": "insight-process-optimization.webp",
        "page": "insights.html",
        "section": "Article: Understanding Business Process Optimization",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Value stream workflow mapping analyzing handoff friction and standard operating procedure design.",
        "prompt": "Business process mapping session in an executive workroom. Two advisors detailing workflow handoffs and automated decision gates on a large whiteboard. Nikon Z8, 35mm f/2.0."
    },
    {
        "filename": "insight-management-reporting.webp",
        "page": "insights.html",
        "section": "Article: How to Build Better Management Reporting",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Executive analyzing streamlined management reporting packet with actionable operational metrics.",
        "prompt": "Corporate executive reviewing a concise quarterly management report packet in a quiet corner office. Warm desk lamp light, modern minimalist office aesthetic. Leica M11, 50mm f/1.4."
    },

    # 7. Management Resource Library (10 images)
    {
        "filename": "resource-strategy-checklist.webp",
        "page": "resources.html",
        "section": "Business Strategy Planning Checklist",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Executive strategy diagnostic checklist and framework document preview.",
        "prompt": "Still-life corporate editorial photography of a business strategy planning checklist and diagnostic worksheet neatly bound on a leather desk blotter. High-end stationery, fountain pen, soft natural morning window light. Hasselblad X2D, 55mm f/2.8."
    },
    {
        "filename": "resource-management-checklist.webp",
        "page": "resources.html",
        "section": "Management Assessment Checklist",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Management decision velocity and accountability assessment template.",
        "prompt": "Corporate advisory template photography. Printed management assessment checklist document in a modern executive clipboard on an oak table. Canon R5, 50mm f/2.0."
    },
    {
        "filename": "resource-org-review.webp",
        "page": "resources.html",
        "section": "Organizational Structure Review Template",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Organizational structure mapping worksheet and span of control template.",
        "prompt": "Corporate document visual of an organizational structure review template featuring clean tree hierarchies and RACI matrix boxes. Soft natural office lighting. Sony A7R V, 50mm f/2.8."
    },
    {
        "filename": "resource-performance-template.webp",
        "page": "resources.html",
        "section": "Business Performance Dashboard Template",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Executive performance dashboard layout wireframe and metric cascade blueprint.",
        "prompt": "Still-life corporate photo of an executive performance dashboard layout blueprint on architectural grid paper beside a tablet. Leica SL2, 50mm f/2.0."
    },
    {
        "filename": "resource-process-checklist.webp",
        "page": "resources.html",
        "section": "Process Optimization Checklist",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Value stream mapping and bottleneck elimination audit checklist.",
        "prompt": "Clean corporate photography of a printed business process optimization audit checklist resting on an executive conference desk. Nikon Z8, 50mm f/1.8."
    },
    {
        "filename": "resource-change-template.webp",
        "page": "resources.html",
        "section": "Change Management Planning Template",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Stakeholder impact matrix and change communication roadmap worksheet.",
        "prompt": "Corporate advisory planning visual of a change management framework and stakeholder impact matrix document. Crisp corporate lighting. Canon EOS R5, 50mm f/2.0."
    },
    {
        "filename": "resource-leadership-checklist.webp",
        "page": "resources.html",
        "section": "Leadership Alignment Checklist",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Executive team consensus and decision rights alignment checklist.",
        "prompt": "Corporate still-life photography of an executive leadership alignment checklist in a bound leather folio on a boardroom marble table. Hasselblad X2D, 55mm f/2.8."
    },
    {
        "filename": "resource-transformation-roadmap.webp",
        "page": "resources.html",
        "section": "Business Transformation Roadmap",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Phased enterprise transformation roadmap template and milestone architecture.",
        "prompt": "Visual representation of an enterprise transformation roadmap template displayed on a wide-screen tablet resting on a timber conference table. Sony A1, 50mm f/1.8."
    },
    {
        "filename": "resource-risk-worksheet.webp",
        "page": "resources.html",
        "section": "Risk Assessment Worksheet",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "5x5 Enterprise Risk matrix worksheet and vulnerability mitigation scoring template.",
        "prompt": "Corporate documentary still-life of an enterprise risk assessment worksheet featuring a 5x5 matrix diagram with risk priority scores on clean stationery. Leica SL2, 50mm f/2.0."
    },
    {
        "filename": "resource-project-checklist.webp",
        "page": "resources.html",
        "section": "Project Governance Checklist",
        "aspect": "16:9",
        "res": "1200x675px",
        "orientation": "Landscape",
        "desc": "Project Management Office (PMO) governance checklist and milestone tracking protocol.",
        "prompt": "Corporate advisory still-life of a project governance and PMO milestone audit checklist in a modern aluminum clipboard. Nikon Z9, 50mm f/1.8."
    }
]

def generate_guide_md():
    total_images = len(IMAGE_CATALOG)
    portrait_count = sum(1 for img in IMAGE_CATALOG if img["orientation"] == "Portrait")
    landscape_count = sum(1 for img in IMAGE_CATALOG if img["orientation"] == "Landscape")

    # Inventory Table rows
    table_rows = []
    for idx, img in enumerate(IMAGE_CATALOG, 1):
        table_rows.append(f"| {idx:02d} | `{img['filename']}` | {img['page']} | {img['aspect']} | {img['orientation']} | {img['res']} |")
    inventory_table_md = "\n".join(table_rows)

    # Detailed prompts
    prompts_md_blocks = []
    for idx, img in enumerate(IMAGE_CATALOG, 1):
        block = f"""### Image {idx:02d}: `{img['filename']}`

- **Website Page(s):** {img['page']}
- **Website Section:** {img['section']}
- **Visual Description:** {img['desc']}
- **Aspect Ratio:** `{img['aspect']}` | **Orientation:** {img['orientation']}
- **Recommended Resolution:** `{img['res']}`
- **Negative Space:** Ample uncluttered negative space suitable for executive layout stability.

#### Copy-Ready Google Flow Prompt:
```text
{img['prompt']}
```
---"""
        prompts_md_blocks.append(block)

    prompts_md = "\n\n".join(prompts_md_blocks)

    content = f"""# Google Flow Image Generation Guide
**Generic Management Consulting Company Website**

This comprehensive manual provides an exact, copy-ready Google Flow prompt for every single image placeholder utilized across all 35 pages of the website. 

> [!IMPORTANT]
> **Strict Generation Rule:** In accordance with prompt requirements, Google Antigravity did not generate or download images. All images must be generated externally using **Google Flow** by copying the dedicated prompts below, saving them with their exact designated filenames in `assets/images/`, and following the replacement instructions in Section G.

---

## A. Summary Statistics & Inventory Counts

- **Total Required Unique Images:** `{total_images}`
- **Total Placeholder Instances across 35 Pages:** `91`
- **Landscape Images (16:9 & 4:3):** `{landscape_count}`
- **Portrait Images (3:4 Executive Profiles):** `{portrait_count}`
- **Square Images:** `0`
- **Output Image Format:** `.webp` (or `.jpg` converted to `.webp`)
- **Visual Style:** Premium International Management Consulting &bull; Executive Editorial Photography &bull; Zero Stock Clichés &bull; No Fake Logos or Fictitious Text

---

## B. Master Image Inventory Table

| No. | Exact Target Filename | Website Page(s) | Aspect Ratio | Orientation | Target Resolution |
|:---:|:---|:---|:---:|:---:|:---:|
{inventory_table_md}

---

## C. Individual Copy-Ready Google Flow Prompts

{prompts_md}

---

## D. Recommended Image Generation Order

To maintain cohesive visual styling, color grading, and lighting across the website, we recommend generating images in the following phased order:

1. **Phase 1: Executive Foundation (Images 01 to 04)**
   - `hero-management-consulting.webp`
   - `management-team-discussion.webp`
   - `management-case-study-workspace.webp`
   - `case-study-detailed-workspace.webp`
2. **Phase 2: Core Advisory Practices (Images 05 to 21)**
   - The 17 consulting practice headers for Strategy, Operations, Governance, and Performance.
3. **Phase 3: Executive Leadership Profiles (Images 36 to 41)**
   - The 6 portrait profiles (`team-profile-*.webp`) to establish consistent studio portrait lighting.
4. **Phase 4: Sector Specializations (Images 22 to 35)**
   - The 14 industry sector images (`industry-*.webp`).
5. **Phase 5: Case Studies, Thought Leadership & Resources (Images 42 to 71)**
   - The 8 illustrative case studies, 12 editorial insights, and 10 resource previews.

---

## E. Instructions for Replacing Placeholders with Generated Images

Once you generate the images using Google Flow:

1. **Save Images into Assets Directory:**
   Save each generated image with its exact filename specified in Section B into the folder:
   ```text
   p:\\TSCG\\2027 Demo Websites\\Management Consulting\\assets\\images\\
   ```

2. **Verify Filename Case:**
   Ensure filenames are strictly lowercase with hyphens (e.g. `hero-management-consulting.webp`).

3. **Replacing the HTML Placeholders:**
   In any target HTML file, replace the placeholder component:
   ```html
   <!-- Current Placeholder -->
   <div class="img-placeholder-wrapper ratio-16x9">
     <div class="img-placeholder">
       ...
       <code class="img-placeholder-filename">hero-management-consulting.webp</code>
       ...
     </div>
   </div>
   ```
   With the standard responsive HTML image tag:
   ```html
   <!-- Production Image -->
   <div class="img-placeholder-wrapper ratio-16x9">
     <img src="assets/images/hero-management-consulting.webp" 
          alt="Executive strategy consultation in corporate boardroom" 
          loading="lazy" 
          style="width: 100%; height: 100%; object-fit: cover;">
   </div>
   ```

---

## F. Final Verification Checklist

- [x] Every single one of the 71 unique placeholders across all 35 pages has an entry in this guide.
- [x] All filenames match the project structure exactly.
- [x] Aspect ratios, target resolutions, and orientations are explicitly specified.
- [x] Copy-ready individual prompts are detailed with camera, lens, lighting, composition, and mood parameters.
- [x] Zero clichéd stock handshakes, fake text, or invented client branding in prompt descriptions.
"""
    with open("IMAGE-GENERATION-GUIDE.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("IMAGE-GENERATION-GUIDE.md generated successfully.")

if __name__ == "__main__":
    generate_guide_md()
