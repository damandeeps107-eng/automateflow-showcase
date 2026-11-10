#!/usr/bin/env python3
"""
Master Interior Designer Landing Page Generator
Faithfully implements the design aesthetic of PixelOwn Studio + High-End Interior Architecture:
- Full professional header with brand logo, nav links & direct WhatsApp CTA
- Prominent Hero section featuring a large, ultra-sharp interior architectural photograph
- Curated project collection with high-res photography, design specs & WhatsApp consultation scheduler
- 'Why Choose Our Studio' trust pillars
- Editorial luxury footer
"""

def generate_interior_page(biz_name, handle, phone, city, logo_url, slug, projects=None):
    clean_handle = handle.replace("@", "").strip()

    if not projects:
        projects = [
            {
                "title": "Minimalist Penthouse Living Lounge",
                "category": "Turnkey Residential",
                "specs": "4,200 Sq. Ft. • Italian Statuario Marble & Fluted Paneling",
                "desc": "Monochromatic architectural living space with concealed ambient warm lighting, bespoke brass accents, and custom low-profile seating.",
                "img": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": "Sculpted Master Bedroom Suite",
                "category": "Private Villa",
                "specs": "Custom Walk-in Wardrobe & Concealed LED Vanity",
                "desc": "Acoustic fabric wall panels, warm European oak flooring, motorized velvet drapes, and an integrated private reading alcove.",
                "img": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": "Bespoke German Island Kitchen & Bar",
                "category": "Luxury Modular",
                "specs": "Quartz Countertops & Soft-Close Blum Hardware",
                "desc": "Seamless handle-less cabinetry with integrated appliances, smart pull-out pantries, and an adjoining breakfast marble counter.",
                "img": "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=1200&q=80"
            }
        ]

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{biz_name} | Bespoke Interior Architecture &amp; Turnkey Homes</title>
  <meta name="description" content="Luxury residential and commercial interiors in {city} by {biz_name}. Turnkey design, modular craftsmanship, and transparent budget delivery.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --ic-bg: #FAF5EC;
      --ic-ink: #2B2318;
      --ic-cream: #F5EFE0;
      --ic-gold: #D4AF37;
      --ic-gold-text: #8A6A12;
      --font-display: 'Fraunces', Georgia, serif;
      --font-body: 'Inter', -apple-system, sans-serif;
    }}
    body {{
      background-color: var(--ic-bg);
      color: var(--ic-ink);
      font-family: var(--font-body);
      -webkit-font-smoothing: antialiased;
      line-height: 1.6;
    }}
    .font-serif-display {{
      font-family: var(--font-display);
    }}
    .border-subtle {{
      border-color: rgba(43, 35, 24, 0.12);
    }}
    .btn-dark {{
      background-color: var(--ic-ink);
      color: #FAF5EC;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .btn-dark:hover {{
      background-color: #1A150E;
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(43, 35, 24, 0.2);
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
  </style>
</head>
<body class="selection:bg-[#2B2318] selection:text-[#FAF5EC]">

  <!-- Top Announcement -->
  <aside aria-label="Announcement" class="bg-[#2B2318] text-[#F5EFE0] py-2.5 px-4 text-center text-xs tracking-wider uppercase font-medium border-b border-black/20">
    <div class="max-w-7xl mx-auto flex items-center justify-center space-x-2">
      <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
      <span>Turnkey Architectural Interiors &amp; Luxury Residence Handover Across {city}</span>
    </div>
  </aside>

  <!-- Complete Professional Navigation Header -->
  <header class="sticky top-0 z-50 bg-[#FAF5EC]/95 backdrop-blur-md border-b border-subtle">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      
      <!-- Brand Logo & Identity -->
      <a href="#" class="flex items-center space-x-3.5 group">
        <div class="relative">
          <img src="{logo_url}" alt="{biz_name} Logo" class="w-12 h-12 rounded-full object-cover border border-[#2B2318]/20 shadow-sm transition group-hover:scale-105" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=200&q=80'">
          <span class="absolute bottom-0 right-0 w-3.5 h-3.5 bg-amber-500 border-2 border-[#FAF5EC] rounded-full"></span>
        </div>
        <div>
          <span class="text-lg sm:text-xl font-bold tracking-tight text-[#2B2318] font-serif-display block leading-none">
            {biz_name}
          </span>
          <span class="text-[11px] tracking-widest text-[#8A6A12] uppercase font-semibold mt-1 block">
            Bespoke Interior Studio • {city}
          </span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden lg:flex items-center space-x-8 text-xs font-semibold uppercase tracking-wider text-[#2B2318]/80">
        <a href="#featured-projects" class="hover:text-[#2B2318] transition">Featured Portfolios</a>
        <a href="#studio-approach" class="hover:text-[#2B2318] transition">Our Approach</a>
        <a href="#studio-stats" class="hover:text-[#2B2318] transition">Studio Milestones</a>
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-[#2B2318] transition flex items-center">
          <svg class="w-3.5 h-3.5 mr-1 text-pink-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          @{clean_handle}
        </a>
      </nav>

      <!-- CTA -->
      <div class="flex items-center space-x-3">
        <a href="https://wa.me/{phone}?text=Hi%20{biz_name}%20Team,%20I%20would%20like%20to%20discuss%20an%20interior%20design%20project." class="btn-dark px-5 py-2.5 rounded-lg text-xs sm:text-sm font-semibold tracking-wide flex items-center shadow-sm">
          Book Consultation
        </a>
      </div>
    </div>
  </header>

  <!-- BREATHTAKING HERO SECTION WITH HERO IMAGE -->
  <main class="border-b border-subtle">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-12 sm:pt-16 pb-16">
      
      <!-- Headline -->
      <div class="max-w-4xl mx-auto text-center mb-10">
        <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-4">
          Every Space Tells a Story • Let's Write Yours
        </span>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-normal font-serif-display text-[#2B2318] leading-[1.15] mb-6">
          Architectural Interiors &amp; <br class="hidden sm:inline">
          <span class="italic font-medium text-[#8A6A12]">Turnkey Homes in {city}</span>
        </h1>
        <p class="text-sm sm:text-lg text-[#2B2318]/80 max-w-2xl mx-auto leading-relaxed">
          From concept sketching to final key handover, {biz_name} shapes turnkey spaces that blend timeless elegance with effortless livability.
        </p>
      </div>

      <!-- PROMINENT HERO IMAGE SHOWCASE (As Requested by User) -->
      <div class="relative max-w-5xl mx-auto rounded-2xl overflow-hidden shadow-2xl border border-[#2B2318]/15 group mb-12">
        <div class="aspect-[16/9] sm:aspect-[21/9] w-full overflow-hidden bg-[#2B2318]">
          <img 
            src="https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1800&q=85" 
            alt="Interior Studio Signature Living Space" 
            class="w-full h-full object-cover object-center group-hover:scale-105 transition duration-700 ease-out"
          >
        </div>

        <!-- Hero Dark Gradient Overlay -->
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/25 to-transparent flex flex-col justify-end p-6 sm:p-10 text-white">
          <div class="flex flex-wrap items-center justify-between gap-4">
            <div>
              <span class="inline-block bg-white/20 backdrop-blur-md px-3 py-1 rounded text-xs uppercase tracking-widest font-semibold mb-2">
                Signature Concept Handover • Turnkey Execution
              </span>
              <h2 class="text-xl sm:text-3xl font-serif-display font-medium text-white">
                Bespoke Penthouse Living &amp; Lighting Architecture
              </h2>
              <p class="text-xs sm:text-sm text-neutral-200 mt-1 max-w-xl">
                Integrated Italian marble floorings, concealed warm perimeter cove illumination, and hand-finished walnut joinery.
              </p>
            </div>
            <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20saw%20your%20showcase%20living%20room%20design%20and%20would%20love%20to%20know%20more." class="btn-wa px-6 py-3 rounded-lg text-xs sm:text-sm font-bold uppercase tracking-wider flex items-center shadow-lg">
              Discuss Your Space →
            </a>
          </div>
        </div>
      </div>

      <!-- Stats Grid -->
      <div id="studio-stats" class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-5xl mx-auto">
        <div class="bg-white/80 border border-subtle p-5 rounded-xl shadow-sm">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">200+</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Projects Delivered</span>
        </div>
        <div class="bg-white/80 border border-subtle p-5 rounded-xl shadow-sm">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">45 Days</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Turnkey Delivery Guarantee</span>
        </div>
        <div class="bg-white/80 border border-subtle p-5 rounded-xl shadow-sm">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">10-Year</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Hardware &amp; Modular Warranty</span>
        </div>
        <div class="bg-white/80 border border-subtle p-5 rounded-xl shadow-sm">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">100%</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Transparent Cost Transparency</span>
        </div>
      </div>

    </div>
  </main>

  <!-- FEATURED PROJECTS -->
  <section id="featured-projects" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 pb-6 border-b border-subtle">
      <div>
        <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-2">Curated Portfolio</span>
        <h2 class="text-2xl sm:text-4xl font-normal font-serif-display text-[#2B2318]">
          Selected Residential Works
        </h2>
      </div>
      <p class="text-xs sm:text-sm text-[#2B2318]/70 max-w-md mt-4 md:mt-0">
        Every detail engineered with custom millwork, curated materials, and timeless finishes tailored to your lifestyle.
      </p>
    </div>

    <!-- Projects Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">"""

    for p in projects:
        html += f"""
      <div class="bg-white/80 border border-subtle rounded-xl overflow-hidden flex flex-col justify-between shadow-sm hover:shadow-xl hover:border-[#2B2318]/30 transition duration-300">
        <div>
          <div class="relative h-64 overflow-hidden bg-neutral-200 group">
            <img src="{p['img']}" alt="{p['title']}" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
            <div class="absolute top-3 left-3 bg-[#2B2318]/90 text-[#FAF5EC] px-3 py-1 rounded-md text-[11px] font-semibold tracking-wide">
              {p['category']}
            </div>
          </div>
          <div class="p-6">
            <span class="text-xs font-semibold text-[#8A6A12] block mb-1">{p['specs']}</span>
            <h3 class="text-lg font-bold font-serif-display text-[#2B2318] mb-2 leading-snug">{p['title']}</h3>
            <p class="text-xs text-[#2B2318]/70 leading-relaxed mb-4">{p['desc']}</p>
          </div>
        </div>
        <div class="p-6 pt-0">
          <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20am%20interested%20in%20a%20similar%20design%20to%20{p['title']}.%20Can%20we%20schedule%20a%20site%20visit?" class="w-full btn-dark py-3 rounded-lg text-xs font-bold uppercase tracking-wider text-center block">
            Discuss Similar Design →
          </a>
        </div>
      </div>"""

    html += f"""
    </div>
  </section>

  <!-- STUDIO APPROACH -->
  <section id="studio-approach" class="border-t border-subtle bg-[#F5EFE0] py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-2xl mx-auto mb-14">
        <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-2">Our Method</span>
        <h3 class="text-2xl sm:text-3xl font-serif-display font-normal text-[#2B2318]">Craftsmanship &amp; Precision</h3>
        <p class="text-xs sm:text-sm text-[#2B2318]/70 mt-2">No guesswork. Complete 3D photorealistic visualization, transparent BOQ materials, and on-time site handover.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white/90 p-8 rounded-xl border border-subtle shadow-sm">
          <span class="text-sm font-bold text-[#8A6A12] font-serif-display block mb-2">01</span>
          <h4 class="text-base font-bold text-[#2B2318] mb-2 font-serif-display">Photorealistic 3D Renders</h4>
          <p class="text-xs text-[#2B2318]/70 leading-relaxed">
            See your exact lighting, finishes, and spatial flow before a single nail is hammered into the wall.
          </p>
        </div>
        <div class="bg-white/90 p-8 rounded-xl border border-subtle shadow-sm">
          <span class="text-sm font-bold text-[#8A6A12] font-serif-display block mb-2">02</span>
          <h4 class="text-base font-bold text-[#2B2318] mb-2 font-serif-display">Turnkey Millwork &amp; Modular</h4>
          <p class="text-xs text-[#2B2318]/70 leading-relaxed">
            Factory-finished cabinetry and joinery crafted with German hardware to ensure zero dust on site and flawless alignments.
          </p>
        </div>
        <div class="bg-white/90 p-8 rounded-xl border border-subtle shadow-sm">
          <span class="text-sm font-bold text-[#8A6A12] font-serif-display block mb-2">03</span>
          <h4 class="text-base font-bold text-[#2B2318] mb-2 font-serif-display">Strict Milestone Handover</h4>
          <p class="text-xs text-[#2B2318]/70 leading-relaxed">
            Daily site reports, material inspection sign-offs, and guaranteed handover timelines with zero budget slippages.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Editorial Footer -->
  <footer class="border-t border-subtle bg-white py-14 text-xs text-[#2B2318]/60">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="flex items-center space-x-3.5">
        <img src="{logo_url}" alt="{biz_name}" class="w-10 h-10 rounded-full object-cover border border-[#2B2318]/20" onerror="this.src='https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=200&q=80'">
        <div>
          <span class="font-bold text-[#2B2318] block uppercase tracking-wide">{biz_name}</span>
          <span>Bespoke Interior Architecture • {city}</span>
        </div>
      </div>
      <div class="flex items-center space-x-6">
        <a href="https://instagram.com/{clean_handle}" target="_blank" rel="noopener noreferrer" class="hover:text-[#2B2318] transition flex items-center">
          Instagram: @{clean_handle}
        </a>
        <a href="https://wa.me/{phone}" class="text-emerald-700 font-bold hover:underline flex items-center">
          WhatsApp: +{phone}
        </a>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-10 pt-8 border-t border-subtle text-center text-[11px] text-[#2B2318]/40">
      Preview Portal prepared for {biz_name}. All rights reserved.
    </div>
  </footer>

</body>
</html>"""
    return html

if __name__ == "__main__":
    print("Interior Template Generator Loaded.")
