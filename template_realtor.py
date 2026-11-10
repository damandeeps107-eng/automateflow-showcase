#!/usr/bin/env python3
"""
Master Realtor / Property Advisory Landing Page Generator
Faithfully implements the layout of DNA Realtors (User's Exact Reference 'home page idea'):
1. Slim Top Bar with RERA Regd Nos & Social Icons
2. Main Header with Company Logo + Call Box + Mail/Connect Box
3. Deep Navy Full-Width Horizontal Navigation Bar
4. Signature Hero Banner with Left Plum Brand Card + Cursive Tagline 'Where Luxury Meets Comfort'
5. Slider Navigation (<, >, dots) & High-Resolution Architectural Background
6. Floating WhatsApp Button
7. Curated Inventory & Corporate RERA Footprint
"""

def generate_realtor_page(biz_name, handle, phone, city, logo_url, slug, properties=None):
    clean_handle = handle.replace("@", "").strip()
    
    if not properties:
        properties = [
            {
                "title": f"Luxury Independent Builder Floor",
                "tag": "Ready for Registry",
                "specs": f"350–500 Sq. Yds. • {city}",
                "desc": "Italian marble flooring, private elevator access directly into apartment foyer, 3 dedicated covered stilt car parks, and private terrace.",
                "img": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": f"Signature Park Facing Penthouse",
                "tag": "Exclusive Distress Deal",
                "specs": f"500 Sq. Yds. Corner • {city}",
                "desc": "Two-side open corner floor with double height living lounge, central VRV air conditioning, and unobstructed green park views.",
                "img": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": f"Executive 3 BHK Builder Floor",
                "tag": "Prime Connectivity",
                "specs": f"270–300 Sq. Yds. • {city}",
                "desc": "Walking distance from prime sector road. Gated 24/7 security with 100% power backup and immediate occupancy ready.",
                "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"
            }
        ]

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{biz_name} | Verified Real Estate &amp; Builder Floors in {city}</title>
  <meta name="description" content="{biz_name} - Trusted Real Estate Advisory and luxury builder floors in {city}. RERA verified properties and direct builder mandate.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #FFFFFF;
      color: #1F2937;
      line-height: 1.5;
    }}
    .font-cursive {{
      font-family: 'Caveat', cursive;
    }}
    .top-bar-bg {{
      background-color: #380E38;
    }}
    .nav-bar-bg {{
      background-color: #151D30;
    }}
    .plum-card-bg {{
      background-color: #481148;
    }}
    .plum-card-border {{
      border-color: #5D185D;
    }}
    .slider-arrow {{
      border: 1px solid rgba(255, 255, 255, 0.6);
      transition: all 0.2s ease;
    }}
    .slider-arrow:hover {{
      background: rgba(255, 255, 255, 0.2);
      border-color: #FFFFFF;
    }}
    .floating-wa {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999;
      box-shadow: 0 8px 24px rgba(37, 211, 102, 0.4);
      transition: all 0.3s ease;
    }}
    .floating-wa:hover {{
      transform: scale(1.08);
    }}
  </style>
