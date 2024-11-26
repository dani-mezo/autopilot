[...document.querySelectorAll('a[href*="linkedin.com/in/"]')].forEach(link => {
    window.open(link.href, '_blank');
});
// disable popup blockage in chrome