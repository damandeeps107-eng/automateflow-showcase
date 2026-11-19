import re

template_file = '/Users/user/.gemini/antigravity/scratch/automateflow-showcase/dimora-elite.html'
with open(template_file) as f:
    html = f.read()

# Replace Brand and Contact
html = html.replace('Dimora Elite Interiors', 'Madhav Furniture & Interior')
html = html.replace('Dimora Elite', 'Madhav Furniture & Interior')
html = html.replace('DIMORA ELITE', 'MADHAV FURNITURE & INTERIOR')
html = html.replace('dimora', 'madhav')
html = html.replace('Gurugram', 'Ahmedabad')
html = html.replace('Gurgaon', 'Ahmedabad & Gandhinagar')
html = html.replace('919266477827', '919033629130')
html = html.replace('+91 92664 77827', '+91 90336 29130')
html = html.replace('Curated Turnkey Residences', 'Bespoke Interiors & Custom Furniture')

# Add Modal CSS and HTML and JS
modal_css = """
    /* Inquiry Modal on Page Load */
    .inquiry-modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 17, 21, 0.75);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      visibility: hidden;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .inquiry-modal-backdrop.active {
      opacity: 1;
      visibility: visible;
    }
    .inquiry-modal {
      background: #FFFFFF;
      border-radius: 20px;
      max-width: 500px;
      width: 100%;
      padding: 32px;
      position: relative;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.3);
      transform: translateY(20px) scale(0.96);
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      border: 1px solid rgba(184, 142, 95, 0.2);
    }
    .inquiry-modal-backdrop.active .inquiry-modal {
      transform: translateY(0) scale(1);
    }
    .modal-close-btn {
      position: absolute;
      top: 18px;
      right: 18px;
      background: #F4EDE4;
      border: none;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      font-size: 18px;
      color: #18191D;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }
    .modal-close-btn:hover {
      background: #B88E5F;
      color: #FFFFFF;
    }
    .modal-badge {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #B88E5F;
      background: #FBF9F5;
      padding: 4px 12px;
      border-radius: 20px;
      border: 1px solid rgba(184, 142, 95, 0.3);
      margin-bottom: 12px;
    }
    .modal-title {
      font-family: 'Playfair Display', serif;
      font-size: 24px;
      font-weight: 700;
      color: #121316;
      line-height: 1.3;
      margin-bottom: 8px;
    }
    .modal-subtitle {
      font-size: 13px;
      color: #6A6E78;
      margin-bottom: 22px;
      line-height: 1.5;
    }
    .modal-form-group {
      margin-bottom: 14px;
      text-align: left;
    }
    .modal-form-group label {
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: #121316;
      margin-bottom: 6px;
    }
    .modal-form-group input, .modal-form-group select {
      width: 100%;
      padding: 11px 14px;
      border-radius: 10px;
      border: 1px solid rgba(18, 19, 22, 0.15);
      background: #FAF8F5;
      font-size: 14px;
      color: #121316;
      outline: none;
      transition: border 0.2s;
      font-family: inherit;
    }
    .modal-form-group input:focus, .modal-form-group select:focus {
      border-color: #B88E5F;
      background: #FFFFFF;
    }
    .modal-submit-btn {
      width: 100%;
      background: #18191D;
      color: #FFFFFF;
      font-size: 14px;
      font-weight: 700;
      padding: 14px 20px;
      border-radius: 12px;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 8px 24px rgba(24, 25, 29, 0.2);
      transition: all 0.25s;
      margin-top: 18px;
    }
    .modal-submit-btn:hover {
      background: #B88E5F;
      transform: translateY(-2px);
      box-shadow: 0 10px 28px rgba(184, 142, 95, 0.35);
    }
    .modal-footnote {
      font-size: 11px;
      color: #8C909A;
      margin-top: 12px;
      text-align: center;
    }
"""