</head>
<body class="antialiased">

  <!-- 1. Top Bar with RERA Regd Numbers and Social Media Icons -->
  <div class="top-bar-bg text-white text-[11px] sm:text-xs py-2 px-4">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
      <div class="tracking-wide">
        <span class="font-semibold text-neutral-200">RERA Regd no.</span> 
        <span class="text-pink-300">Punjab :</span> PBRERA-SAS79-REA0957, 
        <span class="text-pink-300">Haryana:</span> HRERA-PKL-REA-200-2019
      </div>
      <div class="flex items-center space-x-4 text-neutral-300">
        <a href="#" class="hover:text-white transition">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
        </a>
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-pink-300 transition">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
        </a>
        <a href="#" class="hover:text-red-400 transition">
          <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        </a>
      </div>
    </div>
  </div>

  <!-- 2. Main White Branding Header (Logo + Call Us + Connect Us) -->
  <header class="bg-white py-4 px-4 sm:px-6 lg:px-8 border-b border-gray-100">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- Brand Logo & Slogan -->
      <a href="#" class="flex items-center space-x-3.5 text-left">
        <img src="{logo_url}" alt="{biz_name} Logo" class="w-14 h-14 rounded-md object-cover border border-purple-200 shadow-sm" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=200&q=80'">
        <div>
          <span class="text-xl sm:text-2xl font-bold tracking-tight text-[#380E38] block uppercase leading-none">
            {biz_name}
          </span>
          <span class="text-[11px] font-medium text-gray-500 tracking-wider block mt-1">
            Your Prosperity, Our Priority • {city}
          </span>
        </div>
      </a>

      <!-- Contact Badges Matching Reference -->
      <div class="flex flex-wrap items-center justify-center gap-6 sm:gap-8 text-left">
        
        <!-- Call Box -->
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#380E38]">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          </div>
          <div>
            <a href="tel:+{phone}" class="text-xs sm:text-sm font-bold text-gray-900 block hover:text-[#380E38] transition leading-tight">
              +{phone}
            </a>
            <span class="text-[11px] text-gray-400 font-normal">Call us</span>
          </div>
        </div>

        <!-- Connect Box -->
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-full border border-gray-300 flex items-center justify-center text-[#380E38]">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
          </div>
          <div>
            <a href="https://wa.me/{phone}" class="text-xs sm:text-sm font-bold text-gray-900 block hover:text-[#380E38] transition leading-tight">
              contact@{slug}.in
            </a>
            <span class="text-[11px] text-gray-400 font-normal">You can mail us</span>
          </div>
        </div>

      </div>

    </div>
  </header>

  <!-- 3. Full-Width Deep Navy Horizontal Navigation Bar -->
  <nav class="nav-bar-bg text-white text-[11px] sm:text-xs font-semibold tracking-wider uppercase sticky top-0 z-40 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between overflow-x-auto py-3 space-x-6 sm:space-x-8 no-scrollbar">
        <a href="#" class="text-pink-400 hover:text-white transition whitespace-nowrap">HOME</a>
        <a href="#about" class="hover:text-pink-300 transition whitespace-nowrap">ABOUT US</a>
        <a href="#projects" class="hover:text-pink-300 transition whitespace-nowrap flex items-center">
          PROJECTS <span class="text-[9px] ml-1">▼</span>
        </a>
        <a href="#requirement" class="hover:text-pink-300 transition whitespace-nowrap">POST YOUR REQUIREMENT</a>
        <a href="#buyers-guide" class="hover:text-pink-300 transition whitespace-nowrap flex items-center">
          BUYER'S GUIDE <span class="text-[9px] ml-1">▼</span>
        </a>
        <a href="#nri-section" class="hover:text-pink-300 transition whitespace-nowrap">NRI SECTION</a>
        <a href="#home-loans" class="hover:text-pink-300 transition whitespace-nowrap flex items-center">
          HOME LOANS <span class="text-[9px] ml-1">▼</span>
        </a>
        <a href="#careers" class="hover:text-pink-300 transition whitespace-nowrap">CAREERS</a>
        <a href="#contact" class="hover:text-pink-300 transition whitespace-nowrap">CONTACT US</a>
      </div>
    </div>
  </nav>

  <!-- 4. Signature Hero Banner Matching User's Image Idea Exactly -->
  <div class="relative w-full overflow-hidden bg-neutral-900">
    
    <!-- Background High-Rise Architectural Image -->
    <div class="relative h-[440px] sm:h-[520px] lg:h-[580px] w-full">
      <img 
        src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1920&q=85" 
        alt="Prime Luxury Residential High-Rise Towers" 
        class="w-full h-full object-cover object-center"
      >
      <!-- Dark overlay for contrast -->
      <div class="absolute inset-0 bg-black/25"></div>
    </div>

    <!-- Left Plum Brand Card Overlay Matching DNA Realtors Screenshot -->
    <div class="absolute top-0 left-0 bottom-0 w-full sm:w-[480px] lg:w-[540px] plum-card-bg text-white flex flex-col justify-center px-8 sm:px-14 py-12 z-10 shadow-2xl">
      <div class="max-w-md">
        <span class="text-xl sm:text-2xl font-light text-neutral-200 block leading-tight">
          Experience
        </span>
        <span class="text-xl sm:text-2xl font-light text-neutral-200 block leading-tight mb-2">
          elevated living at
        </span>
        <h1 class="text-2xl sm:text-4xl font-extrabold uppercase tracking-tight text-white mb-6 leading-tight">
          {biz_name.upper()}
        </h1>

        <!-- Cursive Script Tagline Matching Reference -->
        <div class="font-cursive text-3xl sm:text-5xl text-neutral-100 font-semibold mb-8 transform -rotate-1">
          Where Luxury Meets Comfort
        </div>

        <!-- Slider Arrow Button (Left) -->
        <button class="slider-arrow w-10 h-10 rounded flex items-center justify-center text-white" aria-label="Previous Slide">
          <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
        </button>
      </div>
    </div>

    <!-- Right Slider Arrow Button -->
    <button class="slider-arrow absolute right-6 top-1/2 -translate-y-1/2 w-10 h-10 rounded flex items-center justify-center text-white z-10 hidden sm:flex" aria-label="Next Slide">
      <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
    </button>

    <!-- Slider Pagination Dots at Bottom Center -->
    <div class="absolute bottom-6 left-1/2 sm:left-2/3 -translate-x-1/2 flex items-center space-x-2.5 z-10">
      <span class="w-3 h-3 rounded-full bg-white shadow"></span>
      <span class="w-3 h-3 rounded-full bg-white/50 border border-white/80"></span>
      <span class="w-3 h-3 rounded-full bg-white/50 border border-white/80"></span>
      <span class="w-3 h-3 rounded-full bg-white/50 border border-white/80"></span>
    </div>

  </div>

  <!-- 5. Featured Properties Section -->
  <section id="projects" class="py-16 bg-gray-50 border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-2xl mx-auto mb-12">
        <span class="text-xs font-bold text-[#380E38] uppercase tracking-widest block mb-1">Curated Inventory</span>
        <h2 class="text-2xl sm:text-3xl font-bold text-gray-900">Featured Residential Projects in {city}</h2>
        <p class="text-xs sm:text-sm text-gray-500 mt-2">100% RERA compliant properties verified by {biz_name} advisory desk.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">"""

    for prop in properties:
        html += f"""
        <div class="bg-white rounded-lg overflow-hidden border border-gray-200 shadow-sm flex flex-col justify-between hover:shadow-lg transition">
          <div>
            <div class="relative h-60 overflow-hidden bg-gray-100">
              <img src="{prop['img']}" alt="{prop['title']}" class="w-full h-full object-cover">
              <span class="absolute top-3 left-3 bg-[#380E38] text-white text-[11px] font-semibold px-2.5 py-1 rounded">
                {prop['tag']}
              </span>
            </div>
            <div class="p-6">
              <span class="text-xs font-semibold text-gray-400 block mb-1">{prop['specs']}</span>
              <h3 class="text-lg font-bold text-gray-900 mb-2 leading-snug">{prop['title']}</h3>
              <p class="text-xs text-gray-600 leading-relaxed mb-4">{prop['desc']}</p>
            </div>
          </div>
          <div class="p-6 pt-0">
            <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20am%20interested%20in%20visiting%20{prop['title']}.%20Please%20send%20brochure%20and%20location." class="w-full bg-[#151D30] hover:bg-[#380E38] text-white py-3 rounded text-xs font-bold uppercase tracking-wider text-center block transition">
              View Project Details →
            </a>
          </div>
        </div>"""

    html += f"""
      </div>
    </div>
  </section>

  <!-- 6. About & Advisory Trust Section -->
  <section id="about" class="py-16 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="p-6 rounded-lg bg-purple-50 border border-purple-100">
          <span class="text-sm font-bold text-[#380E38] block mb-2">01. RERA Compliance</span>
          <h4 class="text-base font-bold text-gray-900 mb-2">Pre-Verified Titles &amp; Approvals</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Every residential and commercial property is audited for clear registry documents, sanctioned town planning, and occupancy approvals.
          </p>
        </div>
        <div class="p-6 rounded-lg bg-blue-50 border border-blue-100">
          <span class="text-sm font-bold text-[#151D30] block mb-2">02. Direct Mandates</span>
          <h4 class="text-base font-bold text-gray-900 mb-2">Direct Developer Terms</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Transparent payment schedules linked directly to construction milestones with zero hidden brokerage overheads.
          </p>
        </div>
        <div class="p-6 rounded-lg bg-green-50 border border-green-100">
          <span class="text-sm font-bold text-green-800 block mb-2">03. NRI Advisory Desk</span>
          <h4 class="text-base font-bold text-gray-900 mb-2">End-to-End Property Concierge</h4>
          <p class="text-xs text-gray-600 leading-relaxed">
            Dedicated assistance for NRI investors, site inspection videos, legal registry deeds, and property management across Tricity &amp; NCR.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- 7. Corporate Real Estate Footer -->
  <footer id="contact" class="bg-[#151D30] text-gray-300 py-12 text-xs border-t border-neutral-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="text-center sm:text-left">
        <span class="text-white font-bold text-sm block uppercase tracking-wide">{biz_name}</span>
        <span class="text-gray-400 mt-1 block">RERA Registered Real Estate Consultancy • {city}</span>
      </div>
      <div class="flex items-center space-x-6 text-gray-300">
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-pink-400 transition">
          Instagram: @{clean_handle}
        </a>
        <a href="https://wa.me/{phone}" class="text-emerald-400 font-semibold hover:underline">
          WhatsApp: +{phone}
        </a>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8 pt-8 border-t border-gray-700/60 text-center text-[11px] text-gray-500">
      © 2026 {biz_name}. All Rights Reserved. RERA Regd Partner.
    </div>
  </footer>

  <!-- 8. Floating WhatsApp Button (Matching Reference Image) -->
  <a href="https://wa.me/{phone}?text=Hi%20{biz_name}%20Team,%20I%20am%20interested%20in%20properties%20in%20{city}." class="floating-wa w-14 h-14 bg-[#25D366] rounded-full flex items-center justify-center text-white" aria-label="WhatsApp Us" target="_blank" rel="noopener noreferrer">
    <svg class="w-8 h-8 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
  </a>

</body>
</html>"""
    return html

if __name__ == "__main__":
    print("Realtor Template Generator Loaded.")
