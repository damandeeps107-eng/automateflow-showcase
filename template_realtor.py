#!/usr/bin/env python3
"""
Master Realtor / Property Advisory Landing Page Generator
Faithfully implements the layout of CCS Real Estate + Modern Ultra-Luxury Real Estate:
- Full professional header with brand logo, nav links & direct WhatsApp CTA
- Breathtaking Hero section featuring a large, ultra-sharp architectural photograph & floating luxury badges
- Curated luxury inventory collection with high-res photography, floor specs & WhatsApp visit scheduler
- 'Why Choose Direct Advisory' trust pillars
- Prime locality / sector highlights
- Editorial luxury footer
"""

def generate_realtor_page(biz_name, handle, phone, city, logo_url, slug, properties=None):
    clean_handle = handle.replace("@", "").strip()
    
    if not properties:
        properties = [
            {
                "title": f"4 BHK Ultra-Luxury Independent Floor • {city}",
                "tag": "Ready for Registry",
                "specs": "350–500 Sq. Yds. • Private Lift • 3 Covered Car Parks",
                "desc": "Italian marble flooring, German modular kitchen with built-in appliances, wrap-around balconies, and private landscaped terrace garden.",
                "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": f"Signature Corner Penthouse • {city}",
                "tag": "Exclusive Distress Opportunity",
                "specs": "500 Sq. Yds. Corner • Double Height Living Lounge",
                "desc": "Two-side open corner floor with private elevator access directly into apartment foyer, VRV central cooling, and panoramic green park views.",
                "img": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": f"Executive 3 BHK Builder Floor • {city}",
                "tag": "Prime Connectivity",
                "specs": "270–300 Sq. Yds. • Gated 24/7 Security",
                "desc": "Walking distance from wide arterial roads and city center. Sanctioned master plans with 100% power backup and immediate possession ready.",
                "img": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=80"
            }
        ]

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{biz_name} | Prime Luxury Builder Floors &amp; Real Estate in {city}</title>
  <meta name="description" content="Verified luxury builder floors, kothis and independent villas across {city}. Direct builder mandate, clear title registry, and private inspections with {biz_name}.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #FAF9F6;
      color: #1A1A1A;
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }}
    .font-serif-luxury {{
      font-family: 'Playfair Display', Georgia, serif;
    }}
    .border-subtle {{
      border-color: #E8E5DF;
    }}
    .btn-primary {{
      background-color: #111827;
      color: #FFFFFF;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-primary:hover {{
      background-color: #1F2937;
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.15);
    }}
    .btn-wa {{
      background-color: #0F5132;
      color: #FFFFFF;
      transition: all 0.25s ease;
    }}
    .btn-wa:hover {{
      background-color: #146C43;
      transform: translateY(-2px);
      box-shadow: 0 10px 20px -5px rgba(15, 81, 50, 0.3);
    }}
    .hero-glow {{
      background: radial-gradient(circle at 50% 20%, rgba(212, 175, 55, 0.08), transparent 70%);
    }}
  </style>