modal_html = """
  <!-- Automatic Inquiry Modal on Page Load -->
  <div class="inquiry-modal-backdrop" id="inquiryModal">
    <div class="inquiry-modal">
      <button class="modal-close-btn" onclick="closeInquiryModal()">&times;</button>
      <span class="modal-badge">✨ Limited Period Festive Offer</span>
      <h3 class="modal-title">Get Free 3D Design & Instant Cost Estimate</h3>
      <p class="modal-subtitle">Share your space details below — our design team in Ahmedabad will prepare an instant itemized estimate & 3D layout on WhatsApp.</p>
      
      <form id="leadModalForm" onsubmit="handleModalSubmit(event)">
        <div class="modal-form-group">
          <label>Your Name</label>
          <input type="text" id="mName" placeholder="e.g. Rajesh Patel" required>
        </div>
        <div class="modal-form-group">
          <label>WhatsApp Number</label>
          <input type="tel" id="mPhone" placeholder="e.g. 98980 12345" required>
        </div>
        <div class="modal-form-group">
          <label>Property / Interior Requirement</label>
          <select id="mRequirement">
            <option value="3 BHK Complete Interior & Furniture">3 BHK Complete Turnkey Interior & Furniture</option>
            <option value="2 BHK Complete Interior">2 BHK Complete Interior Package</option>
            <option value="4 BHK / Villa Luxury Makeover">4 BHK / Villa Luxury Makeover</option>
            <option value="Modular Kitchen & Custom Wardrobes">Modular Kitchen & Custom Wardrobes Only</option>
            <option value="Custom Wooden Furniture">Custom Wooden Furniture Only</option>
          </select>
        </div>
        <div class="modal-form-group">
          <label>Estimated Project Budget</label>
          <select id="mBudget">
            <option value="₹6 Lakh - ₹10 Lakh">₹6 Lakh - ₹10 Lakh</option>
            <option value="₹10 Lakh - ₹18 Lakh" selected>₹10 Lakh - ₹18 Lakh</option>
            <option value="₹18 Lakh - ₹30 Lakh+">₹18 Lakh - ₹30 Lakh+</option>
          </select>
        </div>
        <button type="submit" class="modal-submit-btn">
          <span>📲 Get Instant Estimate on WhatsApp</span>
        </button>
        <p class="modal-footnote">🔒 100% Privacy Protected. 45-Day Handover Guarantee & 10-Year Warranty.</p>
      </form>
    </div>
  </div>
"""

modal_js = """
  <script>
    // Open inquiry modal automatically 1.2s after page load
    window.addEventListener('DOMContentLoaded', () => {
      setTimeout(() => {
        const modal = document.getElementById('inquiryModal');
        if (modal) modal.classList.add('active');
      }, 1200);
    });

    function closeInquiryModal() {
      const modal = document.getElementById('inquiryModal');
      if (modal) modal.classList.remove('active');
    }

    function handleModalSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('mName').value.trim();
      const phone = document.getElementById('mPhone').value.trim();
      const req = document.getElementById('mRequirement').value;
      const budget = document.getElementById('mBudget').value;

      const waMsg = encodeURIComponent(
        `Hi Madhav Furniture & Interior! My name is ${name}. I am looking for ${req} with an estimated budget of ${budget} in Ahmedabad. My contact number is ${phone}. Please share 3D concepts and estimated cost breakdown.`
      );
      
      closeInquiryModal();
      window.open(`https://wa.me/919033629130?text=${waMsg}`, '_blank');
    }
  </script>
"""

# Insert CSS before </style>
html = html.replace('</style>', modal_css + '\n</style>')

# Insert modal HTML right after <body>
html = html.replace('<body>', '<body>\n' + modal_html)

# Insert modal JS right before </body>
html = html.replace('</body>', modal_js + '\n</body>')

with open('/Users/user/.gemini/antigravity/scratch/automateflow-showcase/madhav-furniture.html', 'w') as f:
    f.write(html)

print("Generated madhav-furniture.html with Auto-Inquiry Popup successfully!")
