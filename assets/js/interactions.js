/**
 * MANAGEMENT CONSULTING COMPANY - INTERACTIONS
 * FAQ Accordion, Filtering Tabs, Search, Interactive Modals/Toasts
 */

document.addEventListener('DOMContentLoaded', () => {
  initFaqAccordion();
  initCaseStudyFilter();
  initInsightsFilterAndSearch();
});

/* Toast Notification Utility */
window.showToast = function(message, duration = 4000) {
  let toast = document.querySelector('.toast-notice');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast-notice';
    toast.setAttribute('role', 'alert');
    document.body.appendChild(toast);
  }
  toast.innerHTML = `
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color:var(--muted-gold);flex-shrink:0;">
      <circle cx="12" cy="12" r="10"></circle>
      <line x1="12" y1="16" x2="12" y2="12"></line>
      <line x1="12" y1="8" x2="12.01" y2="8"></line>
    </svg>
    <span>${message}</span>
  `;
  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, duration);
};

/* FAQ Accordion */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  if (!faqItems.length) return;

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');
      
      // Close other items in the same container for clean accordion effect
      const parentList = item.closest('.faq-list');
      if (parentList) {
        parentList.querySelectorAll('.faq-item').forEach(other => {
          if (other !== item) other.classList.remove('is-open');
        });
      }

      item.classList.toggle('is-open', !isOpen);
      questionBtn.setAttribute('aria-expanded', !isOpen);
    });
  });
}

/* Case Study Filter Tabs */
function initCaseStudyFilter() {
  const filterTabs = document.querySelectorAll('.case-filter-tab');
  const caseCards = document.querySelectorAll('.case-study-card-item');

  if (!filterTabs.length || !caseCards.length) return;

  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const filterCategory = tab.getAttribute('data-filter');

      caseCards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        if (filterCategory === 'all' || cardCategory === filterCategory) {
          card.style.display = 'flex';
          card.classList.add('fade-in');
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* Insights Category Filters and Live Search */
function initInsightsFilterAndSearch() {
  const filterTabs = document.querySelectorAll('.insight-filter-tab');
  const searchInput = document.querySelector('.insights-search-input');
  const articleCards = document.querySelectorAll('.insight-card-item');

  if (!articleCards.length) return;

  let activeCategory = 'all';
  let searchTerm = '';

  const applyFilters = () => {
    articleCards.forEach(card => {
      const cardCategory = card.getAttribute('data-category') || '';
      const title = card.querySelector('.article-card-title')?.innerText.toLowerCase() || '';
      const excerpt = card.querySelector('.article-card-excerpt')?.innerText.toLowerCase() || '';

      const matchesCategory = (activeCategory === 'all' || cardCategory === activeCategory);
      const matchesSearch = (!searchTerm || title.includes(searchTerm) || excerpt.includes(searchTerm));

      if (matchesCategory && matchesSearch) {
        card.style.display = 'flex';
        card.classList.add('fade-in');
      } else {
        card.style.display = 'none';
      }
    });
  };

  if (filterTabs.length) {
    filterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        filterTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        activeCategory = tab.getAttribute('data-filter');
        applyFilters();
      });
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }
}
