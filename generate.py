#!/usr/bin/env python3
"""Read /tmp/sheet_raw.json, inject into index.template.html, write index.html"""
import json, sys, os

YEAR_MAP = {
  "Partner Process Transformation":"2024","Phoenix Program":"2026",
  "Steering Reporting and Planning - Phase 2":"2024","Steering Reporting and Planning - Phase 3":"2024",
  "E-Signature Tool":"2025","RedShift Migration":"2025","Oracle Phase-Out & Migration":"2024",
  "ICM":"2024","ICM Raw Data for Analytics":"2024",
  "S/4HANA Expanded Sweep Archiving (Phase 4)":"2024","VAT Compliant Reporting":"2026",
  "Databricks Cost Efficiency Initiative":"2025","The ERP Technology Strategy":"2024",
  "[VAT Upgrade] Deemed-Supplier Sales Compliance":"2024",
  "[VAT Upgrade] Scalable and Compliant Customer Invoicing":"2024",
  "Corporate Sustainability Reporting Directive (CSRD)":"2025","Premium Engagement of SAP":"2026",
  "User Experience in SAP ERP":"2025","AWS Lighthouse":"2024","ICM Enhancement":"2025",
  "VIM Upgrade":"2025","Stores Re-Design (Offprice)":"2025","PMDM":"2025",
  "ICM EaseOps":"2025","DAC 7 Online Sales Tax Reporting":"2025","S/4HANA Upgrade 2025":"2025",
  "Month-End Closing Process Reengineering":"2025","Real Estate Management Extension Project":"2025",
  "E2E Business Travel Optimization Project":"2026","Danoub M2":"2025",
  "Partner Stock Management":"2025","Databricks - Unity Catalog":"2026",
  "BI Tooling Strategy":"2025","SAP S4HANA Clean Core '25":"2025",
  "ERPE Knowledge Base and Documentation":"2025","Fashion Store Expansion":"2026",
  "Debit Note Automation":"2025","Real Estate Management Lease Out Project (V2)":"2026",
  "WOW and Confluence Knowledge Base and Documentation":"2025","SRP Stock Ownership":"2025",
  "ERPE Innovation Fund (BTP Integration Suite & BTP CAP)":"2025",
  "O2C Process Improvements - O2C+":"2025","OTC Improvements Project - Reporting":"2025",
  "PPM Change Ambassador":"2026","Customer Data Access":"2026","User Experience Phase 2":"2025",
  "Jira & SolMan ChaRM Integration":"2025","CALM":"2025","DAC2025":"2026",
  "GRC Tool":"2025","Fiori Fusion":"2025","Spay":"2026",
  "ERPE Innovation Fund (BTP gCTS CI/CD)":"2025","EPR Category Classification - Phase 2":"2026",
  "ZxAY Orbit Project - PMO Body for Engineering Team":"2026","Archiving Project":"2026",
  "E-Reporting (Poland KSeF)":"2026","SAP BDC Set Up & Migration (SAP BW4HANA PcE Migration)":"2026",
  "DAC2025 (Ilker)":"2026","ICCM 1.0":"2026","ERP Innovation Fund - AI Initiatives":"2026",
  "ERP Innovation Fund - Digital Core Acceleration":"2026","SAP Taulia Implementation":"2026",
  "Orbit Cut-over":"2026","Databricks SQL Warehouse":"2026",
  "ZSE MT940 to CAMT053 / ISO 20022":"2026","IC Cashless Settlement & Netting":"2026",
  "ATT Migration":"2026","Print Materials for Jersey Customization M2":"2026","MBC M2":"2026",
}

updated = sys.argv[1] if len(sys.argv) > 1 else "unknown"
dir_ = os.path.dirname(os.path.abspath(__file__))

data = json.load(open("/tmp/sheet_raw.json"))
rows = data.get("values", [])

projects = []
for r in rows:
    name = r[0].strip() if len(r) > 0 else ""
    if not name:
        continue
    p = {
        "name":   name,
        "pm":     r[2].strip()  if len(r) > 2  else "",
        "phase":  r[3].strip()  if len(r) > 3  else "",
        "entity": r[4].strip()  if len(r) > 4  else "",
        "rag":    r[5].strip()  if len(r) > 5  else "",
        "status": r[7].strip()  if len(r) > 7  else "",
        "eta":    r[9].strip()  if len(r) > 9  else "",
        "budget": r[11].strip() if len(r) > 11 else "",
        "update": r[12].strip() if len(r) > 12 else "",
        "year":   YEAR_MAP.get(name, "2025"),
    }
    projects.append(p)

with open(os.path.join(dir_, "index.template.html")) as f:
    html = f.read()

html = html.replace("__PROJECTS_DATA__", json.dumps(projects, ensure_ascii=False))
html = html.replace("__UPDATED__", updated)

with open(os.path.join(dir_, "index.html"), "w") as f:
    f.write(html)

print(f"Generated {len(projects)} projects")
