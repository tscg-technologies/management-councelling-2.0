/**
 * MANAGEMENT CONSULTING COMPANY - FORMS MANAGEMENT
 * Multi-step Consultation Wizard (Steps 1-6) & Contact / Career Demo Handlers
 * STRICT DEMO RULE: Frontend-only simulation, no data transmitted or stored.
 */

document.addEventListener('DOMContentLoaded', () => {
  initConsultationWizard();
  initContactForm();
  initCareerForm();
});

/* Multi-Step Consultation Enquiry Wizard (Rule #32) */
function initConsultationWizard() {
  const wizardContainer = document.querySelector('.wizard-container');
  if (!wizardContainer) return;

  let currentStep = 1;
  const totalSteps = 6;

  const stepPanes = wizardContainer.querySelectorAll('.wizard-step-pane');
  const stepNodes = wizardContainer.querySelectorAll('.wizard-step-node');
  const nextBtn = wizardContainer.querySelector('.wizard-next-btn');
  const prevBtn = wizardContainer.querySelector('.wizard-prev-btn');
  const submitBtn = wizardContainer.querySelector('.wizard-submit-btn');

  // Form State Store (Local Memory Only - Not Transmitted)
  const formData = {
    fullName: '',
    email: '',
    phone: '',
    organization: '',
    industry: '',
    orgSize: '',
    stage: '',
    designation: '',
    challenges: [],
    mainChallengeText: '',
    desiredOutcome: '',
    additionalNotes: '',
    consultationMode: '',
    preferredDate: '',
    preferredTime: ''
  };

  const updateWizardUI = () => {
    // Show/hide panes
    stepPanes.forEach(pane => {
      const stepIndex = parseInt(pane.getAttribute('data-step'), 10);
      pane.classList.toggle('active', stepIndex === currentStep);
    });

    // Update node states
    stepNodes.forEach(node => {
      const stepIndex = parseInt(node.getAttribute('data-step-target'), 10);
      node.classList.remove('active', 'completed');
      if (stepIndex === currentStep) {
        node.classList.add('active');
      } else if (stepIndex < currentStep) {
        node.classList.add('completed');
      }
    });

    // Update navigation button states
    if (prevBtn) {
      prevBtn.style.display = currentStep === 1 ? 'none' : 'inline-flex';
    }

    if (nextBtn) {
      nextBtn.style.display = currentStep === totalSteps ? 'none' : 'inline-flex';
    }

    if (submitBtn) {
      submitBtn.style.display = currentStep === totalSteps ? 'inline-flex' : 'none';
    }

    // If on review step (Step 6), populate review table
    if (currentStep === 6) {
      populateReviewSummary();
    }

    // Scroll to wizard header smoothly
    wizardContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  // Step Validation Logic
  const validateCurrentStep = () => {
    let isValid = true;
    const currentPane = wizardContainer.querySelector(`.wizard-step-pane[data-step="${currentStep}"]`);
    if (!currentPane) return true;

    // Reset feedback
    currentPane.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
    currentPane.querySelectorAll('.form-feedback').forEach(el => el.remove());

    const showError = (input, msg) => {
      isValid = false;
      input.classList.add('is-invalid');
      const err = document.createElement('div');
      err.className = 'form-feedback';
      err.innerText = msg;
      input.parentNode.appendChild(err);
    };

    if (currentStep === 1) {
      const name = currentPane.querySelector('#wizard-name');
      const email = currentPane.querySelector('#wizard-email');
      const phone = currentPane.querySelector('#wizard-phone');
      const org = currentPane.querySelector('#wizard-org');

      if (!name.value.trim()) showError(name, 'Full name is required.');
      if (!email.value.trim() || !/\S+@\S+\.\S+/.test(email.value)) showError(email, 'Valid email is required.');
      if (!phone.value.trim()) showError(phone, 'Contact phone is required.');
      if (!org.value.trim()) showError(org, 'Organization name is required.');

      if (isValid) {
        formData.fullName = name.value.trim();
        formData.email = email.value.trim();
        formData.phone = phone.value.trim();
        formData.organization = org.value.trim();
      }
    } else if (currentStep === 2) {
      const industry = currentPane.querySelector('#wizard-industry');
      const orgSize = currentPane.querySelector('#wizard-org-size');
      const stage = currentPane.querySelector('#wizard-org-stage');
      const designation = currentPane.querySelector('#wizard-designation');

      if (!industry.value) showError(industry, 'Please select your industry.');
      if (!orgSize.value) showError(orgSize, 'Please select organization size.');
      if (!stage.value) showError(stage, 'Please select business stage.');
      if (!designation.value.trim()) showError(designation, 'Executive designation is required.');

      if (isValid) {
        formData.industry = industry.value;
        formData.orgSize = orgSize.value;
        formData.stage = stage.value;
        formData.designation = designation.value.trim();
      }
    } else if (currentStep === 3) {
      const checked = currentPane.querySelectorAll('input[name="challenges"]:checked');
      if (checked.length === 0) {
        isValid = false;
        const group = currentPane.querySelector('.option-tiles-grid');
        const err = document.createElement('div');
        err.className = 'form-feedback';
        err.innerText = 'Please select at least one management challenge.';
        group.parentNode.appendChild(err);
      } else {
        formData.challenges = Array.from(checked).map(c => c.value);
      }
    } else if (currentStep === 4) {
      const mainChallenge = currentPane.querySelector('#wizard-main-challenge');
      const desiredOutcome = currentPane.querySelector('#wizard-desired-outcome');

      if (!mainChallenge.value.trim()) showError(mainChallenge, 'Please describe your primary challenge.');
      if (!desiredOutcome.value.trim()) showError(desiredOutcome, 'Please specify your target outcome.');

      if (isValid) {
        formData.mainChallengeText = mainChallenge.value.trim();
        formData.desiredOutcome = desiredOutcome.value.trim();
        formData.additionalNotes = currentPane.querySelector('#wizard-notes')?.value.trim() || '';
      }
    } else if (currentStep === 5) {
      const mode = currentPane.querySelector('input[name="consultation_mode"]:checked');
      const prefDate = currentPane.querySelector('#wizard-date');
      const prefTime = currentPane.querySelector('#wizard-time');

      if (!mode) {
        isValid = false;
        const container = currentPane.querySelector('.mode-options');
        const err = document.createElement('div');
        err.className = 'form-feedback';
        err.innerText = 'Please select consultation preference mode.';
        container.parentNode.appendChild(err);
      }
      if (!prefDate.value) showError(prefDate, 'Please select a preferred date.');
      if (!prefTime.value) showError(prefTime, 'Please select a preferred time slot.');

      if (isValid) {
        formData.consultationMode = mode.value;
        formData.preferredDate = prefDate.value;
        formData.preferredTime = prefTime.value;
      }
    }

    return isValid;
  };

  const populateReviewSummary = () => {
    const summaryContainer = wizardContainer.querySelector('#wizard-review-container');
    if (!summaryContainer) return;

    summaryContainer.innerHTML = `
      <table class="review-summary-table">
        <tbody>
          <tr>
            <th>Full Name & Title</th>
            <td>${formData.fullName} (${formData.designation})</td>
          </tr>
          <tr>
            <th>Organization & Industry</th>
            <td>${formData.organization} &bull; ${formData.industry} (${formData.orgSize})</td>
          </tr>
          <tr>
            <th>Contact Details</th>
            <td>Email: ${formData.email} | Phone: ${formData.phone}</td>
          </tr>
          <tr>
            <th>Management Areas</th>
            <td>${formData.challenges.join(', ') || 'General Strategy'}</td>
          </tr>
          <tr>
            <th>Primary Challenge</th>
            <td>${formData.mainChallengeText}</td>
          </tr>
          <tr>
            <th>Target Desired Outcome</th>
            <td>${formData.desiredOutcome}</td>
          </tr>
          <tr>
            <th>Consultation Preference</th>
            <td>${formData.consultationMode} &bull; ${formData.preferredDate} at ${formData.preferredTime}</td>
          </tr>
        </tbody>
      </table>
      <div class="case-demo-notice">
        <strong>Demo Notice:</strong> This is a demonstration submission preview. Submitting this form does not connect to external calendar APIs, store data, or send emails.
      </div>
    `;
  };

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      if (validateCurrentStep()) {
        if (currentStep < totalSteps) {
          currentStep++;
          updateWizardUI();
        }
      }
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      if (currentStep > 1) {
        currentStep--;
        updateWizardUI();
      }
    });
  }

  if (submitBtn) {
    submitBtn.addEventListener('click', (e) => {
      e.preventDefault();
      // Render success state
      const wizardBody = wizardContainer.querySelector('.wizard-content');
      wizardBody.innerHTML = `
        <div class="text-center" style="padding: 3rem 1rem;">
          <div style="width: 64px; height: 64px; background: #D1FAE5; color: #065F46; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1.5rem;">
            <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="20 6 9 17 4 12"></polyline>
            </svg>
          </div>
          <span class="badge badge-demo mb-2">Demonstration Simulation</span>
          <h3 style="font-size: 1.85rem; margin-bottom: 0.75rem;">Consultation Enquiry Prepared</h3>
          <p style="max-width: 580px; margin: 0 auto 1.75rem; color: var(--secondary-text);">
            Thank you, <strong>${formData.fullName}</strong>. In an active production environment, your consulting brief for <strong>${formData.organization}</strong> would be routed directly to the appropriate executive practice lead for scheduling.
          </p>
          <div style="background: #F8FAFC; border: 1px dashed var(--border-color); padding: 1.25rem; max-width: 520px; margin: 0 auto 2rem; border-radius: var(--radius-sm); font-size: 0.85rem; color: var(--secondary-text);">
            Note: This static prototype does not transmit or store personal information. To discuss actual client engagements, please contact the advisory office directly via our official channels.
          </div>
          <a href="index.html" class="btn btn-primary">Return to Homepage</a>
        </div>
      `;
    });
  }

  updateWizardUI();
}

