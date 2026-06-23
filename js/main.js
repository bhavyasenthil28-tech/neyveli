document.addEventListener('DOMContentLoaded', () => {
    loadHeader();
    loadFooter();
});

function loadHeader() {
    const isDetailsDir = window.location.pathname.includes('/details/');
    const base = isDetailsDir ? '../' : '';
    const detailBase = isDetailsDir ? '' : 'details/';

    const headerHTML = `
        <div class="navbar">
            <div class="logo"><a href="${base}index.html" style="text-transform: none; font-size: 1.65rem; font-weight: 800; color: #cc0000 !important;">Neyveli.jbss.in</a></div>
            <div class="mobile-toggle" onclick="document.querySelector('.nav-links').classList.toggle('show')">☰</div>
            <nav class="nav-links">
                <div class="nav-item">
                    <a href="${base}index.html">Home</a>
                </div>
                <div class="nav-item">
                    <a href="${base}about.html">About</a>
                </div>
                <div class="nav-item">
                    <a href="${base}infrastructure.html">Infrastructure</a>
                </div>
                <div class="nav-item">
                    <a href="#">Places to Visit ▼</a>
                    <ul class="dropdown-menu">
                        <li><a href="${base}tourist-places.html">Places to Visit</a></li>
                        <li><a href="${base}temples.html">Temples</a></li>
                        <li><a href="${base}churches.html">Churches</a></li>
                        <li><a href="${base}mosques-dargahs.html">Mosques & Dargahs</a></li>
                    </ul>
                </div>
                <div class="nav-item">
                    <a href="#">Business Directory ▼</a>
                    <ul class="dropdown-menu">
                        <li><a href="${base}marriage-halls.html">Marriage Halls</a></li>
                        <li><a href="${base}petrol-bunks.html">Petrol Bunks</a></li>
                        <li><a href="${base}medical-shops.html">Medical Shops</a></li>
                        <li><a href="${base}hotels-restaurants.html">Hotels & Restaurants</a></li>
                        <li><a href="${base}shopping-centers.html">Shopping Centers</a></li>
                    </ul>
                </div>
                <div class="nav-item">
                    <a href="#">Information ▼</a>
                    <ul class="dropdown-menu">
                        <li><a href="${base}government-offices.html">Government Offices</a></li>
                        <li><a href="${base}hospitals.html">Hospitals</a></li>
                        <li><a href="${base}schools-colleges.html">Educational Institutions</a></li>
                        <li><a href="${base}public-services.html">Important Services</a></li>
                    </ul>
                </div>
                <div class="nav-item">
                    <a href="${base}transport-services.html">Transport Services</a>
                </div>
                <div class="nav-item">
                    <a href="${base}contact.html">Contact</a>
                </div>
            </nav>
        </div>
    `;
    const headerEl = document.querySelector('header');
    if (headerEl) {
        headerEl.innerHTML = headerHTML;
        
        // Highlight active link
        let currentPath = window.location.pathname.split('/').pop();
        if (!currentPath || currentPath === '') currentPath = 'index.html';
        
        const links = headerEl.querySelectorAll('.nav-item > a, .dropdown-menu a');
        links.forEach(link => {
            let href = link.getAttribute('href');
            if (href) {
                // strip base path prefixes for matching
                const linkFile = href.replace('../', '').replace('./', '');
                if (linkFile === currentPath) {
                    link.classList.add('active');
                    // If it's in a dropdown, also highlight the parent nav-item
                    const parentNav = link.closest('.nav-item');
                    if (parentNav && parentNav.querySelector('> a')) {
                        parentNav.querySelector('> a').classList.add('active');
                    }
                }
            }
        });
    }
}

function loadFooter() {
    const isDetailsDir = window.location.pathname.includes('/details/');
    const base = isDetailsDir ? '../' : '';

    const footerHTML = `
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="${base}tourist-places.html">Places to Visit</a></li>
                        <li><a href="${base}marriage-halls.html">Business Directory</a></li>
                        <li><a href="${base}government-offices.html">Information</a></li>
                        <li><a href="${base}transport-services.html">Transport</a></li>
                        <li><a href="${base}contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Contact Information</h3>
                    <p style="margin-bottom:10px;"><strong>Address:</strong><br>
                    New No 39 (Old No 16,17), 2nd Floor,<br>
                    Kodambakkam Road,<br>
                    West Mambalam,<br>
                    Chennai – 600033.</p>
                    <p style="margin-bottom:10px;"><strong>Email:</strong> <a href="mailto:sales@jbsoft.in">sales@jbsoft.in</a></p>
                    <p><strong>Phone:</strong> <a href="tel:+919840279047">+91 98402 79047</a></p>
                </div>
                <div class="footer-col">
                    <h3>Follow Us</h3>
                    <ul>
                        <li><a href="#">Facebook</a></li>
                        <li><a href="#">Instagram</a></li>
                        <li><a href="#">YouTube</a></li>
                        <li><a href="#">X (Twitter)</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Neyveli Information Portal. All Rights Reserved.</p>
                <p style="margin-top:5px;">Designed & Developed by JBSOFT Technologies.</p>
            </div>
        </div>
    `;
    const footerEl = document.querySelector('footer');
    if (footerEl) {
        footerEl.innerHTML = footerHTML;
    }
}
