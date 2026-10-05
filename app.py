import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="EEHC | Smart Grid Portfolio Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced CSS Styling (EEHC Visual Theme)
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Title Banner */
    .header-banner {
        background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
        padding: 24px 32px;
        border-radius: 16px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin: 0;
        color: #FFFFFF;
    }
    .header-subtitle {
        font-size: 1.05rem;
        color: #93C5FD;
        margin-top: 6px;
        font-weight: 400;
    }

    /* Domain Headers */
    .domain-card {
        background: #1E293B;
        color: #F8FAFC;
        padding: 12px 16px;
        border-radius: 10px 10px 0px 0px;
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        text-align: center;
        border-bottom: 3px solid #2563EB;
    }

    /* Column Container Box */
    div[data-testid="column"] > div {
        background: #FFFFFF;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }

    /* Customizing Streamlit Buttons to behave like Dashboard Cards */
    div.stButton > button {
        width: 100% !important;
        background-color: #FFFFFF !important;
        color: #334155 !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 8px !important;
        padding: 10px 12px !important;
        font-size: 0.88rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        transition: all 0.2s ease-in-out !important;
        margin-bottom: 4px !important;
    }

    div.stButton > button:hover {
        background-color: #EFF6FF !important;
        color: #1D4ED8 !important;
        border-color: #93C5FD !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.1) !important;
    }

    /* Highlight Active GIS Project Button (IF2) */
    div.stButton > button[data-testid="baseButton-secondary"]:has(div:contains("IF2")) {
        background-color: #EFF6FF !important;
        border: 2px solid #2563EB !important;
        color: #1E40AF !important;
        font-weight: 700 !important;
    }

    /* Metric Cards */
    .metric-card {
        background: #FFFFFF;
        padding: 18px;
        border-radius: 12px;
        border-left: 5px solid #2563EB;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }
    .metric-title { font-size: 0.85rem; color: #64748B; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 1.4rem; color: #0F172A; font-weight: 700; margin-top: 4px; }
    .metric-desc { font-size: 0.8rem; color: #2563EB; font-weight: 500; margin-top: 2px; }
</style>
""", unsafe_allow_html=True)

# 3. Roadmap Data Structure
PROJECTS = {
    "1. Policy & Regulatory": [
        ("PS1", "Policy & regulatory review"),
        ("PS2", "Technical standards & regulation"),
        ("PS3", "Privacy & customer data"),
        ("PS4", "Cybersecurity")
    ],
    "2. Organizational": [
        ("OS1", "Business goals & use cases"),
        ("OS2", "Organizational KPIs"),
        ("OS3", "Asset management strategy"),
        ("OS4", "Smart grid governance")
    ],
    "3. Infrastructure": [
        ("IF1", "Smart meters: C&I"),
        ("IF2", "Asset Mgmt & GIS Implementation"),
        ("IF3", "Smart meters: Res >200kWh"),
        ("IF4", "Asset mgmt & monitoring"),
        ("IF5", "Smart Meter Plus: Res <200kWh"),
        ("IF6", "Phasor measurement units")
    ],
    "4. Technology": [
        ("TE1", "Tech evaluation & selection"),
        ("TE2", "Integrated solution selection"),
        ("TE3", "Smart meter analytics"),
        ("TE4", "PV and EV monitoring"),
        ("TE5", "Demand response"),
        ("TE6", "DSM pilot"),
        ("TE7", "Energy storage pilots")
    ],
    "5. Customer Engagement": [
        ("C1", "Green DISCO"),
        ("C2", "AMI lessons learned"),
        ("C3", "Buy REN@DISCO"),
        ("C4", "Advanced meter analytics"),
        ("C5", "Interactive energy apps")
    ]
}

# State Management
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

def navigate_to(proj_code):
    st.session_state["selected_project"] = proj_code

# Header Banner
st.markdown("""
<div class="header-banner">
    <div class="header-title">EEHC Smart Grid Portfolio Dashboard</div>
    <div class="header-subtitle">Egyptian Electricity Holding Company • 9 Distribution Companies (DISCOs)</div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# MAIN DASHBOARD VIEW
# ----------------------------------------------------
if st.session_state["selected_project"] is None:
    
    # Quick Stats Row
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        st.markdown('<div class="metric-card"><div class="metric-title">Portfolio Scope</div><div class="metric-value">5 Domains</div><div class="metric-desc">Strategic Pillars</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="metric-card"><div class="metric-title">Total Projects</div><div class="metric-value">26 Projects</div><div class="metric-desc">12 Support • 14 Direct</div></div>', unsafe_allow_html=True)
    with s3:
        st.markdown('<div class="metric-card"><div class="metric-title">Coverage Target</div><div class="metric-value">9 DISCOs</div><div class="metric-desc">Unified Standards</div></div>', unsafe_allow_html=True)
    with s4:
        st.markdown('<div class="metric-card"><div class="metric-title">Active Implementation</div><div class="metric-value">IF2: GIS Rollout</div><div class="metric-desc">Phase 1 In Progress</div></div>', unsafe_allow_html=True)

    st.markdown("###")
    st.markdown("##### 📍 Interactive Roadmap Matrix — Click any project to view details")

    # 5-Column Grid Layout
    cols = st.columns(5)
    
    for idx, (domain_title, proj_list) in enumerate(PROJECTS.items()):
        with cols[idx]:
            st.markdown(f'<div class="domain-card">{domain_title}</div>', unsafe_allow_html=True)
            st.markdown("<div style='padding: 8px;'>", unsafe_allow_html=True)
            
            for code, name in proj_list:
                # Custom label format
                if code == "IF2":
                    button_label = f"⭐ **{code}**: {name}"
                else:
                    button_label = f"• **{code}**: {name}"
                
                if st.button(button_label, key=f"btn_{code}"):
                    navigate_to(code)
                    st.rerun()
                    
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Potential Portfolio Benefits")
    
    b1, b2, b3, b4, b5 = st.columns(5)
    b1.info("💰 **B1 / B2**\n\nDeferred & Avoided Grid Investments")
    b2.warning("⚡ **B3 / B4**\n\nReduced Outages & Technical Losses")
    b3.success("🌱 **B5 / B6**\n\nImproved Customer Satisfaction")
    b4.metric("B7 / B8", "CO₂ Reduction", "Operational Efficiency")
    b5.metric("B9", "EV Integration", "Grid Readiness")

# ----------------------------------------------------
# PROJECT DETAIL VIEWS
# ----------------------------------------------------
else:
    # Back Button Navigation
    if st.button("← Return to Smart Grid Dashboard"):
        st.session_state["selected_project"] = None
        st.rerun()
        
    proj_code = st.session_state["selected_project"]
    
    # DETAIL PAGE: GIS ROLLOUT (IF2)
    if proj_code == "IF2":
        st.markdown("## 🗺️ IF2: Asset Management Design & Implementation (GIS Rollout)")
        st.caption("Central GIS Foundation, Network Digitization, and Operating Applications")
        
        st.markdown("---")
        
        # Key Progress Metrics
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Short Term (2026–2027)", "Full MV Coverage", "Jan 2026 – Jun 2027")
        m2.metric("Medium Term (2027–2030)", "LV Network & Apps", "Jun 2027 – May 2030")
        m3.metric("Long Term (2030+)", "ADMS & Automation", "May 2030 Onward")
        m4.metric("Standardization", "Unified Schema", "9 DISCOs")

        st.markdown("###")
        
        # Detailed Content Tabs
        tab1, tab2, tab3, tab4 = st.tabs([
            "🎯 Strategic Objectives", 
            "📅 Three Horizons Timeline", 
            "🔄 Update Workflow", 
            "🔌 Integrated Applications"
        ])
        
        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("""
                #### Core Objectives
                * **Unified Network Record**: Establishing one common network standard across all 9 DISCOs.
                * **Trusted Network Data**: Verified asset locations, stable IDs, and connectivity rules.
                """)
            with c2:
                st.markdown("""
                #### Operational Integration
                * **Continuous Updates**: Controlled workflow to capture, verify, approve, and publish changes.
                * **Sector Applications**: Foundation for Asset Management, OMS, and ADMS tools.
                """)

        with tab2:
            st.markdown("""
            | Horizon | Target Dates | Focus Area | Deliverable / Gate |
            | :--- | :--- | :--- | :--- |
            | **Short Term** | Jan 2026 – Jun 2027 | Central GIS foundation & 9 DISCO pilots | Accepted MV records across all 9 DISCOs |
            | **Medium Term** | Jun 2027 – May 2030 | LV expansion & specialized applications | Validated electrical models & active apps |
            | **Long Term** | May 2030 Onward | Coordinated operations & ADMS | Approved investment cases & operating readiness |
            """)

        with tab3:
            st.info("🔄 **Update Workflow**: Field Change → QA Check → Acceptance Approval → Central SQL/GIS Synchronization")
            st.markdown("""
            * **EEHC GIS/R&D Team**: Provides common data models, SQL integration, and sync support.
            * **DISCO Teams**: Responsible for field surveys, attribute verification, and local updates.
            """)

        with tab4:
            st.selectbox("Select Application Domain to View Configuration Details:", [
                "Asset Management & Risk-Based Maintenance",
                "Fleet & Workforce Management",
                "Outage Management System (OMS)",
                "Loss Analysis & Cost Visibility",
                "Renewable Energy Screening",
                "Power Quality & Battery Support"
            ])
            st.json({
                "Project Code": "IF2-APP",
                "Integration Status": "Roadmap Architecture Defined",
                "Central Database": "Connected Enterprise SQL / ArcGIS",
                "Target Deployment": "Medium-Term Horizon"
            })

    # PLACEHOLDER PAGE: OTHER 25 PROJECTS
    else:
        proj_name = "Selected Project"
        for domain in PROJECTS.values():
            for code, name in domain:
                if code == proj_code:
                    proj_name = name
                    break
                    
        st.markdown(f"## ⚙️ {proj_code}: {proj_name}")
        st.warning("🔒 This module space is reserved for implementation details.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Project Lead / Department", value="To be assigned", disabled=True)
            st.selectbox("Current Phase", ["Concept", "Specification", "Implementation", "Deployed"])
        with c2:
            st.date_input("Target Implementation Date")
            st.number_input("Allocated Budget ($)", value=0)
            
        st.text_area("Scope & Deliverables", placeholder="Define project goals, technical scope, and KPIs...")
        st.button("Save Draft", disabled=True)