</head>
<body class="selection:bg-neutral-900 selection:text-white">

  <!-- Top Announcement Bar -->
  <aside aria-label="Announcement" class="bg-[#111827] text-neutral-300 py-2.5 px-4 text-center text-xs tracking-wider uppercase font-medium border-b border-neutral-800">
    <div class="max-w-7xl mx-auto flex items-center justify-center space-x-2">
      <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
      <span>Direct Developer Inventory • Verified Luxury Floors &amp; Kothis in {city} • Zero Middlemen</span>
    </div>
  </aside>

  <!-- Complete Professional Navigation Header -->
  <header class="sticky top-0 z-50 bg-[#FAF9F6]/95 backdrop-blur-md border-b border-subtle">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Brand Logo & Identity -->
      <a href="#" class="flex items-center space-x-3.5 group">
        <div class="relative">
          <img src="{logo_url}" alt="{biz_name} Logo" class="w-12 h-12 rounded-full object-cover border border-neutral-300 shadow-sm transition group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=200&q=80'">
          <span class="absolute bottom-0 right-0 w-3.5 h-3.5 bg-emerald-500 border-2 border-white rounded-full"></span>
        </div>
        <div>
          <span class="text-lg sm:text-xl font-bold tracking-tight text-neutral-900 font-serif-luxury block leading-none">
            {biz_name}
          </span>
          <span class="text-[11px] tracking-wider text-neutral-500 uppercase font-semibold mt-1 block">
            {city} Luxury Advisory Desk
          </span>
        </div>
      </a>

      <!-- Desktop Navigation Links -->
      <nav class="hidden lg:flex items-center space-x-8 text-xs font-semibold uppercase tracking-wider text-neutral-700">
        <a href="#featured-collection" class="hover:text-neutral-900 transition">Exclusive Inventory</a>
        <a href="#why-choose" class="hover:text-neutral-900 transition">Buyer Assurance</a>
        <a href="#specifications" class="hover:text-neutral-900 transition">Specifications</a>
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-neutral-900 transition flex items-center">
          <svg class="w-3.5 h-3.5 mr-1 text-pink-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          @{clean_handle}
        </a>
      </nav>

      <!-- Action Button -->
      <div class="flex items-center space-x-3">
        <a href="https://wa.me/{phone}?text=Hi%20{biz_name}%20Team,%20I%20am%20interested%20in%20visiting%20luxury%20builder%20floors%20in%20{city}." class="btn-primary px-5 py-2.5 rounded-lg text-xs sm:text-sm font-semibold tracking-wide flex items-center shadow-sm">
          <svg class="w-4 h-4 mr-1.5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
          Schedule Site Visit
        </a>
      </div>
    </div>
  </header>

  <!-- BREATHTAKING HERO SECTION WITH HERO IMAGE -->
  <main class="relative hero-glow border-b border-subtle overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 sm:pt-16 pb-16">
      
      <!-- Headline & Introduction -->
      <div class="max-w-4xl mx-auto text-center mb-10">
        <div class="inline-flex items-center space-x-2 bg-neutral-900/5 border border-neutral-300/80 px-3.5 py-1.5 rounded-full mb-5">
          <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
          <span class="text-xs uppercase tracking-widest text-neutral-800 font-semibold">Direct Developer Mandate • 2026 Collection</span>
        </div>

        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-normal font-serif-luxury text-neutral-900 leading-[1.18] mb-6">
          Architectural Builder Floors &amp; <br class="hidden sm:inline">
          <span class="italic font-medium text-neutral-800">Luxury Residences in {city}</span>
        </h1>

        <p class="text-sm sm:text-lg text-neutral-600 max-w-2xl mx-auto leading-relaxed">
          Curated portfolio with private elevators, dedicated stilt bays, Italian marble living rooms, and 100% verified registry titles.
        </p>
      </div>

      <!-- PROMINENT HERO IMAGE SHOWCASE (As Requested by User) -->
      <div class="relative max-w-5xl mx-auto rounded-2xl overflow-hidden shadow-2xl border border-neutral-200/90 group mb-12">
        <div class="aspect-[16/9] sm:aspect-[21/9] w-full overflow-hidden bg-neutral-900">
          <img 
            src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1800&q=85" 
            alt="Prime Luxury Property Showcase" 
            class="w-full h-full object-cover object-center group-hover:scale-105 transition duration-700 ease-out"
          >
        </div>

        <!-- Hero Image Dark Gradient Overlay -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex flex-col justify-end p-6 sm:p-10 text-white">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <span class="inline-block bg-white/20 backdrop-blur-md px-3 py-1 rounded text-xs uppercase tracking-widest font-semibold mb-2">
                Featured Facade • Ready For Possession
              </span>
              <h2 class="text-xl sm:text-3xl font-serif-luxury font-medium text-white">
                Signature Modern Villa &amp; Floor Concept
              </h2>
              <p class="text-xs sm:text-sm text-neutral-200 mt-1 max-w-xl">
                Exclusive gated floor series featuring double-height entrance foyers, VRV temperature control, and lush green park frontage.
              </p>
            </div>
            <a href="https://wa.me/{phone}?text=Namaste%20{biz_name},%20please%20share%20the%20complete%20walkthrough%20video%20and%20details%20for%20this%20property." class="btn-wa px-6 py-3 rounded-lg text-xs sm:text-sm font-bold uppercase tracking-wider flex items-center shadow-lg">
              Watch Walkthrough Video →
            </a>
          </div>
        </div>
      </div>

      <!-- Quick Specifications Strip -->
      <div id="specifications" class="grid grid-cols-2 lg:grid-cols-4 gap-4 max-w-5xl mx-auto">
        <div class="bg-white border border-subtle p-5 rounded-xl shadow-sm hover:border-neutral-400 transition">
          <span class="text-[11px] uppercase tracking-wider text-neutral-400 font-semibold block">Plot Dimensions</span>
          <span class="text-lg sm:text-xl font-bold font-serif-luxury text-neutral-900 mt-1 block">250–500 Sq. Yds.</span>
          <span class="text-xs text-neutral-500 mt-0.5 block">East &amp; Park Facing</span>
        </div>
        <div class="bg-white border border-subtle p-5 rounded-xl shadow-sm hover:border-neutral-400 transition">
          <span class="text-[11px] uppercase tracking-wider text-neutral-400 font-semibold block">Elevator Access</span>
          <span class="text-lg sm:text-xl font-bold font-serif-luxury text-neutral-900 mt-1 block">Private Lift Access</span>
          <span class="text-xs text-neutral-500 mt-0.5 block">Direct into Foyer</span>
        </div>
        <div class="bg-white border border-subtle p-5 rounded-xl shadow-sm hover:border-neutral-400 transition">
          <span class="text-[11px] uppercase tracking-wider text-neutral-400 font-semibold block">Dedicated Parking</span>
          <span class="text-lg sm:text-xl font-bold font-serif-luxury text-neutral-900 mt-1 block">2–4 Stilt Covered Cars</span>
          <span class="text-xs text-neutral-500 mt-0.5 block">Zero Street Clutter</span>
        </div>
        <div class="bg-white border border-subtle p-5 rounded-xl shadow-sm hover:border-neutral-400 transition">
          <span class="text-[11px] uppercase tracking-wider text-neutral-400 font-semibold block">Clear Paperwork</span>
          <span class="text-lg sm:text-xl font-bold font-serif-luxury text-neutral-900 mt-1 block">100% Registry Ready</span>
          <span class="text-xs text-neutral-500 mt-0.5 block">OC &amp; Sanctioned Plans</span>
        </div>
      </div>

    </div>
  </main>

  <!-- FEATURED PROPERTY COLLECTION -->
  <section id="featured-collection" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 pb-6 border-b border-subtle">
      <div>
        <span class="text-xs uppercase tracking-widest text-neutral-500 font-semibold block mb-2">Curated Inventory</span>
        <h2 class="text-2xl sm:text-4xl font-normal font-serif-luxury text-neutral-900">
          Featured Luxury Developments
        </h2>
      </div>
      <p class="text-xs sm:text-sm text-neutral-500 max-w-md mt-4 md:mt-0">
        Direct inventory across {city}. Each property is ready for immediate private walkthrough and title inspection.
      </p>
    </div>

    <!-- Properties Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">"""

    for prop in properties:
        html += f"""
      <div class="bg-white border border-subtle rounded-xl overflow-hidden flex flex-col justify-between shadow-sm hover:shadow-xl hover:border-neutral-400 transition duration-300">
        <div>
          <div class="relative h-64 overflow-hidden bg-neutral-200 group">
            <img src="{prop['img']}" alt="{prop['title']}" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <div class="absolute top-3 left-3 bg-[#111827]/90 text-white px-3 py-1 rounded-md text-[11px] font-semibold tracking-wide">
              {prop['tag']}
            </div>
          </div>
          <div class="p-6">
            <span class="text-xs font-semibold text-neutral-500 block mb-1">{prop['specs']}</span>
            <h3 class="text-lg font-bold font-serif-luxury text-neutral-900 mb-2 leading-snug">{prop['title']}</h3>
            <p class="text-xs text-neutral-600 leading-relaxed mb-4">{prop['desc']}</p>
          </div>
        </div>
        <div class="p-6 pt-0">
          <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20am%20interested%20in%20visiting%20{prop['title']}.%20Please%20send%20brochure%20and%20exact%20location." class="w-full btn-primary py-3 rounded-lg text-xs font-bold uppercase tracking-wider text-center block">
            Schedule Private Inspection →
          </a>
        </div>
      </div>"""

    html += f"""
    </div>
  </section>

  <!-- WHY BUYERS WORK DIRECTLY WITH ADVISOR -->
  <section id="why-choose" class="border-t border-subtle bg-[#F4F3EE] py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-14">
        <span class="text-xs uppercase tracking-widest text-neutral-500 font-semibold block mb-2">Credibility &amp; Trust</span>
        <h3 class="text-2xl sm:text-3xl font-serif-luxury font-normal text-neutral-900">Why Buyers Choose {biz_name}</h3>
        <p class="text-xs sm:text-sm text-neutral-600 mt-2">Zero false commitments. Complete title scrutiny, direct builder mandates, and full registry assistance.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-8 rounded-xl border border-subtle shadow-sm">
          <span class="text-sm font-bold text-neutral-400 font-serif-luxury block mb-2">01</span>
          <h4 class="text-base font-bold text-neutral-900 mb-2 font-serif-luxury">100% Pre-Verified Titles</h4>
          <p class="text-xs text-neutral-600 leading-relaxed">
            Every builder floor is vetted for sanctioned layouts, occupancy certificate approvals, structural certificates, and non-encumbrance chain of deeds.
          </p>
        </div>
        <div class="bg-white p-8 rounded-xl border border-subtle shadow-sm">
          <span class="text-sm font-bold text-neutral-400 font-serif-luxury block mb-2">02</span>
          <h4 class="text-base font-bold text-neutral-900 mb-2 font-serif-luxury">Direct Builder Mandate</h4>
          <p class="text-xs text-neutral-600 leading-relaxed">
            Transparent payment schedules linked directly with construction milestones and registry timeline. Direct negotiations without multiple middlemen.
          </p>
        </div>
        <div class="bg-white p-8 rounded-xl border border-subtle shadow-sm">
          <span class="text-sm font-bold text-neutral-400 font-serif-luxury block mb-2">03</span>
          <h4 class="text-base font-bold text-neutral-900 mb-2 font-serif-luxury">End-to-End Concierge</h4>
          <p class="text-xs text-neutral-600 leading-relaxed">
            Dedicated vehicle coordination, architect walkthroughs, interior customization consultation, and legal deed execution support from start to finish.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Editorial Footer -->
  <footer class="border-t border-subtle bg-white py-14 text-xs text-neutral-500">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="flex items-center space-x-3.5">
        <img src="{logo_url}" alt="{biz_name}" class="w-10 h-10 rounded-full object-cover border border-neutral-300" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=200&q=80'">
        <div>
          <span class="font-bold text-neutral-900 block uppercase tracking-wide">{biz_name}</span>
          <span>Prime Luxury Real Estate Advisory Desk • {city}</span>
        </div>
      </div>
      <div class="flex items-center space-x-6">
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-neutral-900 transition flex items-center">
          Instagram: @{clean_handle}
        </a>
        <a href="https://wa.me/{phone}" class="text-emerald-700 font-bold hover:underline flex items-center">
          WhatsApp: +{phone}
        </a>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-10 pt-8 border-t border-subtle text-center text-[11px] text-neutral-400">
      Private Portfolio Portal prepared for {biz_name}. All rights reserved.
    </div>
  </footer>

</body>
</html>"""
    return html

if __name__ == "__main__":
    print("Realtor Template Generator Loaded.")
