-- CONSTRUCTION PROJECT ANALYTICS - SQL QUERIES
-- These queries demonstrate data extraction and analysis

-- Query 1: Project Performance Overview
SELECT 
    project_id,
    project_name,
    contract_value,
    actual_cost,
    ROUND((actual_cost - contract_value) / contract_value * 100, 2) AS budget_variance_percent
FROM construction_projects
ORDER BY budget_variance_percent DESC;

-- Query 2: High-Risk Projects
SELECT 
    project_id,
    project_name,
    project_location,
    ROUND((actual_cost - contract_value) / contract_value * 100, 2) AS budget_variance_percent,
    safety_incidents,
    quality_issues
FROM construction_projects
WHERE (actual_cost > contract_value * 1.1)
   OR (safety_incidents > 0)
ORDER BY budget_variance_percent DESC;

-- Query 3: Supplier Analysis
SELECT 
    material_supplier,
    COUNT(project_id) AS project_count,
    ROUND(AVG(material_cost), 2) AS avg_material_cost,
    ROUND(AVG(quality_score), 2) AS avg_quality_score
FROM construction_projects
GROUP BY material_supplier
ORDER BY avg_material_cost DESC;

-- Query 4: Workforce Efficiency
SELECT 
    project_id,
    project_name,
    workforce_allocated,
    workforce_used,
    ROUND((workforce_allocated - workforce_used) / workforce_allocated * 100, 2) AS efficiency_percent
FROM construction_projects
WHERE workforce_used > 0
ORDER BY efficiency_percent DESC;

-- Query 5: Projects by Status
SELECT 
    project_status,
    COUNT(*) AS total_projects,
    ROUND(AVG(contract_value), 2) AS avg_contract_value,
    ROUND(AVG(quality_score), 2) AS avg_quality_score
FROM construction_projects
GROUP BY project_status
ORDER BY total_projects DESC;

-- Query 6: Cost Optimization Opportunities
SELECT 
    project_id,
    project_name,
    material_supplier,
    material_cost,
    quality_score,
    CASE 
        WHEN quality_score >= 90 THEN 'High Quality'
        WHEN quality_score >= 80 THEN 'Good Quality'
        ELSE 'Quality Concerns'
    END AS supplier_recommendation
FROM construction_projects
ORDER BY material_cost DESC;