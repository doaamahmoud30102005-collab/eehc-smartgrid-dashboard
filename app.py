import streamlit as st

# Set page config
st.set_page_config(
    page_title="EEHC Smart Grid Dashboard",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS styling for visual polish
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0E1117;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #555;
        margin-bottom: 25px;
    }
    .domain-header {
        background-color: #1E3A8A;
        color: white;
        padding: 10px;
        border-radius: 6px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 12px;
    }
    .stButton>button {
        width: 100%;
        text-align: left;
        border-radius: 6px;
        border: 1px solid #E0E0E0;
        padding: 8px 12px;
        background-color: #FFFFFF;
    }
    .stButton>button:hover {
        border-color: #1E3A8A;
        color: #1E3A8A;
    }
    .highlight-btn>button {
        border: 2px solid #2563EB !important;
        background-color: #EFF6FF !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Define all 26 projects organized by domain
PROJECTS = {
    "1. Policy & Regulatory Support": [
        ("PS1", "Policy and regulatory review"),
        ("PS2", "Technical standards and regulation"),
        ("PS3", "Privacy and customer data ownership"),
        ("PS4", "Cybersecurity")
    ],
    "2. Organizational Support": [
        ("OS1", "Business goals and use cases"),
        ("OS2", "Organizational KPIs"),
        ("OS3", "Asset management strategy"),
        ("OS4", "Smart grid governance")
    ],
    "3. Infrastructure": [
        ("IF1", "Smart meters: commercial and industrial"),
        ("IF2", "Asset management design and implementation (GIS Project)"),
        ("IF3", "Smart meters: residential >200 kWh/month"),
        ("IF4", "Asset management and monitoring"),
        ("IF5", "Smart Meter Plus: residential <200 kWh/month"),
        ("IF6", "Phasor measurement units")
    ],
    "4. Technology": [
        ("TE1", "Technology evaluation and selection"),
        ("TE2", "Integrated solution selection"),
        ("TE3", "Smart meter analytics"),
        ("TE4", "PV and EV monitoring"),
        ("TE5", "Demand response"),
        ("TE6", "Demand-side management pilot"),
        ("TE7", "Energy storage pilots")
    ],
    "5. Customer Engagement": [
        ("C1", "Green DISCO"),
        ("C2", "AMI lessons learned"),
        ("C3", "Buy REN@DISCO"),
        ("C4", "Advanced smart meter analytics"),
        ("C5", "Interactive energy applications")
    ]
}

# Initialize session state for navigation
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

def navigate_to(proj_code):
    st.session_state["selected_project"] = proj_code

# Header
st.markdown("<div class='main-title'>EEHC Smart Grid Portfolio Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Egyptian Electricity Holding Company & 9 Distribution Companies (DISCOs)</div>", unsafe_allow_html=True)

# Navigation Bar / Back button
if st.session_state["selected_project"]:
    if st.button("← Back to Smart Grid Roadmap Matrix"):
        st.session_state["selected_project"] = None
        st.rerun()
    st.markdown("---")

# ----------------------------------------------------
# MAIN DASHBOARD VIEW
# ----------------------------------------------------
if st.session_state["selected_project"] is None:
    st.subheader("Smart Grid Roadmap (5 Domains • 26 Projects)")
    st.info("💡 **Click on any project below** to navigate directly to its detail page.")
    
    cols = st.columns(5)
    
    for idx, (domain, proj_list) in enumerate(PROJECTS.items()):
        with cols[idx]:
            st.markdown(f"<div class='domain-header'>{domain}</div>", unsafe_allow_html=True)
            for code, name in proj_list:
                # Highlight GIS Project IF2
                is_active = (code == "IF2")
                label = f"🔵 **{code}**: {name}" if is_active else f"⚪ **{code}**: {name}"
                
                if st.button(label, key=f"btn_{code}"):
                    navigate_to(code)
                    st.rerun()

    st.markdown("---")
    
    # Portfolio Benefits Overview
    st.subheader("Potential Benefits of the Smart-Grid Portfolio")
    b_col1, b_col2, b_col3, b_col4, b_col5 = st.columns(5)
    b_col1.metric("B1 / B2", "Grid Investment", "Deferred / Avoided")
    b_col2.metric("B3 / B4", "Outages & Losses", "Reduced")
    b_col3.metric("B5 / B6", "Customer Experience", "Improved")
    b_col4.metric("B7 / B8", "Efficiency", "CO₂ & Ops Reduced")
    b_col5.metric("B9", "EV Integration", "Benefits Enabled")

# ----------------------------------------------------
# PROJECT DETAIL VIEWS
# ----------------------------------------------------
else:
    proj_code = st.session_state["selected_project"]
    
    # --- PROJECT IF2: GIS ROLLOUT DETAIL PAGE ---
    if proj_code == "IF2":
        st.title("IF2: Asset Management Design & Implementation — GIS Rollout Project")
        st.caption("Strategic Roadmap & Execution Framework for EEHC and 9 DISCOs")
        
        # Key Metrics Overview
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Short-Term Focus", "MV Coverage", "By June 2027")
        m2.metric("Medium-Term Focus", "LV Expansion", "2027 – 2030")
        m3.metric("Long-Term Focus", "ADMS / Operations", "2030 Onward")
        m4.metric("Target Scope", "9 DISCOs", "Unified Standard")
        
        st.markdown("---")
        
        # Tabs for GIS Modules
        tab1, tab2, tab3, tab4 = st.tabs([
            "🎯 Strategic Objectives", 
            "📅 3-Horizon Timeline", 
            "🔄 Update Workflow & Monitoring", 
            "🗂️ Application Domains"
        ])
        
        with tab1:
            st.subheader("Strategic Core Objectives")
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown("""
                * **Unified Network Record**: 9 DISCOs operating on one common data schema standard.
                * **Trusted Network Data**: Verified asset locations, stable IDs, and connectivity validation.
                """)
            with col_b:
                st.markdown("""
                * **Continuous Updates**: Structured *Capture → Verify → Approve → Publish* lifecycle.
                * **Sector Applications**: Integration with Asset Management, OMS, and ADMS.
                """)
                
        with tab2:
            st.subheader("Implementation Horizons")
            st.markdown("""
            | Horizon | Timeline | Focus Area | Key Target / Evidence |
            | :--- | :--- | :--- | :--- |
            | **Short Term** | Jan 2026 – Jun 2027 | Central foundation, 9 DISCO pilots, full MV network coverage | Accepted MV records across all 9 DISCOs |
            | **Medium Term** | Jun 2027 – May 2030 | LV network coverage, Asset Mgmt, OMS, Loss Analysis, RE/EV pilots | Measured value & validated electrical models |
            | **Long Term** | May 2030 Onward | ADMS automation, restoration, voltage/peak optimization, AMI | Approved investment cases & operating readiness |
            """)
            
        with tab3:
            st.subheader("GIS Rollout & Workflow Monitoring")
            st.markdown("""
            ```
            [ Field Change ] ──> [ QA Verification ] ──> [ Approval ] ──> [ Publish to Central SQL/GIS ]
            ```
            """)
            st.info("The monitoring engine tracks MV coverage status, data quality scores, update backlogs, and sync timestamps across each DISCO.")
            
        with tab4:
            st.subheader("Connected Operating Applications")
            app_choice = st.selectbox("Select Application Domain to View Roadmap Details:", [
                "Asset Management & Maintenance",
                "Fleet & Field Workforce Management",
                "Outage Management System (OMS)",
                "Loss Analysis & Energy Cost Visibility",
                "Renewable Energy & EV Connection Planning",
                "Power Quality Assessment",
                "Battery Energy Storage (BESS)"
            ])
            st.write(f"**Selected Domain:** {app_choice}")
            st.json({
                "Status": "Defined in GIS Master Plan",
                "Data Requirements": "Verified topology, Common Asset IDs, SQL Integration",
                "Target Deployment": "Medium-Term Horizon (2027-2030)"
            })

    # --- PLACEHOLDER FOR OTHER 25 PROJECTS ---
    else:
        st.title(f"Project Code: {proj_code}")
        
        # Retrieve project name
        proj_name = "Selected Project"
        for domain_list in PROJECTS.values():
            for code, name in domain_list:
                if code == proj_code:
                    proj_name = name
                    break
        
        st.subheader(proj_name)
        st.warning("🚧 This project module is currently reserved in the master roadmap. Detailed workflow and data structures will be configured here.")
        
        st.markdown("### Placeholder Specifications")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Project Owner / Department", value="Pending Allocation", disabled=True)
            st.selectbox("Project Status", ["Planning", "Pilot", "In Progress", "Completed"], index=0)
        with col2:
            st.date_input("Target Start Date")
            st.number_input("Estimated Budget ($)", value=0)
            
        st.text_area("Scope & Objectives Overview", placeholder="Enter project scope and requirements here...")
        st.button("Save Configuration", disabled=True)
