/**
 * MANAGEMENT CONSULTING COMPANY - MAIN JAVASCRIPT
 * Core Navigation, Sticky Header, Mobile Drawer, Back to Top
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNavigation();
  initActiveNavLink();
  initBackToTop();
});

/* Sticky Header on Scroll */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/* Mobile Hamburger & Expandable Dropdowns */
function initMobileNavigation() {
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  const mainNav = document.querySelector('.main-nav');
  const dropdownItems = document.querySelectorAll('.nav-item.has-dropdown');

  if (!toggleBtn || !mainNav) return;

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = mainNav.classList.toggle('is-open');
    toggleBtn.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  // Mobile submenu expanders for all dropdowns
  dropdownItems.forEach(item => {
    const trigger = item.querySelector(':scope > .nav-link');
    if (trigger) {
      trigger.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const wasExpanded = item.classList.contains('is-expanded');
          dropdownItems.forEach(other => other.classList.remove('is-expanded'));
          if (!wasExpanded) {
            item.classList.add('is-expanded');
          }
        }
      });
    }
  });

  // Close mobile menu when clicking outside
  document.addEventListener('click', (e) => {
    if (mainNav.classList.contains('is-open') && !mainNav.contains(e.target) && !toggleBtn.contains(e.target)) {
      mainNav.classList.remove('is-open');
      toggleBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });

  // Close menu on ESC key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mainNav.classList.contains('is-open')) {
      mainNav.classList.remove('is-open');
      toggleBtn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  });
}

/* Highlight Active Nav Link based on Current URL */
function initActiveNavLink() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .mega-menu-link, .dropdown-link, .footer-links a');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
      // If inside a dropdown menu, also highlight parent top-level nav link
      const parentDropdown = link.closest('.nav-item.has-dropdown');
      if (parentDropdown) {
        const parentLink = parentDropdown.querySelector(':scope > .nav-link');
        if (parentLink) parentLink.classList.add('active');
      }
    }
  });
}

/* Back to Top Smooth Scroll */
function initBackToTop() {
  const backToTopBtn = document.querySelector('.back-to-top-btn');
  if (!backToTopBtn) return;

  backToTopBtn.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}
