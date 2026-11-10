#!/usr/bin/env python3
"""
Master Interior Designer Landing Page Generator
Faithfully implements the design aesthetic of https://lalit-pixelownstudio.github.io/interior-designer-demo1/
- Warm cream background (#FAF5EC)
- Deep warm espresso ink (#2B2318)
- Subtle muted gold accents (#8A6A12)
- Fraunces & Inter typography
- Dynamic Logo & Contact injection
"""

def generate_interior_page(biz_name, handle, phone, city, logo_url, slug, projects=None):
    if not projects:
        projects = [
            {
                "title": "Minimalist Penthouse Living",
                "category": "Turnkey Residential",
                "specs": "4,200 Sq. Ft. • Italian Marble & Fluted Paneling",
                "img": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": "Sculpted Master Suite",
                "category": "Private Villa",
                "specs": "Custom Walk-in Wardrobe & Concealed Warm LED",
                "img": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1200&q=80"
            },
            {
                "title": "Bespoke German Kitchen & Bar",
                "category": "Luxury Modular",
                "specs": "Quartz Countertops & Soft-Close Blum Hardware",
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
      background-color: #2B2318;
      color: #FAF5EC;
      transition: all 0.2s ease;
    }}
    .btn-dark:hover {{
      background-color: #1A150E;
      transform: translateY(-1px);
    }}
  </style>
