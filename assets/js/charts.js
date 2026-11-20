/**
 * MANAGEMENT CONSULTING COMPANY - CHARTS & DIAGRAM VISUALIZATIONS
 * Lightweight SVG & Canvas Visualizations for Dashboards and Methodologies
 * All Sample Metrics Clearly Labelled: "Illustrative Demo Data"
 */

document.addEventListener('DOMContentLoaded', () => {
  initPerformanceTrendCanvas();
  initRiskMatrixInteractivity();
  initWorkflowStepInspector();
});

/* Simple Canvas Trend Line for Performance Dashboard */
function initPerformanceTrendCanvas() {
  const canvas = document.getElementById('performanceTrendCanvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();

  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  ctx.scale(dpr, dpr);

  const width = rect.width;
  const height = rect.height;

  // Clear
  ctx.clearRect(0, 0, width, height);

  // Background Grid Lines
  ctx.strokeStyle = '#EEF2F6';
  ctx.lineWidth = 1;
  for (let y = 20; y < height - 20; y += 30) {
    ctx.beginPath();
    ctx.moveTo(30, y);
    ctx.lineTo(width - 20, y);
    ctx.stroke();
  }

  // Sample Trend Line 1: Optimized Trajectory (Accent Blue)
  const pointsOptimized = [
    { x: 30, y: height - 35 },
    { x: width * 0.25, y: height - 60 },
    { x: width * 0.5, y: height - 90 },
    { x: width * 0.75, y: height - 120 },
    { x: width - 20, y: 30 }
  ];

  // Draw Area Gradient
  const grad = ctx.createLinearGradient(0, 0, 0, height);
  grad.addColorStop(0, 'rgba(71, 123, 183, 0.25)');
  grad.addColorStop(1, 'rgba(71, 123, 183, 0.0)');

  ctx.beginPath();
  ctx.moveTo(pointsOptimized[0].x, height - 20);
  pointsOptimized.forEach(pt => ctx.lineTo(pt.x, pt.y));
  ctx.lineTo(pointsOptimized[pointsOptimized.length - 1].x, height - 20);
  ctx.closePath();
  ctx.fillStyle = grad;
  ctx.fill();

  // Draw Optimized Line
  ctx.beginPath();
  ctx.strokeStyle = '#477BB7';
  ctx.lineWidth = 3;
  pointsOptimized.forEach((pt, i) => {
    if (i === 0) ctx.moveTo(pt.x, pt.y);
    else ctx.lineTo(pt.x, pt.y);
  });
  ctx.stroke();

  // Draw Points
  pointsOptimized.forEach(pt => {
    ctx.beginPath();
    ctx.arc(pt.x, pt.y, 4, 0, Math.PI * 2);
    ctx.fillStyle = '#10213A';
    ctx.fill();
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 2;
    ctx.stroke();
  });

  // Baseline Comparison Line (Muted Gold)
  const pointsBaseline = [
    { x: 30, y: height - 35 },
    { x: width * 0.25, y: height - 45 },
    { x: width * 0.5, y: height - 52 },
    { x: width * 0.75, y: height - 58 },
    { x: width - 20, y: height - 65 }
  ];

  ctx.beginPath();
  ctx.strokeStyle = '#B69A65';
  ctx.setLineDash([4, 4]);
  ctx.lineWidth = 2;
  pointsBaseline.forEach((pt, i) => {
    if (i === 0) ctx.moveTo(pt.x, pt.y);
    else ctx.lineTo(pt.x, pt.y);
  });
  ctx.stroke();
  ctx.setLineDash([]);
}

/* Interactive Risk Matrix Cell Inspector (Rule #19) */
function initRiskMatrixInteractivity() {
  const riskCells = document.querySelectorAll('.risk-interactive-cell');
  const detailsBox = document.getElementById('risk-cell-details');
  if (!riskCells.length || !detailsBox) return;

  riskCells.forEach(cell => {
    cell.addEventListener('click', () => {
      riskCells.forEach(c => c.style.outline = 'none');
      cell.style.outline = '2px solid #10213A';

      const likelihood = cell.getAttribute('data-likelihood') || 'Moderate';
      const impact = cell.getAttribute('data-impact') || 'Medium';
      const severity = cell.getAttribute('data-severity') || 'Moderate';
      const exampleRisk = cell.getAttribute('data-example') || 'Process bottleneck or operational friction.';
      const mitigation = cell.getAttribute('data-mitigation') || 'Establish clear ownership, SLA controls, and proactive monitoring.';

      detailsBox.innerHTML = `
        <div style="background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1.25rem; margin-top: 1rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <strong style="color: var(--primary-navy); font-size: 0.95rem;">Risk Scenario: ${severity.toUpperCase()} Priority</strong>
            <span class="badge badge-demo">Illustrative Framework</span>
          </div>
          <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>Likelihood:</strong> ${likelihood} | <strong>Impact:</strong> ${impact}</p>
          <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>Illustrative Risk:</strong> ${exampleRisk}</p>
          <p style="font-size: 0.85rem; color: var(--secondary-navy); margin-bottom: 0;"><strong>Mitigation Approach:</strong> ${mitigation}</p>
        </div>
      `;
    });
  });
}

/* Interactive Workflow Step Inspector (Rule #12) */
function initWorkflowStepInspector() {
  const steps = document.querySelectorAll('.workflow-step-interactive');
  const inspector = document.getElementById('workflow-step-inspector');
  if (!steps.length || !inspector) return;

  steps.forEach(step => {
    step.addEventListener('click', () => {
      steps.forEach(s => s.classList.remove('active-step'));
      step.classList.add('active-step');

      const title = step.getAttribute('data-title') || 'Process Stage';
      const bottleneck = step.getAttribute('data-bottleneck') || 'None identified';
      const solution = step.getAttribute('data-solution') || 'Standard operating procedure';

      inspector.innerHTML = `
        <div style="background: #F8FAFC; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1rem 1.25rem;">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
            <strong style="color: var(--primary-navy);">${title}</strong>
            <span class="badge badge-subtle">Diagnostic Detail</span>
          </div>
          <p style="font-size: 0.85rem; margin-bottom: 0.4rem;"><strong>Identified Friction:</strong> ${bottleneck}</p>
          <p style="font-size: 0.85rem; color: var(--accent-blue); margin-bottom: 0;"><strong>Optimization Strategy:</strong> ${solution}</p>
        </div>
      `;
    });
  });
}
