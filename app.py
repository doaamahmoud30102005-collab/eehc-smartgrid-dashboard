import streamlit as st
import pandas as pd

# ----------------------------------------------------
# 1. PAGE CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="EEHC | Smart Grid Master Control",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session State
if "selected_project" not in st.session_state:
    st.session_state["selected_project"] = None

# Header
st.title("⚡ EEHC Smart Grid Command Center")
st.caption("Egyptian Electricity Holding Company & 9 Distribution Companies (DISCOs) Strategic Roadmap")
st.divider()

# ----------------------------------------------------
# 2. ROADMAP DATA MATRIX
# ----------------------------------------------------
PROJECTS = {
    "1. Policy & Regulatory": [
        ("PS1", "Policy and regulatory review"),
        ("PS2", "Technical standards & regulation"),
        ("PS3", "Privacy & customer data ownership"),
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
        ("IF3", "Smart meters: Res >200 kWh/mo"),
        ("IF4", "Asset management & monitoring"),
        ("IF5", "Smart Meter Plus: Res <200 kWh/mo"),
        ("IF6", "Phasor measurement units")
    ],
    "4. Technology": [
        ("TE1", "Technology evaluation & selection"),
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
        ("C5", "Interactive energy applications")
    ]
}

# ----------------------------------------------------
# 3. DASHBOARD VIEW
# ----------------------------------------------------
if st.session_state["selected_project"] is None:
    
    # Portfolio Metrics
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Portfolio Scope", "5 Domains", "26 Projects")
    k2.metric("Target Network", "9 DISCOs", "Unified Model")
    k3.metric("Active Flagship", "IF2 (GIS)", "Short-Term Horizon")
    k4.metric("Program Horizon", "2026 – 2030+", "3 Phases")

    st.markdown("---")
    st.subheader("⚡ Smart Grid Portfolio Matrix — Select a Project")

    cols = st.columns(5)
    
    for idx, (domain_name, proj_list) in enumerate(PROJECTS.items()):
        with cols[idx]:
            st.markdown(f"### {domain_name}")
            for code, name in proj_list:
                label = f"⭐ {code}: {name}" if code == "IF2" else f"🔹 {code}: {name}"
                if st.button(label, key=f"btn_{code}"):
                    st.session_state["selected_project"] = code
                    st.rerun()

    st.markdown("---")
    
    st.subheader("🎯 Portfolio Benefits Framework")
    b1, b2, b3, b4 = st.columns(4)
    b1.info("💰 **B1 / B2**: Deferred & Avoided Grid Investment")
    b2.warning("⚡ **B3 / B4**: Reduced Losses & Planned Outages")
    b3.success("🌱 **B5 / B6 / B7**: Customer Experience & CO₂ Reduction")
    b4.metric("B8 / B9", "Operational Efficiency", "EV Integration")

# ----------------------------------------------------
# 4. DETAILED PROJECT VIEWS
# ----------------------------------------------------
else:
    if st.button("← Return to Smart Grid Command Center"):
        st.session_state["selected_project"] = None
        st.rerun()

    proj_code = st.session_state["selected_project"]

    if proj_code == "IF2":
        st.header("🗺 IF2: Asset Management Design & Implementation (GIS Project)")
        st.caption("Central GIS Foundation, Network Digitization, and Strategic Asset Record")
        st.divider()
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Short Term Target", "MV Network Coverage", "By June 2027")
        m2.metric("Medium Term Target", "LV Network & Apps", "2027 – 2030")
        m3.metric("Long Term Target", "ADMS Operations", "May 2030 Onward")
        m4.metric("Scope", "9 DISCOs", "1 Unified Model")

        st.markdown("###")

        tab1, tab2, tab3, tab4 = st.tabs([
            "🎯 Strategic Objectives", 
            "📅 3-Horizon Roadmap", 
            "🔄 Update Workflow & Acceptance", 
            "🔌 Connected Applications"
        ])

        with tab1:
            col_left, col_right = st.columns(2)
            with col_left:
                st.markdown("""
                ### Core Pillars
                * **Unified Network Record**: 9 Distribution Companies operating under one agreed data standard and schema.
                * **Trusted Network Data**: Verified asset locations, stable global asset IDs, and validated electrical topology.
                """)
            with col_right:
                st.markdown("""
                ### Deployment Principles
                * **Continuous Lifecycle**: *Capture → Verify → Approve → Publish* update workflow.
                * **Sector Applications**: Powering Asset Management, OMS, ADMS, and Loss Analysis.
                """)

        with tab2:
            st.subheader("Implementation Horizons Timeline")
            horizon_df = pd.DataFrame({
                "Horizon": ["Short Term", "Medium Term", "Long Term"],
                "Timeline": ["Jan 2026 – Jun 2027", "Jun 2027 – May 2030", "May 2030 Onward"],
                "Focus Area": [
                    "Central foundation; 9 DISCO pilots; full MV network coverage",
                    "LV network expansion; operating apps; RE/PQ/BESS pilots",
                    "Coordinated ADMS operations; voltage & peak optimization; AMI"
                ],
                "Gate Evidence": [
                    "Accepted MV network records in all 9 DISCOs",
                    "Measured value and validated electrical models",
                    "Approved investment cases and operating readiness"
                ]
            })
            st.dataframe(horizon_df, use_container_width=True)

        with tab3:
            st.subheader("Continuous Update & Acceptance Workflow")
            st.code("""
[ Field Change / Survey ] ──> [ DISCO QA Check ] ──> [ Joint Acceptance ] ──> [ Central SQL / GIS Sync ]
            """, language="text")
            st.markdown("""
            * **EEHC GIS & R&D Team**: Common model, SQL integration, central platform maintenance.
            * **DISCO Teams**: Field locating, attribute verification, record ownership.
            * **Joint Acceptance Team**: QA checklist verification, coordinate matching, and approval workflow.
            """)

        with tab4:
            st.subheader("Connected Application Modules")
            app_select = st.selectbox("Select Application Domain to View Status:", [
                "Asset Management & Maintenance",
                "Fleet & Workforce Management",
                "Outage Management System (OMS)",
                "Loss Analysis & Cost Visibility",
                "Renewable Energy & EV Connection Screening",
                "Power Quality Assessment & Response",
                "Battery Energy Storage (BESS) Support"
            ])
            st.success(f"Configured View: {app_select}")
            st.json({
                "Project Code": "IF2-APP",
                "Integration Architecture": "ArcGIS Enterprise / Central SQL Link",
                "Primary Identifier": "Unified Global Asset ID",
                "Deployment Horizon": "Medium-Term (2027-2030)"
            })

    else:
        proj_name = "Selected Project"
        for domain in PROJECTS.values():
            for code, name in domain:
                if code == proj_code:
                    proj_name = name
                    break

        st.header(f"⚙ {proj_code}: {proj_name}")
        st.info("🔒 Dedicated workspace allocated within the Smart Grid Master Roadmap.")

        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Lead Department / Owner", value="EEHC Operations", disabled=True)
            st.selectbox("Implementation Status", ["Planning", "Pilot Phase", "Active Rollout", "Completed"])
        with col2:
            st.date_input("Target Start Date")
            st.number_input("Estimated Investment ($)", value=0)

        st.text_area("Scope Definition & Project Objectives", placeholder="Enter technical requirements, key deliverables, and target KPIs...")