</head>
<body class="selection:bg-[#2B2318] selection:text-[#FAF5EC]">

  <!-- Top Announcement -->
  <aside aria-label="Announcement" class="bg-[#2B2318] text-[#F5EFE0] py-2 px-4 text-center text-xs tracking-wider uppercase font-medium">
    Exclusive Consultation: Turnkey Architectural Interiors Across {city}
  </aside>

  <!-- Sticky Navbar -->
  <header class="sticky top-0 z-50 bg-[#FAF5EC]/95 backdrop-blur-md border-b border-subtle">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
      <div class="flex items-center space-x-3.5">
        <img src="{logo_url}" alt="{biz_name} Logo" class="w-11 h-11 rounded-full object-cover border border-[#2B2318]/20 shadow-sm" onerror="this.style.display='none'">
        <div>
          <span class="text-lg sm:text-xl font-bold tracking-tight text-[#2B2318] font-serif-display block leading-none">
            {biz_name}
          </span>
          <span class="text-[11px] tracking-widest text-[#8A6A12] uppercase font-semibold">
            Bespoke Interior Studio • {city}
          </span>
        </div>
      </div>
      <div class="flex items-center space-x-4">
        <a href="https://instagram.com/{handle.replace('@', '')}" target="_blank" rel="noopener noreferrer" class="hidden sm:inline-flex items-center text-xs font-medium text-[#2B2318]/70 hover:text-[#2B2318] transition">
          <svg class="w-4 h-4 mr-1.5 text-pink-700" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          {handle}
        </a>
        <a href="https://wa.me/{phone}?text=Hi%20{biz_name}%20Team,%20I%20would%20like%20to%20book%20an%20interior%20design%20consultation." class="btn-dark px-4 py-2.5 rounded text-xs sm:text-sm font-semibold tracking-wide">
          Book Consultation
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <main class="border-b border-subtle">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-20 text-center">
      <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-4">
        Interiors That Reflect Your Life
      </span>
      <h1 class="text-4xl sm:text-6xl font-normal font-serif-display text-[#2B2318] leading-[1.15] mb-6">
        Every Space Tells a Story, <br><span class="italic font-medium">Let's Write Yours</span>
      </h1>
      <p class="text-base sm:text-lg text-[#2B2318]/80 max-w-2xl mx-auto mb-10 leading-relaxed font-normal">
        From concept sketch to final handover, {biz_name} shapes turnkey homes and commercial spaces that blend timeless aesthetics with effortless livability.
      </p>

      <!-- Stats Grid matching pixelown demo -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto mb-12 text-left">
        <div class="bg-white/80 border border-subtle p-5 rounded">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">200+</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Projects Delivered</span>
        </div>
        <div class="bg-white/80 border border-subtle p-5 rounded">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">12+</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Years of Craft</span>
        </div>
        <div class="bg-white/80 border border-subtle p-5 rounded">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">100%</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Turnkey In-House</span>
        </div>
        <div class="bg-white/80 border border-subtle p-5 rounded">
          <span class="text-2xl font-bold font-serif-display text-[#2B2318] block">On-Time</span>
          <span class="text-xs text-[#2B2318]/70 mt-1 block">Fixed Cost Delivery</span>
        </div>
      </div>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
        <a href="#projects" class="w-full sm:w-auto btn-dark px-8 py-3.5 rounded text-sm font-semibold tracking-wide">
          Explore Our Projects ↓
        </a>
        <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20am%20looking%20for%20home%20interior%20quotation%20and%203D%20consultation." class="w-full sm:w-auto bg-white border border-subtle text-[#2B2318] px-8 py-3.5 rounded text-sm font-semibold hover:border-[#2B2318] transition">
          Direct WhatsApp Estimate
        </a>
      </div>
    </div>
  </main>

  <!-- About / 3 Pillars Section -->
  <section class="py-20 bg-[#F5EFE0] border-b border-subtle">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl mb-12">
        <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-2">Our Methodology</span>
        <h2 class="text-3xl sm:text-4xl font-normal font-serif-display text-[#2B2318]">Designing Spaces <em>With Purpose</em></h2>
        <p class="text-sm text-[#2B2318]/80 mt-3 leading-relaxed">
          A home should feel as good as it looks. We blend architectural precision with bespoke craftsmanship, shaping every project around how you actually live.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-7 rounded border border-subtle">
          <span class="text-xs font-bold text-[#8A6A12] uppercase tracking-wider block mb-2">Pillar 01</span>
          <h3 class="text-xl font-bold font-serif-display text-[#2B2318] mb-3">Design to Handover, One Team</h3>
          <p class="text-xs text-[#2B2318]/70 leading-relaxed">
            Concept, detailed 3D renders, civil masonry, false ceiling, lighting, modular furniture and final styling — executed seamlessly under one roof.
          </p>
        </div>
        <div class="bg-white p-7 rounded border border-subtle">
          <span class="text-xs font-bold text-[#8A6A12] uppercase tracking-wider block mb-2">Pillar 02</span>
          <h3 class="text-xl font-bold font-serif-display text-[#2B2318] mb-3">Master In-House Artisans</h3>
          <p class="text-xs text-[#2B2318]/70 leading-relaxed">
            Zero random sub-contractors. Our dedicated site supervisors, carpenters, and polish masters guarantee millimeter-precise finishing.
          </p>
        </div>
        <div class="bg-white p-7 rounded border border-subtle">
          <span class="text-xs font-bold text-[#8A6A12] uppercase tracking-wider block mb-2">Pillar 03</span>
          <h3 class="text-xl font-bold font-serif-display text-[#2B2318] mb-3">Fixed Budgets &amp; Timelines</h3>
          <p class="text-xs text-[#2B2318]/70 leading-relaxed">
            Transparent BOQs with clear material grades. What we quote before commencement is what you pay upon keys handover.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Featured Projects Gallery -->
  <section id="projects" class="py-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 border-b border-subtle pb-6">
      <div>
        <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-1">Portfolio</span>
        <h2 class="text-3xl font-normal font-serif-display text-[#2B2318]">Signature Interior Transformations</h2>
      </div>
      <p class="text-xs sm:text-sm text-[#2B2318]/70 max-w-md mt-2 md:mt-0">
        Curated residential and commercial developments crafted across {city}.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">"""

    for p in projects:
        html += f"""
      <div class="bg-white border border-subtle rounded overflow-hidden flex flex-col justify-between">
        <div>
          <div class="h-64 overflow-hidden bg-neutral-200">
            <img src="{p['img']}" alt="{p['title']}" class="w-full h-full object-cover">
          </div>
          <div class="p-6">
            <span class="text-[11px] uppercase tracking-wider text-[#8A6A12] font-semibold block mb-1">{p['category']}</span>
            <h3 class="text-xl font-normal font-serif-display text-[#2B2318] mb-2">{p['title']}</h3>
            <p class="text-xs text-[#2B2318]/70">{p['specs']}</p>
          </div>
        </div>
        <div class="p-6 pt-0">
          <a href="https://wa.me/{phone}?text=Hi%20{biz_name},%20I%20saw%20your%20{p['title']}%20project.%20I%20would%20like%20a%20similar%20concept%20for%20my%20property." class="w-full btn-dark py-3 rounded text-xs font-semibold uppercase tracking-wider text-center block">
            Enquire for My Space →
          </a>
        </div>
      </div>"""

    html += f"""
    </div>
  </section>

  <!-- Consultation Booking Box -->
  <section class="py-16 bg-[#F5EFE0] border-t border-subtle">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <span class="text-xs uppercase tracking-widest text-[#8A6A12] font-semibold block mb-2">Connect Directly</span>
      <h2 class="text-3xl font-normal font-serif-display text-[#2B2318] mb-4">Start Your Space Transformation</h2>
      <p class="text-sm text-[#2B2318]/80 max-w-lg mx-auto mb-8">
        Share your floor plan, mood-board ideas, and budget. Our design team coordinates a detailed 3D consultation.
      </p>
      <a href="https://wa.me/{phone}?text=Namaste%20{biz_name}%20Team,%20please%20share%20your%20full%20interior%20catalogue%20and%20consultation%20availability." class="inline-block btn-dark px-8 py-4 rounded text-xs font-bold uppercase tracking-wider">
        Book 3D Design Session on WhatsApp
      </a>
      <span class="block text-xs text-[#2B2318]/60 mt-3">Direct Studio WhatsApp: +{phone}</span>
    </div>
  </section>

  <!-- Editorial Footer -->
  <footer class="border-t border-subtle bg-white py-12 text-xs text-[#2B2318]/70">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-6">
      <div class="flex items-center space-x-3">
        <img src="{logo_url}" alt="{biz_name}" class="w-8 h-8 rounded-full object-cover border border-subtle" onerror="this.style.display='none'">
        <div>
          <span class="font-bold text-[#2B2318] block">{biz_name.upper()}</span>
          <span>Bespoke Interior Design &amp; Architectural Turnkey Execution • {city}</span>
        </div>
      </div>
      <div class="flex items-center space-x-6">
        <a href="https://instagram.com/{handle.replace('@', '')}" target="_blank" rel="noopener noreferrer" class="hover:text-[#2B2318] transition">Instagram: {handle}</a>
        <a href="https://wa.me/{phone}" class="text-[#2B2318] font-semibold hover:underline">WhatsApp: +{phone}</a>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-8 pt-8 border-t border-subtle text-center text-[11px] text-[#2B2318]/40">
      Preview Portal curated by AutomateFlow for {biz_name}.
    </div>
  </footer>

</body>
</html>"""
    return html

if __name__ == "__main__":
    print("Interior Designer Template Generator Loaded.")