/* Contact Form Validation & Feedback (Rule #31) */
function initContactForm() {
  const contactForm = document.querySelector('#general-contact-form');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;

    // Reset errors
    contactForm.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
    contactForm.querySelectorAll('.form-feedback').forEach(el => el.remove());

    const showError = (input, msg) => {
      isValid = false;
      input.classList.add('is-invalid');
      const err = document.createElement('div');
      err.className = 'form-feedback';
      err.innerText = msg;
      input.parentNode.appendChild(err);
    };

    const name = contactForm.querySelector('#contact-name');
    const email = contactForm.querySelector('#contact-email');
    const phone = contactForm.querySelector('#contact-phone');
    const org = contactForm.querySelector('#contact-org');
    const message = contactForm.querySelector('#contact-message');

    if (!name?.value.trim()) showError(name, 'Full name is required.');
    if (!email?.value.trim() || !/\S+@\S+\.\S+/.test(email.value)) showError(email, 'Valid business email is required.');
    if (!phone?.value.trim()) showError(phone, 'Contact phone number is required.');
    if (!org?.value.trim()) showError(org, 'Organization name is required.');
    if (!message?.value.trim()) showError(message, 'Please provide a brief summary of the business challenge.');

    if (isValid) {
      const formContainer = contactForm.parentElement;
      formContainer.innerHTML = `
        <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: var(--radius-md); padding: 2.5rem; text-align: center;">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#16A34A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin: 0 auto 1rem;">
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
          </svg>
          <span class="badge badge-demo mb-2">Demo Submission Confirmed</span>
          <h3 style="color: #166534; margin-bottom: 0.5rem;">Message Received (Demo Mode)</h3>
          <p style="color: #15803D; font-size: 0.95rem; max-width: 500px; margin: 0 auto 1.5rem;">
            Your demonstration inquiry has been processed locally. No personal data was uploaded to any remote server or database.
          </p>
          <button type="button" class="btn btn-outline" onclick="window.location.reload();">Submit Another Demo Inquiry</button>
        </div>
      `;
    }
  });
}

/* Careers Form (Rule #33) */
function initCareerForm() {
  const careerForm = document.querySelector('#career-application-form');
  if (!careerForm) return;

  careerForm.addEventListener('submit', (e) => {
    e.preventDefault();
    if (window.showToast) {
      window.showToast('Demonstration Application Received: No data is saved or processed in this static preview.');
    }
    careerForm.reset();
  });
}
